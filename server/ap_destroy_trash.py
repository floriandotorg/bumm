# -*- coding: utf-8 -*-

# Dateiname: ap_destroy_trash.py
# Beschreibung: BSCW-API-Erweiterung zum Leeren der Mülleimer aller
# oder einiger Benutzer
# Version: 1
# Autor: Florian Kaiser
# Letzte Änderung: 23.02.09

#################################################################################
# Copyright (C) 2009 Benjamin Flader, Benjamin Leipold, André Naumann,          #
# Corinna Vollert, Florian Kaiser                                               #
#                                                                               #
# Redistribution and use in source and binary forms, with or without            #
# modification, are permitted provided that the following conditions            #
# are met:                                                                      #
#                                                                               #
# 1. Redistributions of source code must retain the above copyright             #
#    notice, this list of conditions and the following disclaimer.              #
# 2. Redistributions in binary form must reproduce the above copyright          #
#    notice, this list of conditions and the following disclaimer in the        #
#    documentation and/or other materials provided with the distribution.       #
#                                                                               #
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR          #
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES     #
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.       #
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,              #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT      #
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,     #
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY         #
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT           #
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF      #
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.             #
#################################################################################

def param_def():
    from api_def import ASCII, ARRAY, INT
    return (
        # Mindestalter der zu löschenden Dateien in Tagen
        ('outdated', INT, 0),
        # Eine Liste mit den Namen der zu löschenden Benutzer oder eine leere
        # Liste für alle Benutzer
        ('user_names', ARRAY, 0, [('user_name', ASCII, 1)]),
    )
    
def do_it(request, outdated, user_names):
    from admin import bs_admutil
    from admin import op_rmwaste
    from cl_request import Request
    import time
    
    # Prüfen ob der Benutzer, der diese Datei ausführt Admin-Rechte besitzt,
    # wenn nicht, Ausführung abbrechen
    if not request.user.is_admin():
        return None
        
    req = Request()
    # Zeit von Tagen in Sekunden umrechnen
    outdated = time.time() - 24 * 3600 * outdated
    
    # Usernamen in Userobjekte umwandeln
    # Keine User angegeben? Dann alle User verwenden
    users = bs_admutil.userlist(user_names or None)[0]

    # Liste mit Userobjekten durchgehen ..
    for user in users:
        req.set_user(user.name)
        # .. und die Mülleimer dieser leeren
        op_rmwaste.clear_waste(req, user.waste, outdated, True, False)