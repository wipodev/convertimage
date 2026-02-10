import sys
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMessageBox)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal, QTimer
from PIL import Image
from pathlib import Path
from src.interface import BaseWindow
from src.helper import show_help, is_image_extension

class Handle(QFrame):
    def __init__(self, parent, cursor_type):
        super().__init__(parent)
        self.setFixedSize(12, 12)
        self.setStyleSheet("""
            background-color: white; 
            border: 2px solid #3498db; 
            border-radius: 6px;
        """)
        self.cursor_type = cursor_type

    def enterEvent(self, event):
        self.setCursor(self.cursor_type)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setCursor(Qt.CursorShape.ArrowCursor)
        super().leaveEvent(event)

class ResizableImage(QFrame):
    sizeChanged = Signal(int, int)

    def __init__(self, parent, image_path, start_w=256, start_h=256):
        super().__init__(parent)
        self.setObjectName("MainContainer")
        self.setStyleSheet("#MainContainer { border: 2px dashed #3498db; background-color: rgba(52, 152, 219, 0.1); }")
        self.padding = 10
        
        # Guardar el ratio original
        self.ratio = start_w / start_h
        self.keep_ratio = False # Se controlará desde la MainWindow

        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)
        self.image_label.setPixmap(QPixmap(image_path))

        self.h_w = Handle(self, Qt.CursorShape.SizeHorCursor)
        self.h_h = Handle(self, Qt.CursorShape.SizeVerCursor)
        self.h_b = Handle(self, Qt.CursorShape.SizeFDiagCursor)
        
        self.mode = None
        self.setMouseTracking(True)
        self.resize_from_value(start_w, start_h)

    def resize_from_value(self, w_real, h_real):
        new_w = w_real + (self.padding * 2)
        new_h = h_real + (self.padding * 2)
        self.resize(new_w, new_h)
        self.update_layout()

    def update_layout(self):
        w, h = self.width(), self.height()
        self.image_label.setGeometry(self.padding, self.padding, w - (self.padding*2), h - (self.padding*2))
        
        self.h_w.move(w - 12, h // 2 - 6)
        self.h_h.move(w // 2 - 6, h - 12)
        self.h_b.move(w - 12, h - 12)

        real_w = w - (self.padding * 2)
        real_h = h - (self.padding * 2)
        
        self.sizeChanged.emit(real_w, real_h)

    def mousePressEvent(self, event):
        x, y = event.position().x(), event.position().y()
        w, h = self.width(), self.height()
        if x > w - 20 and y > h - 20: self.mode = 'BOTH'
        elif x > w - 20: self.mode = 'W'
        elif y > h - 20: self.mode = 'H'
        else: self.mode = None

    def mouseMoveEvent(self, event):
        if self.mode:
            pos = event.position()
            new_w = self.width()
            new_h = self.height()

            if self.mode == 'W':
                new_w = max(50, int(pos.x()))
            elif self.mode == 'H':
                new_h = max(50, int(pos.y()))
            elif self.mode == 'BOTH':
                new_w = max(50, int(pos.x()))
                new_h = max(50, int(pos.y()))
                
                # APLICAR RATIO SI ESTÁ ACTIVADO
                if self.keep_ratio:
                    # Ajustamos el alto basado en el nuevo ancho y el ratio original
                    # Restamos padding para el cálculo puro de la imagen
                    pure_w = new_w - (self.padding * 2)
                    pure_h = pure_w / self.ratio
                    new_h = int(pure_h + (self.padding * 2))

            self.resize(new_w, new_h)
            self.update_layout()

    def mouseReleaseEvent(self, event):
        self.mode = None

class MainWindow(BaseWindow):
    def __init__(self, path):
        # 1. Iniciamos la base normal (NO ocultamos el view)
        super().__init__(path, title_text="PROPIEDADES / ESCALA", mode="resize")
        
        # 2. Ocultamos el item estático original porque vamos a usar el interactivo
        self.img_item.hide()

        # 3. Creamos el componente interactivo
        self.img_comp = ResizableImage(None, path, self.pixmap.width(), self.pixmap.height())
        
        # 4. ¡LA CLAVE!: Lo metemos en la escena del visor base
        # Esto hace que el componente herede el comportamiento de fitInView
        self.proxy = self.scene.addWidget(self.img_comp)
        
        # Conectar señales
        self.img_comp.sizeChanged.connect(self.update_inputs_from_comp)
        self.check_ratio.toggled.connect(self.sync_ratio)
        self.input_w.returnPressed.connect(self.manual_resize)
        self.input_h.returnPressed.connect(self.manual_resize)
        
        self.callback = self.save_resized_image
        self.update_inputs_from_comp(self.pixmap.width(), self.pixmap.height())

        # 5. Forzamos el ajuste inicial para que el componente interactivo quepa en pantalla
        QTimer.singleShot(50, lambda: self.view.fitInView(self.proxy, Qt.KeepAspectRatio))

    def sync_ratio(self, state):
        self.img_comp.keep_ratio = state

    def update_inputs_from_comp(self, w, h):
        self.input_w.blockSignals(True)
        self.input_h.blockSignals(True)
        self.input_w.setText(str(w))
        self.input_h.setText(str(h))
        self.input_w.blockSignals(False)
        self.input_h.blockSignals(False)

    def manual_resize(self):
        try:
            w, h = int(self.input_w.text()), int(self.input_h.text())
            if self.img_comp.keep_ratio:
                if self.input_w.hasFocus(): h = int(w / self.img_comp.ratio)
                else: w = int(h * self.img_comp.ratio)
            self.img_comp.resize_from_value(w, h)
        except ValueError: pass

    def save_resized_image(self):
        try:
            tw, th = int(self.input_w.text()), int(self.input_h.text())
            name = self.input_name.text().strip()
            final_name = name if name else f"{self.image_path.stem}_resized"
            output_path = self.image_path.parent / f"{final_name}{self.image_path.suffix}"

            with Image.open(self.image_path) as img:
                img.resize((tw, th), Image.Resampling.LANCZOS).save(output_path, quality=95)
            
            QMessageBox.information(self, "Éxito", f"Guardada en:\n{output_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

def start_resize(path: str) -> None:
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
        start_resize(sys.argv[1])