from models import *


# Players
def print_player_infos(player):
    print(vars(player))


def print_player_list():
    player_list = []
    for p in Player.instances:
        player_list.append(vars(p))
    print(player_list)


# Tournaments
def print_tournament_infos(tournament):
    print(vars(tournament))


# Matches
def print_match_infos(match):
    print(vars(match))


# Rounds
def print_rounds_infos(chess_round):
    print(vars(chess_round))
