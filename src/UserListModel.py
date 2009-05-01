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

    ## Wandelt eine Speicherangabe von MB in KB und gibt sie formatiert, mit
    # 1000er Trennzeichen und Einheit zurück
    # @param p_mem Speicher in MB
    # @return Formatierter String
    def formatMemory(p_mem):
        result = ""
        points = 0
		# Umwandeln in KB
        p_mem = str(int(p_mem * 1000))

		#  Speichern der einzelnen Stellen in einer Liste
        for i in range(0, len(p_mem))[::-1]:
            result = p_mem[i] + result

			# Einfügen eines Punktes nach jeweils 3 Stellen
            if not (len(result) - points) % 3 and i:
                result = "." + result
                points += 1

        return result + " KB"
    
	## Statische Methode für formatMemory 
    formatMemory = staticmethod(formatMemory)

    ## Konstruktor
    # @param p_header_data Eine Liste von Tupels mit jeweils zwei Elementen,
    # in denen der Schlüssel und die Überschrift stehen.
    def __init__(self, p_header_data):
		# Übergeordneten Konstruktor aufrufen
        QtCore.QAbstractTableModel.__init__(self)
        ## Liste der angezeigten Spalten
        self.header_list = p_header_data
        ## Gefilterte Benutzerliste
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
		# leeren QVariant zurück geben, wenn der übergeben Index nicht anzeigbar
		# ist
        if p_index.isValid() != True:
            return QtCore.QVariant()
		# leeren QVariant zurück geben, wenn die übergebenen Werte nicht den 
		# zur Anzeige von Text bestimmt sind
        elif p_role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
		# leeren QVariant zurück geben, wenn die gewünschte Reihe größer als die 
		# Länge der Userliste ist
        elif p_index.row() >= len(self.user_list):
            return QtCore.QVariant()
		# Ausgabe von "Ja" und "Nein" statt "True" und "False" 
        elif self.header_list[p_index.column()][0] == "admin" or \
                self.header_list[p_index.column()][0] == "locked":
            if self.user_list[p_index.row()] \
			[self.header_list[p_index.column()][0]] == True:
                return QtCore.QVariant("Ja")
            elif self.user_list[p_index.row()] \
			[self.header_list[p_index.column()][0]] == False:
                return QtCore.QVariant("Nein")
		# Ausgabe von "Nie" wenn der Typ von "last_login" "None" ist
        elif self.header_list[p_index.column()][0] == "last_login" and \
            type(self.user_list[p_index.row()]["last_login"]) == type(None):
            return QtCore.QVariant("Nie")
		# formatierte Ausgabe des verbrauchten Speicherplatzes
        elif self.header_list[p_index.column()][0] == "used_memory":
            return QtCore.QVariant(self.formatMemory( \
			self.user_list[p_index.row()] \
			[self.header_list[p_index.column()][0]]))
		# formatierte Datumsausgabe
        elif self.header_list[p_index.column()][0] == "last_login":
            date_time = datetime.datetime.strptime(self.user_list[p_index.row()] \
            [self.header_list[p_index.column()][0]].value, "%Y%m%dT%H:%M:%S")
            return QtCore.QVariant(date_time.strftime("%d.%m.%Y %H:%M"))
		# formatierte Datumsausgabe
        elif self.header_list[p_index.column()][0] == "create_time":
            date_time = datetime.datetime.strptime(self.user_list[p_index.row()] \
            [self.header_list[p_index.column()][0]].value, "%Y%m%dT%H:%M:%S")
            return QtCore.QVariant(date_time.strftime("%d.%m.%Y %H:%M"))
		# einfaches Anzeigen
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
		# leeren QVariant zurück geben, wenn der Text nicht zum anzeigen
		# bestimmt ist
        if p_role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
		# leeren QVariant zurück geben, wenn die Spaltennummer länger als die 
		# Liste der Kopfdaten ist
        elif p_section >= len(self.header_list):
            return QtCore.QVariant()
        else:
            return \
			QtCore.QVariant(QtCore.QString(self.header_list[p_section][1]))

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
	#@param p_complete p_complete ist True, wenn die komplette User-Liste angezeigt werden soll (kein Filter aktiv)
    def loadList(self, p_user_list, p_complete = True):
		# wenn kein Filter aktiv ist
        if p_complete == True:
            ## Komplette Benutzerliste
            self.complete_user_list = p_user_list
        self.user_list = p_user_list
        self.emit(QtCore.SIGNAL("layoutChanged()"))

    ## Sortiert die angezeigten Benutzer
    # @param p_column Die Nummer der Spalte nach der sortiert werden soll.
    # @param p_order Die Richtung in die sortiert werden soll.
    def sort(self, p_column, p_order):
		# wenn die User-Liste nicht leer ist
        if len(self.user_list) != 0:
			# aufsteigende Sortierung
            if p_order == QtCore.Qt.AscendingOrder:
				# Sortierung nach "Letzter Login"
                if self.header_list[p_column][0] == "last_login":
                    if len(self.user_list):
                        sorted_list = []
                        temp_list = []
						# durchgehen jedes Benutzers in der Liste
                        for user in self.user_list:
							# Kopieren aller noch nicht eingelogten Benutzer an
							# den Anfang der Sortierten Liste
                            if type(user["last_login"]) == type(None):
                                sorted_list.append(user)
							# Benutzer die sich bereits eingeloggt haben in eine
							# temporäre Liste speichern
                            else:
                                temp_list.append(user)
						# temporäre Liste sortieren
                        temp_list.sort(key = operator.itemgetter( \
                                self.header_list[p_column][0]), reverse = True)
						# Zusammenfügen beider Listen
                        temp_list.extend(sorted_list)
                        self.user_list = temp_list
				# wenn der zu sortierende Wert ein String ist, wird unabhängig
				# von Groß- und Kleinschreibung sortiert werden
                elif type(self.user_list[p_column] \
				[self.header_list[p_column][0]]) == type("String"):
                    self.user_list.sort(lambda a, b: cmp(a.lower(), b.lower()), \
					key = operator.itemgetter( \
                        self.header_list[p_column][0]))
				# einfache Sortierung von Zahlen
                else:
                    self.user_list.sort(key = operator.itemgetter( \
                                        self.header_list[p_column][0]))
			# absteigende Sortierung
            elif p_order == QtCore.Qt.DescendingOrder:
				# Sortierung nach "Letzter Login"
                if self.header_list[p_column][0] == "last_login":
                    if len(self.user_list):
                        sorted_list = []
                        temp_list = []
						# durchgehen jedes Benutzers in der Liste
                        for user in self.user_list:
							# Kopieren aller noch nicht eingelogten Benutzer an
							# den Anfang der Sortierten Liste
                            if type(user["last_login"]) == type(None):
                                sorted_list.append(user)
							# Benutzer die sich bereits eingeloggt haben in eine
							# temporäre Liste speichern
                            else:
                                temp_list.append(user)
						# temporäre Liste sortieren
                        temp_list.sort(key = operator.itemgetter( \
                        self.header_list[p_column][0]))
						# Zusammenfügen beider Listen
                        sorted_list.extend(temp_list)
                        self.user_list = sorted_list
				# wenn der zu sortierende Wert ein String ist, wird unabhängig
				# von Groß- und Kleinschreibung sortiert werden
                elif type(self.user_list[p_column] \
				[self.header_list[p_column][0]]) == type("String"):
                    self.user_list.sort(lambda a, b: cmp(a.lower(), b.lower()), \
					key = operator.itemgetter( \
                        self.header_list[p_column][0]), reverse = True)
				# einfache Sortierung von Zahlen
                else:
                    self.user_list.sort(key = operator.itemgetter( \
                        self.header_list[p_column][0]), reverse = True)
			# Emitieren eines Signals, dass sich das Layout verändert hat
            self.emit(QtCore.SIGNAL("layoutChanged()"))

    ## Übergibt eine Liste mit Spalten die angezeigt werden sollen.
    # @param p_header_data Eine Liste von Tupels mit jeweils zwei Elementen,
    # in denen der Schlüssel und die Überschrift stehen.
    # @see loadList()
    def changeHeaderData(self, p_header_data):
        self.header_list = p_header_data
		# Emitieren eines Signals, dass sich das Layout verändert hat
        self.emit(QtCore.SIGNAL("layoutChanged()"))

    ## Entfernt einen oder mehrere Benutzer aus der Liste
    # @param p_user Liste mit den Usernamen
    def removeUser(self, p_user):
		# Vergleichen der übergebenen Benutzernamen zum löschen und bei 
		# Übereinstimmung das Entfernen des jeweiligen Benutzers
        for user_name in p_user:
            counter = 0
            for user in self.user_list:
                if user_name == user["name"]:
                    del self.user_list[counter]
                counter = counter + 1
		# Laden der neuen Liste
        self.loadList(self.user_list)
		# Emitieren eines Signals, dass sich das Layout verändert hat
        self.emit(QtCore.SIGNAL("layoutChanged()"))

    ## Überschreibt ein Attribut eines oder mehrerer Benutzer mit einem neuen
	# Wert
    # p_name Liste von Namen der Benutzer
    # p_key Name des Attributs (Siehe loadList())
    # p_value Neuer Wert
    def updateUserAttr(self, p_name, p_key, p_value):
		# für jeden Benutzer in der Namensliste
        for i in range(len(p_name)):
            counter = 0
            update_id = -1
			# durchgehen der internen Liste
            for user in self.user_list:
                if user["name"] == p_name[i]:
                    update_id = counter
                counter = counter + 1
			# Setzen des neuen Userattributes
            if update_id != -1:
                self.user_list[update_id][p_key] = p_value
                self.loadList(self.user_list)

    ## Definiert einen Suchtext, nachdem gefilert wird
    # @param p_text Suchtext
    def setFilter(self, p_text):
        found = False
		# komplette Liste laden, wenn kein Text zum Filtern vorhanden ist
        if p_text == "":
            self.loadList(self.complete_user_list)
        else:
            self.user_list = []
            for user in self.complete_user_list:
				# Prüfen aller Attribute (außer "last_login" und "create_time") 
				# ob der Filtertext vorhanden ist. Bei Erfolg, Anhängen an die 
				# neue Liste.
                for i in user:
                    if i != "last_login" and i != "create_time":
                        if QtCore.QString(unicode(user[i])).contains(p_text, 0) \
						and found == False:
                            self.user_list.append(user)
                            found = True
                found = False
            self.loadList(self.user_list, False)
        self.emit(QtCore.SIGNAL("layoutChanged()"))
        