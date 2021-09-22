# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maineByCdN.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


from splashScreen import Ui_SplashScreen

import lyricsgenius as lg
g = lg.Genius('1I0L1b7M6PBFyT86ZT1WogdrMhubuRWWWNykJTENGMi3WyJuT5gvIQnBGzfvt9UE')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(761, 604)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"C:/Users/Lenovo/.designer/backup/assets/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.tabWidget.setGeometry(QRect(10, 70, 741, 491))
        font = QFont()
        font.setBold(True)
        font.setUnderline(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #00ff00;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 5px solid #00ff00;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(181, 175, 190, 213), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.4"
                        "25 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #00ff00;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"/* make use of negative margins for overlapping tabs */\n"
"QTabBar::tab:selected {\n"
"    /* expand/overlap to the left and right by 4px */\n"
"    margin-left: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"")
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
        self.tab.setAutoFillBackground(False)
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(261, 59, 261, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	border-radius:8px;\n"
"}")
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(261, 19, 261, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	border-radius:8px;\n"
"}")
        self.textBrowser = QTextBrowser(self.tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(40, 160, 651, 291))
        self.textBrowser.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textBrowser.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color:black;\n"
"border-radius:8px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.534, x2:1, y2:0.5, stop:0.164773 rgba(255, 96, 165, 251), stop:1 rgba(255, 255, 255, 255));\n"
"border: 2px solid rgb(255, 255, 255);\n"
"")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 20, 111, 21))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(311, 109, 101, 41))
        self.pushButton.clicked.connect(self.searchLyrics)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 800 italic 12pt \"Segoe UI\";\n"
"	color:black;\n"
"    border: 2px solid #8f8f91;\n"
"	border-radius:10px;\n"
"	background-color:rgb(200, 62, 255)\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:green;\n"
"}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 70, 141, 16))
        self.label_4.setFont(font1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(540, 60, 161, 51))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:rgba(255, 31, 38, 227)")
        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(261, 19, 261, 31))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	border-radius:8px;\n"
"}")
        self.textBrowser_2 = QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(40, 160, 651, 291))
        self.textBrowser_2.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textBrowser_2.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color:black;\n"
"border-radius:8px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.534, x2:1, y2:0.5, stop:0.164773 rgba(255, 96, 165, 251), stop:1 rgba(255, 255, 255, 255));\n"
"border: 2px solid rgb(255, 255, 255);\n"
"")
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(311, 109, 101, 41))
        self.pushButton_2.clicked.connect(self.SongInfo)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 800 italic 12pt \"Segoe UI\";\n"
"	color:black;\n"
"    border: 2px solid #8f8f91;\n"
"	border-radius:10px;\n"
"	background-color:rgb(200, 62, 255)\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:green;\n"
"}")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(False)
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 20, 111, 21))
        self.label_6.setFont(font1)
        self.lineEdit_4 = QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(261, 59, 261, 31))
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	border-radius:8px;\n"
"}")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 70, 141, 16))
        self.label_7.setFont(font1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lineEdit_5 = QLineEdit(self.tab_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(261, 19, 201, 31))
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	border-radius:8px;\n"
"}")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 30, 141, 16))
        self.label_8.setFont(font1)
        self.pushButton_3 = QPushButton(self.tab_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(320, 110, 101, 41))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 800 italic 12pt \"Segoe UI\";\n"
"	color:black;\n"
"    border: 2px solid #8f8f91;\n"
"	border-radius:10px;\n"
"	background-color:rgb(200, 62, 255)\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:green;\n"
"}")
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(480, 20, 101, 81))
        self.label_11.setFont(font1)
        self.spinBox = QSpinBox(self.tab_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(580, 20, 61, 22))
        self.spinBox.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.spinBox.setMaximum(100)
        self.spinBox.setValue(3)
        self.comboBox = QComboBox(self.tab_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(260, 70, 111, 22))
        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(90, 70, 151, 16))
        self.label_12.setFont(font1)
        self.textBrowser_3 = QTextBrowser(self.tab_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(50, 160, 651, 291))
        self.pushButton_3.clicked.connect(self.ArtistInfo)
        self.textBrowser_3.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textBrowser_3.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color:black;\n"
