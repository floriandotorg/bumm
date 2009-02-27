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
import operator
import datetime
import string

## Schnittstelle zwischen Benutzerdaten und der User-Liste
# Siehe Qt Model/View Framework
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
        if p_index.isValid() != True:
            return QtCore.QVariant()
        elif p_role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        elif p_index.row() >= len(self.user_list):
            return QtCore.QVariant()
        elif self.header_list[p_index.column()][0] == "admin" or \
                self.header_list[p_index.column()][0] == "locked":
            if self.user_list[p_index.row()][self.header_list[p_index.column()][0]] == True:
                return QtCore.QVariant("Ja")
            elif self.user_list[p_index.row()][self.header_list[p_index.column()][0]] == False:
                return QtCore.QVariant("Nein")
        elif not self.user_list[p_index.row()][self.header_list[p_index.column()][0]] and \
                self.header_list[p_index.column()][0] == "last_login":
            return QtCore.QVariant("Nie")
        elif self.header_list[p_index.column()][0] == "used_memory":
            kilobyte_output = \
            str(int(self.user_list[p_index.row()] \
            [self.header_list[p_index.column()][0]] * 1000)) \
            + " KB"
            return QtCore.QVariant(kilobyte_output)
        elif self.header_list[p_index.column()][0] == "last_login":
            date_time = datetime.datetime.strptime(self.user_list[p_index.row()]
                    [self.header_list[p_index.column()][0]].value, "%Y%m%dT%H:%M:%S")
            return QtCore.QVariant(date_time.strftime("%d.%m.%Y %H:%M"))
        elif self.header_list[p_index.column()][0] == "create_time":
            date_time = datetime.datetime.strptime(self.user_list[p_index.row()]
                    [self.header_list[p_index.column()][0]].value, "%Y%m%dT%H:%M:%S")
            return QtCore.QVariant(date_time.strftime("%d.%m.%Y %H:%M"))
        else:
            return QtCore.QVariant(
                self.user_list[p_index.row()]
                    [self.header_list[p_index.column()][0]])

    ## Gibt den Text, der in der gewünschten Spalte stehen soll zurück
    # @param p_section Für horizontale Header entspricht section der Nummer der
    # Spalte, für vertikale Header der Nummer der Zeile.
    # @param p_orientation Gibt an, ob der Header horizontal oder vertikal
    # ausgerichtet ist.
    # @param p_role Funktion des Aufrufes
    def headerData(self, p_section, p_orientation,
                                p_role = QtCore.Qt.DisplayRole):
        if p_role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        elif p_section >= len(self.header_list):
            return QtCore.QVariant()
        else:
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
    # - locked : User gesperrt ja/nein (Boolean)
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
    def loadList(self, p_user_list, p_complete = True):
        if p_complete == True:
            self.complete_user_list = p_user_list
        self.user_list = p_user_list
        self.emit(QtCore.SIGNAL("layoutChanged()"))

    ## Sortiert die angezeigten Benutzer
    # @param p_column Die Nummer der Spalte nach der sortiert werden soll.
    # @param p_order Die Richtung in die sortiert werden soll.
    def sort(self, p_column, p_order):
        if len(self.user_list) != 0:
            if p_order == QtCore.Qt.AscendingOrder:
                '''if self.header_list[p_column][0] == "last_login":
                    self.user_list.sort(key = (operator.itemgetter(self.header_list[p_column][0])).value)
                elif self.header_list[p_column][0] == "create_time":
                    self.user_list.sort(key = (operator.itemgetter(self.header_list[p_column][0])).value)
                else:
                self.user_list.sort(key = operator.itemgetter(self.header_list[p_column][0]))'''
            elif p_order == QtCore.Qt.DescendingOrder:
                '''if self.header_list[p_column][0] == "last_login":
                    pass
                elif self.header_list[p_column][0] == "create_time":
                    pass
                else:'''
                #self.user_list.sort(key = operator.itemgetter(self.header_list[p_column][0]), reverse = True)

            self.emit(QtCore.SIGNAL("layoutChanged()"))

    ## Übergibt eine Liste mit Spalten die angezeigt werden sollen.
    # @param p_header_data Eine Liste von Tupels mit jeweils zwei Elementen,
    # in denen der Schlüssel und die Überschrift stehen.
    # @see loadList()
    def changeHeaderData(self, p_header_data):
        self.header_list = p_header_data
        self.emit(QtCore.SIGNAL("layoutChanged()"))

    ## Entfernt einen oder mehrere Benutzer aus der Liste
    # @param p_user Liste mit den Usernamen
    def removeUser(self, p_user):
        for user_name in p_user:
            counter = 0
            for user in self.user_list:
                if user_name == user["name"]:
                    del self.user_list[counter]
                counter = counter + 1
        self.loadList(self.user_list)
        self.emit(QtCore.SIGNAL("layoutChanged()"))

    ## Überschreibt ein Attribut eines oder mehrerer Benutzer mit einem neuen Wert
    # p_name Liste von Namen der Benutzer
    # p_key Name des Attributs (Siehe loadList())
    # p_value Neuer Wert
    def updateUserAttr(self, p_name, p_key, p_value):
        counter = 0
        update_id = -1
        for i in range(len(p_name)):
            for user in self.user_list:
                if user["name"] == p_name[i]:
                    update_id = counter
                counter = counter + 1
            if update_id != -1:
                self.user_list[update_id][p_key] = p_value
                self.loadList(self.user_list)

    ## Definiert einen Suchtext, nachdem gefilert wird
    # @param p_text Suchtext
    def setFilter(self, p_text):
        found = False
        if p_text == "":
            self.loadList(self.complete_user_list)
        else:
            self.user_list = []
            for user in self.complete_user_list:
                for i in user:
                    if i != "last_login" and i != "create_time":
                        if user[i] == p_text and found == False:
                            self.user_list.append(user)
                            found = True
                found = False
            self.loadList(self.user_list, False)
        self.emit(QtCore.SIGNAL("layoutChanged()"))