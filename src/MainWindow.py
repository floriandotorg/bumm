# -*- coding: utf-8 -*-

## @package MainWindow
# @brief Implementation der MainWindow Klasse
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
import interface
#from interface.BscwInterface import BscwInterface
from test import BscwInterface
from UserList import UserList
from UserDetails import UserDetails
from LoginDialog import LoginDialog

## Diese Klasse stellt das Hauptfenster der Anwendung da und managed alle
# Funktionen des Programms.
class MainWindow(QtGui.QMainWindow):
    
    ## Konstruktor
    # @param p_parent Übergeordnetes QObject. 
    def __init__(self, p_parent = None):
        QtGui.QMainWindow.__init__(self, p_parent)
        self._login()
    
    ## Zeigt den LoginDialog an und versucht sich per BscwInterface am
    #  BSCW-Server anzumelden. 
    def _login(self):
        self._bscw_interface = BscwInterface()
        
        login_dialog = LoginDialog(self)
        if not login_dialog.exec_() == QtGui.QDialog.Accepted:
            QtGui.QApplication.quit()
            return
        
        try:
            self._bscw_interface.login(login_dialog.username,
                                        login_dialog.passwd)
        except interface.Exceptions.AuthorizationFailed:
            QtGui.QMessageBox.critical(self, self.trUtf8(
                                            "Anmeldung fehlgeschlagen"), 
                            self.trUtf8("""Die Anmeldung ist fehlgeschlagen!
Möglicherweise wurde ein falsches Passwort oder ein falscher Benutzername
verwendet oder sie verfügen nicht über die nötigen Rechte."""))
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        