from pathlib import Path
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel, 
                             QPushButton, QHBoxLayout, QFrame, QGraphicsView, 
                             QGraphicsScene, QGraphicsPixmapItem, QLineEdit, 
                             QSlider, QCheckBox)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QPainter

# --- ESTILO UNIFICADO (BASE) ---
UI_STYLE = """
    QMainWindow { background-color: #121212; }
    QFrame#SidePanel { 
        background-color: #1e1e1e; 
        border-left: 1px solid #333; 
    }
    QLabel { color: #eeeeee; font-family: 'Segoe UI'; font-size: 13px; }
    QLabel#Title { color: #00a2ed; font-weight: bold; font-size: 16px; margin-bottom: 10px; }
    QLineEdit { 
        background-color: #2d2d2d; color: white; border: 1px solid #3f3f3f; 
        padding: 8px; border-radius: 4px; font-size: 14px;
    }
    QLineEdit:focus { border: 1px solid #00a2ed; }
    QPushButton#MainBtn { 
        background-color: #00a2ed; color: white; font-weight: bold; 
        font-size: 14px; border-radius: 5px; border: none; padding: 12px;
    }
    QPushButton#MainBtn:hover { background-color: #0081bd; }
    QSlider::groove:horizontal { background: #333; height: 6px; border-radius: 3px; }
    QSlider::handle:horizontal { background: #00a2ed; width: 16px; height: 16px; margin: -5px 0; border-radius: 8px; }
    QCheckBox { color: white; spacing: 8px; }
"""

class BaseWindow(QMainWindow):
    def __init__(self, image_path, title_text="HERRAMIENTA", mode="generic", callback=None):
        super().__init__()
        self.image_path = Path(image_path)
        self.callback = callback
        
        self.setWindowTitle(f"Image Toolkit - {self.image_path.name}")
        self.setMinimumSize(1000, 750)
        self.setStyleSheet(UI_STYLE)

        # 1. Componentes de Imagen (Visor)
        self.pixmap = QPixmap(str(self.image_path))
        self.scene = QGraphicsScene()
        self.img_item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(self.img_item)

        # 2. Layout Principal
        central = QWidget()
        self.setCentralWidget(central)
        self.main_layout = QHBoxLayout(central)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # 3. Visor Izquierda
        self.view = QGraphicsView(self.scene)
        self.view.setStyleSheet("background-color: #121212; border: none;")
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)
        
        # 4. Panel Derecha
        self.side_panel = QFrame()
        self.side_panel.setObjectName("SidePanel")
        self.side_panel.setFixedWidth(280)
        self.side_layout = QVBoxLayout(self.side_panel)
        self.side_layout.setContentsMargins(20, 30, 20, 20)
        self.side_layout.setSpacing(15)

        # --- CONSTRUCCIÓN DINÁMICA DEL PANEL ---
        self._add_header(title_text)
        self._setup_controls(mode)
        
        # Botón de acción siempre al fondo
        self.side_layout.addStretch()
        self.btn_main = QPushButton("EJECUTAR ACCIÓN")
        self.btn_main.setObjectName("MainBtn")
        self.btn_main.setFixedHeight(50)
        self.btn_main.clicked.connect(self._on_execute)
        self.side_layout.addWidget(self.btn_main)

        # Agregar al layout principal
        self.main_layout.addWidget(self.view, stretch=1)
        self.main_layout.addWidget(self.side_panel)
        
        # Ajuste inicial
        #self.view.fitInView(self.img_item, Qt.KeepAspectRatio)
        QTimer.singleShot(0, lambda: self.view.fitInView(self.img_item, Qt.KeepAspectRatio))

    def _add_header(self, text):
        lbl = QLabel(text)
        lbl.setObjectName("Title")
        self.side_layout.addWidget(lbl)

    def _setup_controls(self, mode):
        # Nombre de salida (Común a todos)
        self.side_layout.addWidget(QLabel("NOMBRE DE SALIDA"))
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText(f"{self.image_path.stem}_out")
        self.side_layout.addWidget(self.input_name)

        # Inputs de tamaño (Para Recorte y Redimensionar)
        if mode in ["crop", "resize"]:
            self.side_layout.addWidget(QLabel("ANCHO (PX)"))
            self.input_w = QLineEdit("0")
            self.side_layout.addWidget(self.input_w)
            
            self.side_layout.addWidget(QLabel("ALTO (PX)"))
            self.input_h = QLineEdit("0")
            self.side_layout.addWidget(self.input_h)

            if mode == "resize":
                self.check_ratio = QCheckBox("Mantener Proporción")
                self.check_ratio.setChecked(False)
                self.side_layout.addWidget(self.check_ratio)

        # Slider (Para Optimizar)
        if mode == "optimize":
            self.side_layout.addWidget(QLabel("CALIDAD / COMPRESIÓN"))
            self.slider = QSlider(Qt.Horizontal)
            self.slider.setRange(10, 100)
            self.slider.setValue(80)
            self.side_layout.addWidget(self.slider)

    def resizeEvent(self, event):
        """Mantiene la imagen ocupando todo el espacio si el usuario estira la ventana."""
        super().resizeEvent(event)
        # Verificamos que los objetos existan para evitar errores
        if hasattr(self, 'view') and self.img_item:
            if not hasattr(self, 'proxy'): 
                self.view.fitInView(self.img_item, Qt.KeepAspectRatio)

    def _on_execute(self):
        if self.callback:
            self.callback()
        self.close()