# OC_project04
Développez un programme logiciel en Python

## Présentation
Pour ce projet, il faut écrire une application permettant de gérer un tournois d'échecs et de produire des rapports sur celui ci.

## Usage
Tout d'abbord, il faut s'assurer que `Python 3` et `PIP` sont installés et de préférence à jour sur votre machine.

Il est possible de créer/activer un environnement virtuel avec `venv`:
```sh
$ python3 -m venv env
$ source env/bin/activate
```
Il faudra ensuite installer les dépendences necessaires au script:
```sh
$ python3 -m pip install -r requirements.txt
```
La commande permantant de lancer le programme est la suivante:
```sh
$ python3 main.py
```
Un menu à été implémenté pour faciliter l'utilisation de l'application. `main.py` à été pensé pour etre une solution "clées en main".

Pour executer `flake8-html` uniquement sur le code source, la commande suivante sera lancée depuis la racine du projet:
```sh
$ python3 -m flake8 --format=html --htmldir=flake-report/ ./*.py
```
Le rapport `flake8` sera généré dans le dossier `flake-report/`

NOTE: `flake8-html` ayant des soucis de compatibilité avec `flake8` à partir de la version `5.0.0`, il est cloné pour ce projet d'un [fork](https://github.com/skadyan/flake8-html) contenant un fix permettant de l'utiliser.
