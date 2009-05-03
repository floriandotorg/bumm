1. Installation

Alle Dateien aus dem Ordner 'bin' in einen beliebigen Ordner kopieren und das
Programm mit 'pythonw __main__.pyc' starten

Sollte kein Ordner 'bin' vorhanden sein, muss das Programm erst mit
'python Build.py' kompiliert werden.

Bevor das Programm ausgeführt werden kann, müssen alle Dateien aus dem Ordner
'server' in den Ordner 'src' auf dem BSCW-Server kopiert werden.

2. Vorrausetzungen

Hardware
- Handelsüblicher PC mit für Python ausreichende Ressourcen
- Netzwerkverbindung zum BSCW-Server

Software
- Python 2.5.x oder höher
- PyQt4

3. Ordnerstruktur:

bin/	Kompilierte Python Dateien
doc/	Dokumentation	
manual/	Benutzerhandbuch
qrc/	Qt-Resourcen Dateien
server/	Server-Erweiterung
src/	Quellen
ui/	Qt-User Interdace Dateien