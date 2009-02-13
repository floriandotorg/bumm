# -*- coding: utf-8 -*-

## @package UserListModel
# @brief Implementation der Modellklasse der Liste aller Benutzer
# @version 0.1
# @author Benjamin Leipold
# @date 12.02.09

#################################################################################
# Copyright (C) 2009 Benjamin Flader, Bejamin Leipold, André Naumann,           #
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

## UserList Steuerelement
# Diese Klasse implementiert ein Steuerelement zum Anzeigen aller Benutzer
# anhand einer Liste. Mehrfachauswahl ist nicht zugelassen.
#
# Die Klasse emitiert folgende Signals:
# - SelectionChanged(p_user_id) wenn auf ein Eintrag geklickt wurde. "p_user_id"
# gibt die ID des Users zurück, welcher selektiert wurde.
class UserListModel(QtCore.QAbstractTableModel):

    ## Konstruktor
    # @param p_header_data Eine Liste von Tupels mit jeweils zwei Elementen,
    # in denen der Schlüssel und die Überschrift stehen.
    def __init__(self, p_header_data):
        QtCore.QAbstractTableModel.__init__(self)
        self.header_list = p_header_data
        self.user_list = []

    ## Gibt die Anzahl der Zeilen zurück
    # @param p_parent Übergeordnetes QObject
    def rowCount(self, p_parent=QtCore.QModelIndex()):
        return len(self.user_list)

    ## Gibt die Anzahl der Spalten zurück
    # @param p_parent Übergeordnetes QObject
    def columnCount(self, p_parent=QtCore.QModelIndex()):
        return len(self.header_list)

    ## Gibt den Wert, der in der gewünschten Zelle stehen soll zurück
    # @param p_index Spezifiziert die Zelle in der der zurückgegeben Wert 
    # stehen soll
    # @param p_role Funktion des Aufrufes
    def data(self, p_index, p_role=QtCore.Qt.DisplayRole):
        if index.isValid() != True:
            return QtCore.QVariant()
        elif p_role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        elif p_index.row() >= len(self.user_list):
            return QtCore.QVariant()
        else:
            return QtCore.QVariant(
                self.user_list[p_index.row()][self.header_list[p_index.column()][0]]
                                    )

    ## Gibt den Text, der in der gewünschten Spalte stehen soll zurück
    # @param p_section Für horizontale Header entspricht section der Nummer der
    # Spalte, für vertikale Header der Nummer der Zeile. 
    # @param p_orientation Gibt an, ob der Header horizontal oder vertikal 
    # ausgerichtet ist.
    # @param p_role Funktion des Aufrufes
    def headerData(self, p_section, p_orientation, p_role=QtCore.Qt.DisplayRole):
        if p_role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return QtCore.QVariant(QtCore.QString(self.header_list[p_section][1]))

    ## Löscht den Inhalt der Liste und zeigt den Inhalt von p_user_list an.
    # @param p_user_list Eine Liste von Dictonaries mit folgendem Aufbau:
    # - user_id : Benutzer-ID
    # - name : Benutzername
    # - longname : Vor- und Nachname
    # - email : E-Mail Adresse
    # - secondary_email : Liste mit weiteren E-Mail Adressen
    # - organization : Organisation
    # - phone_home : Telefon Heim
    # - phone_mobile : Telefon Handy
    # - phone_office : Telefon Büro
    # - fax : Faxnummer
    # - language : Sprache
    # - address : Adresse
    # - url_homepage : Webseite privat
    # - url : website Büro
    # - messaging_services : Messaging Services, Dictronary mit
    # dem Name des Service als Schlüssel und der ID (z.B ICQ-Nummer)
    # als Wert
    # - additional_info : Weitere Informationen
    # - photo : Link zum Benutzerbild oder None wenn keins existiert
    # - locked : User geserrt ja/nein (Boolean)
    # - used_memory : Speicherverbrauch in MB
    # - last_login : Letzte Anmeldung als datetime.datetime
    # - create_time : Zeit der Erstellung des Users als datetime.datetime
    # - files : Dateien (Anzahl)
    # - admin : User ist BSCW-Admin ja/nein (Boolean)
    # - workspaces : Liste aller Arbeitsbereiche, in den der User Mitglied ist
    # - accress_right : Zugriffsrechte, Dictornary mit folgendem Aufbau:
    #     - owner : Zugriffsrechte für Eigentümer: Liste mit zwei Elementen
    #        - Liste mit Usernamen, die dieser Rolle entsprechen
    #        - Liste mit Zugriffsrechten
    #     - manager : Zugriffsrechte für Manager: Liste mit zwei Elementen
    #        - Liste mit Usernamen, die dieser Rolle entsprechen
    #        - Liste mit Zugriffsrechten
    #     - other : Zugriffsrechte für alle Anderen: Liste mit zwei Elementen
    #        - Liste mit Usernamen, die dieser Rolle entsprechen
    #        - Liste mit Zugriffsrechten
    def loadList(self, p_user_list):
        self.user_list = p_user_list
        self.emit(QtCore.SIGNAL("layoutChanged()"))
        
    ## Sortiert die angezeigten Benutzer
    # @param p_column Die Nummer der Spalte nach der sortiert werden soll.
    # @param p_order Die Richtung in die sortiert werden soll.
    def sort(self, p_column, p_order):
        if p_order == QtCore.Qt.AscendingOrder:
            self.user_list.sort(key=operator.itemgetter(self.header_list[p_column][0]))
        elif p_order == QtCore.Qt.DescendingOrder:
            self.user_list.sort(key=operator.itemgetter(self.header_list[p_column][0]), reverse=True)
        self.emit(QtCore.SIGNAL("layoutChanged()"))


