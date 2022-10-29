import math, datetime
import main
from models import *


# Players
def add_player():
    player = Player(
        firstname=input("First name: "),
        lastname=input("Last name: "),
        birthdate=input("Birthday date: "),
        elo=int(input("ELO: "))
    )
    main.playersTable.insert(player.__dict__)


# Tournaments
def create_tournament():
    # TODO: Input date (blank for datetime now)
    tournament = Tournament(
        name=input("Name: "),
        location=input("Location: "),
        date=str(datetime.datetime.now())
    )
    main.tournamentTable.insert(tournament.__dict__)


# Rounds
# def create_round(nb):
#     return Round(f"Round {nb + 1}", datetime.now(), "")


def swiss(player_list):
    # Bubble sort
    swap = True
    length = len(player_list) - 1
    while swap:
        i = 0
        swap = False
        while i < length:
            if player_list[i]['elo'] > player_list[i + 1]['elo']:
                buffer = player_list[i]
                player_list[i] = player_list[i + 1]
                player_list[i + 1] = buffer
                swap = True
            i += 1
        length -= 1

    # Pairing
    i = 0
    pairs = []
    while i < (len(player_list) - 1):
        pairs.append([player_list[i], player_list[i + 1]])
        i += 2

    return pairs


def start_tournament():
    rounds = matches = []
    players = []
    for p in main.playersTable:
        players.append(p)
    print("-- Rounds --")
    # TODO: print paricipants for each round
    matches_dict = []
    # NOTE: logarithm base 2 to figure the amount of rounds.
    for n in range(math.ceil(math.log2(len(main.playersTable)))):
        rounds.append(
            Round(
                nb=n + 1,
                start_date=str(datetime.datetime.now()),
                end_date=str(datetime.datetime.now()) + str(datetime.timedelta(hours=1))
            )
        )
        print(f"Round {rounds[-1].nb}")
        print("-- Matches --")
        matches = [Match(paired_players=_) for _ in swiss(players)]

        for _ in matches:
            for p in enumerate(_.paired_players):
                print(f"{p[0]}: {p[1]['firstname']} {p[1]['lastname']} ({p[1]['elo']})")
            _.winner = _.paired_players[int(input("winner: "))]
            main.matchesTable.insert(_.__dict__)
        pl = players
        players = []
        for _ in matches:
            for p in pl:
                if _.winner == p:
                    players.append(p)

    for _ in rounds:
        main.roundsTable.insert(_.__dict__)
