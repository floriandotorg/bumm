# -*- coding: utf-8 -*-

## @package interface.BscwInterface
# @brief Implementation der BscwInterface Klasse
# @version 0.1
# @author Florian Kaiser
# @date 10.02.09

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

import xmlrpclib                                         # XML-RPC
import Exceptions                                        # Ausnahmen
import socket                                            # Socket
import string
## Interface zum BSCW-Server
#
# Diese Klasse stellt Methoden zum Auslesen aller User inkl. aller Attribute
# bereit. Zusätzlich können Benutzer gelöscht, gesperrt und entsperrt werden
# Außerdem ist es möglich die Zwischenablage einiger oder alle User aufzuräumen
# oder die Mülleimer zu leeren.
class BscwInterface(object):

    ## Initialisiert die BscwInterface-Klasse
    def __init__(self):
        pass

    ## Baut eine Verbindung zum BSCW Server auf und versucht sich anzumelden.
    # Sollte der Versuch scheitern wird eine Exception geworfen.
    # @param p_hostname DNS-Name oder IP-Adresse des BSCW-Servers
    # @param p_username Benutzername für die Anmeldung am BSCW-Server
    # @param p_passwd Passwort für die Anmeldung am BSCW-Server
    def login(self, p_hostname, p_username, p_passwd):
        # Verbindung herstellen
        self._connect(p_hostname, p_username, p_passwd)
        try:
            # Authorisierung überprüfen (User? Admin?)
            if self._server.mist(p_username):#is_admin(p_username) == False:
                # Benutzer hat keine Administratorenrechte
                raise Exceptions.NoAdminRights
            if self._server.is_admin(p_username) == None:
                # Benutzer ist nicht vorhanden
                raise Exceptions.LoginIncorrect
        except(socket.error):
            # Server nicht erreichbar
            raise Exceptions.HostUnreachable
        except(xmlrpclib.ProtocolError):
            # Login-Daten nicht korrekt
            raise Exceptions.LoginIncorrect
        except(xmlrpclib.Fault) as err:
            if string.find(str(err),"Fault 10010") != -1:
                print "blubb"
                raise err
            raise Exceptions.ServerExtensionNotInstalled



    ## Loggt den User aus und bricht die Verbindung zum BSCW-Server ab
    def logout(self):

        # Server-Objekt löschen
        del self._server

    ## Gibt eine Liste aller am BSCW-Server angemeldeten User inklusive
    # verschiedener Attribute zurück.
    # @return Liste von Dictionaries mit folgendem Aufbau
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
    def getAllUser(self):
        try:
            # Rückgabe aller Benutzer
            return self._server.get_all_user()
        except(socket.error):
            # Verbindung abgebrochen
            raise Exceptions.ConnectionError

    ## Löscht ein oder mehrere Benuzter endgültig und irreversibel vom
    # BSCW-Server.
    # @param p_user Eine Liste mit den Namen der zu löschenden Benutzer
    def deleteUser(self, p_user):
        try:
            # Löschen des Benutzer
            self._server.delete_user(p_user)
        except(socket.error):
            # Verbindung abgebrochen
            raise Exceptions.ConnectionError

    ## Sperrt ein oder mehrere User für die Anmeldung am BSCW-Server.
    # @param p_user Eine Liste mit den Namen der zu sperrenden Benutzer
    # @see unlockUser()
    def lockUser(self, p_user):
        try:
            # Sperren eines Benutzers
            self._server.lock_user(p_user)
        except(socket.error):
            # Verbindung abgebrochen
            raise Exceptions.ConnectionError

    ## Hebt die Anmeldesperre eines oder mehrerer Benutzer auf
    # @param p_user Eine Liste mit den Namen der zu entsprrenden Benutzer
    def unlockUser(self, p_user):
        try:
            # Entsperren eines Benutzers
            self._server.unlock_user(p_user)
        except(socket.error):
            # Verbindung abgebrochen
            raise Exceptions.ConnectionError

    ## Löscht alle Objekte im Mülleimer einiger oder aller User.
    # @param p_outdated Mindestalter der zu löschenden Dateien in Tagen
    # @param p_user Eine Liste mit den Namen der zu löschenden Benutzer oder
    # eine leere Liste für alle Benutzer
    def destroyTrash(self, p_outdated, p_user = []):
        try:
            # Löschen des Mülleimers für eine Liste von Benutzern
            self._server.destroy_trash(p_outdated, p_user)
        except(socket.error):
            # Verbindung abgebrochen
            raise Exceptions.ConnectionError

    ## Löscht alle Objekte in der Ablage einiger oder aller User.
    # @param p_outdated Mindestalter der zu löschenden Dateien in Tagen
    # @param p_user Eine Liste mit den Namen der zu löschenden Benutzer oder
    # eine leere Liste für alle Benutzer
    def destroyClipboard(self, p_outdated, p_user = []):
        try:
            # Löschen der Ablage für eine Liste von Benutzern
            self._server.destroy_clipboard(p_outdated, p_user)
        except(socket.error):
            # Verbindung abgebrochen
            raise Exceptions.ConnectionError

    ## Stellt eine Verbindung zum BSCW-Server her
    # @param p_hostname DNS-Name oder IP-Adresse des BSCW-Servers
    # @param p_username Benutzername für die Anmeldung am BSCW-Server
    # @param p_passwd Passwort für die Anmeldung am BSCW-Server
    def _connect(self, p_hostname, p_username, p_passwd):
        # flexible Anpassung des Hostnames
        p_hostname = string.replace(p_hostname,"http://","")
        p_hostname = string.split(p_hostname,"/")[0]


        # Verbindung mit dem Server herstellen
        self.hostname = 'http://' + p_username + ':' + p_passwd \
        + '@' + p_hostname + '/bscw/bscw.cgi/?op=xmlrpc'

        ## XMLRPC-Verbindung zum BSCW Server
        self._server = xmlrpclib.ServerProxy(self.hostname)

