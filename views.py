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
            create_delete = "DELETE TOURNAMENT"
        else:
            create_delete = "Create tournament"
        i = int(input(
            "1. Tournament infos\n"
            + f"9. {create_delete}\n"
            + "0. Main Menu\n"
        ))
        if i == 1:
            clear_screen()
            print_tournament_infos()
        elif i == 9:
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
def players_menu():
    while (True):
        print("-- Players --")
        i = int(input(
            "1. List players\n"
            + "2. Add player\n"
            + "9. CLEAR PLAYER LIST\n"
            + "0. Main Menu\n"
        ))
        if i == 1:
            clear_screen()
            print_all_players()
        elif i == 2:
            controllers.add_player()
        elif i == 9:
            delete_all_players()
        elif i == 0:
            return
        else:
            continue


def delete_all_players():
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
