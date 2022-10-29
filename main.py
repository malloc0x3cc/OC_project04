import os
from tinydb import TinyDB
import views


CLEAR_SCREEN = os.system('cls' if os.name == 'nt' else 'clear')
FILE = "db.json"
# open(FILE, 'w').close()
db = TinyDB(FILE, sort_keys=True, indent=4)
roundsTable = db.table("Rounds")
matchesTable = db.table("Matches")
playersTable = db.table("Players")
tournamentTable = db.table("Tournament")

if __name__ == "__main__":
    print("-- Tournament Manager --")
    while (True):
        i = int(input("1. Manage Tournament\n2. Manage Players\n3. Launch tournament\n0. Exit\n"))
        if i == 1:
            views.tournament_menu()
        elif i == 2:
            views.players_menu()
        elif i == 3:
            views.start_tournament()
        elif i == 0:
            quit()
        else:
            continue
