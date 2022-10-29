import os, datetime
import main
from models import *


# Menus
def tournament_menu():
    while (True):
        print("-- Tournament --")
        create_delete = "DELETE TOURNAMENT" if len(main.tournamentTable) > 0 else "Create tournament"
        i = int(input(f"1. Tournament infos\n9. {create_delete}\n0. Main Menu\n"))
        if i == 1:
            clear_screen()
            print_tournament_infos()
        elif i == 9:
            if len(main.tournamentTable) > 0:
                delete_tournament()
            else:
                create_tournament()
        elif i == 0:
            return
        else:
            continue


def players_menu():
    while (True):
        print("-- Players --")
        i = int(input("1. List players\n2. Add player\n9. CLEAR PLAYER LIST\n0. Main Menu\n"))
        if i == 1:
            clear_screen()
            print_player_list()
        elif i == 2:
            add_player()
        elif i == 9:
            delete_all_players()
        elif i == 0:
            return
        else:
            continue

# Players
def add_player():
    player = Player(
        firstname=input("First name: "),
        lastname=input("Last name: "),
        birthdate=input("Birthday date: "),
        elo=int(input("ELO: "))
    )
    main.playersTable.insert(player.__dict__)


def delete_all_players():
    main.playersTable.truncate()
    print("All players deleted from database")


def print_player_list():

    for p in enumerate(main.playersTable):
        print(f"{p[0]}: {p[1]}")


# Tournaments
def create_tournament():
    tournament = Tournament(
        name=input("Name: "),
        location=input("Location: "),
        date=str(datetime.datetime.now())
        # TODO: Input date (blank for datetime now)
    )
    main.tournamentTable.insert(tournament.__dict__)


def delete_tournament():
    main.tournamentTable.truncate()
    print("Tournament deleted from database")


def print_tournament_infos():
    for t in main.tournamentTable:
        print(t)


# Matches
def print_match_infos(match):
    print(vars(match))


# Rounds
def print_rounds_infos(chess_round):
    print(vars(chess_round))


# Misc
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
