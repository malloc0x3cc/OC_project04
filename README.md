# OC_project04
Développez un programme logiciel en Python

## Présentation
Pour ce projet, il faut écrire une application permettant de gérer un tournois d'échecs et de produire des rapports sur celui ci.

## Usage
Tout d'abbord, il faut s'assurer que `Python 3` et `PIP` sont installés et de préférence à jour sur votre machine.
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
