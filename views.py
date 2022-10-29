import math, datetime
import main, controllers
from tinydb import Query
from models import *


# Menus
def tournament_menu():
    while (True):
        main.CLEAR_SCREEN
        print("-- Tournament --")
        create_delete = "DELETE TOURNAMENT" if len(main.tournamentTable) > 0 else "Create tournament"
        i = int(input(f"1. Tournament infos\n9. {create_delete}\n0. Main Menu\n"))
        if i == 1:
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
        main.CLEAR_SCREEN
        print("-- Players --")
        i = int(input("1. List players\n2. Add player\n9. CLEAR PLAYER LIST\n0. Main Menu\n"))
        if i == 1:
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
        elo_rank=int(input("ELO Rank: "))
    )
    main.playersTable.insert(player.__dict__)


def delete_all_players():
    main.playersTable.truncate()
    print("All players deleted from database")


def print_player_list():
    i = 0
    for p in main.playersTable:
        i += 1
        print(f"{i}: {p}")


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


def start_tournament():
    rounds = matches = []
    print("-- Rounds --")
    # TODO: print paricipants for each round
    matches_dict = []
    # NOTE: logarithm base 2 to figure the amount of rounds.
    for n in range(math.ceil(math.log2(len(main.playersTable)))):
        rounds.append(
            Round(
                n + 1,
                str(datetime.datetime.now()),
                str(datetime.datetime.now()) + str(datetime.timedelta(hours=1))
            )
        )
        print(f"Round {rounds[-1].nb}")
        print("-- Matches --")
        matches = [Match(paired_players_ids=_) for _ in controllers.swiss(players)]

        for _ in matches:
            # TODO: print participants for each match
            # TODO: Get player infos from DB
            print(_.paired_players_ids)
            _.winner = int(input("winner: "))
            matches_dict.append(_.__dict__)
        pl = players
        players = []
        for _ in matches:
            for p in pl:
                if _.winner == p.id:
                    players.append(p)
    main.matchesTable.insert_multiple(matches_dict)

    rounds_dict = []
    for _ in rounds:
        rounds_dict.append(_.__dict__)
    main.roundsTable.insert_multiple(rounds_dict)


# Matches
def print_match_infos(match):
    print(vars(match))


# Rounds
def print_rounds_infos(chess_round):
    print(vars(chess_round))
