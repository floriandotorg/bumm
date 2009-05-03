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

from PyQt4 import QtGui, QtCore
from ui_MainWindow import Ui_MainWindow
from interface.BscwInterface import BscwInterface
from UserList import UserList
from UserDetails import UserDetails
from LoginDialog import LoginDialog
from Settings import Settings
from InfoDialog import InfoDialog
from SetColumnDialog import SetColumnDialog
from ActionThread import ActionThread
from ErrorDialog import ErrorDialog
import webbrowser
import urllib
import tempfile
import interface

## Diese Klasse stellt das Hauptfenster der Anwendung da und managed alle
# Funktionen des Programms
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    ## Konstruktor
    # @param p_parent Übergeordnetes QObject
    def __init__(self, p_parent = None):
        try:
            # Übergeordneten Konstruktor aufrufen
            QtGui.QMainWindow.__init__(self, p_parent)
            # Und Fenster konstruieren (Siehe Qt-Dokumentation)
            self.setupUi(self)

            ## Liste aller heruntergeladenen Benutzerbilder
            self._img_cache = []

            ## DockWidget indem nähere Benutzerinformationen angezeigt werden
            self._user_details = UserDetails(self)
            # DockWidget dem Fenster hinzufügen
            self.addDockWidget(QtCore.Qt.RightDockWidgetArea,
                                                    self._user_details)

            ## Programmeinstellungen
            self._settings = Settings()

            ## Login öffnen
            self._login()
            
            # Einstellungen laden
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
            
            ## Button um die Liste zu filtern
            self._button_filter = QtGui.QPushButton(self)
            self._button_filter.setText(self.trUtf8("Suchen"))
            self._toolbar.addWidget(self._button_filter)
            
            # Wenn ein oder mehrere Einträge markiert werden, dann 
            # das SockWidget aktualisieren
            self.connect(self._user_list,
                            QtCore.SIGNAL("SelectionChanged()"),
                            self._selectionChangedSlot)
            
            # Die UserDetails abhängig vom "User Details"-Button
            # anzeigen bzw. verbergen
            self.connect(self._action_user_details,
                            QtCore.SIGNAL("triggered(bool)"),
                            self._user_details.setVisible)
            self.connect(self._user_details,
                            QtCore.SIGNAL("visibilityChanged(bool)"),
                            self._action_user_details.setChecked)

            # Die User-Liste anzeigen, wenn auf "Alles aktualisieren" geklickt
            # wurde
            self.connect(self._action_update_all, QtCore.SIGNAL("triggered()"),
                            self._loadList)

            # SetColumnDialog anzeigen, wenn auf "Spalten auswählen..."
            # geklickt wurde
            self.connect(self._action_set_cols, QtCore.SIGNAL("triggered()"),
                            self._showSetColumnDialogSlot)

            # User (ent-)sperren, User löschen und Aufräumarbeiten starten,
            # wenn auf den entsprechenden Button geklicht wurde
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

            # Hilfe im Standard-Webbrowser anzeigen, wenn auf
            # "Hilfe -> Inhalt" geklckt wurde
            self.connect(self._action_help_content, QtCore.SIGNAL("triggered()"),
                         self._showManualSlot)

            # Info-Dialog anzeigen wenn auf "Hilfe -> Info" geklickt wurde
            self.connect(self._action_info, QtCore.SIGNAL("triggered()"),
                            self._showInfoSlot)

            # Die Liste filtern, wenn im Suchtextfeld "Enter" gedrückt oder
            # der "Suchen"-Button angeklickt wurde
            self.connect(self._line_edit_filter,
                            QtCore.SIGNAL("returnPressed()"),
                            self._setUserListFilterSlot)
            self.connect(self._button_filter,
                            QtCore.SIGNAL("clicked()"),
                            self._setUserListFilterSlot)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Überladene Methode:  Lädt die Benutzerdaten vom BSCW Server und zeigt das
    # Hauptfenster an
    def show(self):
        try:
            # Fenster anzeigen
            QtGui.QMainWindow.show(self)
            # Benutzerliste laden
            self._loadList()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()
            
    ## Überladene Methode: Speichert den Status vom Benutzer-Details-Dialog 
    # (offen/zu)
    # @param p_event QEvent, übergibt das von Qt gesendete Event
    def event(self, p_event):

        # Event überprüfen
        if p_event.WindowStateChange:

            # Wenn Fenster (noch) nicht minimiert und nicht geschlossen
            if not self.isMinimized() and not self.isHidden():
                    self._settings.show_user_details \
                        = self._user_details.isVisible()

        # Standard-Methode ausführen
        return QtGui.QMainWindow.event(self, p_event)

    ## Überladene Methode: Speichert alle Einstellungen, wenn das Fenster
    # geschlossen wurde
    # @param p_event Qt-Close-Event
    def closeEvent(self, p_event):

        try:
            # Einstellungen speichern
            self._settings.columns = [i[0] for i in self._headers]
            self._settings.main_window_geometry = self.geometry()
            self._settings.user_details_geometry = \
                                    self._user_details.geometry()

            # Wenn das Hauptfenster minimiert wurde, dann die Sichtbarkeit
            # des DockWidgets nicht speichern, weil diese dann immer
            # "False" ist
            if not self.isMinimized():
                self._settings.show_user_details = \
                                    self._user_details.isVisible()

                self._settings.state = self.saveState()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()
            
    ## Erzeugt einen Thread, der eine Aufgabe ausführt, die die Anwendung
    # durch eine lange Laufzeit blockieren könnte
    # @param p_func Zeiger auf eine Funktion mit langer Laufzeit
    # @param p_finished Zeiger auf eine Funktion, die aufgerufen wird,
    # wenn die Aufgabe bearbeitet wurde
    # @param p_params Parameter, die beim Aufruf übergeben werden
    def _action(self, p_func, p_finished, *p_params):
        try:
            ## Thread für Aufgaben mit langer Laufzeit
            self._action_thread = ActionThread(self, p_func, *p_params)
            
            # Wenn der Thread beendet wurde, dann führe die im Parameter
            # p_finished spezifizierte Funktion aus
            self.connect(self._action_thread, QtCore.SIGNAL("finished()"),
                         p_finished)
            
            # Thread starten
            self._action_thread.start()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()
 
    ## Lädt die Daten aller Benutzer und stellt diese in der Liste da
    def _loadList(self):
        try:
            # Fenster blockieren und Statusmeldung anzeigen
            self._lockWidget(True,
                             self.trUtf8("Benutzerliste wird geladen ..."))
            
            # Thread starten, der die Liste vom Server lädt
            self._action(self._bscw_interface.getAllUser,
                             self._listLoadedSlot)
            
        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Sperrt/Entsperrt das Widget und zeigt eine Meldung in der Statusleiste an
    # @param p_lock Widget sperren ja/nein (Boolean)
    # @param p_message Nachricht für die Statusbar
    def _lockWidget(self, p_lock, p_message = None):
        try:
            # Steuerelement sperren ja/nein in 
            # Steuerelement aktiv ja/nein umwandeln
            p_lock = not p_lock
            
            # Die wichtigsten Elemente der GUI sperren bzw. entsperren
            self._toolbar.setEnabled(p_lock)
            self._user_list.setEnabled(p_lock)
            self._menubar.setEnabled(p_lock)
            self._user_details.setEnabled(p_lock)
            
            # Statusnachricht setzten, wenn gewünscht
            if p_message:
                ## Label in der Statusleiste, indem Statusnachrichten
                # angezeigt werden
                self._lbl_status = QtGui.QLabel(p_message, self)
                self._statusbar.addWidget(self._lbl_status, 2)
            else:
                self._statusbar.removeWidget(self._lbl_status)
                
            # Fenster aktualisieren
            QtGui.qApp.processEvents()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Entsperrt das Widget und löscht die Status-Nachricht
    # Wrapper für _lockWidget(False)
    def _unlockWidget(self):
        try:
            self._lockWidget(False)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Aktiviert/Deaktiviert die User-Aktions-Menüs
    # @param p_enabled Menüs aktiviert ja/nein (Boolean)
    def _setUserActionEnabled(self, p_enabled):
        try:
            # Menüpunkte und Toolbar-Buttons, die sich auf bestimmte User
            # beziehen, sperren bzw. entsperren
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
            # UserDetails nuranzeigen, wenn genau EIN Benutzer ausgewählt
            # wurde
            if len(p_selection) == 1:
                
                # Wenn ein Benutzerbild existiert und es noch nicht runter-
                # geladen wurde ...
                if not "local_photo" in p_selection[0] \
                                                    and p_selection[0]["photo"]:
                    # .. Widget sperren und Bild herunterladen
                    self._lockWidget(True,
                                self.trUtf8("Benutzerbild wird geladen ..."))
                    p_selection[0]["local_photo"] = \
                                self._getFileByUrl(p_selection[0]["photo"])
                    self._unlockWidget()
                
                # Benutzerinfo im DockWidget anzeigen
                self._user_details.showUser(p_selection[0])
            
            else:
                self._user_details.showUser(None)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()
            
    ## Zeigt den LoginDialog an und versucht sich per BscwInterface am
    #  BSCW-Server anzumelden.
    def _login(self):
        try:
            # Login Dialog
            login_dialog = LoginDialog(self._settings, self)

            # Wurde auf "Abbrechen" geklickt?
            if login_dialog.exec_() != QtGui.QDialog.Accepted:
                # Dann Programm beenden
                QtGui.qApp.quit()
                exit()

            # Einstellungen des Login Dialogs speichern
            self._settings = login_dialog.getSettings()

            ## Interface zum BSCW-Server
            self._bscw_interface = login_dialog.getInterface()

            # HTTP-Adresse aus Server Adresse extrahieren
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
            # Liegt das Bild auf dem BSCW-Server?
            if p_url[0] == "/":
                # Dann Server Adresse vor den Pfad des Bildes setzten
                p_url = self._img_url_prefix + p_url
            
            try:
                # URLopener Objekt speichern, damit das Bild nicht
                # gelöscht wird
                self._img_cache.append(urllib.URLopener())
                
                # Datei runterladen und zurückgeben
                file = self._img_cache[-1].retrieve(p_url)[0]
                return file
            except:
                return None

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Sperrt alle in der Benutzerliste angewählten User
    def _lockUserSlot(self):
        try:
            # Liste der zu sperrenden Benutzer
            to_lock = []

            # Den Benutzernamen aller selektierten User der Liste hinzufügen
            for i in self._user_list.getSelection():
                to_lock.append(i["name"])

            # Fenster sperren und Thread starten, der die Benutzer sperrt
            self._lockWidget(True, self.trUtf8("Benutzer werden gesperrt ..."))
            self._action(self._bscw_interface.lockUser, self._unlockWidget,
                            to_lock)

            # Benutzerliste aktualisieren
            self._user_list.updateUserAttr(to_lock, "locked", True)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Entsperrt alle in der Benutzerliste angewählten User
    def _unlockUserSlot(self):
        try:
            # Liste der zu entsperrenden Benutzer
            to_unlock = []

            # Den Benutzernamen aller selektierten User der Liste hinzufügen
            for i in self._user_list.getSelection():
                to_unlock.append(i["name"])

            # Fenster sperren und Thread starten, der die Benutzer entsperrt
            self._lockWidget(True, self.trUtf8("Benutzer werden entsperrt ..."))
            self._action(self._bscw_interface.unlockUser, self._unlockWidget,
                            to_unlock)
            
            # Benutzerliste aktualisieren
            self._user_list.updateUserAttr(to_unlock, "locked", False)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Leer die Mülleimer der Benutzer. Das Mindestalter der Dateien wird mithilfe
    # eines Dialogs definiert.
    def _destroyTrashSlot(self):
        try:
            # Liste der Benutzer, bei denen der Mülleimer geleert werden soll 
            user = []

            # Den Benutzernamen aller selektierten User der Liste hinzufügen
            for i in self._user_list.getSelection():
                user.append(i["name"])

            # Per Dialog das Mindestalter der Dateien ermitteln
            outdated = QtGui.QInputDialog.getInteger(self,
                            self.trUtf8("Mindestalter angeben"),
                            self.trUtf8("Mindestalter der zu " \
                                        "löschenden Dateien (in Tagen):"),
                            5, 0)

            # Wurde im Buttin auf OK geklickt ..
            if outdated[1]:
                # .. dann Widget sperren und Thread starten, der die Mülleimer
                # leert
                self._lockWidget(True, self.trUtf8("Mülleimer werden " \
                                                   "geleert ..."))
                self._action(self._bscw_interface.destroyTrash,
                             self._unlockWidget,
                             outdated[0], user)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Räumt die Zwischenablagen der Benutzer auf. Das Mindestalter der Dateien
    # wird mithilfe eines Dialogs definiert.
    def _destroyClipboardSlot(self):
        try:
            # Liste der Benutzer, bei denen die Zwischenablage gelöscht werden soll 
            user = []

            # Den Benutzernamen aller selektierten User der Liste hinzufügen
            for i in self._user_list.getSelection():
                user.append(i["name"])
            
            # Per Dialog das Mindestalter der Dateien ermitteln
            outdated = QtGui.QInputDialog.getInteger(self,
                            self.trUtf8("Mindestalter angeben"),
                            self.trUtf8("Mindestalter der zu " \
                                        "löschenden Dateien (in Tagen):"),
                            5, 0)
            
            # Wurde im Buttin auf OK geklickt ..
            if outdated[1]:
                # .. dann Widget sperren und Thread starten, der die Zwischenablagen
                # löscht
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
            # Liste der zu löschenden User
            to_delete = []

            # Den Benutzernamen aller selektierten User der Liste hinzufügen
            for i in self._user_list.getSelection():
                to_delete.append(i["name"])
                
            # Sicherheitsabfrage durchführen
            ret = QtGui.QMessageBox.question(self,
                            self.trUtf8("%1 User löschen?") \
                            .arg(len(to_delete)),
                            self.trUtf8("Sind Sie sicher, dass Sie die " \
                            "ausgewählten Benutzer löschen möchten?"),
                            QtGui.QMessageBox.Yes , QtGui.QMessageBox.No)

            # Wurde auf "Ja" geklickt ..
            if ret == QtGui.QMessageBox.Yes:
                # .. dann Fenster sperren und Thread starten, der die Benutzer 
                # löscht
                self._lockWidget(True,
                                 self.trUtf8("Benutzer werden gelöscht ..."))
                self._action(self._bscw_interface.deleteUser,
                             self._unlockWidget,
                             to_delete)
                
                # Benutzer aus der Liste entfernen
                self._user_list.removeUser(to_delete)
                
                # User Details ausgrauen
                self._user_details.showUser(None)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()

    ## Setzt den Filter der User-Liste
    def _setUserListFilterSlot(self):
        try:
            # Filter setzten
            self._user_list.setFilter(self._line_edit_filter.text())

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()
            
    ## Lädt die Benutzerdaten in die User-Liste und entsperrt das Fenster
    def _listLoadedSlot(self):
        try:
            # Die Benutzerdaten in der Liste anzeigen
            self._user_list.loadList(self.sender().getResult())
            # User Details ausgrauen
            self._user_details.showUser(None)
            # Fenster entsperren
            self._unlockWidget()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()
            
    ## Zeigt das Benutzerhandbuch im Standard-Webrowser an
    def _showManualSlot(self):
        try:
            webbrowser.open(QtCore.QFileInfo(__file__).dir().absolutePath() +
                            "/manual/index.html")
            
        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()
        
            
    ## Zeigt ein Info-Dialog an
    def _showInfoSlot(self):
        try:
            # Info-Dialog instanzieren ..
            info_dialog = InfoDialog(self)
            # .. und anzeigen
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
            # Dialog erstellen, die Größe des Dialogs aus den Einstellungen
            # laden und den Dialog anzeigen
            set_column_dialog = SetColumnDialog(self._headers, self)
            set_column_dialog.setGeometry(self._settings.col_dialog_geometry)
            set_column_dialog.exec_()
            
            # Wurde auf OK geklickt?
            if set_column_dialog.result() == QtGui.QDialog.Accepted:
                # Dann die User-Liste aktualisieren
                self._headers = set_column_dialog.getHeaderData()
                self._user_list.changeHeaderData(self._headers)
                
            # Die neuen Maße des Dialogs in den Einstellungen speichern
            self._settings.col_dialog_geometry = set_column_dialog.geometry()

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()
            
    ## Aktualisiert die User-Details und die Toolbar
    def _selectionChangedSlot(self):
        try:
            # Liste der ausgewählten User holen
            selection = self._user_list.getSelection()
            
            # Sind User selektiert?
            if selection != []:
                # Dann Operationen aktivieren, die sich auf bestimmte User
                # beziehen
                self._setUserActionEnabled(True)
            else:
                # Ansonsten diese Operationen deaktivieren
                self._setUserActionEnabled(False)
            
            # UserDetails-DockWidget aktualisieren
            self._updateUserDetails(selection)

        except Exception, exception:
            # Fehlerdialog anzeigen
            err_dialog = ErrorDialog(exception, self)
            err_dialog.exec_()
