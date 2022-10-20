import os
import datetime
import main
from tinydb import Query
from models import *


# Players
def players_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-- Players --")
    while (True):
        i = int(input("1. List players\n2. Add players\n0. Main Menu\n"))
        if i == 1:
            pass
        elif i == 2:
            create_players()
        elif i == 0:
            return
        else:
            continue


def create_players():
    players = []
    count = 0
    while True:
        print_player_list()
        i = input("1. Add players ? [Y/n]\n")
        if i.upper() == 'Y':
            players.append(
                Player(
                    player_id=count,
                    firstname=input("First name: "),
                    lastname=input("Last name: "),
                    birthdate=input("Birthday date: "),
                    elo_rank=int(input("ELO Rank: "))
                )
            )
            count += 1
        elif i.upper() == 'N':
            break
        else:
            print("USAGE: [Y/n]")
    players_dict = []
    for _ in players:
        players_dict.append(_.__dict__)
    main.playersTable.insert_multiple(players_dict)


def print_player_list():
    player_list = []
    for p in Player.instances:
        player_list.append(vars(p))
    print(player_list)


# Tournaments
def tournament_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-- Tournament --")
    while (True):
        i = int(input("1. Tournament infos\n2. Create tournament\n0. Main Menu\n"))
        if i == 1:
            pass
        elif i == 2:
            create_tournament()
        elif i == 0:
            return
        else:
            continue


def create_tournament():
    tournament = Tournament(
        name=input("Name: "),
        location=input("Location: "),
        description=input("Description (optional): "),
        date=str(datetime.datetime.now())
    )
    main.tournamentTable.insert(tournament.__dict__)


# Matches
def print_match_infos(match):
    print(vars(match))


# Rounds
def print_rounds_infos(chess_round):
    print(vars(chess_round))
