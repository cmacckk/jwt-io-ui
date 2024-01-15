# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secretCrack.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_CrackForm(object):
    def setupUi(self, CrackForm):
        if not CrackForm.objectName():
            CrackForm.setObjectName(u"CrackForm")
        CrackForm.resize(865, 774)
        self.verticalLayout_2 = QVBoxLayout(CrackForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.crackSecretLabel = QLabel(CrackForm)
        self.crackSecretLabel.setObjectName(u"crackSecretLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crackSecretLabel.sizePolicy().hasHeightForWidth())
        self.crackSecretLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.crackSecretLabel.setFont(font)
        self.crackSecretLabel.setStyleSheet(u"font-weight:bold;")

        self.horizontalLayout.addWidget(self.crackSecretLabel)

        self.crackSecretExplainLabel = QLabel(CrackForm)
        self.crackSecretExplainLabel.setObjectName(u"crackSecretExplainLabel")
        self.crackSecretExplainLabel.setStyleSheet(u"color:gray;")

        self.horizontalLayout.addWidget(self.crackSecretExplainLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.label = QLabel(CrackForm)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font-weight:bold;")

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(CrackForm)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.encodedHorizontalLayout = QHBoxLayout()
        self.encodedHorizontalLayout.setObjectName(u"encodedHorizontalLayout")
        self.encodedLabel = QLabel(CrackForm)
        self.encodedLabel.setObjectName(u"encodedLabel")
        sizePolicy.setHeightForWidth(self.encodedLabel.sizePolicy().hasHeightForWidth())
        self.encodedLabel.setSizePolicy(sizePolicy)
        self.encodedLabel.setFont(font)
        self.encodedLabel.setStyleSheet(u"font-weight:bold;")

        self.encodedHorizontalLayout.addWidget(self.encodedLabel)

        self.encodedExplainLabel = QLabel(CrackForm)
        self.encodedExplainLabel.setObjectName(u"encodedExplainLabel")
        self.encodedExplainLabel.setStyleSheet(u"color:gray;")

        self.encodedHorizontalLayout.addWidget(self.encodedExplainLabel)


        self.verticalLayout.addLayout(self.encodedHorizontalLayout)

        self.plainTextEdit = QPlainTextEdit(CrackForm)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font2 = QFont()
        font2.setPointSize(11)
        self.plainTextEdit.setFont(font2)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.dictionaryHorizontalLayout = QHBoxLayout()
        self.dictionaryHorizontalLayout.setObjectName(u"dictionaryHorizontalLayout")
        self.dictionaryLabel = QLabel(CrackForm)
        self.dictionaryLabel.setObjectName(u"dictionaryLabel")
        sizePolicy.setHeightForWidth(self.dictionaryLabel.sizePolicy().hasHeightForWidth())
        self.dictionaryLabel.setSizePolicy(sizePolicy)
        self.dictionaryLabel.setFont(font)
        self.dictionaryLabel.setStyleSheet(u"font-weight:bold;")

        self.dictionaryHorizontalLayout.addWidget(self.dictionaryLabel)

        self.dictionaryExplainLabel = QLabel(CrackForm)
        self.dictionaryExplainLabel.setObjectName(u"dictionaryExplainLabel")
        self.dictionaryExplainLabel.setStyleSheet(u"color:gray;")

        self.dictionaryHorizontalLayout.addWidget(self.dictionaryExplainLabel)


        self.verticalLayout.addLayout(self.dictionaryHorizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.fileLineEdit = QLineEdit(CrackForm)
        self.fileLineEdit.setObjectName(u"fileLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fileLineEdit.sizePolicy().hasHeightForWidth())
        self.fileLineEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.fileLineEdit)

        self.selectFileButton = QPushButton(CrackForm)
        self.selectFileButton.setObjectName(u"selectFileButton")

        self.horizontalLayout_4.addWidget(self.selectFileButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.startButton = QPushButton(CrackForm)
        self.startButton.setObjectName(u"startButton")

        self.horizontalLayout_5.addWidget(self.startButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.infoHorizontalLayout = QHBoxLayout()
        self.infoHorizontalLayout.setObjectName(u"infoHorizontalLayout")
        self.infoLabel = QLabel(CrackForm)
        self.infoLabel.setObjectName(u"infoLabel")
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setFont(font)
        self.infoLabel.setStyleSheet(u"font-weight:bold;")

        self.infoHorizontalLayout.addWidget(self.infoLabel)

        self.infoExplainLabel = QLabel(CrackForm)
        self.infoExplainLabel.setObjectName(u"infoExplainLabel")
        self.infoExplainLabel.setStyleSheet(u"color: gray;")

        self.infoHorizontalLayout.addWidget(self.infoExplainLabel)


        self.verticalLayout.addLayout(self.infoHorizontalLayout)

        self.resultPlainTextEdit = QPlainTextEdit(CrackForm)
        self.resultPlainTextEdit.setObjectName(u"resultPlainTextEdit")
        self.resultPlainTextEdit.setFont(font2)

        self.verticalLayout.addWidget(self.resultPlainTextEdit)

        self.progressBar = QProgressBar(CrackForm)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(CrackForm)

        QMetaObject.connectSlotsByName(CrackForm)
    # setupUi

    def retranslateUi(self, CrackForm):
        CrackForm.setWindowTitle(QCoreApplication.translate("CrackForm", u"JWT Secret Crack", None))
        self.crackSecretLabel.setText(QCoreApplication.translate("CrackForm", u"Crack", None))
        self.crackSecretExplainLabel.setText(QCoreApplication.translate("CrackForm", u"crack json web token secret", None))
        self.label.setText(QCoreApplication.translate("CrackForm", u"Algorithm", None))
        self.encodedLabel.setText(QCoreApplication.translate("CrackForm", u"Encoded", None))
        self.encodedExplainLabel.setText(QCoreApplication.translate("CrackForm", u"JWT encoded here", None))
        self.dictionaryLabel.setText(QCoreApplication.translate("CrackForm", u"Dictionary", None))
        self.dictionaryExplainLabel.setText(QCoreApplication.translate("CrackForm", u"Dictionary file here", None))
        self.selectFileButton.setText(QCoreApplication.translate("CrackForm", u"\u9009\u62e9\u6587\u4ef6", None))
        self.startButton.setText(QCoreApplication.translate("CrackForm", u"\u5f00\u59cb", None))
        self.infoLabel.setText(QCoreApplication.translate("CrackForm", u"Result", None))
        self.infoExplainLabel.setText(QCoreApplication.translate("CrackForm", u"running info", None))
    # retranslateUi

