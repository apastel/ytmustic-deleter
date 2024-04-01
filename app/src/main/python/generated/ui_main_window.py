# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 685)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.removeLibraryButton = QPushButton(self.centralWidget)
        self.removeLibraryButton.setObjectName(u"removeLibraryButton")
        self.removeLibraryButton.setGeometry(QRect(220, 140, 101, 41))
        self.consoleTextArea = QPlainTextEdit(self.centralWidget)
        self.consoleTextArea.setObjectName(u"consoleTextArea")
        self.consoleTextArea.setGeometry(QRect(40, 320, 811, 311))
        self.consoleTextArea.setReadOnly(True)
        self.deleteUploadsButton = QPushButton(self.centralWidget)
        self.deleteUploadsButton.setObjectName(u"deleteUploadsButton")
        self.deleteUploadsButton.setGeometry(QRect(330, 140, 101, 41))
        self.consoleLabel = QLabel(self.centralWidget)
        self.consoleLabel.setObjectName(u"consoleLabel")
        self.consoleLabel.setGeometry(QRect(50, 300, 81, 21))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.consoleLabel.setFont(font)
        self.signInButton = QPushButton(self.centralWidget)
        self.signInButton.setObjectName(u"signInButton")
        self.signInButton.setGeometry(QRect(770, 20, 81, 41))
        font1 = QFont()
        font1.setBold(True)
        self.signInButton.setFont(font1)
        self.deletePlaylistsButton = QPushButton(self.centralWidget)
        self.deletePlaylistsButton.setObjectName(u"deletePlaylistsButton")
        self.deletePlaylistsButton.setGeometry(QRect(440, 140, 101, 41))
        self.unlikeAllButton = QPushButton(self.centralWidget)
        self.unlikeAllButton.setObjectName(u"unlikeAllButton")
        self.unlikeAllButton.setGeometry(QRect(550, 140, 101, 41))
        self.deleteAllButton = QPushButton(self.centralWidget)
        self.deleteAllButton.setObjectName(u"deleteAllButton")
        self.deleteAllButton.setGeometry(QRect(40, 140, 121, 41))
        self.sortPlaylistButton = QPushButton(self.centralWidget)
        self.sortPlaylistButton.setObjectName(u"sortPlaylistButton")
        self.sortPlaylistButton.setGeometry(QRect(40, 240, 101, 41))
        self.deleteHistoryButton = QPushButton(self.centralWidget)
        self.deleteHistoryButton.setObjectName(u"deleteHistoryButton")
        self.deleteHistoryButton.setGeometry(QRect(660, 140, 101, 41))
        self.orLabel = QLabel(self.centralWidget)
        self.orLabel.setObjectName(u"orLabel")
        self.orLabel.setGeometry(QRect(180, 150, 21, 21))
        self.orLabel.setFont(font)
        self.accountPhotoButton = QPushButton(self.centralWidget)
        self.accountPhotoButton.setObjectName(u"accountPhotoButton")
        self.accountPhotoButton.setGeometry(QRect(790, 10, 60, 60))
        self.accountPhotoButton.setStyleSheet(u"QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    border-radius: 30px;\n"
"    border: 2px solid #FF0000\n"
"}")
        self.playlistFunctionsLabel = QLabel(self.centralWidget)
        self.playlistFunctionsLabel.setObjectName(u"playlistFunctionsLabel")
        self.playlistFunctionsLabel.setGeometry(QRect(40, 210, 101, 20))
        self.accountWidget = QWidget(self.centralWidget)
        self.accountWidget.setObjectName(u"accountWidget")
        self.accountWidget.setGeometry(QRect(680, 80, 171, 121))
        self.accountWidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(202, 202, 202);\n"
