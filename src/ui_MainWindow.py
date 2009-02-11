# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Wed Feb 11 08:29:12 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self._centralwidget = QtGui.QWidget(MainWindow)
        self._centralwidget.setObjectName("_centralwidget")
        MainWindow.setCentralWidget(self._centralwidget)
        self._menubar = QtGui.QMenuBar(MainWindow)
        self._menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self._menubar.setObjectName("_menubar")
        self._menu_program = QtGui.QMenu(self._menubar)
        self._menu_program.setObjectName("_menu_program")
        self._menu_view = QtGui.QMenu(self._menubar)
        self._menu_view.setObjectName("_menu_view")
        self._menu_help = QtGui.QMenu(self._menubar)
        self._menu_help.setObjectName("_menu_help")
        MainWindow.setMenuBar(self._menubar)
        self._statusbar = QtGui.QStatusBar(MainWindow)
        self._statusbar.setObjectName("_statusbar")
        MainWindow.setStatusBar(self._statusbar)
        self._action_quit = QtGui.QAction(MainWindow)
        self._action_quit.setObjectName("_action_quit")
        self._action_info = QtGui.QAction(MainWindow)
        self._action_info.setObjectName("_action_info")
        self._action_user_Details = QtGui.QAction(MainWindow)
        self._action_user_Details.setCheckable(True)
        self._action_user_Details.setChecked(True)
        self._action_user_Details.setObjectName("_action_user_Details")
        self._action_set_cols = QtGui.QAction(MainWindow)
        self._action_set_cols.setObjectName("_action_set_cols")
        self._menu_program.addAction(self._action_quit)
        self._menu_view.addAction(self._action_user_Details)
        self._menu_view.addSeparator()
        self._menu_view.addAction(self._action_set_cols)
        self._menu_help.addAction(self._action_info)
        self._menubar.addAction(self._menu_program.menuAction())
        self._menubar.addAction(self._menu_view.menuAction())
        self._menubar.addAction(self._menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self._action_quit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "BSCW Userverwaltung", None, QtGui.QApplication.UnicodeUTF8))
        self._menu_program.setTitle(QtGui.QApplication.translate("MainWindow", "Programm", None, QtGui.QApplication.UnicodeUTF8))
        self._menu_view.setTitle(QtGui.QApplication.translate("MainWindow", "Ansicht", None, QtGui.QApplication.UnicodeUTF8))
        self._menu_help.setTitle(QtGui.QApplication.translate("MainWindow", "Hilfe", None, QtGui.QApplication.UnicodeUTF8))
        self._action_quit.setText(QtGui.QApplication.translate("MainWindow", "Beenden", None, QtGui.QApplication.UnicodeUTF8))
        self._action_info.setText(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self._action_user_Details.setText(QtGui.QApplication.translate("MainWindow", "User Details", None, QtGui.QApplication.UnicodeUTF8))
        self._action_set_cols.setText(QtGui.QApplication.translate("MainWindow", "Spalten auswählen", None, QtGui.QApplication.UnicodeUTF8))

