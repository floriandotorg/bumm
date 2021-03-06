# -*- coding: utf-8 -*-

# Dateiname: ap_lock_user.py
# Beschreibung: BSCW-API-Erweiterung zum Sperren eines Benutzers
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
        # Liste von Benutzernamen
        ('user_names', ARRAY, 0, [('user_name', ASCII, 1)]),
    )
    
def do_it(request, user_names):
    import bs_passwd
    from cl_request import get_user
    
    # Prüfen ob der Benutzer, der diese Datei ausführt Admin-Rechte besitzt,
    # wenn nicht, Ausführung abbrechen
    if not request.user.is_admin():
        return None
    
    # Alle User durchgehen ..
    for user_name in user_names:
        try:
            # .. und Benutzerkonto sperren
            bs_passwd.updatelock(get_user(user_name), bs_passwd.LOCK, bs_passwd.LCK_ADMIN)
        except:
            # Es tritt ein Fehler auf, wenn der User bereits gelockt ist,
            # deshalb werden alle Fehler ignoriert
            pass