from venv import create
from models import *
from views import *
from controllers import *
from faker import Faker
import random
import datetime


if __name__ == "__main__":
	players = [ Player(firstname=Faker().first_name(), lastname=Faker().last_name(), gender=random.choice(["M", "F"]), birthdate=Faker().date_of_birth(), elo_rank=0) for p in range(16) ]
	tournament = Tournament(name="Unreal Tournament", players=players, location="Cupertino, CA", description="A test tournament", date=datetime.datetime.now())

	# Ranking round pairing (all ranks are zero)
	for p in swiss(tournament.players):
		print(f"{p[0].firstname} {p[0].lastname} (ELO: {p[0].elo_rank}) VS. {p[1].firstname} {p[1].lastname} (ELO: {p[1].elo_rank})")

	# TODO: Replace random test values with a ranking round, give new elo rank
	for p in players:
		p.elo_rank = random.randint(1200, 1400)
		print(p.elo_rank)

	for p in swiss(tournament.players):
		print(f"{p[0].firstname} {p[0].lastname} (ELO: {p[0].elo_rank}) VS. {p[1].firstname} {p[1].lastname} (ELO: {p[1].elo_rank})")

	rounds = [ Round(n + 1, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(hours=1)) for n in range(tournament.nb_of_rounds) ]

	print(f"Number of rounds: {len(rounds)}")

	# printTournamentInfos(tournament)
	# printPlayerInfos(players[0])
	# printMatchInfos(players[0])
	# printRoundInfos(players[0])
