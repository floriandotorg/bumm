# -*- coding: utf-8 -*-

## @package UserDetails
# @brief Implementation eines DockWidgets zum Anzeigen zusätzlicher User
# Informationen
# @version 1
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
from UserListModel import UserListModel
from ImageLabel import ImageLabel
import datetime

## Implementation eines Steuerelements zum Anzeigen zusätzlicher
# Benutzerinformationen.
class UserDetails(QtGui.QDockWidget, Ui_UserDetails):

    ## Konstruktor
    # @param p_parent Übergeordnetes QObject
    def __init__(self, p_parent = None):
        QtGui.QDockWidget.__init__(self, p_parent)
        self.setupUi(self)

        ## Label in dem das Benutzerbild angezeigt wird
        self._lbl_pic = ImageLabel(self._pic_tab)
        # Layout erstellen, Bildlabel hinzufügen und Layout setzten
        lay = QtGui.QHBoxLayout(self._pic_tab)
        lay.addWidget(self._lbl_pic)
        self._pic_tab.setLayout(lay)

        ## Ein Dictonary, das die Benutzerrechte enthält
        self._rights_describtion = {"change_pwd" : "Passwort aendern",
                                   "contact" : "Ansprechen",
                                   "edit_prefs" : "Einstellungen",
                                   "editdetails" : "Profil aendern",
                                   "get" : "Oeffnen",
                                   "history" : "Verlauf zeigen",
                                   "info" : "Weitere Informationen",
                                   "mail_to" : "Email",
                                   "get_vcard" : "vCard"}


    ## Zeigt alle Userinformationen im Widget an
    # @param p_user Ein Dictonary mit folgendem Aufbau oder
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
    # - url_home : Webseite privat
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
    # - access_rights : Zugriffsrechte, Dictornary mit folgendem Aufbau:
    #     - owner : Zugriffsrechte für Eigentümer: Tupel mit zwei Listen
    #        - Liste mit Usernamen, die dieser Rolle entsprechen
    #        - Liste mit Zugriffsrechten
    #     - manager : Zugriffsrechte für Manager: Liste mit zwei Elementen
    #        - Liste mit Usernamen, die dieser Rolle entsprechen
    #        - Liste mit Zugriffsrechten
    #     - other : Zugriffsrechte für alle Anderen: Liste mit zwei Elementen
    #        - Liste mit Usernamen, die dieser Rolle entsprechen
    #        - Liste mit Zugriffsrechten
    def showUser(self, p_user):

        if not p_user: # Es ist kein Benutzer ausgewählt:

            # Im Feld "Benutzername" steht der Text "Kein Benutzer!"
            self._user.setText("Kein Benutzer!")
            # Alle anderen Felder werden gelehrt
            self._user_id.setText("")
            self._full_name.setText("")
            self._admin.setText("")
            self._locked.setText("")
            self._mail.setText("")
            self._more_mail.setText("")
            self._last_login.setText("")
            self._workspace.setText("")
            self._create_time.setText("")
            self._storage_usage.setText("")
            self._objects.setText("")
            self._role_owner_as_owner.setText("")
            self._actions_as_owner.setText("")
            self._role_owner_as_manager.setText("")
            self._actions_as_manager.setText("")
            self._role_owner_as_other.setText("")
            self._actions_as_other.setText("")
            self._private_tel.setText("")
            self._mobile_tel.setText("")
            self._office_tel.setText("")
            self._fax.setText("")
            self._language.setText("")
            self._organisation.setText("")
            self._private_url.setText("")
            self._office_url.setText("")
            self._address.setText("")
            self._instant_messenger.setText("")
            self._more_info.setText("")

            # Alle Felder werden ausgegraut
            self._user.setEnabled(False)
            self._user_id.setEnabled(False)
            self._full_name.setEnabled(False)
            self._admin.setEnabled(False)
            self._locked.setEnabled(False)
            self._mail.setEnabled(False)
            self._more_mail.setEnabled(False)
            self._last_login.setEnabled(False)
            self._workspace.setEnabled(False)
            self._create_time.setEnabled(False)
            self._storage_usage.setEnabled(False)
            self._objects.setEnabled(False)
            self._role_owner_as_owner.setEnabled(False)
            self._actions_as_owner.setEnabled(False)
            self._role_owner_as_manager.setEnabled(False)
            self._actions_as_manager.setEnabled(False)
            self._role_owner_as_other.setEnabled(False)
            self._actions_as_other.setEnabled(False)
            self._private_tel.setEnabled(False)
            self._mobile_tel.setEnabled(False)
            self._office_tel.setEnabled(False)
            self._fax.setEnabled(False)
            self._language.setEnabled(False)
            self._organisation.setEnabled(False)
            self._private_url.setEnabled(False)
            self._office_url.setEnabled(False)
            self._address.setEnabled(False)
            self._instant_messenger.setEnabled(False)
            self._more_info.setEnabled(False)

            # Bildlabel wird geleert
            self._lbl_pic.clear()

        else: # Ein Benutzer wurde ausgewählt:

            # Alle Felder werden aktiviert
            self._user.setEnabled(True)
            self._user_id.setEnabled(True)
            self._full_name.setEnabled(True)
            self._admin.setEnabled(True)
            self._locked.setEnabled(True)
            self._mail.setEnabled(True)
            self._more_mail.setEnabled(True)
            self._last_login.setEnabled(True)
            self._workspace.setEnabled(True)
            self._create_time.setEnabled(True)
            self._storage_usage.setEnabled(True)
            self._objects.setEnabled(True)
            self._role_owner_as_owner.setEnabled(True)
            self._actions_as_owner.setEnabled(True)
            self._role_owner_as_manager.setEnabled(True)
            self._actions_as_manager.setEnabled(True)
            self._role_owner_as_other.setEnabled(True)
            self._actions_as_other.setEnabled(True)
            self._private_tel.setEnabled(True)
            self._mobile_tel.setEnabled(True)
            self._office_tel.setEnabled(True)
            self._fax.setEnabled(True)
            self._language.setEnabled(True)
            self._organisation.setEnabled(True)
            self._private_url.setEnabled(True)
            self._office_url.setEnabled(True)
            self._address.setEnabled(True)
            self._instant_messenger.setEnabled(True)
            self._more_info.setEnabled(True)

            ## Benutzername und Benutzer-ID
            self._user.setText(p_user["name"])
            self._user_id.setText(str(p_user["user_id"]))

            ## Daten des Info-Tab
            # Voller Name
            self._full_name.setText(p_user["longname"])
            # Administrator-Rechte?
            if p_user["admin"] == False:
                self._admin.setText("Nein")
            else:
                self._admin.setText("Ja")
            # Benutzer gesperrt?
            if p_user["locked"] == False:
                self._locked.setText("Nein")
            else:
                self._locked.setText("Ja")
            # Primäre Email-Adresse
            self._mail.setText(p_user["email"])
            # Sekundäre Email-Adressen
            if p_user["secondary_email"]:
                text = ""
                # text = Liste aller sekundären Email-Adressen
                for i in range(len(p_user["secondary_email"])):
                    text += (p_user["secondary_email"][i] + "\n")
                self._more_mail.setText(text)
            else:
                self._more_mail.setText("")
            # Letzter Login
            if type(p_user["last_login"]) == type(None):
                self._last_login.setText("Nie")
            else:
                last_logged = datetime.datetime. \
                strptime(p_user["last_login"].value, "%Y%m%dT%H:%M:%S")
                self._last_login.setText(last_logged.strftime("%d.%m.%Y %H:%M"))
            # Arbeitsbereiche
            if p_user["workspaces"]:
                text = ""
                # text = Liste aller Arbeitsbereiche
                for i in range(len(p_user["workspaces"])):
                    text += (p_user["workspaces"][i] + "\n")
                self._workspace.setText(text)
            else:
                self._workspace.setText("")

            ## Daten des Konto-Tab
            # Erstellungsdatum
            if type(p_user["create_time"]) == type(None):
                self._create_time.setText("Nie")
            else:
                created = datetime.datetime.strptime(p_user["create_time"].value,
                                                     "%Y%m%dT%H:%M:%S")
                self._create_time.setText(created.strftime("%d.%m.%Y %H:%M"))
            # Speicherverbrauch
            self._storage_usage.setText(UserListModel. \
                                        formatMemory(p_user["used_memory"]))
            # Anzahl der Dateien
            self._objects.setText(str(p_user["files"]))
            # Besitzerrollen
            if p_user["access_rights"]["owner"][0]:
                text = ""
                # text = Liste aller eingenommenen Besitzerrollen
                for i in range(len(p_user["access_rights"]["owner"][0])):
                    text += (p_user["access_rights"]["owner"][0][i] + "\n")
                self._role_owner_as_owner.setText(text)
            else:
                self._role_owner_as_owner.setText("None")
            # Benutzerrechte als Besitzer
            if p_user["access_rights"]["owner"][1]:
                text = ""
                # text = Liste aller Benutzerrechte als Besitzer
                for i in range(len(p_user["access_rights"]["owner"][1])):
                    if p_user["access_rights"]["owner"][1][i] == "change_pwd":
                        text += (self._rights_describtion["change_pwd"] + "\n")
                    if p_user["access_rights"]["owner"][1][i] == "contact":
                        text += (self._rights_describtion["contact"] + "\n")
                    if p_user["access_rights"]["owner"][1][i] == "edit_prefs":
                        text += (self._rights_describtion["edit_prefs"] + "\n")
                    if p_user["access_rights"]["owner"][1][i] == "editdetails":
                        text += (self._rights_describtion["editdetails"] + "\n")
                    if p_user["access_rights"]["owner"][1][i] == "get":
                        text += (self._rights_describtion["get"] + "\n")
                    if p_user["access_rights"]["owner"][1][i] == "history":
                        text += (self._rights_describtion["history"] + "\n")
                    if p_user["access_rights"]["owner"][1][i] == "info":
                        text += (self._rights_describtion["info"] + "\n")
                    if p_user["access_rights"]["owner"][1][i] == "mail_to":
                        text += (self._rights_describtion["mail_to"] + "\n")
                    if p_user["access_rights"]["owner"][1][i] == "get_vcard":
                        text += (self._rights_describtion["get_vcard"] + "\n")
                self._actions_as_owner.setText(text)
            else:
                self._actions_as_owner.setText("None")
            # Managerrollen
            if p_user["access_rights"]["manager"][0]:
                text = ""
                # text = Liste aller eingenommenen Managerrollen
                for i in range(len(p_user["access_rights"]["manager"][0])):
                    text += (p_user["access_rights"]["manager"][0][i] + "\n")
                self._role_owner_as_manager.setText(text)
            else:
                self._role_owner_as_manager.setText("None")
            # Benutzerrechte als Manager
            if p_user["access_rights"]["manager"][1]:
                text = ""
                # text = Liste aller Benutzerrechte als Manager
                for i in range(len(p_user["access_rights"]["manager"][1])):
                    if p_user["access_rights"]["manager"][1][i] == "change_pwd":
                        text += (self._rights_describtion["change_pwd"] + "\n")
                    if p_user["access_rights"]["manager"][1][i] == "contact":
                        text += (self._rights_describtion["contact"] + "\n")
                    if p_user["access_rights"]["manager"][1][i] == "edit_prefs":
                        text += (self._rights_describtion["edit_prefs"] + "\n")
                    if p_user["access_rights"]["manager"][1][i] == "editdetails":
                        text += (self._rights_describtion["editdetails"] + "\n")
                    if p_user["access_rights"]["manager"][1][i] == "get":
                        text += (self._rights_describtion["get"] + "\n")
                    if p_user["access_rights"]["manager"][1][i] == "history":
                        text += (self._rights_describtion["history"] + "\n")
                    if p_user["access_rights"]["manager"][1][i] == "info":
                        text += (self._rights_describtion["info"] + "\n")
                    if p_user["access_rights"]["manager"][1][i] == "mail_to":
                        text += (self._rights_describtion["mail_to"] + "\n")
                    if p_user["access_rights"]["manager"][1][i] == "get_vcard":
                        text += (self._rights_describtion["get_vcard"] + "\n")
                self._actions_as_manager.setText(text)
            else:
                self._actions_as_manager.setText("None")
            # Andere Rollen
            if p_user["access_rights"]["other"][0]:
                text = ""
                # text = Liste aller eingenommenen anderen Rollen
                for i in range(len(p_user["access_rights"]["other"][0])):
                    text += (p_user["access_rights"]["other"][0][i] + "\n")
                self._role_owner_as_other.setText(text)
            else:
                self._role_owner_as_other.setText("None")
            # Benutzerrechte für andere
            if p_user["access_rights"]["other"][1]:
                text = ""
                # text = Liste aller Benutzerrechte für andere
                for i in range(len(p_user["access_rights"]["other"][1])):
                    if p_user["access_rights"]["other"][1][i] == "change_pwd":
                        text += (self._rights_describtion["change_pwd"] + "\n")
                    if p_user["access_rights"]["other"][1][i] == "contact":
                        text += (self._rights_describtion["contact"] + "\n")
                    if p_user["access_rights"]["other"][1][i] == "edit_prefs":
                        text += (self._rights_describtion["edit_prefs"] + "\n")
                    if p_user["access_rights"]["other"][1][i] == "editdetails":
                        text += (self._rights_describtion["editdetails"] + "\n")
                    if p_user["access_rights"]["other"][1][i] == "get":
                        text += (self._rights_describtion["get"] + "\n")
                    if p_user["access_rights"]["other"][1][i] == "history":
                        text += (self._rights_describtion["history"] + "\n")
                    if p_user["access_rights"]["other"][1][i] == "info":
                        text += (self._rights_describtion["info"] + "\n")
                    if p_user["access_rights"]["other"][1][i] == "mail_to":
                        text += (self._rights_describtion["mail_to"] + "\n")
                    if p_user["access_rights"]["other"][1][i] == "get_vcard":
                        text += (self._rights_describtion["get_vcard"] + "\n")
                self._actions_as_other.setText(text)
            else:
                self._actions_as_other.setText("None")

            ## Daten des Persönliches-Tab
            # Private TelefonNr.
            self._private_tel.setText(p_user["phone_home"])
            # Mobile TelefonNr.
            self._mobile_tel.setText(p_user["phone_mobile"])
            # TelefonNr. des Büros
            self._office_tel.setText(p_user["phone_office"])
            # FaxNr.
            self._fax.setText(p_user["fax"])
            # Sprache
            self._language.setText(p_user["language"])
            # Organisation
            self._organisation.setText(p_user["organization"])
            # Private Homepage
            self._private_url.setText(p_user["url_home"])
            # Firmen-Webpage
            self._office_url.setText(p_user["url"])
            # Private Anschrift
            self._address.setText(p_user["address"])
            # Instant Massanger
            if p_user["messaging_services"]:
                text = ""
                # text = Liste aller Instant Massanger
                for i in range(len(p_user["messaging_services"])):
                    text += (p_user["messaging_services"].keys()[i] + " : " + \
                             p_user["messaging_services"].values()[i] + "\n")
                self._instant_messenger.setText(text)
            else:
                self._instant_messenger.setText("")
            # Weitere Informationen
            self._more_info.setText(p_user["additional_info"])

            try:
                # Versuche das Foto zu laden
                self._lbl_pic.setPixmap(QtGui.QPixmap(p_user["local_photo"]))
            except:
                # Wenn kein Bild vorhanden, leere das Bildlabel
                self._lbl_pic.clear()
