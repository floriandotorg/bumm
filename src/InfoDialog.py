# -*- coding: utf-8 -*-

## @package InfoDialog
# @brief Implementation der InfoDialog Klasse
# @version 0.1
# @author Florian Kaiser
# @date 13.02.09

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
from ui_InfoDialog import Ui_InfoDialog

## Stellt ein Dialog da, indem Informationen zum Programm angezeigt werden.
class InfoDialog(QtGui.QDialog, Ui_InfoDialog):
    
    ## Konstruktor 
    # @param p_parent übergeordnetes QObject.
    def __init__(self, p_parent = None):
        QtGui.QDialog.__init__(self, p_parent)
        self.setupUi(self)
        self.connect(self._button_qt_info, QtCore.SIGNAL("clicked()"), QtGui.qApp.aboutQt)