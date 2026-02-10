import sys
from PIL import Image
from pathlib import Path
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsRectItem
from PySide6.QtCore import QRectF, QSize, Qt
from PySide6.QtGui import QColor, QPen, QBrush
from src.interface import BaseWindow
from src.helper import show_help, is_image_extension

class CropRectItem(QGraphicsRectItem):
    def __init__(self, rect, parent=None):
        super().__init__(rect, parent)
        self.setPen(QPen(QColor("#00a2ed"), 2, Qt.DashLine))
        self.setBrush(QBrush(QColor(0, 162, 237, 40)))
        self.setFlags(QGraphicsRectItem.ItemIsMovable | QGraphicsRectItem.ItemIsSelectable | QGraphicsRectItem.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)
        self.resizing = False

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        painter.setBrush(QColor("#00a2ed"))
        painter.setPen(QPen(Qt.white, 1))
        r = self.rect()
        for p in [r.topLeft(), r.topRight(), r.bottomLeft(), r.bottomRight()]:
            painter.drawRect(QRectF(p.x()-5, p.y()-5, 10, 10))

    def hoverMoveEvent(self, event):
        r = self.rect()
        if QRectF(r.right()-15, r.bottom()-15, 15, 15).contains(event.pos()):
            self.setCursor(Qt.SizeFDiagCursor)
        else:
            self.setCursor(Qt.SizeAllCursor)
        super().hoverMoveEvent(event)

    def mousePressEvent(self, event):
        r = self.rect()
        if QRectF(r.right()-15, r.bottom()-15, 15, 15).contains(event.pos()):
            self.resizing = True
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.resizing:
            r = self.rect()
            r.setBottomRight(event.pos())
            self.setRect(r.normalized())
        else:
            super().mouseMoveEvent(event)
        
        # Sincronizamos con el panel de la interfaz
        self.scene().views()[0].window().update_panel_from_rect()

    def mouseReleaseEvent(self, event):
        self.resizing = False
        super().mouseReleaseEvent(event)

class MainWindow(BaseWindow):
    def __init__(self, image_path):
        # Llamamos a la base con modo "crop" para que pinte el panel azul
        super().__init__(image_path, title_text="RECORTE PROFESIONAL", mode="crop")
        
        self.crop_item = None
        self.origin = None

        # Reemplazamos los eventos del visor de la interfaz con los de este archivo
        self.view.mousePressEvent = self.view_press
        self.view.mouseMoveEvent = self.view_move
        
        # Conectamos los inputs que la interfaz ya creó
        self.input_w.editingFinished.connect(self.update_rect_from_panel)
        self.input_h.editingFinished.connect(self.update_rect_from_panel)
        
        # Definimos que el botón ejecute nuestro proceso de recorte
        self.callback = self.apply_crop

    def view_press(self, event):
        if event.button() == Qt.LeftButton:
            scene_pos = self.view.mapToScene(event.position().toPoint())
            if self.crop_item and self.crop_item.contains(self.crop_item.mapFromScene(scene_pos)):
                QGraphicsView.mousePressEvent(self.view, event)
                return
            if self.crop_item: self.scene.removeItem(self.crop_item)
            self.origin = scene_pos
            self.crop_item = CropRectItem(QRectF(self.origin, QSize(0,0)))
            self.scene.addItem(self.crop_item)

    def view_move(self, event):
        if event.buttons() & Qt.LeftButton and self.crop_item and not self.crop_item.resizing:
            if not self.crop_item.isSelected():
                cur_pos = self.view.mapToScene(event.position().toPoint())
                self.crop_item.setRect(QRectF(self.origin, cur_pos).normalized())
                self.update_panel_from_rect()
        QGraphicsView.mouseMoveEvent(self.view, event)

    def update_panel_from_rect(self):
        if self.crop_item:
            rect = self.crop_item.rect()
            self.input_w.blockSignals(True)
            self.input_h.blockSignals(True)
            self.input_w.setText(str(int(rect.width())))
            self.input_h.setText(str(int(rect.height())))
            self.input_w.blockSignals(False)
            self.input_h.blockSignals(False)

    def update_rect_from_panel(self):
        if self.crop_item:
            try:
                new_w = float(self.input_w.text())
                new_h = float(self.input_h.text())
                rect = self.crop_item.rect()
                self.crop_item.setRect(rect.x(), rect.y(), new_w, new_h)
            except ValueError: pass

    def apply_crop(self):
        if not self.crop_item: return
        rect = self.crop_item.sceneBoundingRect()
        real_coords = (int(rect.left()), int(rect.top()), int(rect.right()), int(rect.bottom()))
        
        # Obtener nombre del input o usar el placeholder
        custom_name = self.input_name.text().strip()
        final_name = custom_name if custom_name else None
        
        crop_image(str(self.image_path), real_coords, final_name)
        self.close()

def crop_image(input_path: str, coords: tuple, output_name: str | None = None) -> Path:
    p = Path(input_path)
    output_path = p.parent / f"{output_name if output_name else p.stem + '_cut'}{p.suffix}"
    with Image.open(p) as img:
        cropped = img.crop(coords)
        cropped.save(output_path, optimize=True)
    return output_path

def start_cut(path: str):
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
        start_cut(sys.argv[1])