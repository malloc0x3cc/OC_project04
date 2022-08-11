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

	players = [ Player(firstname=Faker().first_name(), lastname=Faker().last_name(), gender=random.choice(["M", "F"]), birthdate=str(Faker().date_of_birth()), elo_rank=0) for p in range(2) ]
	tournament = Tournament(name="Unreal Tournament", location="Cupertino, CA", description="A test tournament", date=str(datetime.datetime.now()))

	# Ranking round pairing (all ranks are zero)
	for p in swiss(players):
		print(f"{p[0].firstname} {p[0].lastname} (ELO: {p[0].elo_rank}) VS. {p[1].firstname} {p[1].lastname} (ELO: {p[1].elo_rank})")

	# TODO: Replace random test values with a ranking round, give new elo rank
	for p in players:
		p.elo_rank = random.randint(1200, 1400)
		print(p.elo_rank)

	for p in swiss(players):
		print(f"{p[0].firstname} {p[0].lastname} (ELO: {p[0].elo_rank}) VS. {p[1].firstname} {p[1].lastname} (ELO: {p[1].elo_rank})")

	rounds = [ Round(n + 1, str(datetime.datetime.now()), str(datetime.datetime.now()) + str(datetime.timedelta(hours=1))) for n in range(tournament.nb_of_rounds) ]

	print(f"Number of rounds: {len(rounds)}")

	# Objects to dictionaries
	players_dict = []
	rounds_dict = []
	matches_dict = []

	for _ in players:
		players_dict.append(_.__dict__)
	for _ in rounds:
		rounds_dict.append(_.__dict__)

	# db insert
	tournamentTable.insert(tournament.__dict__)
	playersTable.insert_multiple(players_dict)
	roundsTable.insert_multiple(rounds_dict)

	# printTournamentInfos(tournament)
	# printPlayerInfos(players[0])
	# printMatchInfos(players[0])
	# printRoundInfos(players[0])
