# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QScreen)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from modules.jwt_encode import encode_jwt
from modules.jwt_decode import decode_jwt
from modules.verify_jwt import verify_signature
import json
import base64

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.screen = QApplication.primaryScreen().geometry()
        self.screen_width = self.screen.width()
        self.screen_height = self.screen.height()
        
        MainWindow.resize(int(self.screen_width // 2),
                    int(self.screen_height // 2))
        
        self.window_center()
        MainWindow.setWindowIcon(QIcon('./icon/jwt.ico'))
        self.verticalLayout_4 = QVBoxLayout(MainWindow)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 9, -1, -1)
        self.globalHorizontalLayout = QHBoxLayout()
        self.globalHorizontalLayout.setObjectName(u"globalHorizontalLayout")
        self.leftVerticalLayout = QVBoxLayout()
        self.leftVerticalLayout.setObjectName(u"leftVerticalLayout")
        self.encodedHorizontalLayout = QHBoxLayout()
        self.encodedHorizontalLayout.setObjectName(u"encodedHorizontalLayout")
        self.encodedLabel = QLabel(MainWindow)
        self.encodedLabel.setObjectName(u"encodedLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encodedLabel.sizePolicy().hasHeightForWidth())
        self.encodedLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Inconsolata LGC Nerd Font Mono"])
        font.setPointSize(16)
        font.setBold(True)
        self.encodedLabel.setFont(font)
        self.encodedLabel.setStyleSheet(u"font-weight:bold;")

        self.encodedHorizontalLayout.addWidget(self.encodedLabel)

        self.encodedExplainLabel = QLabel(MainWindow)
        self.encodedExplainLabel.setObjectName(u"encodedExplainLabel")
        font1 = QFont()
        font1.setFamilies([u"Inconsolata LGC Nerd Font Mono"])
        font1.setPointSize(8)
        self.encodedExplainLabel.setFont(font1)
        self.encodedExplainLabel.setStyleSheet(u"color: gray;")

        self.encodedHorizontalLayout.addWidget(self.encodedExplainLabel)


        self.leftVerticalLayout.addLayout(self.encodedHorizontalLayout)

        self.algorithmHorizontalLayout = QHBoxLayout()
        self.algorithmHorizontalLayout.setObjectName(u"algorithmHorizontalLayout")
        self.algorithmLabel = QLabel(MainWindow)
        self.algorithmLabel.setObjectName(u"algorithmLabel")
        sizePolicy.setHeightForWidth(self.algorithmLabel.sizePolicy().hasHeightForWidth())
        self.algorithmLabel.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Inconsolata LGC Nerd Font Mono"])
        font2.setPointSize(11)
        self.algorithmLabel.setFont(font2)

        self.algorithmHorizontalLayout.addWidget(self.algorithmLabel)

        self.algorithmComboBox = QComboBox(MainWindow)
        self.algorithmComboBox.setObjectName(u"algorithmComboBox")
        self.algorithmComboBox.addItem(u"HS256")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.algorithmComboBox.sizePolicy().hasHeightForWidth())
        self.algorithmComboBox.setSizePolicy(sizePolicy1)
        self.algorithmComboBox.setEditable(False)

        self.algorithmHorizontalLayout.addWidget(self.algorithmComboBox)

        self.algotithmHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.algorithmHorizontalLayout.addItem(self.algotithmHorizontalSpacer)


        self.leftVerticalLayout.addLayout(self.algorithmHorizontalLayout)

        self.encodedPlainTextEdit = QPlainTextEdit(MainWindow)
        self.encodedPlainTextEdit.setObjectName(u"encodedPlainTextEdit")
        font3 = QFont()
        font3.setFamilies([u"Inconsolata LGC Nerd Font Mono"])
        font3.setPointSize(14)
        self.encodedPlainTextEdit.setFont(font3)
        self.encodedPlainTextEdit.setProperty("tabStopWidth", 80)

        self.leftVerticalLayout.addWidget(self.encodedPlainTextEdit)

        self.statusLabel = QLabel(MainWindow)
        self.statusLabel.setObjectName(u"statusLabel")
        font4 = QFont()
        font4.setFamilies([u"Inconsolata LGC Nerd Font Mono"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.statusLabel.setFont(font4)
        self.statusLabel.setStyleSheet(u"color:green;font-weight:bold;")

        self.leftVerticalLayout.addWidget(self.statusLabel)


        self.globalHorizontalLayout.addLayout(self.leftVerticalLayout)

        self.midVerticalLayout = QVBoxLayout()
        self.midVerticalLayout.setObjectName(u"midVerticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.midVerticalLayout.addItem(self.verticalSpacer_2)

        self.encodeButton = QPushButton(MainWindow)
        self.encodeButton.setObjectName(u"encodeButton")

        self.midVerticalLayout.addWidget(self.encodeButton)

        self.decodeButton = QPushButton(MainWindow)
        self.decodeButton.setObjectName(u"decodeButton")

        self.midVerticalLayout.addWidget(self.decodeButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.midVerticalLayout.addItem(self.verticalSpacer)


        self.globalHorizontalLayout.addLayout(self.midVerticalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.decodedHorizontalLayout = QHBoxLayout()
        self.decodedHorizontalLayout.setObjectName(u"decodedHorizontalLayout")
        self.decodedLabel = QLabel(MainWindow)
        self.decodedLabel.setObjectName(u"decodedLabel")
        sizePolicy.setHeightForWidth(self.decodedLabel.sizePolicy().hasHeightForWidth())
        self.decodedLabel.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamilies([u"Inconsolata LGC Nerd Font"])
        font5.setPointSize(16)
        font5.setBold(True)
        self.decodedLabel.setFont(font5)
        self.decodedLabel.setStyleSheet(u"font-weight:bold;")

        self.decodedHorizontalLayout.addWidget(self.decodedLabel)

        self.decodedExplainLabel = QLabel(MainWindow)
        self.decodedExplainLabel.setObjectName(u"decodedExplainLabel")
        self.decodedExplainLabel.setFont(font1)
        self.decodedExplainLabel.setStyleSheet(u"color: gray;")

        self.decodedHorizontalLayout.addWidget(self.decodedExplainLabel)


        self.verticalLayout.addLayout(self.decodedHorizontalLayout)

        self.headerHorizontalLayout = QHBoxLayout()
        self.headerHorizontalLayout.setObjectName(u"headerHorizontalLayout")
        self.headerLabel = QLabel(MainWindow)
        self.headerLabel.setObjectName(u"headerLabel")
        sizePolicy.setHeightForWidth(self.headerLabel.sizePolicy().hasHeightForWidth())
        self.headerLabel.setSizePolicy(sizePolicy)
        self.headerLabel.setFont(font2)

        self.headerHorizontalLayout.addWidget(self.headerLabel)

        self.headerExplainLabel = QLabel(MainWindow)
        self.headerExplainLabel.setObjectName(u"headerExplainLabel")
        font6 = QFont()
        font6.setPointSize(8)
        self.headerExplainLabel.setFont(font6)
        self.headerExplainLabel.setStyleSheet(u"color: gray;")

        self.headerHorizontalLayout.addWidget(self.headerExplainLabel)


        self.verticalLayout.addLayout(self.headerHorizontalLayout)

        self.headerTextEdit = QPlainTextEdit(MainWindow)
        self.headerTextEdit.setObjectName(u"headerTextEdit")
        font7 = QFont()
        font7.setFamilies([u"Inconsolata LGC Nerd Font Mono"])
        font7.setPointSize(10)
        self.headerTextEdit.setFont(font7)

        self.verticalLayout.addWidget(self.headerTextEdit)

        self.payloadHorizontalLayout = QHBoxLayout()
        self.payloadHorizontalLayout.setObjectName(u"payloadHorizontalLayout")
        self.payloadLabel = QLabel(MainWindow)
        self.payloadLabel.setObjectName(u"payloadLabel")
        sizePolicy.setHeightForWidth(self.payloadLabel.sizePolicy().hasHeightForWidth())
        self.payloadLabel.setSizePolicy(sizePolicy)
        self.payloadLabel.setFont(font2)

        self.payloadHorizontalLayout.addWidget(self.payloadLabel)

        self.dataLabel = QLabel(MainWindow)
        self.dataLabel.setObjectName(u"dataLabel")
        self.dataLabel.setFont(font6)
        self.dataLabel.setStyleSheet(u"color: gray;")

        self.payloadHorizontalLayout.addWidget(self.dataLabel)


        self.verticalLayout.addLayout(self.payloadHorizontalLayout)

        self.payloadTextEdit = QPlainTextEdit(MainWindow)
        self.payloadTextEdit.setObjectName(u"payloadTextEdit")
        self.payloadTextEdit.setFont(font7)

        self.verticalLayout.addWidget(self.payloadTextEdit)

        self.signHorizontalLayout = QHBoxLayout()
        self.signHorizontalLayout.setObjectName(u"signHorizontalLayout")
        self.signLabel = QLabel(MainWindow)
        self.signLabel.setObjectName(u"signLabel")
        sizePolicy.setHeightForWidth(self.signLabel.sizePolicy().hasHeightForWidth())
        self.signLabel.setSizePolicy(sizePolicy)
        self.signLabel.setFont(font2)

        self.signHorizontalLayout.addWidget(self.signLabel)

        self.verifySignButton = QPushButton(MainWindow)
        self.verifySignButton.setObjectName(u"verifySignButton")

        self.signHorizontalLayout.addWidget(self.verifySignButton)

        self.base64CheckBox = QCheckBox(MainWindow)
        self.base64CheckBox.setObjectName(u"base64CheckBox")

        self.signHorizontalLayout.addWidget(self.base64CheckBox)

        self.signHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.signHorizontalLayout.addItem(self.signHorizontalSpacer)


        self.verticalLayout.addLayout(self.signHorizontalLayout)

        self.signTextEdit = QPlainTextEdit(MainWindow)
        self.signTextEdit.setObjectName(u"signTextEdit")
        self.signTextEdit.setFont(font7)

        self.verticalLayout.addWidget(self.signTextEdit)


        self.globalHorizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.globalHorizontalLayout)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"JWT IO UI", None))
        self.encodedLabel.setText(QCoreApplication.translate("MainWindow", u"Encoded", None))
        self.encodedExplainLabel.setText(QCoreApplication.translate("MainWindow", u"JWT Encoded Here", None))
        self.algorithmLabel.setText(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.algorithmComboBox.setCurrentText("")
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Signature Verified", None))
        self.encodeButton.setText(QCoreApplication.translate("MainWindow", u"<<加密", None))
        self.decodeButton.setText(QCoreApplication.translate("MainWindow", u"解密>>", None))
        self.decodedLabel.setText(QCoreApplication.translate("MainWindow", u"Decoded", None))
        self.decodedExplainLabel.setText(QCoreApplication.translate("MainWindow", u"Payload and secret", None))
        self.headerLabel.setText(QCoreApplication.translate("MainWindow", u"Header", None))
        self.headerExplainLabel.setText(QCoreApplication.translate("MainWindow", u"Algorithm & Token type", None))
        self.payloadLabel.setText(QCoreApplication.translate("MainWindow", u"Payload", None))
        self.dataLabel.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.signLabel.setText(QCoreApplication.translate("MainWindow", u"Verify Signature", None))
        self.verifySignButton.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u7b7e\u540d", None))
        self.base64CheckBox.setText(QCoreApplication.translate("MainWindow", u"secret base64 encode", None))
        self.encodedPlainTextEdit.setPlainText("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXBvIjoiaHR0cHM6Ly9naXRodWIuY29tL2NtYWNja2svand0LWlvLXVpIn0.UH5WhICLgjyVGdQDNlM4ekydtLMJNsrsEXVXUq7vIbc")
        self.decode()   # 先执行一次解密
        self.decodeButton.clicked.connect(self.decode)
        self.encodeButton.clicked.connect(self.encode)
        self.verifySignButton.clicked.connect(self.verify)
    # retranslateUi

    def window_center(self):
        """窗口居中
        """
        qt_rect = self.frameGeometry()
        center_point = QScreen.availableGeometry(
            QApplication.primaryScreen()).center()

        qt_rect.moveCenter(center_point)
        self.move(qt_rect.topLeft())

    def decode(self):
        """ jwt decode """
        header, payload = decode_jwt(self.encodedPlainTextEdit.toPlainText().strip())
        self.headerTextEdit.setPlainText(header)
        self.payloadTextEdit.setPlainText(payload)
        
    def encode(self):
        """ jwt encode """ 
        header = json.loads(self.headerTextEdit.toPlainText().strip())
        payload = json.loads(self.payloadTextEdit.toPlainText().strip())
        algorithm = self.algorithmComboBox.currentText().strip()
        secret = self.signTextEdit.toPlainText().strip()
        if self.base64CheckBox.isChecked():
            base64_secret = base64.b64encode(secret.encode()).decode('utf-8')
            jwt_token = encode_jwt(payload, header, base64_secret, algorithm)
        else:
            jwt_token = encode_jwt(payload, header, secret, algorithm)
        self.encodedPlainTextEdit.setPlainText(jwt_token)
        
    def verify(self):
        """ jwt verify """
        algorithm = self.algorithmComboBox.currentText().strip()
        secret = self.signTextEdit.toPlainText().strip()
        jwt_token = self.encodedPlainTextEdit.toPlainText().strip()
        if self.base64CheckBox.isChecked():
            base64_secret = base64.b64encode(secret.encode()).decode('utf-8')
            if verify_signature(jwt_token, base64_secret, algorithm):
                self.statusLabel.setText("Signature Verified")
                self.statusLabel.setStyleSheet("color:green;font-weight:bold;")
            else:
                self.statusLabel.setText("Invalid Signature")
                self.statusLabel.setStyleSheet("color:red;font-weight:bold;")
        else:
            if verify_signature(jwt_token, secret, algorithm):
                self.statusLabel.setText("Signature Verified")
                self.statusLabel.setStyleSheet("color:green;font-weight:bold;")
            else:
                self.statusLabel.setText("Invalid Signature")
                self.statusLabel.setStyleSheet("color:red;font-weight:bold;")