# -*- coding: utf-8 -*-

## @package BscwInterface 
# @brief Implementation der BscwInterface Klasse
# @version 0.1
# @author Florian Kaiser
# @date 05.02.09
#
# <Beschreibung>

#################################################################################
# Copyright (C) 2009 Benjamin Flader, Bejamin Leipold, Andé Naumann,            #
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
# auszulesen. Dabei teilet sich das Auslesen der Attribute in zwei Phasen:
#
# -# Allgemeine Attribute werden bereits mit getAllUsers() zurückgegeben
# -# Weitere Attribute können mit getAdditionalUserInfo() gelesen werden
#
# Diese Trennung ist nötig, da das Sammeln der "Additional Information"
# im Vergleich zu den "einfachen" Attributen relativ lange dauert und deshalb 
# erst bei Bedarf nachgeladen werden sollte.
class BscwInterface(object):
    
    ## Gibt eine Liste aller am BSCW-Server angemeldeten User inkl.
    # verschiedener Attribute zurück. 
    # @return Liste von Dictionaries mit folgendem Aufbau
    # - id : Benutzer-ID
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
    # - additional_info : Weitere Informationen
    def getAllUsers(self):
        pass

    ## Gibt zusätzlich Informationen zu einem User zurück, deren Sammlung
    # aufwendiger ist und deshalb aus Performance-Gründen nicht mit in 
    # getAllUsers() aufgenommen wurde.
    # @param p_user Ein Dictonary mit mindestens einem Element names "id" 
    # indem sich die ID des Users befindet 
    # @return Ein Dictonary mit folgendem Aufbau
    # - last_login : Letzte Anmeldung als datetime.date
    # - used_memory : Speicherverbrauch in Byte
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
    # @param p_user Ein Dictonary mit mindestens einem Element names "id"
    # indem sich die ID des Users befindet.
    def deleteUser(self, p_user):
        pass
    
    ## Sperrt einen User, sodass er sich nicht mehr anmelden kann.
    # @param p_user Ein Dictonary mit mindestens einem Element names "id"
    # indem sich die ID des Users befindet.
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
    
    ## Löscht alle Objekte im Mülleimer eins oder aller User.
    # @param p_user Ein Dictonary mit mindestens einem Element names "id"
    # indem sich die ID des Users befindet. Oder None wenn alle Mülleinmer
    # geleert werden sollen.
    def destroyTrash(self, p_user = None):
        pass
    
    ## Löscht alle Objekte in der Ablage eins oder aller User.
    # @param p_user Ein Dictonary mit mindestens einem Element names "id"
    # indem sich die ID des Users befindet. Oder None wenn alle Mülleinmer
    # geleert werden sollen.
    def destroyClipboard(self, p_user = None):
        pass