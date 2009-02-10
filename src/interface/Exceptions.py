# -*- coding: utf-8 -*-

## @package Exceptions
# @brief Deklaration mehrerer Exceptions für das BscwInterface
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

## Benutzername oder Passwort sind inkorrekt oder Benutzer ist kein Admin.
class AuthorizationFailed(Exception):
    pass

## Der BSCW-Server ist nicht erreichbar.
class HostUnreachable(Exception):
    pass

## Der angegebene Proxy ist nicht verfügbar
class ProxyUnreachable(Exception):
    pass

## Die bereits bestehende Verbindung wurde unterbrochen. Ein erneuter Login-
# Vorgang ist erforderlich
class ConnectionError(Exception):
    pass