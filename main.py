# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainRHquJB.ui'
##
# Created by: Qt User Interface Compiler version 6.1.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from splashScreen import Ui_SplashScreen

import lyricsgenius as lg


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(795, 604)
        MainWindow.setStyleSheet(u"background-color:rgb(56, 50, 89);\n"
                                 "color:rgb(255, 255, 255);\n"
                                 "background-image:'./assets/tree-moon.jpg'")
        self.actionOnline_help = QAction(MainWindow)
        self.actionOnline_help.setObjectName(u"actionOnline_help")
        self.actionQuick_tutorial = QAction(MainWindow)
        self.actionQuick_tutorial.setObjectName(u"actionQuick_tutorial")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 70, 771, 491))
        font = QFont()
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"color:rgb(0, 255, 0)")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(530, 70, 91, 20))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(310, 70, 201, 31))
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(310, 30, 201, 31))
        self.textBrowser = QTextBrowser(self.tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(110, 170, 541, 281))
        self.textBrowser.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(139, 31, 111, 21))
        self.label_3.setFont(font1)
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 120, 101, 41))
        self.pushButton.clicked.connect(self.searchSong)
        self.pushButton.setIcon(QIcon('./assets/find.png'))
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(139, 81, 141, 16))
        self.label_4.setFont(font1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(270, 70, 201, 31))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(490, 60, 161, 51))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:rgba(255, 31, 38, 227)")
        self.lineEdit_4 = QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(270, 30, 201, 31))
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(99, 31, 111, 21))
        self.label_6.setFont(font1)
        self.textBrowser_2 = QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(70, 170, 541, 281))
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(99, 81, 141, 16))
        self.label_7.setFont(font1)
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 120, 101, 41))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lineEdit_5 = QLineEdit(self.tab_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(310, 40, 201, 31))
        self.textBrowser_3 = QTextBrowser(self.tab_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(110, 140, 541, 281))
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(139, 51, 141, 16))
        self.label_8.setFont(font1)
        self.pushButton_3 = QPushButton(self.tab_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(320, 90, 101, 41))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.lineEdit_6 = QLineEdit(self.tab_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(310, 30, 201, 31))
        self.textBrowser_4 = QTextBrowser(self.tab_4)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(110, 170, 541, 281))
        self.label_9 = QLabel(self.tab_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(139, 41, 141, 16))
        self.label_9.setFont(font1)
        self.pushButton_4 = QPushButton(self.tab_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(320, 120, 101, 41))
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(140, 70, 141, 81))
        self.label_10.setFont(font1)
        self.lineEdit_7 = QLineEdit(self.tab_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(311, 69, 201, 31))
        self.tabWidget.addTab(self.tab_4, "")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-20, -10, 791, 71))
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setStrikeOut(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color:rgb(255, 114, 253);")
        self.label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 795, 22))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionOnline_help)
        self.menuHelp.addAction(self.actionQuick_tutorial)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def searchSong(self, event):
        g = lg.Genius(
            '1I0L1b7M6PBFyT86ZT1WogdrMhubuRWWWNykJTENGMi3WyJuT5gvIQnBGzfvt9UE')
        song = self.lineEdit.text()
        name = self.lineEdit_2.text()
        info = g.search_song(song, name)
        self.textBrowser.setPlainText(
            QCoreApplication.translate("MainWindow", info.lyrics, None))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"PyLyricFinder", None))
        self.actionOnline_help.setText(
            QCoreApplication.translate("MainWindow", u"Online help", None))
        self.actionQuick_tutorial.setText(
            QCoreApplication.translate("MainWindow", u"Quick tutorial", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"(*Optional)", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is where lyrics shows up.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Name of song", None))
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Name of the artist", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), QCoreApplication.translate("MainWindow", u"Search Lyrics", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-weight:400; font-style:italic;\">*(If song is popular than </span></p><p><span style=\" font-weight:400; font-style:italic;\">name is not needed.)</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Name of song", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Name of artist", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Find", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), QCoreApplication.translate("MainWindow", u"Song Info", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Name of artist", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", u"Find", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_3), QCoreApplication.translate("MainWindow", u"Artist Info", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Name of Album", None))
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Name of artist</p><p><span style=\" font-weight:400; font-style:italic;\">(If it has one artist else</span></p><p><span style=\" font-weight:400; font-style:italic;\">leave it blank.)</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_4), QCoreApplication.translate("MainWindow", u"Album Info", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Welcome to PyLyricFinder</p></body></html>", None))
        self.menuAbout.setTitle(
            QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(
            QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication()
    splashScreen_ = QWidget()
    MainWindow = QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    for i in range(100):
        loop = QEventLoop()
        QTimer.singleShot(20, loop.quit)
        ui.progressBar.setValue(i + 1)
        loop.exec()
    MainWindow = QMainWindow()
    MainWindow.setWindowIcon(QIcon('./assets/favicon.ico'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
