# -*- coding: utf-8 -*-

## @package ImageLabel
# @brief Implementation der ImageLabel Klasse
# @version 1
# @author Florian Kaiser
# @date 24.04.09

#################################################################################
# Copyright (C) 2009 Benjamin Flader, Bejamin Leipold, André Naumann,           #
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

from PyQt4 import Qt, QtCore, QtGui

## Label zum Darstellen von Bildern, deren Größe automatisch angepasst wird
class ImageLabel(QtGui.QLabel):
    
    ## Konstruktor
    # @param p_parent Übergeordnetes QObject
    def __init__(self, p_parent = None):
        QtGui.QLabel.__init__(self, p_parent)
        
        ## Original des Bildes, das angezeigt werden soll
        self.pixmap = None
    
    ## Überladene Methode: Setzt das Bild, das dargestellt werden soll
    # @param p_pixmap Bild als QPixmap
    def setPixmap(self, p_pixmap):
        # Bild speichern
        self.pixmap = p_pixmap
        
        # Das Bild an die Größe des Fenstern anpassen und auf das Label
        # setzten
        QtGui.QLabel.setPixmap(self,
                               pixmap.scaled(min(self.width(),
                                                 p_pixmap.width()),
                                             min(self.height(),
                                                 p_pixmap.height()),
                                             Qt.Qt.IgnoreAspectRatio))
    
    ## Überladene Methode: Wird aufgerufen, wenn sich die Größe des Widgets 
    # ändert
    # @param p_event Größenänderung als QResizeEvent
    def resizeEvent(self, p_event):
        # Ist ein Bild gesetzt?
        if(self.pixmap):
            # Dann Bild an die neue Größe des Fensters anpassen
            QtGui.QLabel.setPixmap(self, 
                                   self.pixmap.scaled(min(p_event.size().width(),
                                                          self.pixmap.width()),
                                                    min(p_event.size().height(),
                                                        self.pixmap.height()),
                                                    Qt.Qt.KeepAspectRatio))
        # Ursprüngliche Methode aufrufen
        QtGui.QLabel.resizeEvent(self, p_event)
    
    ## Überladene Methode: Löscht das Bild und zeigt nichts an
    def clear(self):
        # Bild löschen
        self.pixmap = None
        # Ursprüngliche Methode aufrufen
        QtGui.QLabel.clear(self)
        