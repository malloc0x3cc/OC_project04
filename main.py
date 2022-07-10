from models import *
from views import *
import datetime


if __name__ == "__main__":
	p1 = Player(firstname="John", lastname="Doe", gender="Male", birthdate=datetime.date(1998, 3, 27), rank=1)
	p2 = Player(firstname="Jane", lastname="Doe", gender="Female", birthdate=datetime.date(2002, 5, 9), rank=2)
	t = Tournament(name="Unreal Tournament", location="Cupertino", description="A test tournament", time_control=0, date=datetime.date(2012, 12, 21), nb_of_rounds=4)
	printPlayerList()
