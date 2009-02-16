# -*- coding: utf-8 -*-

## @package SetColumnDialog
# @brief Implementation der SetColumnDialog Klasse
# @version 0.1
# @author Florian Kaiser
# @date 15.02.09

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

from PyQt4 import QtCore, QtGui, Qt
from ui_SetColumnDialog import Ui_SetColumnDialog

## Ein Dialog indem die angezeigten Spalten ausgewählt werden können.
class SetColumnDialog(QtGui.QDialog, Ui_SetColumnDialog):
    
    ## Liste von Tuples, in der die Spaltennamen und Überschriften gespeichert
    # werden.
    # Wird am Anfang auf None gesetzt, weil die Spaltenüberschriften erst 
    # übersetzt werden können, wenn bereits eine QApplication existiert.
    s_column_list = None
    
    ## Konstruktor
    # @param p_list Liste der bereits angewählten Spalten
    # @param p_parent Übergeordnetes QObject.
    def __init__(self, p_list, p_parent = None):
        QtGui.QDialog.__init__(self, p_parent)
        self.setupUi(self)
        
        # s_column_list noch nicht initialisiert?
        if not SetColumnDialog.s_column_list:
            self._initColumnList()
        
        # Liste der Items der Liste, wird später benötigt um die selektierten
        # Spalten zurück zu geben
        self._items = {}
        # Das ItemModel für die Liste
        self._model = QtGui.QStandardItemModel(self)
        
        # Diese Schleife geht alle Spalten durch und fügt sie din die Liste ein
        # sollte ein Eintrag ebenfalls in p_list existierten, wird die Checkbox
        # angewählt.
        for i in SetColumnDialog.s_column_list:
            # Neues Item erstellen
            item = QtGui.QStandardItem(QtCore.QString(i[1]))
            item.setCheckable(True)
            
            # Spalte angewählt?
            if i in p_list:
                item.setCheckState(QtCore.Qt.Checked)
                
            # Item in die Listen aufnehmen
            self._items[i[1]] = item
            self._model.appendRow(item)
        self._column_list.setModel(self._model)
        
    ## Gibt eine Liste der angewählten Spalten zurück
    # @return Liste von Tuples mit Spaltename und Überschrift
    def getHeaderData(self):
        result = []
        
        for i in SetColumnDialog.s_column_list:
            if self._items[i[1]].checkState() == QtCore.Qt.Checked:
                result.append(i)
                
        return result
    
    ## In den Einstellungen werden die angewählten Spalten nur als Spaltenamen
    # geseichert. Diese Methode wandelt die Liste in eine Liste aus Tuples um
    # damit zu arbeiten.
    # @param p_list Liste von Strings mit den Spaltennamen
    # @return Liste von Tuples mit Spaltename und Überschrift
    def tupleByKey(self, p_list):
        result = []
        
        for i in SetColumnDialog.s_column_list:
            if i[0] in p_list:
                result.append(i)
                
        return result
    
    ## Füllt s_column_list mit einer Liste aus Tuples, in der Spaltename und 
    # Überschrift steht.
    def _initColumnList(self):
        SetColumnDialog.s_column_list = \
                    [("user_id", QtGui.qApp.trUtf8(u"Benutzer-ID")),
                     ("name", QtGui.qApp.trUtf8(u"Benutzername")),
                     ("longname", QtGui.qApp.trUtf8(u"Vor- und Nachname")),
                     ("email", QtGui.qApp.trUtf8(u"E-Mail Adresse")),
                     ("language", QtGui.qApp.trUtf8(u"Sprache")),
                     ("organization", QtGui.qApp.trUtf8(u"Organisation")),
                     ("secondary_email", 
                                QtGui.qApp.trUtf8(u"Weitere E-Mail Adressen")),
                     ("phone_home", QtGui.qApp.trUtf8(u"Telefon Heim")),
                     ("phone_mobile", QtGui.qApp.trUtf8(u"Telefon Handy")),
                     ("phone_office", QtGui.qApp.trUtf8(u"Telefon Büro")),
                     ("fax", QtGui.qApp.trUtf8(u"Faxnummer")),
                     ("address", QtGui.qApp.trUtf8(u"Adresse")),
                     ("url_homepage", QtGui.qApp.trUtf8(u"Webseite privat")),
                     ("url", QtGui.qApp.trUtf8(u"Telefon Büro")),
                     ("messaging_services", 
                                QtGui.qApp.trUtf8(u"Messaging Services")),
                     ("additional_info", 
                                QtGui.qApp.trUtf8(u"Weitere Informationen")),
                     ("photo", QtGui.qApp.trUtf8(u"Benutzerbild (URL)")),
                     ("locked", QtGui.qApp.trUtf8(u"User geserrt ja/nein")),
                     ("used_memory", 
                                QtGui.qApp.trUtf8(u"Speicherverbrauch (MB)")),
                     ("last_login", QtGui.qApp.trUtf8(u"Letzte Anmeldung")),
                     ("create_time", QtGui.qApp.trUtf8(u"Datum der Erstellung")),
                     ("files", QtGui.qApp.trUtf8(u"Dateien (Anzahl)")),
                     ("admin", QtGui.qApp.trUtf8(u"Admin ja/nein")),
                     ("workspaces", QtGui.qApp.trUtf8(u"Arbeitsbereiche")),
                     ("access_right", QtGui.qApp.trUtf8(u"Zugriffsrechte"))]
    


