import os
from tinydb import TinyDB
import views, controllers


FILE = "db.json"
# open(FILE, 'w').close()
db = TinyDB(FILE, sort_keys=True, indent=4)
roundsTable = db.table("Rounds")
matchesTable = db.table("Matches")
playersTable = db.table("Players")
tournamentTable = db.table("Tournament")

if __name__ == "__main__":
    while (True):
        print("-- Tournament Manager --")
        i = int(input("1. Manage Tournament\n2. Manage Players\n3. Launch tournament\n0. Exit\n"))
        views.clear_screen()
        if i == 1:
            views.tournament_menu()
        elif i == 2:
            views.players_menu()
        elif i == 3:
            controllers.start_tournament()
        elif i == 0:
            quit()
        else:
            continue
