# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetColumnDialog.ui'
#
# Created: Sun Feb 15 19:54:59 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SetColumnDialog(object):
    def setupUi(self, SetColumnDialog):
        SetColumnDialog.setObjectName("SetColumnDialog")
        SetColumnDialog.resize(367, 310)
        self.gridLayout = QtGui.QGridLayout(SetColumnDialog)
        self.gridLayout.setObjectName("gridLayout")
        self._column_list = QtGui.QTreeView(SetColumnDialog)
        self._column_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self._column_list.setAlternatingRowColors(True)
        self._column_list.setRootIsDecorated(False)
        self._column_list.setItemsExpandable(False)
        self._column_list.setSortingEnabled(False)
        self._column_list.setHeaderHidden(True)
        self._column_list.setObjectName("_column_list")
        self.gridLayout.addWidget(self._column_list, 0, 0, 1, 1)
        self._button_box = QtGui.QDialogButtonBox(SetColumnDialog)
        self._button_box.setOrientation(QtCore.Qt.Horizontal)
        self._button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self._button_box.setObjectName("_button_box")
        self.gridLayout.addWidget(self._button_box, 1, 0, 1, 1)

        self.retranslateUi(SetColumnDialog)
        QtCore.QObject.connect(self._button_box, QtCore.SIGNAL("accepted()"), SetColumnDialog.accept)
        QtCore.QObject.connect(self._button_box, QtCore.SIGNAL("rejected()"), SetColumnDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SetColumnDialog)

    def retranslateUi(self, SetColumnDialog):
        SetColumnDialog.setWindowTitle(QtGui.QApplication.translate("SetColumnDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

