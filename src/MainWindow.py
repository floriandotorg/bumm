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
from ui_MainWindow import Ui_MainWindow
import interface
#from interface.BscwInterface import BscwInterface
from test import BscwInterface
from UserList import UserList
from UserDetails import UserDetails
from LoginDialog import LoginDialog
from Settings import Settings
import time

class LoadingDialog(QtGui.QDialog):
    
    def __init__(self, p_parent = None):
        QtGui.QDialog.__init__(self, p_parent)
        self._label = QtGui.QLabel(self)
        self._label.setText("Bitte Warten ...")
        self.setGeometry(self.x(), self.y(), 100, 200)
        #self.setWindowFlags(QtCore.WindowFlags.)

## Diese Klasse stellt das Hauptfenster der Anwendung da und managed alle
# Funktionen des Programms.
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    
    ## Konstruktor
    # @param p_parent Übergeordnetes QObject. 
    def __init__(self, p_parent = None):
        QtGui.QMainWindow.__init__(self, p_parent)
        self.setupUi(self)
        self._settings = Settings()
        self._centralwidget = UserList([], self)
        self.setCentralWidget(self._centralwidget)
        self._dockwidget = UserDetails(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self._dockwidget)
        self._loading_dialog = LoadingDialog(self)
        self._loading_dialog.show()
        #self._login()
        #self._user_list = self._bscw_interface.getAllUsers()
        #print self._user_list
        
    
    ## Zeigt den LoginDialog an und versucht sich per BscwInterface am
    #  BSCW-Server anzumelden. 
    def _login(self):
        login_dialog = LoginDialog(self._settings, self)
        
        if login_dialog.exec_() != QtGui.QDialog.Accepted:
            QtGui.qApp.quit()
            exit()
                   
        self._bscw_interface = login_dialog.getInterface()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        