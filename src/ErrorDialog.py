# -*- coding: utf-8 -*-

## @package ErrorDialog
# @brief Implementation der ErrorDialog Klasse
# @version 1
# @author Florian Kaiser
# @date 24.02.09

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
from ui_ErrorDialog import Ui_ErrorDialog
import sys
import traceback

## Stellt ein Dialog da, indem der Benutzer über ein Programmfehler informiert
# wird
class ErrorDialog(QtGui.QDialog, Ui_ErrorDialog):
    
    ## Konstruktor 
    # @param p_parent übergeordnetes QObject.
    def __init__(self, exception, p_parent = None):
        QtGui.QDialog.__init__(self, p_parent)
        self.setupUi(self)
        
        # Text der Exception und den Traceback darstellen
        self._lbl_err.setText(type(exception).__name__ + ": " + str(exception))
        self._text_traceback.setPlainText(traceback.format_exc())
        
        # Standard Icon-Größe ermitteln
        ico_size = QtGui.qApp.style() \
                            .pixelMetric(QtGui.QStyle.PM_MessageBoxIconSize)
        # Standard-Icon für Fehler laden
        self._lbl_img.setPixmap(QtGui.qApp.style() \
                            .standardIcon(QtGui.QStyle.SP_MessageBoxCritical) \
                            .pixmap(ico_size))
        # Größe des Icon-Labels anpassen
        self._lbl_img.setMaximumWidth(ico_size + 5)
        
        ## Größe des Fensters, wenn der Traceback angzeigt wird
        self._expand_hight = self.height()
        # Den Traceback verstecken
        self._text_traceback.hide()
        # Und die Fensterhöhe anpassen
        self.setMaximumHeight(119)
        
        self.connect(self._button_details, QtCore.SIGNAL("clicked()"), 
                     self._changeDetailsVisibilitySlot)
        self.connect(self._button_quit, QtCore.SIGNAL("clicked()"), 
                     self._quitAppSlot)
    
    ## Zeigt/Versteckt den Traceback
    def _changeDetailsVisibilitySlot(self):
        if self._text_traceback.isVisible():
            # Die Höhe des Fensters speichern
            self._expand_hight = self.height()
            # Den Traceback verstecken
            self._text_traceback.hide()
            # Die Größe des Fensters anpassen
            self.setFixedHeight(123)
            # Die Buttonbeschreibung ändern
            self._button_details.setText("Details >>")
        else:
            # Den Traceback anzeigen
            self._text_traceback.show()
            # Das Fenster wieder auf Ursprungsbgröße bringen
            self.setFixedHeight(self._expand_hight)
            # Die Fenstergröße auf unendlich stellen
            self.setMaximumHeight(16777215)
            # Die Buttonbeschreibung ändern
            self._button_details.setText("Details <<")
    
    ## Beendet die Anwendung        
    def _quitAppSlot(self):
        QtGui.qApp.quit()
        exit()