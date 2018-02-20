#!/usr/bin/python3.6
# -*- coding: utf-8 -*-


# Énoncé
#
# Pour commencer cette épreuve utilisant le protocole IRC, vous devez envoyer un message privé au bot Candy : !ep1
# Le bot vous répond alors par un message en privé. Il s’agit d’une chaine sous la forme :
#
#     <nombre1>/<nombre2>
#
#
# - Vous devez calculer la racine carré du nombre n°1 et multiplier le résultat obtenu par le nombre n°2.
# - Vous devez ensuite arrondir à deux chiffres après la virgule le résultat obtenu.
# - Vous avez 2 secondes pour envoyer la bonne réponse à partir du moment où le bot reçoit le message !ep1.
# - Si le bot ne répond plus, c’est que vous avez été banni. Pour être débanni, attendez quelques minutes.
# - La réponse doit être envoyée sous la forme :
#
#     !ep1 -rep <reponse>
#
#
# Exemple :
#
#     25/2
#
#     Vous devez renvoyer "!ep1 -rep <reponse>" en message privé au bot.
#
#
#
# Paramètres de connexion au challenge :
# Hôte :	           irc.root-me.org
# Protocole :	       IRC
# Port :	           6667
# Canal IRC :	       #root-me_challenge
# Bot :                candy

# import sys
# import string
import socket
import time

server = "irc.root-me.org"
chann = "#root-me_challenge"
port = 6667
bot = "Candy"
nick = "toto69nick"
ident = "toto69"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # création du socket
print("Socket créé.")

irc.connect((server, port))
print("Connexion au serveur effectué.")

irc.send(bytes("USER {} {} {}:test auth!\n".format(ident, ident, ident), "UTF-8"))
print("Authentification effectuée.")

irc.send(bytes("NICK {}\r\n".format(nick), "UTF-8"))
print("Paramétrage du Nickname.")

irc.send(bytes("JOIN {}\n".format(chann), "UTF-8"))

time.sleep(2)


irc.send(bytes("PRIVMSG {} !ep1\r\n".format(bot), "UTF-8"))
print("Pause....")
time.sleep(2)
text = irc.recv(10240).decode("UTF-8")

print(text)

i = True
c = -1
tr = 1
car = ""
var1 = ""
var2 = ""
while i:
    car = text[c - 1]
    if car in '0123456789':
        if tr == 1:
            var1 = car + var1
            c -= 1
        else:
            var2 = car + var2
            c -= 1

    elif car in ' /:':
        if tr == 1:
            tr += 1
        elif car == ":":
            i = False
        else:
            c -= 1
    else:
        c -= 1


print("Première valeur : {}".format(var2))
print("Deuxième valeur : {}".format(var1))


irc.close()
