# -*- coding: utf-8 -*-

## @package ActionThread
# @brief Implementation der ActionThread-Klasse
# @version 0.1
# @author Florian Kaiser
# @date 21.02.09

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

## Thread für Aufgaben, die eine lange Laufzeit haben und die Anwendung blockieren
# könnten
class ActionThread(QtCore.QThread):
    
    ## Konstruktor
    # @param p_parent Übergeordnetes QObject
    # @param p_func Zeiger auf eine Funktion mit langer Laufzeit
    # @param p_params Parameter, die beim Aufruf übergeben werden
    def __init__(self, p_parent, p_func, *p_params):
        QtCore.QThread.__init__(self, p_parent)
        ## Zeiger auf eine Funktion mit langer Laufzeit
        self._func = p_func
        ## Parameter, die beim Aufruf übergeben werden
        self._params = p_params
        ## Rückgabewert der Funktion
        self._result = None
    
    ## Gibt den Rückgabewert der ausgeführten Funktion zurück    
    def getResult(self):
        return self._result
    
    ## Startet die Funktion und speichert das Ergebnis in self._result
    def run(self):
        self._result = self._func(*self._params)