import json
import os
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt, QPoint
import requests
import dotenv

from main_window import Ui_Form as UI_MainWindow
from solo_load import Ui_Form as UI_SoloLoad
from login import Ui_Form as UI_Login
from registartion import Ui_Form as UI_Reg
from premium import Ui_Form as UI_Premium

is_login = False
login = ""

dotenv.load_dotenv()
print(os.getenv("HOST"))


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
        self.MultiLoad.clicked.connect(self.load_multi_files)
        self.LoginButon.clicked.connect(lambda: (self.close(), create_login()))
        self.PremiumButton.clicked.connect(self.premium_window)

        if is_login:
            self.LoginButon.setText(login)

    def premium_window(self):
        if is_login:
            self.close()
            prem = PremiumWindow()
            prem.show()
        else:
            QMessageBox.information(self, "Войдите в аккаунт", "Для начала войдите в аккаунт.")

    def load_solo_file(self):
        dialog = QFileDialog.getOpenFileName(self, "Выберите файл для конвертации", "",
                                             "Изображение (*.png *.jpg *.jpeg);;Видео (*.mp4 *.webm *.avi *.mkv "
                                             "*.mov);;Текстовый документ (*.txt *.doc *.docx);;Музыка "
                                             "(*.mp3 *.aac *.wav *.ogg)")
        create_solo_load(dialog[0])
        self.close()

    def load_multi_files(self):
        if is_login:
            try:
                data = {"login": login}
                headers = {"Content-Type": "application/json"}
                answer = requests.post(f"{os.getenv("HOST")}/check_subscription", data=json.dumps(data),
                                       headers=headers)
                content = answer.json()
                if content['has_subscription']:
                    dialog = QFileDialog.getOpenFileNames(self, "Выберите файл для конвертации", "",
                                                          "Изображение (*.png *.jpg *.jpeg);;Видео "
                                                          "(*.mp4 *.webm *.avi *.mkv "
                                                          "*.mov);;Текстовый документ (*.txt *.doc *.docx);;Музыка "
                                                          "(*.mp3 *.aac *.wav *.ogg)")
                    create_solo_load(dialog[0])
                    self.close()
                else:
                    QMessageBox.information(self, "Нет премиум-подписки",
                                            "Это премиум-функция. Оформите подписку, чтобы разблокировать её.")
            except Exception as e:
                print(e)
        else:
            QMessageBox.information(self, "Войдите в аккаунт", "Вы не можете пользоваться премиум-функциями, без "
                                                               "аккаунта.\n\nПожалуйста, войдите "
                                                               "в свой акканут или создайте новый")

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


class LoginWindow(QWidget, UI_Login):
    def __init__(self):
        super().__init__()
        self.is_closed_by_user = True
        self.setupUi(self)
        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())
        self.RegistartionButton.clicked.connect(self.switch_panel)
        self.LoginButton.clicked.connect(self.login)

    def switch_panel(self):
        self.is_closed_by_user = False
        self.close()
        create_registration()

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
        if self.is_closed_by_user:
            window = MainWindow()
            window.show()

    def login(self):
        try:
            data = {"login": self.LoginLine.text(), "password": self.PasswordLine.text()}
            headers = {"Content-Type": "application/json"}
            answer = requests.post(f"{os.getenv("HOST")}/login", data=json.dumps(data), headers=headers)
            if answer.status_code == 200:
                global is_login, login
                is_login = True
                login = answer.json()["username"]
                print(is_login, login)
        except Exception as e:
            print(e)


class RegistrationWindow(QWidget, UI_Reg):
    def __init__(self):
        super().__init__()
        self.is_closed_by_user = True
        self.setupUi(self)
        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())
        self.LoginButton.clicked.connect(self.switch_panel)
        self.RegistrationButton.clicked.connect(self.registration)

    def switch_panel(self):
        self.is_closed_by_user = False
        self.close()
        create_login()

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
        if self.is_closed_by_user:
            window = MainWindow()
            window.show()

    def registration(self):
        try:
            data = {"login": self.LoginLine.text(), "password": self.PasswordLine.text()}
            headers = {"Content-Type": "application/json"}
            answer = requests.post(f"{os.getenv("HOST")}/register", data=json.dumps(data), headers=headers)
            print(answer, answer.content)
        except Exception as e:
            print(e)


class PremiumWindow(QWidget, UI_Premium):
    def __init__(self):
        super().__init__()
        self.is_closed_by_user = True
        self.setupUi(self)
        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())
        self.GetButton.clicked.connect(self.get_premium)

        data = {"login": login}
        headers = {"Content-Type": "application/json"}
        answer = requests.post(f"{os.getenv("HOST")}/check_subscription", data=json.dumps(data),
                               headers=headers)
        content = answer.json()
        if content['has_subscription']:
            self.GetButton.setText("Уже подключено")
            self.GetButton.setEnabled(False)

    def get_premium(self):
        try:
            data = {"login": login}
            headers = {"Content-Type": "application/json"}
            answer = requests.post(f"{os.getenv("HOST")}/activate_subscription", data=json.dumps(data),
                                   headers=headers)
        except Exception as e:
            print(e)

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
        if self.is_closed_by_user:
            window = MainWindow()
            window.show()


def create_solo_load(file):
    solo_load_window = SoloLoad(file)
    solo_load_window.show()


def create_login():
    login_window = LoginWindow()
    login_window.show()


def create_registration():
    reg_window = RegistrationWindow()
    reg_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
