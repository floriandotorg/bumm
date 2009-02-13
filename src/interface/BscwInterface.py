# -*- coding: utf-8 -*-

## @package BscwInterface
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
from _ProxiedTransport import ProxiedTransport           # Authorized-Transport

## Interface zum BSCW-Server
#
# Diese Klasse stellt Methoden bereit alle User inkl. aller Attribute
# auszulesen. Dabei teilt sich das Auslesen der Attribute in zwei Phasen:
#
# -# Allgemeine Attribute werden bereits mit getAllUsers() zurückgegeben
# -# Weitere Attribute können mit getAdditionalUserInfo() gelesen werden
#
# Diese Trennung ist nötig, da das Sammeln der "Additional Information"
# im Vergleich zu den "einfachen" Attributen relativ lange dauert und deshalb
# erst bei Bedarf nachgeladen werden sollte.
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

        try:
            # Verbindung herstellen
            self._connect(p_hostname, p_username, p_passwd)

            # Authorisierung überprüfen (User? Admin?)
            if not self._server.is_admin(p_username):
                raise Exceptions.AuthorizationFailed

        except (xmlrpclib.Fault, socket.error):
            # Verbindung überprüfen
            raise Exceptions.HostUnreachable

    ## Loggt den User aus und bricht die Verbindung zum BSCW-Server ab
    def logout(self):

        # Server-Objekt löschen
        del _server

    ## Definiert ein Netzwerk-Proxy für die Verbindung zum BSCW Server.
    # Sollte bereits eine Verbindung bestehen, wird diese getrennt.
    # @param p_hostname DNS-Name oder IP-Adresse des Proxys (None = kein Proxy
    # benötigt)
    # @param p_port Port des Proxys
    # @param p_username Benutzername für die Anmeldung am Proxy (None = keine
    # Anmeldung erforderlich)
    # @param p_passwd Passwort für die Anmeldung am Proxy
    def setProxy(self, p_hostname = "", p_port = "", p_username = "",
                 p_passwd = ""):
        pass

    ## Gibt eine Liste aller am BSCW-Server angemeldeten User inkl.
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
    def getAllUsers(self):
        return self._server.get_all_users()

    ## Löscht ein oder mehrere Benuzter endgültig und irreversibel vom
    # BSCW-Server.
    # @param p_user Eine Liste mit den Namen der zu löschenden Benutzer
    def deleteUsers(self, p_users):
        self._server.delete_users(p_users)

    ## Sperrt einen User, sodass er sich nicht mehr anmelden kann.
    # @param p_user Eine Liste mit den Namen der zu sperrenden Benutzer
    # @see unlockUser()
    def lockUsers(self, p_users):
        self._server.lock_users(p_users)

    ## Entsperrt einen User, damit er sich wieder am BSCW-Server anmelden
    # kann.
    # @param p_user Eine Liste mit den Namen der zu entsprrenden Benutzer
    def unlockUsers(self, p_users):
        self._server.unlock_users(p_users)

    ## Löscht alle Objekte im Mülleimer eines oder aller User.
    # @param p_outdated Mindestalter der zu löschenden Dateien
    # @param p_users Eine Liste mit den Namen der zu löschenden Benutzer oder
    # eine leere Liste für alle Benutzer
    def destroyTrash(self, p_outdated, p_users = []):
        self._server.destroy_trash(p_outdated, p_users)

    ## Löscht alle Objekte in der Ablage eines oder aller User.
    # @param p_outdated Mindestalter der zu löschenden Dateien
    # @param p_users Eine Liste mit den Namen der zu löschenden Benutzer oder
    # eine leere Liste für alle Benutzer
    def destroyClipboard(self, p_outdated, p_users = []):
        self._server.destroy_clipboard(p_outdated, p_users)

    ## Stellt eine Verbindung zum BSCW-Server her
    # @param p_hostname DNS-Name oder IP-Adresse des BSCW-Servers
    # @param p_username Benutzername für die Anmeldung am BSCW-Server
    # @param p_passwd Passwort für die Anmeldung am BSCW-Server
    def _connect(self, p_hostname, p_username, p_passwd):

        # AuthorizedTransport (zum Patchen von XMLRPC, siehe
        # _AuthorizedTransport.py)
        proxied_transport = ProxiedTransport(p_username, p_passwd)

        # Verbindung mit dem Server herstellen
        self.hostname = 'http://' + p_username + ':' + p_passwd \
        + '@' + p_hostname + '/bscw/bscw.cgi/?op=xmlrpc'

        self._server = xmlrpclib.ServerProxy(self.hostname)
        #self._server = xmlrpclib.ServerProxy(self.hostname, proxied_transport)