"border-radius:8px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.534, x2:1, y2:0.5, stop:0.164773 rgba(255, 96, 165, 251), stop:1 rgba(255, 255, 255, 255));\n"
"border: 2px solid rgb(255, 255, 255);\n"
"")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.lineEdit_6 = QLineEdit(self.tab_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(219, 31, 201, 31))
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	border-radius:8px;\n"
"}")
        self.textBrowser_4 = QTextBrowser(self.tab_4)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(50, 170, 541, 281))
        self.textBrowser_4.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.label_9 = QLabel(self.tab_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(48, 32, 141, 16))
        self.label_9.setFont(font1)
        self.pushButton_4 = QPushButton(self.tab_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(300, 120, 101, 41))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 800 italic 12pt \"Segoe UI\";\n"
"	color:black;\n"
"    border: 2px solid #8f8f91;\n"
"	border-radius:10px;\n"
"	background-color:rgb(200, 62, 255)\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:green;\n"
"}")
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(49, 61, 141, 81))
        self.label_10.setFont(font1)
        self.lineEdit_7 = QLineEdit(self.tab_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(220, 70, 201, 31))
        self.lineEdit_7.setStyleSheet(u"QLineEdit{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	border-radius:8px;\n"
"}")
        self.tabWidget.addTab(self.tab_4, "")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-20, -10, 791, 71))
        font2 = QFont()
        font2.setPointSize(35)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setStrikeOut(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color:rgb(255, 114, 253);\n"
"font: 700 italic 35pt \"Harlow Solid Italic\";")
        self.label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 761, 22))
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
        self.pushButton.setDefault(False)
        self.pushButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def searchLyrics(self, event):
        song = self.lineEdit.text()
        name = self.lineEdit_2.text()
        info = g.search_song(song, name)
        self.textBrowser.setPlainText(
            QCoreApplication.translate("MainWindow", info.lyrics, None))

    def SongInfo(self, event):
        song = self.lineEdit_3.text()
        name = self.lineEdit_4.text()
        info = g.search_song(song, name, get_full_info=True)
        text = {'Song Name': info.title,'Artist': info.artist, 'Song Art Image Url': info.song_art_image_url, 'Lyrics': info.lyrics}
        full_text = ''
        for i in text.keys():
            full_text += f'{i}  :  {text[i]} \n'
        self.textBrowser_2.setPlainText(
            QCoreApplication.translate("MainWindow", full_text))

    def ArtistInfo(self, even):
        name = self.lineEdit_5.text()
        max_songs = self.spinBox.value()
        sort = self.comboBox.currentIndex()
        artist = g.search_artist(name,max_songs=int(max_songs), allow_name_change=True)
        text = {'Name': artist.name, "Artist's Photo": artist.image_url, 'Songs(as per your search)': artist.song}
        full_text = ''
        for i in text.keys():
            full_text += f'{i}  :  {text[i]} \n'
        self.textBrowser_3.setPlainText(
            QCoreApplication.translate("MainWindow", full_text))



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyLyricFinder", None))
        self.actionOnline_help.setText(QCoreApplication.translate("MainWindow", u"Online help", None))
        self.actionQuick_tutorial.setText(QCoreApplication.translate("MainWindow", u"Quick tutorial", None))
#if QT_CONFIG(statustip)
        self.tabWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(statustip)
        self.tab.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.tab.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is where lyrics shows up.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name of song*", None))
#if QT_CONFIG(whatsthis)
        self.pushButton.setWhatsThis(QCoreApplication.translate("MainWindow", u"Search those lyrics", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Name of the artist", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Search Lyrics", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400; font-style:italic;\">*(If song is popular than </span></p><p><span style=\" font-weight:400; font-style:italic;\">name is not needed.)</span></p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Your Info will show up here.</p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"Search those lyrics", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Name of song", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Name of the artist", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Song Info", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Name of artist", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Max songs</p><p><span style=\" font-weight:400; font-style:italic;\">(left five for </span></p><p><span style=\" font-weight:400; font-style:italic;\">default search)</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Title", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Popularity", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Sort song names by", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Searching about artist may take upto 10 seconds</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Reasons are-</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1) Your Internet speed.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	 "
                        "         2) we also have to search for so many things like all songs you acc. to number in spin box of max songs, etc.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Artist Info", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Name of Album", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Name of artist</p><p><span style=\" font-weight:400; font-style:italic;\">(If it has one artist else</span></p><p><span style=\" font-weight:400; font-style:italic;\">leave it blank.)</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Album Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:normal;\">Welcome to PyLyricFinder</span></p></body></html>", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
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
