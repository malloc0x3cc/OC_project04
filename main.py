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
        views.clear_screen()
        print("-- Tournament Manager --")
        i = int(input("1. Manage Tournament\n2. Manage Players\n3. Launch tournament\n0. Exit\n"))
        if i == 1:
            views.clear_screen()
            views.tournament_menu()
        elif i == 2:
            views.clear_screen()
            views.players_menu()
        elif i == 3:
            views.clear_screen()
            controllers.start_tournament()
        elif i == 0:
            views.clear_screen()
            quit()
        else:
            continue
