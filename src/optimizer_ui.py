import sys
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QLabel)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from src.interface import BaseWindow
from src.optimizer_engine import optimize_file, get_optimized_preview_data
from src.helper import show_help, is_image_extension

class MainWindow(BaseWindow):
    def __init__(self, image_path):
        # 1. Iniciamos la base en modo optimize
        super().__init__(image_path, title_text="OPTIMIZAR TAMAÑO", mode="optimize")
        
        # 2. Creamos el label de pesos (Original vs Optimizado) que no está en la base
        self.label_pesos = QLabel("Calculando peso...")
        self.label_pesos.setStyleSheet("color: #00ca4e; font-weight: bold; margin-top: 10px;")
        self.label_pesos.setAlignment(Qt.AlignCenter)
        
        # Lo insertamos en el panel lateral, justo antes del botón de ejecución
        # (count - 2 porque el count - 1 es el botón y el count - 2 es el stretch)
        self.side_layout.insertWidget(self.side_layout.count() - 2, self.label_pesos)

        # 3. CONEXIÓN CLAVE: Conectamos el slider que la base ya creó
        self.slider.valueChanged.connect(self.refresh_ui)
        
        # 4. Configuramos el callback del botón
        self.callback = self.run_optimization
        
        # Carga inicial
        self.refresh_ui()

    def refresh_ui(self):
        """Este método se ejecuta cada vez que mueves el slider"""
        calidad = self.slider.value()
        
        # Obtener los datos del motor (Buffer de memoria y peso estimado)
        img_data, est_kb = get_optimized_preview_data(str(self.image_path), calidad)
        
        # Actualizar la imagen en el visor (img_item ya existe en la base)
        q_img = QImage.fromData(img_data)
        pixmap = QPixmap.fromImage(q_img)
        self.img_item.setPixmap(pixmap)
        
        # Calcular ahorro y actualizar el label de pesos
        orig_kb = self.image_path.stat().st_size / 1024
        ahorro = 100 - (est_kb / orig_kb * 100) if orig_kb > 0 else 0
        
        self.label_pesos.setText(
            f"Original: {orig_kb:.1f} KB\n"
            f"Optimizado: {est_kb:.1f} KB\n"
            f"Ahorro: {ahorro:.1f}%"
        )

    def run_optimization(self):
        """Acción final al darle al botón azul"""
        calidad = self.slider.value()
        new_name = self.input_name.text().strip()
        final_name = new_name if new_name else None
        
        result = optimize_file(str(self.image_path), calidad, final_name)
        print(f"Optimización finalizada: {result}")

def start_optimizer(path: str) -> None:
    path_obj = Path(path)

    if not path_obj.exists():
        print(f"Error: La ruta '{path}' no existe.")
        show_help()
        return

    extension = path_obj.suffix 

    if not is_image_extension(extension):
        print(f"Error: La extensión '{extension}' no es soportada.")
        show_help()
        return

    app = QApplication(sys.argv)
    window = MainWindow(path)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    else:
        start_optimizer(sys.argv[1])