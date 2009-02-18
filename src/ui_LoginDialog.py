# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginDialog.ui'
#
# Created: Wed Feb 18 13:06:56 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(497, 144)
        LoginDialog.setMinimumSize(QtCore.QSize(497, 144))
        LoginDialog.setMaximumSize(QtCore.QSize(16777215, 144))
        self.gridLayout = QtGui.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName("gridLayout")
        self._lbl_server_address = QtGui.QLabel(LoginDialog)
        self._lbl_server_address.setObjectName("_lbl_server_address")
        self.gridLayout.addWidget(self._lbl_server_address, 0, 0, 1, 1)
        self._server_address = QtGui.QLineEdit(LoginDialog)
        self._server_address.setObjectName("_server_address")
        self.gridLayout.addWidget(self._server_address, 1, 0, 1, 4)
        self._lbl_username = QtGui.QLabel(LoginDialog)
        self._lbl_username.setObjectName("_lbl_username")
        self.gridLayout.addWidget(self._lbl_username, 2, 0, 1, 1)
        self._lbl_passwd = QtGui.QLabel(LoginDialog)
        self._lbl_passwd.setObjectName("_lbl_passwd")
        self.gridLayout.addWidget(self._lbl_passwd, 2, 1, 1, 2)
        self._username = QtGui.QLineEdit(LoginDialog)
        self._username.setObjectName("_username")
        self.gridLayout.addWidget(self._username, 3, 0, 1, 1)
        self._passwd = QtGui.QLineEdit(LoginDialog)
        self._passwd.setMinimumSize(QtCore.QSize(230, 0))
        self._passwd.setEchoMode(QtGui.QLineEdit.Password)
        self._passwd.setObjectName("_passwd")
        self.gridLayout.addWidget(self._passwd, 3, 1, 1, 3)
        self._lbl_status = QtGui.QLabel(LoginDialog)
        self._lbl_status.setObjectName("_lbl_status")
        self.gridLayout.addWidget(self._lbl_status, 4, 0, 1, 2)
        self._quit_button = QtGui.QPushButton(LoginDialog)
        self._quit_button.setObjectName("_quit_button")
        self.gridLayout.addWidget(self._quit_button, 4, 3, 1, 1)
        self._login_button = QtGui.QPushButton(LoginDialog)
        self._login_button.setDefault(True)
        self._login_button.setObjectName("_login_button")
        self.gridLayout.addWidget(self._login_button, 4, 2, 1, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QObject.connect(self._quit_button, QtCore.SIGNAL("clicked()"), LoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QtGui.QApplication.translate("LoginDialog", "Anmeldung am BSCW Server", None, QtGui.QApplication.UnicodeUTF8))
        self._lbl_server_address.setText(QtGui.QApplication.translate("LoginDialog", "Server-Adresse", None, QtGui.QApplication.UnicodeUTF8))
        self._lbl_username.setText(QtGui.QApplication.translate("LoginDialog", "Benutzername:", None, QtGui.QApplication.UnicodeUTF8))
        self._lbl_passwd.setText(QtGui.QApplication.translate("LoginDialog", "Passwort:", None, QtGui.QApplication.UnicodeUTF8))
        self._lbl_status.setText(QtGui.QApplication.translate("LoginDialog", "Server-Adresse und Logindaten eintragen", None, QtGui.QApplication.UnicodeUTF8))
        self._quit_button.setText(QtGui.QApplication.translate("LoginDialog", "Beenden", None, QtGui.QApplication.UnicodeUTF8))
        self._login_button.setText(QtGui.QApplication.translate("LoginDialog", "Anmelden", None, QtGui.QApplication.UnicodeUTF8))

