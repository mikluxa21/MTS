# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)
import file_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1022, 600)
        icon = QIcon()
        icon.addFile(u"icons/index.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"background-color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBatton: hover{\n"
"background-color: #888;\n"
"}")
        MainWindow.setIconSize(QSize(40, 40))
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionExel = QAction(MainWindow)
        self.actionExel.setObjectName(u"actionExel")
        self.Save = QAction(MainWindow)
        self.Save.setObjectName(u"Save")
        self.Save_as_exel = QAction(MainWindow)
        self.Save_as_exel.setObjectName(u"Save_as_exel")
        self.Save_as_csv = QAction(MainWindow)
        self.Save_as_csv.setObjectName(u"Save_as_csv")
        self.Save_as_txt = QAction(MainWindow)
        self.Save_as_txt.setObjectName(u"Save_as_txt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet(u"background-color: rgb(254, 0, 0);\n"
"color: white;\n"
"font-size: 15pt;")
        self.pushButton.setAutoRepeatInterval(100)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMaximumSize(QSize(601, 16777215))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1022, 22))
        self.Sort = QMenu(self.menubar)
        self.Sort.setObjectName(u"Sort")
        self.Fail = QMenu(self.menubar)
        self.Fail.setObjectName(u"Fail")
        self.Save_as = QMenu(self.Fail)
        self.Save_as.setObjectName(u"Save_as")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.Fail.menuAction())
        self.menubar.addAction(self.Sort.menuAction())
        self.Fail.addAction(self.Save)
        self.Fail.addAction(self.Save_as.menuAction())
        self.Save_as.addAction(self.Save_as_exel)
        self.Save_as.addAction(self.Save_as_csv)
        self.Save_as.addAction(self.Save_as_txt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0422\u0421", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.actionExel.setText(QCoreApplication.translate("MainWindow", u"Exel", None))
        self.Save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.Save_as_exel.setText(QCoreApplication.translate("MainWindow", u"Exel", None))
        self.Save_as_csv.setText(QCoreApplication.translate("MainWindow", u"csv", None))
        self.Save_as_txt.setText(QCoreApplication.translate("MainWindow", u"txt", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Example_1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Example_2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Example_3", None))

        self.Sort.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.Fail.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.Save_as.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None))
    # retranslateUi

