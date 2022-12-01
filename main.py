from tinydb import TinyDB
import views
import controllers


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
        i = int(input(
            "1. Launch Tournament\n"
            + "2. Manage Tournament\n"
            + "3. Manage Players\n"
            + "0. Exit\n"
        ))
        views.clear_screen()
        if i == 1:
            if len(tournamentTable) > 0:
                controllers.start_tournament()
            else:
                print("You have to create a tournament first...")
        elif i == 2:
            views.tournament_menu()
        elif i == 3:
            views.players_menu()
        elif i == 0:
            quit()
        else:
            continue
