#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

'''
Énoncé

Pour commencer cette épreuve utilisant le protocole IRC, vous devez envoyer un message privé au bot Candy : !ep1
Le bot vous répond alors par un message en privé. Il s’agit d’une chaine sous la forme :

    <nombre1>/<nombre2>


- Vous devez calculer la racine carré du nombre n°1 et multiplier le résultat obtenu par le nombre n°2.
- Vous devez ensuite arrondir à deux chiffres après la virgule le résultat obtenu.
- Vous avez 2 secondes pour envoyer la bonne réponse à partir du moment où le bot reçoit le message !ep1.
- Si le bot ne répond plus, c’est que vous avez été banni. Pour être débanni, attendez quelques minutes.
- La réponse doit être envoyée sous la forme :

    !ep1 -rep <reponse>


Exemple :

    25/2

    Vous devez renvoyer "!ep1 -rep <reponse>" en message privé au bot.



Paramètres de connexion au challenge :
Hôte :	           irc.root-me.org
Protocole :	       IRC
Port :	           6667
Canal IRC :	       #root-me_challenge
Bot :              candy
'''
