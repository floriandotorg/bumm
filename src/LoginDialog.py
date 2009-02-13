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
from interface.Exceptions import *
#from interface.BscwInterface import BscwInterface
from test import BscwInterface

## Stellt ein Dialog da, indem Benutzername und Passwort eingegeben werden
# müssen. Optional kann ein Proxy eingegeben werden.
# Sind alle Daten eingegeben, kann ein Verbindungsversuch gestartet werden.
class LoginDialog(QtGui.QDialog, Ui_LoginDialog):
    
    ## Konstruktor
    # @param p_settings Klasse in der die Einstellungen gespeichert sind 
    # @param p_parent Übergeordnetes QObject.
    def __init__(self, p_settings, p_parent = None):
         QtGui.QDialog.__init__(self, p_parent)
         self.setupUi(self)
         
         # Einstellungen laden und in die Steuerelemente schreiben
         self._settings = p_settings
         self._username.setText(p_settings.username)
         self._server_address.setText(p_settings.server_address)
         
         # BscwInterface Klasse initilisieren
         self._bscw_interface = BscwInterface()
         
         # 'Anmelden' Button mit _loginSlot verbinden
         self.connect(self._login_button, QtCore.SIGNAL("clicked()"),
                        self._loginSlot)
         
         # 'Proxy' Button mit _configureProxySlot verbinden
         self.connect(self._proxy_button, QtCore.SIGNAL("clicked()"),
                        self._configureProxySlot)
         
    ## Gibt nach erfolgreicher Anmeldung die verbundene
    # BscwInterface Klasse zurück.
    def getInterface(self):
        return self._bscw_interface
    
    ## Sperrt bzw. Entsperrt alle Steuerelemente auf dem Fenster.
    # @param p_enable Steuerelemente sperren ja/nein (Boolean)
    def _setEnabled(self, p_enable):
        self._server_address.setEnabled(p_enable)
        self._username.setEnabled(p_enable)
        self._passwd.setEnabled(p_enable)
        self._proxy_button.setEnabled(p_enable)
        self._login_button.setEnabled(p_enable)
        self._quit_button.setEnabled(p_enable)
    
    ## Schreibt einen Text auf das Status-Label und ändert die Textfarbe
    # des Labels.
    # @param p_str Text der in das Label geschrieben werden soll
    # @param p_color Die neue Textfarbe als QtGui.QColor     
    def _changeStatus(self, p_str, p_color):
        self._lbl_status.setText(p_str)
        palette = QtGui.QPalette(QtGui.QColor("white"))
        palette.setColor(QtGui.QPalette.Text, p_color)
        palette.setColor(QtGui.QPalette.Foreground, p_color)
        self._lbl_status.setPalette(palette)
    
    ## Versucht sich am BSCW-Server anzumelden und gibt ggf. eine Fehlermeldung
    # aus.
    def _loginSlot(self):
        self._setEnabled(False)()
        self._changeStatus("Verbinde...", QtGui.QColor("black"))
        self.repaint()
        
        # Anmeldung ausführen und ggf. Fehlermeldung anzeigen
        try:
            self._bscw_interface.login(self._username.text(),
                                        self._passwd.text())
            self.accept()
        except AuthorizationFailed:
            self._changeStatus(self.trUtf8("Autorisation fehlgeschlagen!"),
                               QtGui.QColor("Red"))
        except HostUnreachable:
            self._changeStatus(self.trUtf8("Server nicht erreichbar!"),
                                QtGui.QColor("Red"))
        except ProxyUnreachable:
            self._changeStatus(self.trUtf8("Proxy nicht erreichbar!"),
                                QtGui.QColor("Red"))
        except:
            self._changeStatus(self.trUtf8("Unbekannter Fehler aufgetreten!"),
                                QtGui.QColor("Red"))
        finally:
            self._setEnabled(True)()
    
    ## Öffnet ein Eingabefenster für die Proxy-Konfigurationen und übergibt ggf.
    # die Daten an die BscwInterface Klasse.        
    def _configureProxySlot(self):
        # Variable zum Zwischenspeichern der Eingabe
        proxy = (QtCore.QString(self._settings.proxy), True)
        # Regulärer Ausdruck zum Parsen der Eingabe
        reg_exp = QtCore.QRegExp("((([a-zA-Z0-9_]+):([a-zA-Z0-9_]+)@)?"\
                                 "([a-zA-Z0-9_]+)(:([0-9]{1,5}))?)?")
        
        while proxy[1]:
            # Eingabefenster anzeigen            
            proxy = QtGui.QInputDialog.getText(self, self.trUtf8("Proxy"),
                        self.trUtf8("Bitte geben Sie die Adresse des Proxys "\
                                    "im folgenden Format ein:\n\n"
                                    "[benutzer:passwort@]adresse:port"), 
                        QtGui.QLineEdit.Normal,
                        proxy[0])
            
            # Ist die Eingabe korrekt? Dann Werte in BscwInterface schreiben
            # und Konfiguration speichern
            if proxy[1] and reg_exp.exactMatch(proxy[0]):
                self._bscw_interface.setProxy(reg_exp.cap(5), reg_exp.cap(7),
                                              reg_exp.cap(3), reg_exp.cap(4))
                self._settings.proxy = proxy[0]
                break
            # Eingabe nicht korrekt? Dann Fehlermeldung anzeigen
            elif proxy[1]:
                QtGui.QMessageBox.critical(self,
                                           self.trUtf8("Fehlerhafte Eingabe"),
                                        self.trUtf8("Ihre Eingabe entspricht "\
                                                    "nicht dem Muster."))