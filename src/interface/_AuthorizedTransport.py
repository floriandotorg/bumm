# -*- coding: utf-8 -*-

## @package AuthorizedTransport
# @brief erweitert xmlrpclib um die Möglichkeit einer HTTP-Authorization
# @version 0.1
# @author Benjamin Flader
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

import xmlrpclib # Bibliothek zum ferngesteuerten Aufruf von Methoden
import base64, string

## AuthorizedTransport
#
# Diese Klasse erweitert die XML-RPC-Implementation von Python um die
# Möglichkeit einer HTTP-Authorization (Benutzername und Passwort)
# Bemerkung: überlädt xmlrpclib.Transport

class AuthorizedTransport(xmlrpclib.Transport):

    ## initialisiert die AuthorizedTransport-Klasse
    # @param p_passwd Passwort für die Anmeldung am BSCW-Server
    def __init__(self, p_username = None, p_passwd = None):

        # Initialisierung, wird später durch XML-RPC geprüft
        self._use_datetime = False

        # User + Passwort verschlüsseln und festlegen
        self.user_passwd = p_username + ':' + p_passwd
        self.auth = string.strip(base64.encodestring(self.user_passwd))

    ## sendet den Host-Namen
    # @param connection Verbindungs-Alias
    # @param host Hostname
    def send_host(self, connection, host):
        connection.putheader("Host", host)
        if self.auth:
            connection.putheader('Authorization', 'Basic %s' % self.auth)