"    border-radius: 20px;\n"
"    border: 2px solid\n"
"}")
        self.accountNameLabel = QLabel(self.accountWidget)
        self.accountNameLabel.setObjectName(u"accountNameLabel")
        self.accountNameLabel.setGeometry(QRect(10, 10, 151, 31))
        self.accountNameLabel.setTextFormat(Qt.AutoText)
        self.accountNameLabel.setScaledContents(False)
        self.accountNameLabel.setAlignment(Qt.AlignCenter)
        self.signOutButton = QPushButton(self.accountWidget)
        self.signOutButton.setObjectName(u"signOutButton")
        self.signOutButton.setGeometry(QRect(50, 80, 75, 23))
        self.signOutButton.setStyleSheet(u"")
        self.accountWidgetCloseButton = QPushButton(self.accountWidget)
        self.accountWidgetCloseButton.setObjectName(u"accountWidgetCloseButton")
        self.accountWidgetCloseButton.setGeometry(QRect(150, 0, 16, 23))
        font2 = QFont()
        font2.setFamilies([u"Courier"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.accountWidgetCloseButton.setFont(font2)
        self.channelHandleLabel = QLabel(self.accountWidget)
        self.channelHandleLabel.setObjectName(u"channelHandleLabel")
        self.channelHandleLabel.setGeometry(QRect(10, 40, 151, 31))
        self.channelHandleLabel.setTextFormat(Qt.AutoText)
        self.channelHandleLabel.setScaledContents(False)
        self.channelHandleLabel.setAlignment(Qt.AlignCenter)
        self.removeDupesButton = QPushButton(self.centralWidget)
        self.removeDupesButton.setObjectName(u"removeDupesButton")
        self.removeDupesButton.setEnabled(False)
        self.removeDupesButton.setGeometry(QRect(160, 240, 101, 41))
        font3 = QFont()
        font3.setPointSize(8)
        self.removeDupesButton.setFont(font3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.removeLibraryButton.setDefault(False)
        self.deleteUploadsButton.setDefault(False)
        self.deletePlaylistsButton.setDefault(False)
        self.unlikeAllButton.setDefault(False)
        self.deleteAllButton.setDefault(False)
        self.sortPlaylistButton.setDefault(False)
        self.deleteHistoryButton.setDefault(False)
        self.removeDupesButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YTMusic Deleter", None))
#if QT_CONFIG(statustip)
        self.removeLibraryButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Remove all tracks that you have added to your library from within YouTube Music.", None))
#endif // QT_CONFIG(statustip)
        self.removeLibraryButton.setText(QCoreApplication.translate("MainWindow", u"Remove Library", None))
#if QT_CONFIG(statustip)
        self.deleteUploadsButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete all songs that you have uploaded to your YT Music library.", None))
#endif // QT_CONFIG(statustip)
        self.deleteUploadsButton.setText(QCoreApplication.translate("MainWindow", u"Delete Uploads", None))
        self.consoleLabel.setText(QCoreApplication.translate("MainWindow", u"Console Log", None))
        self.signInButton.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
#if QT_CONFIG(statustip)
        self.deletePlaylistsButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete all playlists.", None))
#endif // QT_CONFIG(statustip)
        self.deletePlaylistsButton.setText(QCoreApplication.translate("MainWindow", u"Delete Playlists", None))
#if QT_CONFIG(statustip)
        self.unlikeAllButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Reset all Thumbs Up ratings back to neutral.", None))
#endif // QT_CONFIG(statustip)
        self.unlikeAllButton.setText(QCoreApplication.translate("MainWindow", u"Unlike All", None))
#if QT_CONFIG(statustip)
        self.deleteAllButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Executes each of the deletion functions in sequential order.", None))
#endif // QT_CONFIG(statustip)
        self.deleteAllButton.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
#if QT_CONFIG(statustip)
        self.sortPlaylistButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Sort or shuffle one or more playlists alphabetically by artist and by album.", None))
#endif // QT_CONFIG(statustip)
        self.sortPlaylistButton.setText(QCoreApplication.translate("MainWindow", u"Sort Playlist", None))
#if QT_CONFIG(statustip)
        self.deleteHistoryButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete your play history. This does not currently work with brand accounts.", None))
#endif // QT_CONFIG(statustip)
        self.deleteHistoryButton.setText(QCoreApplication.translate("MainWindow", u"Delete History", None))
        self.orLabel.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.accountPhotoButton.setText("")
        self.playlistFunctionsLabel.setText(QCoreApplication.translate("MainWindow", u"Playlist Functions", None))
        self.accountNameLabel.setText(QCoreApplication.translate("MainWindow", u"Account Name", None))
        self.signOutButton.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.accountWidgetCloseButton.setText(QCoreApplication.translate("MainWindow", u"\u2716", None))
        self.channelHandleLabel.setText(QCoreApplication.translate("MainWindow", u"ChannelHandle", None))
#if QT_CONFIG(tooltip)
        self.removeDupesButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Coming soon!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.removeDupesButton.setStatusTip(QCoreApplication.translate("MainWindow", u"This feature is not yet available. Coming soon!", None))
#endif // QT_CONFIG(statustip)
        self.removeDupesButton.setText(QCoreApplication.translate("MainWindow", u"Remove Duplicates", None))
    # retranslateUi

