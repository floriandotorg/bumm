# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoDialog.ui'
#
# Created: Thu Apr 23 10:55:38 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        InfoDialog.setObjectName("InfoDialog")
        InfoDialog.resize(386, 294)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InfoDialog.sizePolicy().hasHeightForWidth())
        InfoDialog.setSizePolicy(sizePolicy)
        InfoDialog.setMinimumSize(QtCore.QSize(386, 294))
        InfoDialog.setMaximumSize(QtCore.QSize(386, 294))
        self._lbl_info = QtGui.QLabel(InfoDialog)
        self._lbl_info.setGeometry(QtCore.QRect(20, 140, 351, 121))
        self._lbl_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._lbl_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self._lbl_info.setWordWrap(True)
        self._lbl_info.setObjectName("_lbl_info")
        self._button_ok = QtGui.QPushButton(InfoDialog)
        self._button_ok.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self._button_ok.setObjectName("_button_ok")
        self._button_qt_info = QtGui.QPushButton(InfoDialog)
        self._button_qt_info.setGeometry(QtCore.QRect(220, 260, 75, 23))
        self._button_qt_info.setObjectName("_button_qt_info")
        self.label = QtGui.QLabel(InfoDialog)
        self.label.setGeometry(QtCore.QRect(80, 0, 221, 131))
        self.label.setPixmap(QtGui.QPixmap(":/logo/logo/logo.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(InfoDialog)
        QtCore.QObject.connect(self._button_ok, QtCore.SIGNAL("clicked()"), InfoDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        InfoDialog.setWindowTitle(QtGui.QApplication.translate("InfoDialog", "Über BUMM", None, QtGui.QApplication.UnicodeUTF8))
        self._lbl_info.setText(QtGui.QApplication.translate("InfoDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><span style=\" font-weight:600;\">BUMM</span> - <span style=\" font-weight:600;\">B</span>SCW <span style=\" font-weight:600;\">U</span>ser <span style=\" font-weight:600;\">M</span>anag<span style=\" font-weight:600;\">m</span>ent</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\">Version<span style=\" font-weight:400;\">:     1.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><span style=\" font-weight:600;\">Autoren</span>:    Benjamin Flader, Benjamin Leipold, </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\">                     André Naumann, Corinna Vollert, Florian Kaiser</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\">Dieses Programm ist freie Software und steht unter der GPLv2. Es verwendet das Qt Framework.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self._button_ok.setText(QtGui.QApplication.translate("InfoDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self._button_qt_info.setText(QtGui.QApplication.translate("InfoDialog", "Über Qt", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
import images_rc
import images_rc
import images_rc
