# -*- coding: utf-8 -*-

## Buildfile für BUMM

#################################################################################
# Copyright (C) 2009 Benjamin Flader, Benjamin Leipold, Andr� Naumann,          #
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

import compileall
import os
import shutil

def recursive_delete(dirpath, file_ext):
    files = os.listdir(dirpath)
    for file in files:
        path = os.path.join (dirpath, file)
        if os.path.isdir(path):
            recursive_delete(path, file_ext)
        elif file[-len(file_ext):] == file_ext:
            print 'Removing file: "%s"' % path
            retval = os.unlink(path)

# Quellen in 'bin' kopieren
shutil.copytree('src/', 'bin/')

# Dateien kompilieren
compileall.compile_dir('bin/', force=True)
    
# Quellen löschen
recursive_delete('bin', 'py')

# Benutzerhandbuch kopieren
shutil.copytree('manual/', 'bin/manual')

print "Finished!"