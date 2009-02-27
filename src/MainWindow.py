# -*- coding: utf-8 -*-

## @package MainWindow
# @brief Implementation der MainWindow Klasse
# @version 1
# @author Florian Kaiser
# @date 14.02.09

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
from interface.BscwInterface import BscwInterface
#from test import BscwInterface
from UserList import UserList
from UserDetails import UserDetails
from LoginDialog import LoginDialog
from Settings import Settings
from InfoDialog import InfoDialog
from SetColumnDialog import SetColumnDialog
from ActionThread import ActionThread
from ErrorDialog import ErrorDialog
import time
import urllib
import tempfile

## Diese Klasse stellt das Hauptfenster der Anwendung da und managed alle
# Funktionen des Programms
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    ## Wandelt eine Speicherangabe von MB in KB und gibt sie Formatiert mit
    # 1000er Trennzeichen und Einheit zurück
    # @param mem Speicher in MB
    # @return Formatierter String
    def formatMemory(p_mem):
        result = ""
        points = 0
        p_mem = str(int(p_mem * 1000))

        for i in range(0, len(p_mem))[::-1]:
            result = p_mem[i] + result

            if not (len(result) - points) % 3 and i:
                result = "." + result
                points += 1

        return result + " KB"
    formatMemory = staticmethod(formatMemory)

    ## Konstruktor
    # @param p_parent Übergeordnetes QObject
    def __init__(self, p_parent = None):
        try:
            QtGui.QMainWindow.__init__(self, p_parent)
            self.setupUi(self)

            ## Liste aller heruntergeladenen Benutzerbilder
            self._img_cache = []

            ## DockWidget indem nähere Benutzerinformationen angezeigt werden
            self._user_details = UserDetails(self)
            self.addDockWidget(QtCore.Qt.RightDockWidgetArea,
                                                    self._user_details)

            ## Programmeinstellungen laden
            self._settings = Settings()

            ## Login öffnen
            self._login()

            self.setGeometry(self._settings.main_window_geometry)
            self._user_details.setGeometry(self._settings.user_details_geometry)
            self._user_details.setVisible(self._settings.show_user_details)
            self._action_user_details.setChecked(self._settings \
                                                            .show_user_details)
            self.restoreState(self._settings.state);

            ## Liste aller angezeigten Spalten in der User-Liste
            self._headers = SetColumnDialog([], self) \
                                .tupleByKey(self._settings.columns)

            ## Liste aller Benuter
            self._user_list = UserList(self._headers, self)
            self.setCentralWidget(self._user_list)

            self._toolbar.addSeparator()
            ## 'Suchtext'-Label
            self._lbl_filter = QtGui.QLabel(self)
            self._lbl_filter.setText(self.trUtf8("Suchtext: "))
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
            self.connect(self._action_destroy_trash,
                            QtCore.SIGNAL("triggered()"),
                            self._destroyTrashSlot)
            self.connect(self._action_destroy_clipboard,
                            QtCore.SIGNAL("triggered()"),
                            self._destroyClipboardSlot)

            self.connect(self._action_info, QtCore.SIGNAL("triggered()"),
                            self._showInfoSlot)

            self.connect(self._line_edit_filter,
                            QtCore.SIGNAL("returnPressed()"),
                            self._setUserListFilterSlot)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Lädt die Benutzerdaten vom BSCW Server und zeigt das Hauptfenster an
    def show(self):
        try:
            QtGui.QMainWindow.show(self)
            self._loadList()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Überladene Methode: Speichert alle Einstellungen, wenn das Fenster
    # geschlossen wurde
    # @param p_even Qt-Close-Event
    def closeEvent(self, p_event):

        try:
            self._settings.columns = [i[0] for i in self._headers]
            self._settings.main_window_geometry = self.geometry()
            self._settings.user_details_geometry = \
                                    self._user_details.geometry()

            # wenn minimiert nicht den Status speichern, da ansonsten immer
            # false
            if not self.isMinimized():
                self._settings.show_user_details = self._user_details.isVisible()

                self._settings.show_user_details = \
                    self._user_details.isVisible()

                self._settings.state = self.saveState()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Erzeugt einen Thread, der eine Aufgabe ausführt, die die Anwendung
    # blockieren könnte
    # @param p_func Zeiger auf eine Funktion mit langer Laufzeit
    # @param p_finished Zeiger auf eine Funktion, die aufgerufen wird,
    # wenn die Aufgabe bearbeitet wurde
    # @param p_params Parameter, die beim Aufruf übergeben werden
    def _action(self, p_func, p_finished, *p_params):
        try:
            ## Thread für Aufgaben mit langer Laufzeit
            self._action_thread = ActionThread(self, p_func, *p_params)
            self.connect(self._action_thread, QtCore.SIGNAL("finished()"),
                         p_finished)
            self._action_thread.start()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Lädt die Daten aller Benutzer und stellt diese in der Liste da
    def _loadList(self):
        try:
            self._lockWidget(True,
                             self.trUtf8("Benutzerliste wird geladen ..."))
            self._action(self._bscw_interface.getAllUser,
                             self._listLoadedSlot)
        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Lädt die Benutzerdaten in die User-Liste und entsperrt das Fenster
    def _listLoadedSlot(self):
        try:
            self._user_list.loadList(self.sender().getResult())
            self._unlockWidget()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Zeigt ein Info-Dialog an
    def _showInfoSlot(self):
        try:
            info_dialog = InfoDialog(self)
            info_dialog.exec_()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Zeigt den Spalten-Auswählen-Dialog an und speichert, wenn auf
    # 'OK' geklickt wurde die Auswahl in self._headers. Außerdem wird
    # die User-Liste aktualisiert
    def _showSetColumnDialogSlot(self):
        try:
            set_column_dialog = SetColumnDialog(self._headers, self)
            set_column_dialog.setGeometry(self._settings.col_dialog_geometry)

            set_column_dialog.exec_()

            if set_column_dialog.result() == QtGui.QDialog.Accepted:
                self._headers = set_column_dialog.getHeaderData()
                self._user_list.changeHeaderData(self._headers)
            self._settings.col_dialog_geometry = set_column_dialog.geometry()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Sperrt/Entsperrt das Widget und zeigt eine Meldung in der Statusleiste an
    # @param p_lock Widget sperren ja/nein (Boolean)
    # @param p_message Nachricht für die Statusbar
    def _lockWidget(self, p_lock, p_message = None):
        try:
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

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Entsperrt das Widget und löscht die Status-Nachricht
    def _unlockWidget(self):
        try:
            self._lockWidget(False)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Aktualisiert die User-Details und die Toolbar
    def _selectionChangedSlot(self):
        try:
            selection = self._user_list.getSelection()
            if selection == []:
                self._setUserActionEnabled(False)
            else:
                self._setUserActionEnabled(True)
            self._updateUserDetails(selection)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Aktiviert/Deaktiviert die User-Aktions-Menüs
    # @param p_enabled Menüs aktiviert ja/nein (Boolean)
    def _setUserActionEnabled(self, p_enabled):
        try:
            self._action_delete.setEnabled(p_enabled)
            self._action_lock.setEnabled(p_enabled)
            self._action_unlock.setEnabled(p_enabled)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Zeigt den aktuell angewählten User im DockWidget an und lädt bei Bedarf
    # das Benutzerbild herunter.
    # @param p_selection Liste der angewählten User
    def _updateUserDetails(self, p_selection):
        try:
            if len(p_selection) == 1:
                if not "local_photo" in p_selection[0] \
                        and p_selection[0]["photo"]:
                    self._lockWidget(True,
                                self.trUtf8("Benutzerbild wird geladen ..."))
                    p_selection[0]["local_photo"] = \
                                self._getFileByUrl(p_selection[0]["photo"])
                    self._unlockWidget()
                self._user_details.showUser(p_selection[0])
            else:
                self._user_details.showUser(None)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Sperrt alle in der Benutzerliste angewählten User
    def _lockUserSlot(self):
        try:
            to_lock = []

            for i in self._user_list.getSelection():
                to_lock.append(i["name"])

            self._lockWidget(True, self.trUtf8("Benutzer werden gesperrt ..."))
            self._action(self._bscw_interface.lockUser, self._unlockWidget,
                            to_lock)

            for i in to_lock:
                self._user_list.updateUserAttr(to_lock, "locked", True)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Entsperrt alle in der Benutzerliste angewählten User
    def _unlockUserSlot(self):
        try:
            to_unlock = []

            for i in self._user_list.getSelection():
                to_unlock.append(i["name"])

            self._lockWidget(True, self.trUtf8("Benutzer werden entsperrt ..."))
            self._action(self._bscw_interface.unlockUser, self._unlockWidget,
                            to_unlock)

            for i in to_unlock:
                self._user_list.updateUserAttr(to_unlock, "locked", False)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Leer danach die Mülleimer. Das Mindestalter der Dateien wird mithilfe
    # eines Dialogs definiert.
    def _destroyTrashSlot(self):
        try:
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
                self._action(self._bscw_interface.destroyTrash,
                             self._unlockWidget,
                             outdated[0], user)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Räumt danach die Zwischenablagen auf. Das Mindestalter der Dateien
    # wird mithilfe eines Dialogs definiert.
    def _destroyClipboardSlot(self):
        try:
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
                self._action(self._bscw_interface.destroyClipboard,
                             self._unlockWidget,
                             outdated[0], user)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Löscht alle in der Benutzerliste angewählten User
    def _deleteUserSlot(self):
        try:
            to_delete = []

            for i in self._user_list.getSelection():
                to_delete.append(i["name"])

            ret = QtGui.QMessageBox.question(self,
                            self.trUtf8("%1 User löschen?") \
                            .arg(len(to_delete)),
                            self.trUtf8("Sind Sie sicher, dass Sie die " \
                            "ausgewählten Benutzer löschen möchten?"),
                            QtGui.QMessageBox.Yes , QtGui.QMessageBox.No)

            if ret == QtGui.QMessageBox.Yes:
                self._lockWidget(True,
                                 self.trUtf8("Benutzer werden gelöscht ..."))
                self._bscw_interface.deleteUser(to_delete)
                self._user_list.removeUser(to_delete)
                self._action(self._bscw_interface.deleteUser,
                             self._unlockWidget,
                             to_delete)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Setzt den Filter der User-Liste
    def _setUserListFilterSlot(self):
        try:
            self._user_list.setFilter(self._line_edit_filter.text())

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Zeigt den LoginDialog an und versucht sich per BscwInterface am
    #  BSCW-Server anzumelden.
    def _login(self):
        try:
            login_dialog = LoginDialog(self._settings, self)

            if login_dialog.exec_() != QtGui.QDialog.Accepted:
                QtGui.qApp.quit()
                exit()

            self._settings = login_dialog.getSettings()

            ## Interface zum BSCW-Server
            self._bscw_interface = login_dialog.getInterface()

            reg_exp = \
                QtCore.QRegExp("(http://)?([a-zA-Z0-9_\\-:\\.]+)(/[. ^])*")
            reg_exp.exactMatch(login_dialog.getServerAddress())
            ## HTTP-Adresse des BSCW-Servers (Wird zum Herunterladen der
            # Benutzerbilder benötigt)
            self._img_url_prefix = \
                            "http://%s:%s@%s" % (str(login_dialog.getUsername()),
                            str(login_dialog.getPasswd()), str(reg_exp.cap(2)))

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Lädt eine URL in eine temporäre Datei und gibt den Pfad der
    # temporären Datei zurück
    # @param p_url URL der Datei
    # @return Pfad zur Datei als String oder None, wenn  ein Fehler aufgetreten
    # ist
    def _getFileByUrl(self, p_url):
        try:
            if p_url[0] == "/":
                p_url = self._img_url_prefix + p_url
            try:
                self._img_cache.append(urllib.URLopener())
                file = self._img_cache[-1].retrieve(p_url)[0]
                return file
            except:
                return None

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Speichert den Status vom Benutzer-Details-Dialog (offen/zu)
    # Diese Methode ist eine überladene Funktion vom MainWindow.
    # @param p_event QEvent, übergibt das von Qt gesendete Event
    def event(self, p_event):

        # Event überprüfen
        if p_event.WindowStateChange:

            # wenn Fenster (noch) nicht minimiert und nicht geschlossen
            if not self.isMinimized() and not self.isHidden():
                    self._settings.show_user_details \
                        = self._user_details.isVisible()

        # Standard-Methode ausführen
        return QtGui.QMainWindow.event(self, p_event)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
