from tinydb import TinyDB
from views import *
import datetime


if __name__ == "__main__":
	# TODO: Check if DB already exists
	db = TinyDB("db.json", sort_keys=True, indent=4)
	tournamentTable = db.table("Tounament")
	playersTable = db.table("Players")
	roundsTable = db.table("Rounds")
	matchesTable = db.table("Matches")

	tournament = Tournament(name="Unreal Tournament", location="Cupertino, CA", description="A test tournament", date=str(datetime.datetime.now()))
	players = matches = rounds = []

	printMainMenu(tournament, players, rounds, matches)
