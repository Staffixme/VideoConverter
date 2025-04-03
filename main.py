import os
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QLabel, QTableWidgetItem, QListWidget, QFileDialog
from PyQt6.QtCore import Qt, pyqtSlot, QThread, pyqtSignal, QObject, QPoint

from main_window import Ui_Form as UI_MainWindow
from solo_load import Ui_Form as UI_SoloLoad


class MainWindow(QWidget, UI_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())
        self.SoloLoad.clicked.connect(self.load_solo_file)

    def load_solo_file(self):
        dialog = QFileDialog.getOpenFileName(self, "Выберите файл для конвертации", "",
                                             "Изображение (*.png *.jpg *.jpeg);;Видео (*.mp4 *.webm *.avi *.mkv "
                                             "*.mov);;Текстовый документ (*.txt *.doc *.docx);;Музыка "
                                             "(*.mp3 *.aac *.wav *.ogg)")
        create_solo_load(dialog[0])
        self.close()

    def mousePressEvent(self, a0) -> None:
        self.old_pos = a0.globalPosition().toPoint()
        self.is_mouse_pressed = True

    def mouseMoveEvent(self, a0) -> None:
        if self.is_mouse_pressed:
            delta = QPoint(a0.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = a0.globalPosition().toPoint()

    def mouseReleaseEvent(self, a0) -> None:
        self.is_mouse_pressed = False


class SoloLoad(QWidget, UI_SoloLoad):
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.setupUi(self)
        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())
        self.setup_file_data()
        self.PathEditButton.clicked.connect(lambda: self.PathTosave.setText(QFileDialog.getExistingDirectory(self)))

    def setup_file_data(self):
        self.FileName.setText(os.path.basename(self.file))
        self.OriginalFormat.setText(os.path.splitext(self.file)[1])

    def mousePressEvent(self, a0) -> None:
        self.old_pos = a0.globalPosition().toPoint()
        self.is_mouse_pressed = True

    def mouseMoveEvent(self, a0) -> None:
        if self.is_mouse_pressed:
            delta = QPoint(a0.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = a0.globalPosition().toPoint()

    def mouseReleaseEvent(self, a0) -> None:
        self.is_mouse_pressed = False

    def closeEvent(self, a0):
        window = MainWindow()
        window.show()


def create_solo_load(file):
    solo_load_window = SoloLoad(file)
    solo_load_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
