# Application gérant un tournoi d'échecs

### Openclassroom projet 04

Projet consistant à créer une application permettant de créer la structure d'un tournoi d'échecs, permettant d'ajouter des joueurs dans une base de données. Le programme utilise un algorithme permettant de calculer la rotation des joueurs afin que les matchs soit équitables et ne se reproduisent pas (algorithme suisse de tournois).

Le programme utilise le design pattern MVC (Modèles - Vues - Controlleurs), et utilise la librairie TinyDB pour sauvegarder les joueurs et les tournois.

Il permet de :

- Créer et sauvegarder des joueurs.
- Mettre à jour le classement d'un joueur.
- Créer des tournois.
- Lancer des tournois.
- Affiche des rapport concerant les tournois
- Porpose des rapport concerant les joueurs


## Prérequis

Vous devez installer python, la dernière version se trouve à cette adresse 
https://www.python.org/downloads/

Les scripts python se lance depuis un terminal, pour ouvrir un terminal sur Windows, pressez ``` touche windows + r``` et entrez ```cmd```.

Sur Mac, pressez ```touche command + espace``` et entrez ```terminal```.

Sur Linux, vous pouvez ouviri un terminal en pressant les touches ```Ctrl + Alt + T```.

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont repertoriés dans le fichier ```requirements.txt```

Vous pouvez installer un environnement externe via la commande dans le terminal

py -m venv env

dans le terminal, puis entrez la commande :

pip install -r requirement.txt

afin d'installer toutes les librairies.

## Démarrage 

Le programme est écrit en Python, copier tous les fichiers et repertoires du repository, et lancer le programme depuis un terminal via la commande :


py main.py
```



## Rapport flake8

Le repository contient un rapport flake8, qui n'affiche aucune erreur. Il est possible d'en générer un nouveau en entrant dans le terminal :

flake8 --format=html --max-line-length=119 --htmldir=flake-report

Le fichier ```.flake8``` à la racine contient les paramètres concernant la génération du rapport.
