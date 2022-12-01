import os
import main
import controllers


# Misc
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Tournament
def tournament_menu():
    while (True):
        print("-- Tournament --")
        if len(main.tournamentTable) > 0:
            print_tournament_infos()
            create_delete = "DELETE TOURNAMENT"
        else:
            create_delete = "Create tournament"
        i = int(input(
            f"1. {create_delete}\n"
            + "0. Main Menu\n"
        ))
        if i == 1:
            if len(main.tournamentTable) > 0:
                delete_tournament()
            else:
                controllers.create_tournament()
        elif i == 0:
            return
        else:
            continue


def delete_tournament():
    main.tournamentTable.truncate()
    print("Tournament deleted from database")


def print_tournament_infos():
    for t in main.tournamentTable:
        print(t)


# Players
# TODO: add specific player deletion
def players_menu():
    while (True):
        print("-- Players --")
        print_all_players()
        i = int(input(
            "1. Add player\n"
            + "9. CLEAR PLAYER LIST\n"
            + "0. Main Menu\n"
        ))
        if i == 1:
            controllers.add_player()
        elif i == 9:
            clear_player_list()
        elif i == 0:
            return
        else:
            continue


def clear_player_list():
    main.playersTable.truncate()
    print("All players deleted from database")


def print_all_players():
    for p in enumerate(main.playersTable):
        print(f"{p[0]}: {p[1]}")


# Matches
def print_match_infos(match):
    print(vars(match))


# Rounds
def print_rounds_infos(chess_round):
    print(vars(chess_round))
