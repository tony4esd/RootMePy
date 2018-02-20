#!/usr/bin/en python3
# -*- coding: utf-8 -*-


# Énoncé
#
# Pour commencer cette épreuve, envoyez en message privé !ep2 au bot Candy.
#
# - Le bot vous répond alors par un message privé.
# - Il s’agit d’une chaîne de caractères encodée.
# - Vous devez lui renvoyer le message décodé.
# - Vous avez 2 secondes
# - Si le bot ne répond plus, c’est que vous avez été banni. Pour être débanni, attendez quelques minutes.
# - La réponse doit être sous la forme :
# !ep2 -rep <reponse>
#
# Exemple :
# Um9vdE1l
#
# Vous devez renvoyer "!ep2 -rep RootMe" en message privé au bot.
#
# Paramètres de connexion au challenge :
# Hôte	irc.root-me.org
# Protocole	IRC
# Port	6667
# Canal IRC	#root-me_challenge
# Bot	candy

# test

import socket
import time
import base64

server = "irc.root-me.org"
chann = "#root-me_challenge"
port = 6667
bot = "Candy"
nick = "toto69nick"
ident = "toto69"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # création du socket
print("Socket créé.")

irc.connect((server, port))
print("Connexion au serveur effectué.")

irc.send(bytes("USER {} {} {}:test auth!\n".format(ident, ident, ident), "UTF-8"))
print("Authentification effectuée.")

irc.send(bytes("NICK {}\r\n".format(nick), "UTF-8"))
print("Paramétrage du Nickname.")

irc.send(bytes("JOIN {}\n".format(chann), "UTF-8"))

time.sleep(2)

irc.send(bytes("PRIVMSG {} !ep2\r\n".format(bot), "UTF-8"))
time.sleep(1)
res = irc.recv(20000).decode("UTF-8")
print(res)

res = res.split()

res = res[-1][1:]
print(res)
res = base64.b64decode(res)
print(res)
res = str(res)
print(res)
res = res[2:-1]
print(res)

irc.send(bytes("PRIVMSG {} !ep2 -rep {}\r\n".format(bot, res), "UTF-8"))
text = irc.recv(1024).decode("UTF-8")

print(text)

irc.close()
