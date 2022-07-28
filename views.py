from models import *


# TODO: print infos about players
# TODO: print infos about tournaments
# TODO: print infos about matches
# TODO: print infos about rounds

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

# Matches
def printMatchInfos(match):
		print(vars(match))

# Rounds
def printRoundsInfos(round):
		print(vars(round))

