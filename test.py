from venv import create
from models import *
from views import *
from controllers import *
from faker import Faker
import random
import datetime
from tinydb import TinyDB


if __name__ == "__main__":
	# Database + tables
	db = TinyDB("db.json", sort_keys=True, indent=4)
	tournamentTable = db.table("Tounament")
	playersTable = db.table("Players")
	roundsTable = db.table("Rounds")
	matchesTable = db.table("Matches")

	players = [ Player(id=_, firstname=Faker().first_name(), lastname=Faker().last_name(), gender=random.choice(["M", "F"]), birthdate=str(Faker().date_of_birth()), elo_rank=random.randint(1200, 1400)) for _ in range(8) ]
	tournament = Tournament(name="Unreal Tournament", location="Cupertino, CA", description="A test tournament", date=str(datetime.datetime.now()))
	rounds = [ Round(n + 1, str(datetime.datetime.now()), str(datetime.datetime.now()) + str(datetime.timedelta(hours=1))) for n in range(tournament.nb_of_rounds) ]
	matches = [ Match(paired_players_ids=[_]) for _ in swiss(players) ]

	# Objects to dictionaries
	players_dict = []
	rounds_dict = []
	matches_dict = []

	for _ in players: players_dict.append(_.__dict__)
	for _ in rounds: rounds_dict.append(_.__dict__)
	for _ in matches: matches_dict.append(_.__dict__)

	# db insert
	tournamentTable.insert(tournament.__dict__)
	playersTable.insert_multiple(players_dict)
	roundsTable.insert_multiple(rounds_dict)
	matchesTable.insert_multiple(matches_dict)
