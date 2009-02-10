# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginDialog.ui'
#
# Created: Tue Feb 10 14:32:42 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(234, 152)
        self._button_box = QtGui.QDialogButtonBox(LoginDialog)
        self._button_box.setGeometry(QtCore.QRect(10, 110, 211, 32))
        self._button_box.setOrientation(QtCore.Qt.Horizontal)
        self._button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self._button_box.setObjectName("_button_box")
        self._username = QtGui.QLineEdit(LoginDialog)
        self._username.setGeometry(QtCore.QRect(10, 30, 211, 20))
        self._username.setObjectName("_username")
        self._passwd = QtGui.QLineEdit(LoginDialog)
        self._passwd.setGeometry(QtCore.QRect(10, 80, 211, 20))
        self._passwd.setEchoMode(QtGui.QLineEdit.Password)
        self._passwd.setObjectName("_passwd")
        self.label = QtGui.QLabel(LoginDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(LoginDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(LoginDialog)
        QtCore.QObject.connect(self._button_box, QtCore.SIGNAL("accepted()"), LoginDialog.accept)
        QtCore.QObject.connect(self._button_box, QtCore.SIGNAL("rejected()"), LoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QtGui.QApplication.translate("LoginDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LoginDialog", "Benutzername:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("LoginDialog", "Passwort:", None, QtGui.QApplication.UnicodeUTF8))

