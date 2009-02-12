# -*- coding: utf-8 -*-

## @package _ProxiedTransport
# @brief erweitert xmlrpclib um die Möglichkeit einer Proxy-Authorization
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
import urllib
from urllib import unquote, splittype, splithost

## ProxiedTransport
#
# Diese Klasse erweitert die XML-RPC-Implementation von Python um die
# Möglichkeit einer Proxy-Authorization (Benutzername und Passwort)
#
# Bemerkung: überlädt xmlrpclib.Transport

class ProxiedTransport(xmlrpclib.Transport):

    ## initialisiert die AuthorizedTransport-Klasse
    # @param p_passwd Passwort für die Anmeldung am BSCW-Server
    def __init__(self, p_username = None, p_passwd = None):

        # Initialisierung, wird später durch XML-RPC geprüft
        self._use_datetime = False

        # User + Passwort verschlüsseln und festlegen
        #self.user_passwd = p_username + ':' + p_passwd
        #self.auth = string.strip(base64.encodestring(self.user_passwd))

        self.proxyurl = 'http://141.200.122.34:8080'

    def request(self, host, handler, request_body, verbose=0):

        urlopener = urllib.FancyURLopener({'http' : 'http://141.200.122.34'})

        urlopener.addheaders = [('User-agent', self.user_agent)]

        host = unquote(host)

        f = urlopener.open("http://%s%s"%(host,handler), request_body)

        self.verbose = verbose

        return self.parse_response(f)