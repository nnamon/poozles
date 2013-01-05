# -*- coding: utf-8 -*-

# Autor: Hans Bild

import SocketServer
import objectify
import random, md5

objekt_liste = {}

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
         self.data = self.request.recv(1024).strip()
         self.request.sendall(semantics(self.data))

def aller_objekt():
    return "Aller objekt: " + ", ".join(objekt_liste.keys()) + "\n"

def objekt_erstellen():
    pass # Nicht für Nicht-Mitglieder!

def semantics(data):
    response = "Willkommen bei SturmZurück! Nur Mitglieder der Herrenrasse!\n"
    if data[:5] == "liste":
        response += aller_objekt()
    elif data[:5] == "legen":
        oid = data.split()[1]
        if oid in objekt_liste.keys():
            response += objectify.print_object(objekt_liste[oid])
        else:
            response += "Object ID existiert nicht!\n"
    elif data[:9] == "speichern":
        enc = data.split()[1]
        obj = objectify.load_object(enc)
        oid = md5.md5(str(random.gauss(5, 1337)*random.random())).hexdigest()
        objekt_liste[oid] = obj
        response += "Speichern Objekt ist erfolgreich! Die Objekt-ID ist %s. Danke.\n" % oid
    else:
        response += "Hinweis: Wir bieten Dienstleistungen für die Objektivierung von Menschen. Zu diesem Zeitpunkt wissen wir nicht bieten kostenlose Unterstützung für die Schaffung von Objekten. Dies erfordert eine Mitgliedschaft Premium allerdings Mitgliedschaft ist nur auf Einladung durch ein hochrangiges Mitglied der Organisation. Das Laden von öffentlich gespeicherten Objekte und die Einsparung von Objekten ist kostenlos.\n\n"
        response += "Befehle:\n"
        response += "Liste aller Objekte: liste\n"
        response += "Legen Sie Objekt: legen [objekt id]\n"
        response += "Speichern Sie das Objekt: speichern [objekt string]\n"
    return response

if __name__ == "__main__":
    # Wir stahlen diese aus dem Python-Dokumentation
    HOST, PORT = "localhost", 9998
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
