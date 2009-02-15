# -*- coding: utf-8 -*-

## @package UserList
# @brief Implementation der Liste aller Benutzer
# @version 0.1
# @author Benjamin Leipold
# @date 12.02.09

#################################################################################
# Copyright (C) 2009 Benjamin Flader, Benjamin Leipold, André Naumann,           #
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
import UserListModel

## UserList Steuerelement
# Diese Klasse implementiert ein Steuerelement zum Anzeigen aller Benutzer
# anhand einer Liste. Mehrfachauswahl ist zugelassen.
#
# Die Klasse emitiert folgende Signals:
# - SelectionChanged() Wenn die Auswahl geändert wurde.
class UserList(QtGui.QTreeView):

    ## Konstruktor
    # @param p_header_data Siehe changeHeaderData()
    # @param p_parent Übergeordnetes QObject 
    def __init__(self, p_header_data, p_parent = None):
        QtGui.QTreeView.__init__(self, p_parent)
        self.model = UserListModel.UserListModel(p_header_data)
        self.setModel(self.model)
        self.setRootIsDecorated(False)
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QtGui.QTreeView.ExtendedSelection)
        #self.setVerticalScrollMode(QtGui.QTreeView.ScrollPerPixel)
        #self.setHorizontalScrollMode(QtGui.QTreeView.ScrollPerPixel)
    
    ## Gibt eine Liste der selektierten User zurück
    # @return Liste von Dictonaries mit Userdaten (siehe loadList())
    # @see loadList()
    def getSelection(self):
        pass
    
    ## Definiert einen Suchtext, nachdem gefilert wird
    # @param p_text Suchtext 
    def setFilter(self, p_text):
        pass
    
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
    # - access_right : Zugriffsrechte, Dictornary mit folgendem Aufbau:
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
        self.model.loadList(p_user_list)
    
    ## Übergibt eine Liste mit Spalten die angezeigt werden sollen.
    # @param p_header_data Eine Liste von Tupels mit jeweils zwei Elementen,
    # in denen der Schlüssel und die Überschrift stehen.
    # @see loadList()
    def changeHeaderData(self, p_header_data):
         self.model.changeHeaderData(p_header_data)
    
    ## Entfernt einen Benutzer aus der Liste
    # @param p_user Ein Dictonary mit einem Element "user_id" indem sich
    # die ID des Users befindet. 
    # @return Benutzer-ID des Eintrags der nun selektiert ist. None für keinen.
    def removeEntry(self, p_user):
        pass