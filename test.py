from models import *
from views import *
from controllers import *
from faker import Faker
import random
import datetime
import math


if __name__ == "__main__":
	players = [ Player(firstname=Faker().first_name(), lastname=Faker().last_name(), gender=random.choice(["M", "F"]), birthdate=Faker().date_of_birth(), elo_rank=random.randint(1400, 2400)) for p in range(16) ]
	tournament = Tournament(name="Unreal Tournament", players=players, location="Cupertino, CA", description="A test tournament", time_control=0, date=datetime.datetime.now())

	for p in swiss(tournament.players):
		print(f"{p[0].firstname} {p[0].lastname} (ELO: {p[0].elo_rank}) VS. {p[1].firstname} {p[1].lastname} (ELO: {p[1].elo_rank})")

	print(f"Number of rounds: {tournament.nb_of_rounds}")
	print(tournament.date)
	# printTournamentInfos(tournament)
	# printPlayerInfos(players[0])
	# printMatchInfos(players[0])
	# printRoundInfos(players[0])
