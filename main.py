import os
import datetime
from tinydb import TinyDB
from controllers import swiss
from views import *


FILE = "db.json"
db = TinyDB(FILE, sort_keys=True, indent=4)
roundsTable = db.table("Rounds")
matchesTable = db.table("Matches")
playersTable = db.table("Players")
tournamentTable = db.table("Tournament")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-- Tournament Manager --")
    while (True):
        i = int(input("1. Manage Tournament\n2. Manage Players\n3. Launch tournament\n9. Clear Database\n0. Exit\n"))
        if i == 1:
            tournament_menu()
        elif i == 2:
            players_menu()
        elif i == 3:
            break
        elif i == 9:
            db.clear_cache()
            print("Database cleared !")
        elif i == 0:
            quit()
        else:
            continue

    rounds = matches = []
    print("-- Rounds --")
    # TODO: print paricipants for each round
    matches_dict = []
    # NOTE: logarithm base 2 to figure the amount of rounds.
    for n in range(math.ceil(math.log2(len(Player.instances)))):
        rounds.append(
            Round(
                n + 1,
                str(datetime.datetime.now()),
                str(datetime.datetime.now()) + str(datetime.timedelta(hours=1))
            )
        )
        print(f"Round {rounds[-1].nb}")
        print("-- Matches --")
        matches = [Match(paired_players_ids=_) for _ in swiss(players)]

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
    matchesTable.insert_multiple(matches_dict)

    rounds_dict = []
    for _ in rounds:
        rounds_dict.append(_.__dict__)
    roundsTable.insert_multiple(rounds_dict)
