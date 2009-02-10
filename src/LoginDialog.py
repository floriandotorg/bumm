# -*- coding: utf-8 -*-

## @package LoginDialog
# @brief Implementation der LoginDialog Klasse
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

from PyQt4 import QtGui, QtCore
from ui_LoginDialog import Ui_LoginDialog

## Stellt ein Dialog da, indem Benutzername und Passwort eingegeben werden
# müssen.
class LoginDialog(QtGui.QDialog, Ui_LoginDialog):
    
    ## Konstruktor
    # @param p_parent Übergeordnetes QObject
    def __init__(self, p_parent = None):
         QtGui.QDialog.__init__(self, p_parent)
         self.setupUi(self)
    
    ## Getter für den Benutzernamen     
    def getUsername(self):
        return self._username.text()
    username = property(getUsername)
    
    ## Getter für das Passwort
    def getPasswd(self):
        return self._passwd.text()
    passwd = property(getPasswd)