# -*- coding: utf-8 -*-

###############################################################################
# Lyrics finder using lyrics genius (genius)
##
# Created by: Raj singh chauhan
##
# want to contribute any type of new feature, solve or report a bug then go to
# Github - https://github.com/rajsingh010
###############################################################################
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import lyricsgenius as lg


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(762, 602)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(270, 130, 241, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 220, 81, 31))
        self.pushButton.clicked.connect(self.searchSong)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 10, 671, 31))
        self.label.setStyleSheet(u"font: 700 24pt \"Segoe Script\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 60, 221, 31))
        self.label_2.setStyleSheet(u"font: 16pt \"Segoe Print\";")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(120, 250, 551, 301))
        self.plainTextEdit.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 135, 81, 21))
        self.label_4.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 180, 81, 21))
        self.label_5.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(270, 175, 241, 31))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(530, 180, 61, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 762, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

    def searchSong(self, event):
        g = lg.Genius(
            '1I0L1b7M6PBFyT86ZT1WogdrMhubuRWWWNykJTENGMi3WyJuT5gvIQnBGzfvt9UE')
        song = self.lineEdit.text()
        name = self.lineEdit_2.text()
        info = g.search_song(song, name)
        self.plainTextEdit.setPlainText(
            QCoreApplication.translate("MainWindow", info.lyrics, None))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Lyrics Finder - github.com/rajsingh010", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"Find Lyrics", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Welcome to Lyrics Finder By Raj singh ", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Type the song name here", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Song Name", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Artist Name", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"*(optional)", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate(
            "MainWindow",
            u"You're lyrics or info will be displayed here", None))
        self.menuHelp.setTitle(
            QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuAbout.setTitle(
            QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication()
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
