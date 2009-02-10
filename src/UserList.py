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

## UserList Steuerelement
# Diese Klasse implementiert ein Steuerelement zum Anzeigen aller Benutzer
# anhand einer Liste. Mehrfachauswahl ist nicht zugelassen.
#
# Die Klasse emitiert folgende Signals:
# - SelectionChanged(p_user_id) wenn auf ein Eintrag geklickt wurde. "p_user_id"
# gibt die ID des Users zurück, welcher selektiert wurde.
class UserList(QtGui.QTreeView):

    ## Konstruktor
    # @param p_user_list Eine Liste von Dictonaries mit folgendem Aufbau:
    # - user_id : Benutzer-ID
    # - name : Benutzername
    # - longname : Vor- und Nachname
    # - email : E-Mail Adresse
    # - organization : Organisation
    # - phone_home : Telefon Heim
    # - phone_mobile : Telefon Handy
    # - phone_office : Telefon Büro
    # - fax : Faxnummer
    # - language : Sprache
    # - homepage : Webseite
    # - additional_info : Weitere Informationen
    # - locked : User geserrt ja/nein (Boolean)
    # - used_memory : Speicherverbrauch in Byte
    # - last_login : Letzte Anmeldung als datetime.datetime
    # @param p_header_data Liste von Strings mit den Namen der Spalten
    # die angezeigt werden sollen. 
    # @param p_parent Übergeordnetes QObject 
    def __init__(self, p_user_list, p_header_data, p_parent = None):
        QtGui.QTreeView.__init__(self, p_parent)
        pass
    
    ## Übergibt eine neue Liste mit Spalten die angezeigt werden sollen.
    # @param p_header_data Liste von Strings mit den Namen der Spalten
    # die angezeigt werden sollen.
    def changeHeaderData(self, p_header_data):
         pass
    
    ## Entfernt einen Benutzer aus der Liste
    # @param p_user Ein Dictonary mit einem Element "user_id" indem sich
    # die ID des Users befindet. 
    # @return Benutzer-ID des Eintrags der nun selektiert ist. None für keinen.
    def removeEntry(self, p_user):
        pass