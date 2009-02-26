# -*- coding: utf-8 -*-

# Dateiname: ap_get_all_user.py
# Beschreibung: BSCW-API-Erweiterung zum Ermitteln aller Benutzerinformationen
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

# Dummy-Klasse für access_rights_all. Wird benötigt um die fehlenden Rechte für
# diese Operation zu umgehen
class request_dummy(object):
    def want(self, a,b):
        pass
        
def param_def():
    return ()

def do_it(request):
    import time
    import datetime
    from admin import op_fsusage
    from admin import bs_admutil
    from admin import op_members
    import config_meet
    from ap_get_access_rights_all import access_rights_all
    
    # Alle Benutzer ausfindig machen
    all_users = bs_admutil.userlist(None, True)[0]
    result = []

    # Anzahl der Datein den Gesamtspeicherplatz aller User in einem Dict
    # speichern
    mem_list = {}
    for user in op_fsusage.load_lists((True, True), False)[0]:
        mem_list[user[0]] = (user[2], user[1])
    
    # Benutzer durchgehen
    for user in all_users:
        user_info = {}
        
        # Grundlegende Daten aus der Klasse User laden
        user_info["user_id"] = user.__id__
        user_info["name"] = user.def_fullname()
        user_info["longname"] = user.fullname
        user_info["email"] = user.addresses[0].name
        user_info["secondary_email"] = [adr.name for adr in user.addresses[1:]]
        user_info["organization"] = user.org 
        user_info["phone_home"] = user.homephone
        user_info["phone_mobile"] = user.mobile
        user_info["phone_office"] = user.phone
        user_info["fax"] = user.fax
        user_info["language"] = user.def_language()
        user_info["address"] = user.post
        user_info["url"] = user.url
        user_info["url_home"] = user.home_url
        user_info["additional_info"] = user.description()
        user_info["photo"] = user.image
        user_info["locked"] = user.is_locked()
        user_info["admin"] = user.is_admin()
        
        # Liste der Nachrichtendienste in Dictonary umwandeln
        user_info["messaging_services"] = {}
        for (name, url, link, icon, id) in config_meet.MessagingServices:
            if id in user.messaging_services.keys():
                user_info["messaging_services"][name] = user.messaging_services[id]
                
        # Benutzerspeicherplatz aus der Speicherplatzliste laden
        try:
          user_info["used_memory"] = mem_list[user.name][0]
        except:
          user_info["used_memory"] = 0
        
        # Anzahl der Dateien aus der Speicherplatzliste laden
        try:
          user_info["files"] = mem_list[user.name][1]
        except:
          user_info["files"] = 0
        
        # Datum der letzten Anmeldung laden, falls vorhanden
        if user.accessCount.lastlog:
            y,m,d,H,M,S,w,c,s = time.localtime(user.accessCount.lastlog)
            user_info["last_login"] = datetime.datetime(y,m,d,H,M,S)
        else:
            user_info["last_login"] = None
        
        # Datum der Erstellung des Users laden
        try:
            y,m,d,H,M,S,w,c,s = time.localtime(user.createEvent.time)
            user_info["create_time"] = datetime.datetime(y,m,d,H,M,S)
        except:
            user_info["create_time"] = None
        
        # Liste aller Arbeitsbereiche, denen der Benutzer angehört, laden    
        wsgrps=[]
        visited=[]
        op_members.get_wsgroups(user.home, wsgrps, visited, user)
        op_members.get_wsgroups(user.bag, wsgrps, visited, user)
        op_members.get_wsgroups(user.waste, wsgrps, visited, user)
        user_info["workspaces"] = [wsgrp.name[1:] for wsgrp in wsgrps]
        
        # Zugriffsrechte ermitteln
        access_rights = access_rights_all(request_dummy(), user, True)
        try:
            user_info["access_rights"] = {  'owner' : access_rights['R0owner'],
                                            'manager' : access_rights['R2manager'],
                                            'other' : access_rights['R0other']}
        except:
            user_info["access_rights"] = None
        
        result.append(user_info)
        
    return result