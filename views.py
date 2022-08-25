from models import *
from controllers import *
# import datetime
# import main


# Players
def printPlayerInfos(player):
		print(vars(player))

def printPlayerList():
		l = []
		for p in Player.instances:
			l.append(vars(p))
		print(l)

# Tournaments
def printTournamentInfos(tournament):
		print(vars(tournament))

# def createTournament(tournament):
# 	name = str(input("Name: "))
# 	loc = str(input("Location: "))
# 	desc = str(input("Description: "))
# 	date = str(datetime.datetime.now())
# 	tournament = Tournament(name=name, location=loc, description=desc, date=date)

# Matches
def printMatchInfos(match):
		print(vars(match))

# Rounds
def printRoundsInfos(round):
		print(vars(round))
