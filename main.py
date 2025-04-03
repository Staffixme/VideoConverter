import json
import os
import sys
import logging

from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt, QPoint
import requests
import dotenv

from main_window import Ui_Form as UI_MainWindow
from solo_load import Ui_Form as UI_SoloLoad
from login import Ui_Form as UI_Login
from registartion import Ui_Form as UI_Reg
from premium import Ui_Form as UI_Premium
from moviepy.editor import VideoFileClip

# Настройка логирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
                                             "Видео (*.mp4 *.avi *.mkv *.mov *.flv *.wmv *.webm *.mpg *.m4v *.3gp *.ogv *.vob *.asf *.ts *.swf *.f4v *.rmvb)")

        if dialog[0]:  
            create_solo_load(dialog[0])  # Передаем выбранный файл в SoloLoad
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Не был выбран файл для конвертации.")

    def load_multi_files(self):
        if is_login:
            try:
                data = {"login": login}
                headers = {"Content-Type": "application/json"}
                answer = requests.post(f"{os.getenv('HOST')}/check_subscription", data=json.dumps(data),
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
                logging.error(f"Ошибка при загрузке файлов: {e}")
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
        self.progressBar.setValue(0)

        if not os.path.exists(self.file):
            QMessageBox.critical(self, "Ошибка", f"Файл не найден: {self.file}")
            self.close()
            return

        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())
        self.setup_file_data()
        self.PathEditButton.clicked.connect(lambda: self.PathTosave.setText(QFileDialog.getExistingDirectory(self)))


        self.ConvertButton.clicked.connect(self.convert_files)

    def setup_file_data(self):
        self.FileName.setText(os.path.basename(self.file))
        self.OriginalFormat.setText(os.path.splitext(self.file)[1])

        if os.path.splitext(self.file)[1].lower() not in [
    ".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv", ".webm", ".mpg", ".m4v",
    ".3gp", ".ogv", ".vob", ".asf", ".ts", ".swf", ".f4v", ".rmvb"
]:
            QMessageBox.critical(self, "Ошибка", f"Неподдерживаемый формат: {self.file}")
            self.close()

    def update_progress_bar(self, progress):
        """ Update the progress bar based on the conversion progress. """
        self.progressBar.setValue(int(progress * 100))

    def convert_video(self, file_path, output_file_path, output_format):
        try:
            logging.info(f"Начало конвертации: {file_path} в формат {output_format}")
            video = VideoFileClip(file_path)


            # В зависимости от формата прописываем свои кодеки,
            # но теперь добавляем logger=my_logger:
            if output_format == ".avi":
                video.write_videofile(
                    output_file_path,
                    codec='mpeg4',
                    audio_codec='mp3',
                )
            elif output_format == ".mp4":
                video.write_videofile(
                    output_file_path,
                    codec='libx264',
                    audio_codec='aac',
                )
            elif output_format == ".mov":
                video.write_videofile(
                    output_file_path,
                    codec='libx264',
                    audio_codec='aac',
                    threads=4,
                )
            elif output_format == ".flv":
                video.write_videofile(
                    output_file_path,
                    codec='flv',
                    audio_codec='aac',
                    threads=4,
                )
            elif output_format == ".wmv":
                video.write_videofile(
                    output_file_path,
                    codec='wmv2',
                    audio_codec='wmav2',
                    threads=4,
                )
            elif output_format == ".webm":
                video.write_videofile(
                    output_file_path,
                    codec='libvpx',
                    audio_codec='libvorbis',
                    threads=4,
                )
            elif output_format == ".mpg":
                video.write_videofile(
                    output_file_path,
                    codec='mpeg2video',
                    audio_codec='mp2',
                    threads=4,
                )
            elif output_format == ".m4v":
                video.write_videofile(
                    output_file_path,
                    codec='libx264',
                    audio_codec='aac',
                    threads=4,
                )
            elif output_format == ".3gp":
                video.write_videofile(
                    output_file_path,
                    codec='libx264',
                    audio_codec='aac',
                    threads=4,
                )
            elif output_format == ".ogv":
                video.write_videofile(
                    output_file_path,
                    codec='libtheora',
                    audio_codec='libvorbis',
                    threads=4,
                )
            elif output_format == ".vob":
                video.write_videofile(
                    output_file_path,
                    codec='mpeg2video',
                    audio_codec='mp2',
                    threads=4,
                )
            elif output_format == ".asf":
                video.write_videofile(
                    output_file_path,
                    codec='wmv2',
                    audio_codec='wmav2',
                    threads=4,
                )
            elif output_format == ".ts":
                video.write_videofile(
                    output_file_path,
                    codec='mpeg2video',
                    audio_codec='mp2',
                    threads=4,
                )
            elif output_format == ".swf":
                video.write_videofile(
                    output_file_path,
                    codec='flv',
                    audio_codec='aac',
                    threads=4,
                )
            elif output_format == ".f4v":
                video.write_videofile(
                    output_file_path,
                    codec='flv',
                    audio_codec='aac',
                    threads=4,
                )
            elif output_format == ".rmvb":
                video.write_videofile(
                    output_file_path,
                    codec='libx264',
                    audio_codec='aac',
                    threads=4,
                )
            else:
                raise ValueError("Неподдерживаемый формат видео")


            logging.info(f"Конвертация успешно завершена: {output_file_path}")

        except Exception as e:
            logging.error(f"Ошибка при конвертации видео: {e}")
            QMessageBox.critical(self, "Ошибка конвертации", f"Ошибка при конвертации видео: {str(e)}")
            print(f"Ошибка при конвертации видео: {str(e)}") 
            self.close()

    def convert_files(self):
        selected_files = self.file

        if not selected_files:
            QMessageBox.warning(self, "Предупреждение", "Нет выбранных файлов для конвертации.")
            return


        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения")
        if not folder_path:
            return

        output_format = self.FormatBox.currentText()  
        successful_files = []
        failed_files = []
        base_name = os.path.splitext(os.path.basename(selected_files))[0]
        output_file_path = os.path.join(folder_path, f"{base_name}.{output_format}")

        self.progressBar.setValue(0)
        self.convert_video(selected_files, output_file_path, output_format)


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
            answer = requests.post(f"{os.getenv('HOST')}/login", data=json.dumps(data), headers=headers)
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
            answer = requests.post(f"{os.getenv('HOST')}/register", data=json.dumps(data), headers=headers)
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
        answer = requests.post(f"{os.getenv('HOST')}/check_subscription", data=json.dumps(data),
                               headers=headers)
        content = answer.json()
        if content['has_subscription']:
            self.GetButton.setText("Уже подключено")
            self.GetButton.setEnabled(False)

    def get_premium(self):
        try:
            data = {"login": login}
            headers = {"Content-Type": "application/json"}
            answer = requests.post(f"{os.getenv('HOST')}/activate_subscription", data=json.dumps(data),
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
