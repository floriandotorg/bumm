# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserDetails.ui'
#
# Created: Tue Feb 17 12:14:23 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_UserDetails(object):
    def setupUi(self, UserDetails):
        UserDetails.setObjectName("UserDetails")
        UserDetails.resize(447, 390)
        self._content = QtGui.QWidget()
        self._content.setObjectName("_content")
        self.gridLayout = QtGui.QGridLayout(self._content)
        self.gridLayout.setObjectName("gridLayout")
        self._tab_widget = QtGui.QTabWidget(self._content)
        self._tab_widget.setObjectName("_tab_widget")
        self._tab_details = QtGui.QWidget()
        self._tab_details.setObjectName("_tab_details")
        self.gridLayout_2 = QtGui.QGridLayout(self._tab_details)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self._text_details = QtGui.QTextEdit(self._tab_details)
        self._text_details.setReadOnly(True)
        self._text_details.setObjectName("_text_details")
        self.gridLayout_2.addWidget(self._text_details, 0, 0, 1, 1)
        self._tab_widget.addTab(self._tab_details, "")
        self._tab_pic = QtGui.QWidget()
        self._tab_pic.setObjectName("_tab_pic")
        self.gridLayout_3 = QtGui.QGridLayout(self._tab_pic)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self._lbl_pic = QtGui.QLabel(self._tab_pic)
        self._lbl_pic.setScaledContents(True)
        self._lbl_pic.setOpenExternalLinks(False)
        self._lbl_pic.setObjectName("_lbl_pic")
        self.gridLayout_3.addWidget(self._lbl_pic, 0, 0, 1, 1)
        self._tab_widget.addTab(self._tab_pic, "")
        self.gridLayout.addWidget(self._tab_widget, 0, 0, 1, 1)
        UserDetails.setWidget(self._content)

        self.retranslateUi(UserDetails)
        self._tab_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(UserDetails)

    def retranslateUi(self, UserDetails):
        UserDetails.setWindowTitle(QtGui.QApplication.translate("UserDetails", "Details", None, QtGui.QApplication.UnicodeUTF8))
        self._tab_widget.setTabText(self._tab_widget.indexOf(self._tab_details), QtGui.QApplication.translate("UserDetails", "Details", None, QtGui.QApplication.UnicodeUTF8))
        self._tab_widget.setTabText(self._tab_widget.indexOf(self._tab_pic), QtGui.QApplication.translate("UserDetails", "Bild", None, QtGui.QApplication.UnicodeUTF8))

