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
from interface.BscwInterface import BscwInterface

## Stellt ein Dialog da, der die Login-Daten entgegen nimmt und die Anmeldung
# durchührt.
class LoginDialog(QtGui.QDialog, Ui_LoginDialog):

    ## Konstruktor
    # @param p_settings Klasse in der die Einstellungen gespeichert sind
    # @param p_parent Übergeordnetes QObject.
    def __init__(self, p_settings, p_parent = None):
        QtGui.QDialog.__init__(self, p_parent)
        self.setupUi(self)
        
        ## Programmenstellungen
        self._settings = p_settings
        self._username.setText(p_settings.username)
        self._server_address.setText(p_settings.server_address)
        self._passwd.setText("badreligion")
        
        ## Verbindung zum BSCW-Server
        self._bscw_interface = BscwInterface()
        
        # 'Anmelden' Button mit _loginSlot verbinden
        self.connect(self._login_button, QtCore.SIGNAL("clicked()"),
                     self._loginSlot)

    ## Gibt nach erfolgreicher Anmeldung die verbundene
    # BscwInterface Klasse zurück.
    def getInterface(self):
        return self._bscw_interface

    ## Gibt den Inhalt des Eingabefelds für die Server-Adresse zurück.
    # @return Server-Adresse als QString
    def getServerAddress(self):
        return self._server_address.text()

    ## Gibt den Inhalt des Eingabefelds für den Benutzername zurück.
    # @return Benutzername als QString
    def getUsername(self):
        return self._username.text()

    ## Gibt den Inhalt des Eingabefelds für das Passwort zurück.
    # @return Passwort als QString
    def getPasswd(self):
        return self._passwd.text()
    
    ## Gibt die Klasse für die Einstellungen zurück
    # @return Settings Klasse
    def getSettings(self):
        self._settings.username = str(self._username.text())
        self._settings.server_address = str(self._server_address.text())
        return self._settings

    ## Sperrt oder Entsperrt alle Steuerelemente auf dem Fenster.
    # @param p_enable Steuerelemente sperren ja/nein (Boolean)
    def _setEnabled(self, p_enable):
        self._server_address.setEnabled(p_enable)
        self._username.setEnabled(p_enable)
        self._passwd.setEnabled(p_enable)
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

    ## Versucht sich am BSCW-Server anzumelden und gibt gegebenenfalls
    # eine Fehlermeldung aus.
    def _loginSlot(self):
        self._setEnabled(False)
        self._changeStatus("Verbinde...", QtGui.QColor("black"))
        self.repaint()

        # Anmeldung ausführen und ggf. Fehlermeldung anzeigen
        try:
            self._bscw_interface.login(str(self._server_address.text()),
                                       str(self._username.text()),
                                       str(self._passwd.text()))
            self.accept()
        except LoginIncorrect:
            self._changeStatus(self.trUtf8("Benutzername oder Passwort falsch!"),
                               QtGui.QColor("Red"))
        except NoAdminRights:
            self._changeStatus(self.trUtf8("Benutzer hat keine Admin-Rechte!"),
                               QtGui.QColor("Red"))
        except UserLocked:
            self._changeStatus(self.trUtf8("Benutzer gesperrt!"),
                               QtGui.QColor("Red"))
        except HostUnreachable:
            self._changeStatus(self.trUtf8("Server nicht erreichbar!"),
                                QtGui.QColor("Red"))
        #except:
        #    self._changeStatus(self.trUtf8("Unbekannter Fehler aufgetreten!"),
        #                        QtGui.QColor("Red"))
        finally:
            self._setEnabled(True)