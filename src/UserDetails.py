# -*- coding: utf-8 -*-

## @package UserDetails
# @brief Implementation eines DockWidgets zum Anzeigen zusätzlicher User 
# Informationen
# @version 0.1
# @author Corinna Vollert
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

from PyQt4 import QtGui, QtCore

## UserDetails Steuerelement
# Diese Klasse implementiert ein Steuerelement zum Anzeigen zusätzlicher
# Benutzer Informationen.
#
# Die Klasse emitiert folgende Signals:
# - RemoveUser(p_user_id) Wenn auf "Benutzer löschen" geklickt wurde. 
# "p_user_id" gibt die ID des Users zurück, welcher gelöscht werden soll.
# - LockUser(p_user_id) Wenn auf "Benutzer sperren" geklickt wurde. 
# "p_user_id" gibt die ID des Users zurück, welcher gesperrt werden soll.
# - UnlockUser(p_user_id) Wenn auf "Benutzer entsperren" geklickt wurde. 
# "p_user_id" gibt die ID des Users zurück, welcher entsperrt werden soll.
# - DestroyTrash(p_user_id)Leert den Mülleinmer des Benutzers. "p_user_id" ist
# die ID des Benutzers bei dem dies geschied.
# - DestroyClipboard(p_user_id) Räumt die Zwischenablage des Benutzers auf. 
# "p_user_id" ist die ID des Benutzers bei dem dies geschied.
class UserDetails(QtGui.QDockWidget):
    
    ## Konstruktor
    # @param p_parent Übergeordnetes QObject 
    def __init__(self, p_parent = None):
        QtGui.QDockWidget.__init__(self, p_parent)
        pass
    
    ## Zeigt alle Userinformationen im Widget an
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
    def showUser(self, p_user):
        pass
    