from models import *
from views import *
from controllers import *
from faker import Faker
import random
import datetime


if __name__ == "__main__":
	players = []
	for p in range(26):
		players.append(Player(firstname=Faker().first_name(), lastname=Faker().last_name(), gender=random.choice(["M", "F"]), birthdate=Faker().date_of_birth(), elo_rank=random.randint(1400, 2400)))

	t = Tournament(name="Unreal Tournament", location="Cupertino, CA", description="A test tournament", time_control=0, date=datetime.date(2012, 12, 21), nb_of_rounds=4)
	t.addPlayersToList(players)

	for p in swiss(t.player_list):
		print(f"{p[0].firstname} {p[0].lastname} (ELO: {p[0].elo_rank}) VS. {p[1].firstname} {p[1].lastname} (ELO: {p[1].elo_rank})")

	# printTournamentInfos(t)
	# printPlayerInfos(players[0])
	# printMatchInfos(player[0])
	# printRoundInfos(player[0])
