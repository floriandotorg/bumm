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
from ui_UserDetails import Ui_UserDetails
import datetime

## Implementation eines Steuerelements zum Anzeigen zusätzlicher
# Benutzerinformationen.
#
# Die Klasse emitiert folgende Signals:
# - RemoveUser(p_user_name) Wenn auf "Benutzer löschen" geklickt wurde.
# "p_user_name" gibt den Name des Users an, welcher gelöscht werden soll.
# - LockUser(p_user_name) Wenn auf "Benutzer sperren" geklickt wurde.
# "p_user_name" gibt den Name des Users an, welcher gesperrt werden soll.
# - UnlockUser(p_user_name) Wenn auf "Benutzer entsperren" geklickt wurde.
# "p_user_name" gibt den Name des Users an, welcher entsperrt werden soll.
# - DestroyTrash(p_user_name) Leert den Mülleinmer des Benutzers. "p_user_name"
# ist der Name des Benutzers bei dem dies geschied.
# - DestroyClipboard(p_user_name) Räumt die Zwischenablage des Benutzers auf.
# "p_user_name" ist der Name des Benutzers bei dem dies geschied.
class UserDetails(QtGui.QDockWidget, Ui_UserDetails):

    ## Konstruktor
    # @param p_parent Übergeordnetes QObject
    def __init__(self, p_parent = None):
        QtGui.QDockWidget.__init__(self, p_parent)
        self.setupUi(self)

    ## Zeigt alle Userinformationen im Widget an
    # @param p_user Eine Liste von Dictonaries mit folgendem Aufbau oder
    # None für keinen:
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
    # - local_photo : Pfad zum lokal zwischengespeicherten Benutzerbild oder
    # None wenn keins existiert
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
    def showUser(self, p_user):
        if p_user:

            self._user.setText(p_user["name"])
            self._user_id.setText(str(p_user["user_id"]))

            ##Daten des Info-Tab
            self._full_name.setText(p_user["longname"])
            if p_user["admin"] == False:
                self._admin.setText("Nein")
            else:
                self._admin.setText("Ja")
            if p_user["locked"] == False:
                self._locked.setText("Nein")
            else:
                self._locked.setText("Ja")
            self._mail.setText(p_user["email"])
            if p_user["secondary_email"]:
                text = ""
                for i in range(len(p_user["secondary_email"])):
                    text += (p_user["secondary_email"][i] + "\n")
                self._more_mail.setText(text)
            else:
                self._more_mail.setText("")
            last_login = datetime.datetime.strptime(p_user["last_login"].value, "%Y%m%dT%H:%M:%S")
            self._last_login.setText(last_login.strftime("%d.%m.%Y %H:%M"))
            if p_user["workspaces"]:
                text = ""
                for i in range(len(p_user["workspaces"])):
                    text += (p_user["workspaces"][i] + "\n")
                self._workspace.setText(text)
            else:
                self._workspace.setText("")

            ##Daten des Konto-Tab
            create_time = datetime.datetime.strptime(p_user["create_time"].value, "%Y%m%dT%H:%M:%S")
            self._create_time.setText(create_time.strftime("%d.%m.%Y %H:%M"))
            self._storage_usage.setText(str(p_user["used_memory"]))
            self._objects.setText(str(p_user["files"]))
            #self._role_owner_as_owner.setText(str(p_user["access_right"]["owner"]))

            ##Daten des Persönliches-Tab
            self._private_tel.setText(p_user["phone_home"])
            self._mobile_tel.setText(p_user["phone_mobile"])
            self._office_tel.setText(p_user["phone_office"])
            self._fax.setText(p_user["fax"])
            self._language.setText(p_user["language"])
            self._organisation.setText(p_user["organization"])
            #self._private_url.setText(p_user["url_homepage"])
            self._office_url.setText(p_user["url"])
            self._address.setText(p_user["address"])
            self._instant_messenger.setText(str(p_user["messaging_services"]))
            self._more_info.setText(p_user["additional_info"])

            try:
                self._lbl_pic.setPixmap(QtGui.QPixmap(p_user["local_photo"]))
            except:
                self._lbl_pic.clear()
        else:
            self._user.setText("kein Benutzer!")
