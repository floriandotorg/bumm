# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ErrorDialog.ui'
#
# Created: Fri Feb 27 08:22:43 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ErrorDialog(object):
    def setupUi(self, ErrorDialog):
        ErrorDialog.setObjectName("ErrorDialog")
        ErrorDialog.resize(532, 224)
        ErrorDialog.setMinimumSize(QtCore.QSize(460, 0))
        self.gridLayout = QtGui.QGridLayout(ErrorDialog)
        self.gridLayout.setObjectName("gridLayout")
        self._lbl_img = QtGui.QLabel(ErrorDialog)
        self._lbl_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self._lbl_img.setObjectName("_lbl_img")
        self.gridLayout.addWidget(self._lbl_img, 0, 0, 2, 1)
        self._lbl_header = QtGui.QLabel(ErrorDialog)
        self._lbl_header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self._lbl_header.setObjectName("_lbl_header")
        self.gridLayout.addWidget(self._lbl_header, 0, 1, 1, 2)
        self._lbl_err = QtGui.QLabel(ErrorDialog)
        self._lbl_err.setMinimumSize(QtCore.QSize(0, 50))
        self._lbl_err.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self._lbl_err.setWordWrap(True)
        self._lbl_err.setObjectName("_lbl_err")
        self.gridLayout.addWidget(self._lbl_err, 1, 1, 1, 3)
        self._button_details = QtGui.QPushButton(ErrorDialog)
        self._button_details.setMinimumSize(QtCore.QSize(91, 0))
        self._button_details.setMaximumSize(QtCore.QSize(91, 16777215))
        self._button_details.setAutoDefault(False)
        self._button_details.setObjectName("_button_details")
        self.gridLayout.addWidget(self._button_details, 2, 0, 1, 2)
        self._button_quit = QtGui.QPushButton(ErrorDialog)
        self._button_quit.setMinimumSize(QtCore.QSize(111, 0))
        self._button_quit.setMaximumSize(QtCore.QSize(111, 16777215))
        self._button_quit.setObjectName("_button_quit")
        self.gridLayout.addWidget(self._button_quit, 2, 2, 1, 1)
        self._button_continue = QtGui.QPushButton(ErrorDialog)
        self._button_continue.setMaximumSize(QtCore.QSize(77, 16777215))
        self._button_continue.setDefault(True)
        self._button_continue.setObjectName("_button_continue")
        self.gridLayout.addWidget(self._button_continue, 2, 3, 1, 1)
        self._text_traceback = QtGui.QPlainTextEdit(ErrorDialog)
        self._text_traceback.setReadOnly(True)
        self._text_traceback.setObjectName("_text_traceback")
        self.gridLayout.addWidget(self._text_traceback, 3, 0, 1, 4)

        self.retranslateUi(ErrorDialog)
        QtCore.QObject.connect(self._button_continue, QtCore.SIGNAL("clicked()"), ErrorDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(ErrorDialog)

    def retranslateUi(self, ErrorDialog):
        ErrorDialog.setWindowTitle(QtGui.QApplication.translate("ErrorDialog", "Fehler!", None, QtGui.QApplication.UnicodeUTF8))
        self._lbl_header.setText(QtGui.QApplication.translate("ErrorDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Unhandled Exception!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self._lbl_err.setText(QtGui.QApplication.translate("ErrorDialog", "Fehler: ", None, QtGui.QApplication.UnicodeUTF8))
        self._button_details.setText(QtGui.QApplication.translate("ErrorDialog", "Details >>", None, QtGui.QApplication.UnicodeUTF8))
        self._button_quit.setText(QtGui.QApplication.translate("ErrorDialog", "Programm beenden", None, QtGui.QApplication.UnicodeUTF8))
        self._button_continue.setText(QtGui.QApplication.translate("ErrorDialog", "Weiter", None, QtGui.QApplication.UnicodeUTF8))

