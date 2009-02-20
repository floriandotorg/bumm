# -*- coding: utf-8 -*-

## @package Settings
# @brief Implementation der Settings Klasse
# @version 0.1
# @author Florian Kaiser
# @date 12.02.09

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

from PyQt4 import QtCore

## Verwaltet Programmeinstellungen und speichert diese in einer .ini Datei.
# Diese Datei hat immer den Namen "config.ini" und liegt Verzeichnis für 
# Einstellugnen des Betriebsystems (z.B. Dokumente und Einstellungen)
# Bei der Datei handelt sich um ein Standard-Windows-Konfigurationsfile.
# Sollte sich diese Datei am angegebenen Ort befinden, wird sie gelesen,
# anderenfalls wird eine neue Datei mit Standardwerten gefüllt.
class Settings(QtCore.QObject):
    
    ## Konstruktor
    # @param p_parent Übergeordnetes QObject
    def __init__(self, p_parent = None):
        QtCore.QObject.__init__(self, p_parent)
        self.server_address = "http://172.16.124.101/bscw/bscw.cgi/?op=xmlrpc"
        #self.server_address = "http://localhost:8080/bscw/bscw.cgi/?op=xmlrpc"
        self.username = "ChuckNoris"
        self.proxy = ""
        self.columns = ["user_id", "name", "longname"]
    