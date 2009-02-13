# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoDialog.ui'
#
# Created: Fri Feb 13 13:43:05 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        InfoDialog.setObjectName("InfoDialog")
        InfoDialog.resize(386, 284)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InfoDialog.sizePolicy().hasHeightForWidth())
        InfoDialog.setSizePolicy(sizePolicy)
        self._lbl_info = QtGui.QLabel(InfoDialog)
        self._lbl_info.setGeometry(QtCore.QRect(20, 150, 351, 71))
        self._lbl_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._lbl_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self._lbl_info.setWordWrap(False)
        self._lbl_info.setObjectName("_lbl_info")
        self._button_ok = QtGui.QPushButton(InfoDialog)
        self._button_ok.setGeometry(QtCore.QRect(300, 250, 75, 23))
        self._button_ok.setObjectName("_button_ok")
        self._button_qt_info = QtGui.QPushButton(InfoDialog)
        self._button_qt_info.setGeometry(QtCore.QRect(220, 250, 75, 23))
        self._button_qt_info.setObjectName("_button_qt_info")

        self.retranslateUi(InfoDialog)
        QtCore.QObject.connect(self._button_ok, QtCore.SIGNAL("clicked()"), InfoDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        InfoDialog.setWindowTitle(QtGui.QApplication.translate("InfoDialog", "Über BUMM", None, QtGui.QApplication.UnicodeUTF8))
        self._lbl_info.setText(QtGui.QApplication.translate("InfoDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><span style=\" font-weight:600;\">Version</span>:     1.0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><span style=\" font-weight:600;\">Autoren</span>:    Benjamin Flader, Benjamin Leipold, </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\">                     André Naumann, Corinna Vollert, Florian Kaiser</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\">Dieses Programm verwendet das Qt Framework.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self._button_ok.setText(QtGui.QApplication.translate("InfoDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self._button_qt_info.setText(QtGui.QApplication.translate("InfoDialog", "About Qt", None, QtGui.QApplication.UnicodeUTF8))

