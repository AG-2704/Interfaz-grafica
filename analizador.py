# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analizador.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(205, 171, 143);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 190, 671, 351))
        self.widget.setStyleSheet(u"background-color: rgb(143, 240, 164);\n"
"")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 10, 671, 151))
        self.groupBox.setStyleSheet(u"background-color: rgba(253, 246, 226, 178);\n"
"font: 800 9pt \"Noto Sans\";\n"
"border: 2px solid rgb(180,120,210);")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 31, 71, 20))
        self.label.setStyleSheet(u"font: 700 9pt \"Noto Sans\";\n"
"background-color: rgb(220, 138, 221);")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 31, 91, 20))
        self.label_2.setStyleSheet(u"font: 700 italic 9pt \"Noto Sans\";\n"
"background-color: rgb(220, 138, 221);")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 60, 181, 31))
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textEdit_2 = QTextEdit(self.groupBox)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(410, 60, 181, 31))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.MainWindow_2 = QPushButton(self.groupBox)
        self.MainWindow_2.setObjectName(u"MainWindow_2")
        self.MainWindow_2.setGeometry(QRect(250, 90, 131, 25))
        self.MainWindow_2.setStyleSheet(u"font: 700 9pt \"Noto Sans\";\n"
"background-color: rgb(143, 240, 164);")
        self.textEdit_3 = QTextEdit(self.groupBox)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(240, 10, 161, 31))
        self.textEdit_3.setStyleSheet(u"border-color: rgb(205, 171, 143);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Amplitud", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Frecuencia[Hz]", None))
        self.MainWindow_2.setText(QCoreApplication.translate("MainWindow", u" Actualizar grafico", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:9pt; font-weight:800; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Parametros de la se\u00f1al</p></body></html>", None))
    # retranslateUi

