# Form implementation generated from reading ui file 'solo_load.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(933, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/img/AppLogo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.header = QtWidgets.QFrame(parent=Form)
        self.header.setGeometry(QtCore.QRect(0, 0, 933, 42))
        self.header.setStyleSheet("#header{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(59, 59, 59, 255), stop:1 rgba(49, 49, 49, 255));\n"
"    border-top-right-radius: 12px;\n"
"    border-top-left-radius: 12px;\n"
"}\n"
"\n"
".QToolButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: white\n"
"}\n"
"\n"
".QToolButton:hover{\n"
"    background-color: rgba(0, 0, 0, 50);\n"
"}")
        self.header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header.setObjectName("header")
        self.Title = QtWidgets.QLabel(parent=self.header)
        self.Title.setGeometry(QtCore.QRect(350, 9, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title.setObjectName("Title")
        self.CloseButton = QtWidgets.QToolButton(parent=self.header)
        self.CloseButton.setGeometry(QtCore.QRect(897, 6, 30, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/img/iconamoon_close-light.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.CloseButton.setIcon(icon1)
        self.CloseButton.setIconSize(QtCore.QSize(24, 24))
        self.CloseButton.setObjectName("CloseButton")
        self.HideButton = QtWidgets.QToolButton(parent=self.header)
        self.HideButton.setGeometry(QtCore.QRect(865, 6, 30, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/img/mynaui_minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.HideButton.setIcon(icon2)
        self.HideButton.setIconSize(QtCore.QSize(24, 24))
        self.HideButton.setObjectName("HideButton")
        self.Icon = QtWidgets.QLabel(parent=self.header)
        self.Icon.setGeometry(QtCore.QRect(9, 9, 24, 24))
        self.Icon.setText("")
        self.Icon.setPixmap(QtGui.QPixmap("res/img/Vector.png"))
        self.Icon.setObjectName("Icon")
        self.content = QtWidgets.QFrame(parent=Form)
        self.content.setGeometry(QtCore.QRect(0, 42, 933, 507))
        self.content.setStyleSheet("#content{\n"
"    background-color: rgb(59, 59, 59);\n"
"    border-bottom-left-radius: 12px;\n"
"    border-bottom-right-radius: 12px;\n"
"}\n"
"\n"
".QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(235, 46, 65, 255), stop:1 rgba(208, 0, 76, 255));\n"
"    border-radius: 12px;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.FileName = QtWidgets.QLineEdit(parent=self.content)
        self.FileName.setGeometry(QtCore.QRect(470, 30, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.FileName.setFont(font)
        self.FileName.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.FileName.setReadOnly(True)
        self.FileName.setObjectName("FileName")
        self.preview = QtWidgets.QFrame(parent=self.content)
        self.preview.setGeometry(QtCore.QRect(30, 29, 411, 231))
        self.preview.setStyleSheet("#preview{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(59, 59, 59, 255), stop:1 rgba(49, 49, 49, 255));\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(255, 255, 255, 20);\n"
"}")
        self.preview.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.preview.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.preview.setObjectName("preview")
        self.label = QtWidgets.QLabel(parent=self.preview)
        self.label.setGeometry(QtCore.QRect(160, 60, 92, 92))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("res/img/iconamoon_file-light.png"))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(parent=self.content)
        self.progressBar.setGeometry(QtCore.QRect(40, 390, 851, 5))
        self.progressBar.setStyleSheet(".QProgressBar{\n"
"    background-color: rgba(0, 0, 0, 30);\n"
"    max-height: 5px;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
".QProgressBar:chunk{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(235, 46, 65, 255), stop:1 rgba(208, 0, 76, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.widget = QtWidgets.QWidget(parent=self.content)
        self.widget.setGeometry(QtCore.QRect(40, 310, 851, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Title_5 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        self.Title_5.setFont(font)
        self.Title_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Title_5.setWordWrap(True)
        self.Title_5.setObjectName("Title_5")
        self.horizontalLayout.addWidget(self.Title_5)
        self.PathTosave = QtWidgets.QLineEdit(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PathTosave.sizePolicy().hasHeightForWidth())
        self.PathTosave.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.PathTosave.setFont(font)
        self.PathTosave.setStyleSheet("    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(59, 59, 59, 255), stop:1 rgba(49, 49, 49, 255));\n"
"border-radius: 7px;\n"
"border: 1px solid rgba(255, 255, 255, 20);\n"
"color: white;")
        self.PathTosave.setReadOnly(True)
        self.PathTosave.setObjectName("PathTosave")
        self.horizontalLayout.addWidget(self.PathTosave)
        self.PathEditButton = QtWidgets.QToolButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PathEditButton.sizePolicy().hasHeightForWidth())
        self.PathEditButton.setSizePolicy(sizePolicy)
        self.PathEditButton.setStyleSheet("    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(59, 59, 59, 255), stop:1 rgba(49, 49, 49, 255));\n"
"border-radius: 7px;\n"
"border: 1px solid rgba(255, 255, 255, 20);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("res/img/material-symbols_edit-outline-rounded.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.PathEditButton.setIcon(icon3)
        self.PathEditButton.setIconSize(QtCore.QSize(24, 24))
        self.PathEditButton.setObjectName("PathEditButton")
        self.horizontalLayout.addWidget(self.PathEditButton)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 15)
        self.horizontalLayout.setStretch(2, 2)
        self.widget1 = QtWidgets.QWidget(parent=self.content)
        self.widget1.setGeometry(QtCore.QRect(470, 110, 421, 150))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("res/img/iconamoon_file-light.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Title_2 = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.Title_2.setFont(font)
        self.Title_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Title_2.setWordWrap(True)
        self.Title_2.setObjectName("Title_2")
        self.verticalLayout.addWidget(self.Title_2)
        self.OriginalFormat = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.OriginalFormat.setFont(font)
        self.OriginalFormat.setStyleSheet("color: rgb(255, 255, 255);")
        self.OriginalFormat.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.OriginalFormat.setWordWrap(True)
        self.OriginalFormat.setObjectName("OriginalFormat")
        self.verticalLayout.addWidget(self.OriginalFormat)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.label_4 = QtWidgets.QLabel(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("res/img/pajamas_long-arrow.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("res/img/fluent-mdl2_completed.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Title_4 = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.Title_4.setFont(font)
        self.Title_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Title_4.setWordWrap(True)
        self.Title_4.setObjectName("Title_4")
        self.verticalLayout_4.addWidget(self.Title_4)
        self.FormatBox = QtWidgets.QComboBox(parent=self.widget1)
        self.FormatBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.534, y1:0, x2:0.506, y2:1, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(74, 74, 74, 255));\n"
"border-radius: 12px;\n"
"border: 1px solid rgba(255, 255, 255, 20);\n"
"color: white;\n"
"\n"
"")
        self.FormatBox.setObjectName("FormatBox")
        self.verticalLayout_4.addWidget(self.FormatBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.widget2 = QtWidgets.QWidget(parent=self.content)
        self.widget2.setGeometry(QtCore.QRect(40, 420, 851, 51))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(24)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.CloudConvertButton = QtWidgets.QPushButton(parent=self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloudConvertButton.sizePolicy().hasHeightForWidth())
        self.CloudConvertButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Medium")
        font.setPointSize(12)
        self.CloudConvertButton.setFont(font)
        self.CloudConvertButton.setObjectName("CloudConvertButton")
        self.horizontalLayout_3.addWidget(self.CloudConvertButton)
        self.ConvertButton = QtWidgets.QPushButton(parent=self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConvertButton.sizePolicy().hasHeightForWidth())
        self.ConvertButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Medium")
        font.setPointSize(12)
        self.ConvertButton.setFont(font)
        self.ConvertButton.setObjectName("ConvertButton")
        self.horizontalLayout_3.addWidget(self.ConvertButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Конвертация файла"))
        self.Title.setText(_translate("Form", "Конвертировать файл"))
        self.CloseButton.setText(_translate("Form", "..."))
        self.HideButton.setText(_translate("Form", "..."))
        self.Title_5.setText(_translate("Form", "Путь сохранения:"))
        self.PathEditButton.setText(_translate("Form", "..."))
        self.Title_2.setText(_translate("Form", "Оригинальный файл"))
        self.OriginalFormat.setText(_translate("Form", ".ext"))
        self.Title_4.setText(_translate("Form", "Конвертированный файл"))
        self.CloudConvertButton.setText(_translate("Form", "Облачная конвертация"))
        self.ConvertButton.setText(_translate("Form", "Конвертировать"))
