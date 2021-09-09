# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'designerIuufvb.ui'
##
# Created by: Qt User Interface Compiler version 6.1.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import sys


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):

        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
            SplashScreen.setEnabled(False)

            # Removing Frame (windows default frame with close and resize)
            SplashScreen.setWindowFlag(Qt.FramelessWindowHint)
            # Making background translucent
            # (so it won't appear like white border)
            SplashScreen.setAttribute(Qt.WA_TranslucentBackground)

            # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(SplashScreen)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))

        SplashScreen.resize(660, 314)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"dropShadowFrame")
        self.frame.setCursor(QCursor(Qt.BusyCursor))
        self.frame.setStyleSheet(u"QFrame{\n"
                                 "      background-color:rgb(56, 50, 89);\n"
                                 "      color:rgb(220, 220, 220);\n"
                                 "      border-radius:10px;\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.frame.setGraphicsEffect(self.shadow)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(0, 30, 641, 81))
        font = QFont()
        font.setPointSize(43)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.ArrowCursor))
        self.label.setStyleSheet(u"QLabel{\n"
                                 "      color:rgb(255, 114, 253);\n"
                                 "}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 110, 641, 31))
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setCursor(QCursor(Qt.ArrowCursor))
        self.label_2.setStyleSheet(u"QLabel{\n"
                                   "    color:rgb(255, 114, 253);\n"
                                   "}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 190, 581, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
                                       "        background-color:rgb(50, 114, 164);\n"
                                       "        color:rgb(0,0,0);\n"
                                       "        border-style:None;\n"
                                       "        border-radius:10px;\n"
                                       "        text-align:centre;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "        background-color:qlineargradient(spread:pad, x1:0, y1:0.534, x2:1, y2:0.5, stop:0.164773 rgba(255, 96, 165, 251), stop:1 rgba(255, 255, 255, 255))\n"
                                       "        \n"
                                       "}")
        self.progressBar.setValue(24)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 210, 641, 31))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.label_3.setCursor(QCursor(Qt.ArrowCursor))
        self.label_3.setStyleSheet(u"QLabel{\n"
                                   "    color:rgb(255, 114, 253);\n"
                                   "}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
        # setupUi

    def retranslateUi(self, SplashScreen):

        SplashScreen.setWindowTitle(QCoreApplication.translate(
            "SplashScreen", u"MainWindow", None))
        # if QT_CONFIG(whatsthis)
        SplashScreen.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate(
            "SplashScreen", u"<html><head/><body><p>PyLyricFinder</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate(
            "SplashScreen", u"Now enjoy your favourite songs with lyrics for free", None))
        self.label_3.setText(QCoreApplication.translate(
            "SplashScreen", u"Loading.....", None))
        # retranslateUi


if __name__ == "__main__":
    app = QApplication()
    MainWindow = QMainWindow()
    MainWindow.setWindowIcon(QIcon('./assets/favicon.ico'))
    ui = Ui_SplashScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    for i in range(100):
        loop = QEventLoop()
        QTimer.singleShot(20, loop.quit)
        ui.progressBar.setValue(i + 1)
        loop.exec()
    sys.exit()
    app.exec()