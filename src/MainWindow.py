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
from ActionThread import ActionThread
import time
import urllib
import tempfile

## Diese Klasse stellt das Hauptfenster der Anwendung da und managed alle
# Funktionen des Programms
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    ## Konstruktor
    # @param p_parent Übergeordnetes QObject
    def __init__(self, p_parent = None):
        QtGui.QMainWindow.__init__(self, p_parent)
        self.setupUi(self)
        
        ## Programmeinstellungen
        self._settings = Settings()
        ## Liste aller heruntergeladenen Benutzerbilder
        self._img_cache = []
        
        ## Liste aller angezeigten Spalten in der User-Liste
        self._headers = SetColumnDialog([], self) \
                            .tupleByKey(self._settings.columns)
        ## Liste aller Benuter
        self._user_list = UserList(self._headers, self)
        self.setCentralWidget(self._user_list)
        
        ## DockWidget indem nähere Benutzerinformationen angezeigt werden
        self._user_details = UserDetails(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, 
                                                self._user_details)
        
        self._toolbar.addSeparator()
        ## 'Suchtext'-Label
        self._lbl_filter = QtGui.QLabel(self)
        self._lbl_filter.setText(self.trUtf8(u"Suchtext: "))
        self._toolbar.addWidget(self._lbl_filter)
        
        ## Eingabefeld für den Suchbegriff
        self._line_edit_filter = QtGui.QLineEdit(self)
        self._line_edit_filter.setMaximumWidth(150)
        self._toolbar.addWidget(self._line_edit_filter)
        
        self.connect(self._user_list, 
                        QtCore.SIGNAL("SelectionChanged()"), 
                        self._selectionChangedSlot)
        
        self.connect(self._action_user_details, 
                        QtCore.SIGNAL("triggered(bool)"),
                        self._user_details.setVisible)
        self.connect(self._user_details,
                        QtCore.SIGNAL("visibilityChanged(bool)"),
                        self._action_user_details.setChecked)
        
        self.connect(self._action_update_all, QtCore.SIGNAL("triggered()"),
                        self._loadList)
        
        self.connect(self._action_set_cols, QtCore.SIGNAL("triggered()"),
                        self._showSetColumnDialogSlot)
        
        self.connect(self._action_delete, QtCore.SIGNAL("triggered()"),
                        self._deleteUserSlot)
        self.connect(self._action_lock, QtCore.SIGNAL("triggered()"),
                        self._lockUserSlot)
        self.connect(self._action_unlock, QtCore.SIGNAL("triggered()"),
                        self._unlockUserSlot)
        self.connect(self._action_destroy_trash, QtCore.SIGNAL("triggered()"),
                        self._destroyTrashSlot)
        self.connect(self._action_destroy_clipboard, 
                        QtCore.SIGNAL("triggered()"),
                        self._destroyClipboardSlot)
        
        self.connect(self._action_info, QtCore.SIGNAL("triggered()"), 
                        self._showInfoSlot)
                     
        self.connect(self._line_edit_filter, QtCore.SIGNAL("returnPressed()"),
                        self._setUserListFilterSlot)
        
        self._login()
    
    ## Lädt die Benutzerdaten vom BSCW Server und zeigt das Hauptfenster an    
    def show(self):
        QtGui.QMainWindow.show(self)
        self._loadList()
    
    ## Erzeugt einen Thread, der eine Aufgabe ausführt, die die Anwendung 
    # blockieren könnte
    # @param p_func Zeiger auf eine Funktion mit langer Laufzeit
    # @param p_finished Zeiger auf eine Funktion, die aufgerufen wird,
    # wenn die Aufgabe bearbeitet wurde
    # @param p_params Parameter, die beim Aufruf übergeben werden
    def _action(self, p_func, p_finished, *p_params):
        ## Thread für Aufgaben mit langer Laufzeit
        self._action_thread = ActionThread(self, p_func, *p_params)
        self.connect(self._action_thread, QtCore.SIGNAL("finished()"),
                     p_finished)
        self._action_thread.start()
        
    ## Lädt die Daten aller Benutzer und stellt diese in der Liste da
    def _loadList(self):
        self._lockWidget(True, self.trUtf8("Benutzerliste wird geladen ..."))
        self._action(self._bscw_interface.getAllUser, self._listLoadedSlot)
    
    ## Lädt die Benutzerdaten in die User-Liste und entsperrt das Fenster
    def _listLoadedSlot(self):
        self._user_list.loadList(self.sender().getResult())
        self._unlockWidget() 

    ## Zeigt ein Info-Dialog an
    def _showInfoSlot(self):
        info_dialog = InfoDialog(self)
        info_dialog.exec_()
    
    ## Zeigt den Spalten-Auswählen-Dialog an und speichert, wenn auf
    # 'OK' geklickt wurde die Auswahl in self._headers. Außerdem wird
    # die User-Liste aktualisiert
    def _showSetColumnDialogSlot(self):
        set_column_dialog = SetColumnDialog(self._headers, self)
        set_column_dialog.exec_()
        if set_column_dialog.result() == QtGui.QDialog.Accepted:
            self._headers = set_column_dialog.getHeaderData()
            self._user_list.changeHeaderData(self._headers)
    
    ## Sperrt/Entsperrt das Widget und zeigt eine Meldung in der Statusleiste an   
    # @param p_lock Widget sperren ja/nein (Boolean)
    # @param p_message Nachricht für die Statusbar  
    def _lockWidget(self, p_lock, p_message = None):
        p_lock = not p_lock
        self._toolbar.setEnabled(p_lock)
        self._user_list.setEnabled(p_lock)
        self._menubar.setEnabled(p_lock)
        self._user_details.setEnabled(p_lock)
        if p_message:
            self._statusbar.showMessage(p_message)
        else:
            self._statusbar.clearMessage()
        QtGui.qApp.processEvents()
    
    ## Entsperrt das Widget und löscht die Status-Nachricht    
    def _unlockWidget(self):
        self._lockWidget(False)
    
    ## Aktualisiert die User-Details und die Toolbar
    def _selectionChangedSlot(self):
        selection = self._user_list.getSelection()
        if selection == []:
            self._setUserActionEnabled(False)
        else:
            self._setUserActionEnabled(True)
        self._updateUserDetails(selection)
    
    ## Aktiviert/Deaktiviert die User-Aktions-Menüs
    # @param p_enabled Menüs aktiviert ja/nein (Boolean)
    def _setUserActionEnabled(self, p_enabled):
        self._action_delete.setEnabled(p_enabled)
        self._action_lock.setEnabled(p_enabled)
        self._action_unlock.setEnabled(p_enabled)
    
    ## Zeigt den aktuell angewählten User im DockWidget an und lädt bei Bedarf
    # das Benutzerbild herunter.  
    # @param p_selection Liste der angewählten User
    def _updateUserDetails(self, p_selection):
        if len(p_selection) == 1:
            if not "local_photo" in p_selection[0] \
                    and p_selection[0]["photo"]:
                self._lockWidget(True, 
                            self.trUtf8("Benutzerbild wird geladen ..."))
                p_selection[0]["local_photo"] = \
                            self._getFileByUrl(p_selection[0]["photo"])
                self._unlockWidget
            self._user_details.showUser(p_selection[0])
        else:
            self._user_details.showUser(None)
    
    ## Sperrt alle in der Benutzerliste angewählten User
    def _lockUserSlot(self):
        to_lock = []
        
        for i in self._user_list.getSelection():
            to_lock.append(i["name"])
        
        self._lockWidget(True, self.trUtf8("Benutzer werden gesperrt ..."))
        self._action(self._bscw_interface.lockUser, self._unlockWidget, 
                        to_lock)
        self._user_list.lockUser(to_lock)
    
    ## Entsperrt alle in der Benutzerliste angewählten User    
    def _unlockUserSlot(self):
        to_unlock = []
        
        for i in self._user_list.getSelection():
            to_unlock.append(i["name"])
        
        self._lockWidget(True, self.trUtf8("Benutzer werden entsperrt ..."))
        self._action(self._bscw_interface.unlockUser, self._unlockWidget, 
                        to_unlock)
        self._user_list.unlockUser(to_unlock)
    
    ## Leer danach die Mülleimer. Das Mindestalter der Dateien wird mithilfe
    # eines Dialogs definiert.
    def _destroyTrashSlot(self):
        user = []
        
        for i in self._user_list.getSelection():
            user.append(i["name"])
            
        outdated = QtGui.QInputDialog.getInteger(self, 
                        self.trUtf8("Mindestalter angeben"),
                        self.trUtf8("Mindestalter der zu " \
                                    "löschenden Dateien (in Tagen):"),
                        5, 0)
        
        if outdated[1]:
            self._lockWidget(True, self.trUtf8("Mülleimer werden " \
                                               "geleert ..."))
            self._action(self._bscw_interface.destroyTrash, self._unlockWidget, 
                        outdated[0], user)
    
    ## Räumt danach die Zwischenablagen auf. Das Mindestalter der Dateien wird mithilfe
    # eines Dialogs definiert.
    def _destroyClipboardSlot(self):
        user = []
        
        for i in self._user_list.getSelection():
            user.append(i["name"])
            
        outdated = QtGui.QInputDialog.getInteger(self, 
                        self.trUtf8("Mindestalter angeben"),
                        self.trUtf8("Mindestalter der zu " \
                                    "löschenden Dateien (in Tagen):"),
                        5, 0)
        
        if outdated[1]:
            self._lockWidget(True, self.trUtf8("Zwischenablagen werden " \
                                               "aufgeräumt ..."))
            self._action(self._bscw_interface.destroyClipboard, self._unlockWidget, 
                        outdated[0], user)
    
    ## Löscht alle in der Benutzerliste angewählten User    
    def _deleteUserSlot(self):
        to_delete = []
        
        for i in self._user_list.getSelection():
            to_delete.append(i["name"])
        
        ret = QtGui.QMessageBox.question(self, self.trUtf8("%1 User löschen?") \
                        .arg(len(to_delete)), self.trUtf8("Sind Sie sicher,"\
                        "dass Sie die ausgewählten Benutzer löschen möchten?"),
                         QtGui.QMessageBox.Yes , QtGui.QMessageBox.No)
        
        if ret == QtGui.QMessageBox.Yes:
            self._lockWidget(True, self.trUtf8("Benutzer werden gelöscht ..."))
            self._bscw_interface.deleteUser(to_delete)
            self._user_list.removeUser(to_delete)
            self._action(self._bscw_interface.deleteUser, self._unlockWidget, 
                        to_delete)
    
    ## Setzt den Filter der User-Liste       
    def _setUserListFilterSlot(self):
        self._user_list.setFilter(self._line_edit_filter.text())

    ## Zeigt den LoginDialog an und versucht sich per BscwInterface am
    #  BSCW-Server anzumelden.
    def _login(self):
        login_dialog = LoginDialog(self._settings, self)

        if login_dialog.exec_() != QtGui.QDialog.Accepted:
            QtGui.qApp.quit()
            exit()

        ## Interface zum BSCW-Server
        self._bscw_interface = login_dialog.getInterface()
        
        reg_exp = QtCore.QRegExp("(http://)?([a-zA-Z_0-9:]+)(/[a-zA-Z_])*")
        reg_exp.exactMatch(login_dialog.getServerAddress())
        ## HTTP-Adresse des BSCW-Servers (Wird zum Herunterladen der
        # Benutzerbilder benötigt)
        self._img_url_prefix = "http://%s:%s@%s" % (str(login_dialog.getUsername()),
                            str(login_dialog.getPasswd()), str(reg_exp.cap(2)))
        
    ## Lädt eine URL in eine temporäre Datei und gibt den Pfad der 
    # temporären Datei zurück
    # @param p_url URL der Datei
    # @return Pfad zur Datei als String oder None, wenn  ein Fehler aufgetreten
    # ist
    def _getFileByUrl(self, p_url):
        if p_url[0] == "/":
            p_url = self._img_url_prefix + p_url
        try:
            self._img_cache.append(urllib.URLopener())
            file = self._img_cache[-1].retrieve(p_url)[0]
            return file
        except:
            return None

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
