# -*- coding: utf-8 -*-

## @package BscwInterface
# @brief Implementation der BscwInterface Klasse
# @version 0.1
# @author Florian Kaiser
# @date 06.02.09

#################################################################################
# Copyright (C) 2009 Benjamin Flader, Bejamin Leipold, André Naumann,            #
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

## Interface zur BSCW-Server
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

    ## Kein Proxy
    NoProxy = 2
    ## Standard Proxy des Betriebsystems
    DefaultProxy = 0
    ## Socks5 Proxy
    Socks5Proxy =  1
    ## Transparenter HTTP-Proxy
    HttpProxy = 3
    ## HTTP-Proxy für rein HTTP-Anfragen
    HttpCachingProxy = 4

    ## Baut eine Verbindung zum BSCW Server auf und versucht sich anzumelden.
    # Sollte der Versuch scheitern wird eine Exception geworfen.
    # @param p_username Benutzername für die Anmeldung am BSCW-Server
    # @param p_passwd Passwort für die Anmeldung am BSCW-Server
    def login(self, p_username, p_passwd):
        pass

    ## Logged den User aus und bricht die Verbindung zum BSCW-Server ab
    def logout(self):
        pass

    ## Definiert ein Netzwerk-Proxy für die Verbindung zum BSCW Server.
    # Sollte bereits eine Verbindung bestehen, wird diese getrennt.
    # @param p_hostname DNS-Name oder IP-Adresse des Proxys (None = kein Proxy
    # benötigt)
    # @param p_port Port des Proxys
    # @param p_type Proxy-Typ (Siehe Proxy-Klassenattribute)
    # @param p_exceptions Liste von Domänen, für die der Proxy
    # nicht verwendet werden soll
    # @param p_username Benutzername für die Anmeldung am Proxy (None = keine 
    # Anmeldung erforderlich)
    # @param p_passwd Passwort für die Anmeldung am Proxy
    def setProxy(self, p_type, p_hostname = None, p_port = None, p_username = None, p_exceptions = None, p_passwd = None):
        pass

    ## Gibt eine Liste aller am BSCW-Server angemeldeten User inkl.
    # verschiedener Attribute zurück.
    # @return Liste von Dictionaries mit folgendem Aufbau
    # - _user_id : Benutzer-ID
    # - _home_id : ID vom Arbeitsbereich des Benutzers
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
    # - homepage : Webseite
    # - messaging_services : Messaging Services, Dictronary mit
    # dem Name des Service als Schlüssel und der ID (z.B ICQ-Nummer)
    # als Wert
    # - additional_info : Weitere Informationen
    # - photo : Link zum Benutzerbild oder None wenn keins existiert
    # - locked : User geserrt ja/nein (Boolean)
    # - used_memory : Speicherverbrauch in Byte
    # - last_login : Letzte Anmeldung als datetime.datetime
    def getAllUsers(self):
        pass

    ## Gibt zusätzlich Informationen zu einem User zurück, deren Sammlung
    # aufwendiger ist und deshalb aus Performance-Gründen nicht mit in
    # getAllUsers() aufgenommen wurde.
    # @param p_user Ein Dictonary mit einem Element "id" indem sich
    # die ID des Users befindet.
    # @return Ein Dictonary mit folgendem Aufbau
    # - objects : Objekte (Anzahl)
    # - access_rights : Zugriffsrechte, Dictornary mit folgendem Aufbau:
    #  - creator : Liste mit Zugriffsrechten für Erzeuger
    #  - user : Liste mit Zugriffsrechten für registriete Benutzer
    #  - owner : Liste mit Zugriffsrechten für Eigentümer
    #  - manager : Liste mit Zugriffsrechten für Manager
    # - memberships : Mitgliedschaften, Dictonary mit zwei Elementen:
    #  - workspaces : Liste der Namen der Arbeitsbereiche
    #  - communities : Liste der Namen der Gemeinschaften
    def getAdditionalUserInfo(self, p_user):
        pass

    ## Löscht einen Benuzter endgültig und irreversibel vom BSCW-Server.
    # @param p_user Ein Dictonary mit einem Element "id" indem sich
    # die ID des Users befindet.
    def deleteUser(self, p_user):
        pass

    ## Sperrt einen User, sodass er sich nicht mehr anmelden kann.
    # @param p_user Ein Dictonary mit einem Element "id" indem sich
    # die ID des Users befindet.
    # @see unlockUser()
    def lockUser(self, p_user):
        pass

    ## Entsperrt einen User, damit er sich wieder am BSCW-Server anmelden
    # kann.
    # @param p_user Ein Dictonary mit mindestens einem Element names "id"
    # indem sich die ID des Users befindet.
    # @see lockUser()
    def unlockUser(self, p_user):
        pass

    ## Löscht alle Objekte im Mülleimer eines oder aller User.
    # @param p_user Ein Dictonary mit einem Element "id" indem sich
    # die ID des Users befindet. Oder None wenn alle Mülleinmer
    # geleert werden sollen.
    def destroyTrash(self, p_user = None):
        pass

    ## Löscht alle Objekte in der Ablage eines oder aller User.
    # @param p_user Ein Dictonary mit einem Element "id" indem sich
    # die ID des Users befindet. Oder None wenn alle Ablagen
    # geleert werden sollen.
    def destroyClipboard(self, p_user = None):
        pass