# -*- coding: utf-8 -*-

# Dateiname: ap_delete_user.py
# Beschreibung: BSCW-API-Erweiterung zum Löschen von Benutzern
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
    from api_def import ASCII, ARRAY
    return (
        # Liste mit Usernamen der zu löschenden Benutzer
        ('user_names', ARRAY, 0, [('user_name', ASCII, 1)]),
    )

def do_it(request, user_names):
    from admin import op_rmuser
    
    # Prüfen ob der Benutzer, der diese Datei ausführt Admin-Rechte besitzt,
    # wenn nicht, Ausführung abbrechen
    if not request.user.is_admin():
        return None
    
    # Der Rückgabewert ist eine Liste aller Benutzer die nicht gelöscht werden
    # konnten
    result = []    
    
    # Username für Username durchgehen und ..
    for user_name in user_names:
        try:
            # .. versuchen den Benutzer zu löschen
            op_rmuser.handle_main(["bsadmin rmuser", user_name])
        except:
            # Fehler aufgetreten? Dann an die Liste anhängen
            result.append(user_name)
            
    return result