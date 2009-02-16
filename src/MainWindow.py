# -*- coding: utf-8 -*-

## @package MainWindow
# @brief Implementation der MainWindow Klasse
# @version 0.1
# @author Florian Kaiser
# @date 12.02.09

#################################################################################
# Copyright (C) 2009 Benjamin Flader, Benjamin Leipold, André Naumann,          #
# Corinna Vollert, Florian Kaiser                                               #
#                                                                               #
# This program is free software; you can redistribute it andor modify it under  #
# the terms of the GNU General Public License as published by the Free Software #
# Foundation; only version 2 of the License                                     #
#                                                                               #
# This program is distributed in the hope that it will be useful, but WITHOUT   #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS #
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more        #
# details.                                                                      #
#                                                                               #
# You should have received a copy of the GNU General Public License along with  #
# this program; if not, see <http://www.gnu.org/licenses/old-license            #
# /gpl-2.0.html>.                                                               #
#                                                                               #
#################################################################################

from PyQt4 import QtGui, QtCore, Qt
from ui_MainWindow import Ui_MainWindow
import interface
#from interface.BscwInterface import BscwInterface
from test import BscwInterface
from UserList import UserList
from UserDetails import UserDetails
from LoginDialog import LoginDialog
from Settings import Settings
from InfoDialog import InfoDialog
from SetColumnDialog import SetColumnDialog
import time
import urllib
import tempfile

## Diese Klasse stellt das Hauptfenster der Anwendung da und managed alle
# Funktionen des Programms.
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    ## Konstruktor
    # @param p_parent Übergeordnetes QObject.
    def __init__(self, p_parent = None):
        QtGui.QMainWindow.__init__(self, p_parent)
        self.setupUi(self)
        
        self._settings = Settings()
        
        self._headers = SetColumnDialog([], self) \
                            .tupleByKey(self._settings.columns)
        self._user_list_widget = UserList(self._headers, self)
        self.setCentralWidget(self._user_list_widget)
        
        self._user_details = UserDetails(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, 
                                                self._user_details)
        
        self._toolbar.addSeparator()
        self._lbl_filter = QtGui.QLabel(self)
        self._lbl_filter.setText(self.trUtf8(u"Suchtext: "))
        self._toolbar.addWidget(self._lbl_filter)
        
        self._line_edit_filter = QtGui.QLineEdit(self)
        self._line_edit_filter.setMaximumWidth(150)
        self._toolbar.addWidget(self._line_edit_filter)
        
        self.connect(self._action_info, QtCore.SIGNAL("triggered()"), 
                        self._showInfoSlot)
        self.connect(self._action_set_cols, QtCore.SIGNAL("triggered()"),
                        self._showSetColumnDialogSlot)
        self.connect(self._user_list_widget, 
                        QtCore.SIGNAL("SelectionChanged()"), 
                        self._updateUserDetailsSlot)
        self.connect(self._action_user_details, 
                        QtCore.SIGNAL("triggered(bool)"),
                        self._showUserDetails)
        self._login()
    
    ## Läd die Liste vom BSCW Server und zeigt das Fenster an    
    def show(self):
        QtGui.QMainWindow.show(self)
        self._statusbar.showMessage(
                                self.trUtf8("Benutzerliste wird geladen ..."))
        self._setEnabled(False)
        QtGui.qApp.processEvents()
        self._user_list = self._bscw_interface.getAllUsers()
        self._user_list_widget.loadList(self._user_list)
        self._setEnabled(True)
        self._statusbar.clearMessage()

    ## Zeigt ein Info-Dialog an
    def _showInfoSlot(self):
        info_dialog = InfoDialog(self)
        info_dialog.exec_()
    
    ## Zeigt den Spalten-Auswählen-Dialog an und speichert, wenn auf
    # 'OK' geklickt wurde die Auswahl in _headers. Außerdem wird
    # die User-Liste aktualisiert
    def _showSetColumnDialogSlot(self):
        set_column_dialog = SetColumnDialog(self._headers, self)
        set_column_dialog.exec_()
        if set_column_dialog.result() == QtGui.QDialog.Accepted:
            self._headers = set_column_dialog.getHeaderData()
            self._user_list_widget.changeHeaderData(self._headers)
        
    ## Sperrt bzw. Entsperrt alle Steuerelemente auf dem Fenster.
    # @param p_enable Steuerelemente sperren ja/nein (Boolean)
    def _setEnabled(self, p_enable):
        self._toolbar.setEnabled(p_enable)
        self._user_list_widget.setEnabled(p_enable)
        self._menubar.setEnabled(p_enable)
        self._user_details.setEnabled(p_enable)
    
    ## Zeigt den aktuell angewählten User im DockWidget an und läd bei Bedarf
    #  das Benutzerbild herunter.    
    def _updateUserDetailsSlot(self):
        selection = self._user_list_widget.getSelection()
        if len(selection) == 1:
            #if not "local_photo" in selection[0] 
            #        and selection[0]["photo"]:
            #    selection[0]["local_photo"] = \
            #         self._getFileByUrl(selection[0]["photo"])
            self._user_details.showUser(selection[0])
        else:
            self._user_details.showUser(None)
    
    ## Zeigt bzw. versteckt die User Details.
    # @param p_show DockWidget zeigen ja/nein (Boolean)        
    def _showUserDetails(self, p_show):
        if p_show:
            self._user_details.show()
        else:
            self._user_details.hide()

    ## Zeigt den LoginDialog an und versucht sich per BscwInterface am
    #  BSCW-Server anzumelden.
    def _login(self):
        login_dialog = LoginDialog(self._settings, self)

        if login_dialog.exec_() != QtGui.QDialog.Accepted:
            QtGui.qApp.quit()
            exit()

        self._bscw_interface = login_dialog.getInterface()

    ## Lädt eine URL in eine temporäre Date und gibt den Pfad der 
    # temporären Datei zurück
    # @param p_url Pfad der Url
    # @param p_proxy Adresse des Http-Proxys ist None wenn kein 
    # Proxy existiert. Bsp.:"http://proxy_address:port"
    def _getFileByUrl(self, p_url, p_proxy=None):
        tmp_data = ""
        if p_proxy != None:
            tmp_proxies = {'http': p_proxy}
            tmp_data = \
                urllib.urlopen("http://" + p_url,proxies=tmp_proxies).read()
        else:
            tmp_data = urllib.urlopen("http://" + p_url).read()
        tmp_file = tempfile.NamedTemporaryFile(delete=False)
        tmp_file.write(tmp_data)
        tmp_file.close()
        return tmp_file.name

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
