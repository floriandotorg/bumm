# -*- coding: utf-8 -*-

## @package Settings
# @brief Implementation der Settings Klasse
# @version 1
# @author Benjamin Flader
# @date 24.02.09

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

from PyQt4 import QtCore

## Verwaltet Programmeinstellungen und speichert diese.
# Abhängig vom Betriebsystem werden die Einstellungen folgendermaßen gespeichert:
#  - Windows: Registry
#  - Linux: .ini-Dateien
#  - MacOS: XML
#  Sind noch keine Einstellungen vorhanden werden die Einstellungen mit
#  Standard-Werten gefüllt.
class Settings(QtCore.QObject):

    # lege Standardwerte als statische Attribute fest
    s_username = ""
    s_server_address = ""
    s_columns = ["user_id", "name", "longname", "email", "used_memory",
                  "last_login", "locked"]
    s_col_dialog_geometry = QtCore.QRect(100, 100, 100, 100)
    s_main_window_geometry = QtCore.QRect(100, 100, 800, 800)
    s_user_details_geometry = QtCore.QRect(100, 100, 100, 100)
    s_show_user_details = True

    ## Konstruktor
    # Im Konstruktor werden die gespeicherten Werte, bzw. die Standard-Werte
    # geladen.
    # @param p_parent übergeordnetes QObject
    def __init__(self, p_parent = None):
        # initialisiere Objekt
        QtCore.QObject.__init__(self, p_parent)

        # initialisiere QSettings-Objekt
        self._settings = QtCore.QSettings("BUMM")

        # lese Einstellungen aus
        self._username = self._settings.value("username",
                            QtCore.QVariant(Settings.s_username)).toString()
        self._server_address = self._settings.value("server_address",
                            QtCore.QVariant(Settings.s_server_address)) \
                            .toString()
        self._columns = self._settings.value("columns",
                            QtCore.QVariant(Settings.s_columns)).toStringList()
        self._col_dialog_geometry = self._settings.value("col_dialog_geometry",
                            QtCore.QVariant(Settings.s_col_dialog_geometry)) \
                            .toRect()
        self._main_window_geometry = self._settings.value( \
                            "main_window_geometry",
                            QtCore.QVariant(Settings.s_main_window_geometry)) \
                            .toRect()
        self._user_details_geometry = self._settings.value(
                            "user_details_geometry", \
                            QtCore.QVariant(Settings.s_user_details_geometry)) \
                            .toRect()
        self._show_user_details = self._settings.value("show_user_details",
                            QtCore.QVariant(Settings.s_show_user_details)) \
                            .toBool()
        self._state = self._settings.value("state",
                            QtCore.QVariant(QtCore.QByteArray())).toByteArray()

    ## Dekonstruktor
    # Im Dekonstruktor werden die neuen Einstellungen gespeichert.
    # Dies geschieht bei "BUMM" automatisch am Programmende.
    def __del__(self):
        self._settings.setValue("username", QtCore.QVariant(self._username))
        self._settings.setValue("server_address",
                            QtCore.QVariant(self._server_address))
        self._settings.setValue("columns",
                            QtCore.QVariant(self._columns))
        self._settings.setValue("col_dialog_geometry",
                            QtCore.QVariant(self._col_dialog_geometry))
        self._settings.setValue("main_window_geometry",
                            QtCore.QVariant(self._main_window_geometry))
        self._settings.setValue("user_details_geometry",
                            QtCore.QVariant(self._user_details_geometry))
        self._settings.setValue("show_user_details",
                            QtCore.QVariant(self._show_user_details))
        self._settings.setValue("state", QtCore.QVariant(self._state))

        # Daten speichern
        self._settings.sync()

    # Get'er

    ## gibt den Benutzernamen zurück
    # @return Benutzername als QString
    def getUsername(self):
        return self._username

    ## gibt die Serveradresse zurück
    # @return Serveradresse als QString
    def getServerAddress(self):
        return self._server_address

    ## gibt die Spaltennamen zurück
    # @return Spaltennamen als Liste
    def getColumns(self):
        return self._columns

    ## gibt die geometrischen Daten des Spalten-Dialogs zurück
    # @return geometrische Daten des Spalten-Dialogs als QRect
    def getColDialogGeometry(self):
        return self._col_dialog_geometry

    ## gibt die geometrischen Daten des MainWindow-Dialogs zurück
    # @return geometrische Daten des MainWindow-Dialogs als QRect
    def getMainWindowGeometry(self):
        return self._main_window_geometry

    ## gibt die geometrischen Daten des UserDetail-Dialogs zurück
    # @return geometrische Daten des Login-Dialogs als QRect
    def getUserDetailsGeometry(self):
        return self._user_details_geometry

    ## gibt den Boolean ob UserDetails angezeigt werden sollen
    #  zurück
    # @return UserDetails als Boolean
    def getShowUserDetails(self):
        return self._show_user_details

    ## gibt den Status des MainWindows zurück
    #  (beinhaltet die Position und Größe der DockWidgets)
    # @return Status als QByteArray
    def getState(self):
        return self._state

    # Set'er

    ## setzt den Benutzernamen
    # @param p_username Benutzername
    def setUsername(self, p_username):
        self._username = str(p_username)

    ## setzt die Serveradresse
    # @param p_server_address Serveradresse als QString
    def setServerAddress(self, p_server_address):
        self._server_address = p_server_address

    ## setzt die Spaltennamen
    # @param p_columns Spaltennamen als Liste
    def setColumns(self, p_columns):
        self._columns = p_columns

    ## setzt die geometrischen Daten des Spalten-Dialogs
    # @param p_col_dialog_geometry geometrische Daten des Spalten-Dialogs als
    #        QRect
    def setColDialogGeometry(self, p_col_dialog_geometry):
        self._col_dialog_geometry = QtCore.QRect(p_col_dialog_geometry)

    ## setzt die geometrischen Daten des MainWindow-Dialogs
    # @param p_main_window_geometry geometrische Daten des MainWindow-Dialogs
    #        als QRect
    def setMainWindowGeometry(self, p_main_window_geometry):
        self._main_window_geometry = QtCore.QRect(p_main_window_geometry)

    ## setzt die geometrischen Daten des UserDetail-Dialogs
    # @param p_user_details_geometry geometrische Daten des Login-Dialogs als
    #        QRect
    def setUserDetailsGeometry(self, p_user_details_geometry):
        self._user_details_geometry = QtCore.QRect(p_user_details_geometry)

    ## setzt den Boolean ob UserDetails angezeigt werden sollen
    # @param p_show_user_details UserDetails als Boolean
    def setShowUserDetails(self, p_show_user_details):
        self._show_user_details = p_show_user_details

    ## setzt den Status des MainWindows
    # @param p_state MainWindow-Status als QByteArray
    def setState(self, p_state):
        self._state = p_state

    # Properties
    username = property(getUsername, setUsername)
    server_address = property(getServerAddress, setServerAddress)
    columns = property(getColumns, setColumns)
    col_dialog_geometry = property(getColDialogGeometry, setColDialogGeometry)
    main_window_geometry = property(getMainWindowGeometry, setMainWindowGeometry)
    user_details_geometry = property(getUserDetailsGeometry, \
                                     setUserDetailsGeometry)
    show_user_details = property(getShowUserDetails, setShowUserDetails)
    state = property(getState, setState)
