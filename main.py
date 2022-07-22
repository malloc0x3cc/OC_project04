from models import *
from views import *
from controllers import *
import datetime


# NOTE: test app
# TODO: write tests

if __name__ == "__main__":
	p1 = Player(firstname="John", lastname="Doe", gender="Male", birthdate=datetime.date(1998, 3, 27), elo_rank=1800)
	p2 = Player(firstname="Jane", lastname="Doe", gender="Female", birthdate=datetime.date(2002, 5, 9), elo_rank=1900)
	p3 = Player(firstname="Jane", lastname="Doe", gender="Female", birthdate=datetime.date(2002, 5, 9), elo_rank=1550)
	p4 = Player(firstname="Jane", lastname="Doe", gender="Female", birthdate=datetime.date(2002, 5, 9), elo_rank=1500)
	t = Tournament(name="Unreal Tournament", location="Cupertino", description="A test tournament", time_control=0, date=datetime.date(2012, 12, 21), nb_of_rounds=4)
	t.addPlayersToList([p1, p2, p3, p4])

	for p in swiss(t.player_list):
		print(f"{p[0].elo_rank}, {p[1].elo_rank}")
