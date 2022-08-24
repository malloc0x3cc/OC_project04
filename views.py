from models import *
from controllers import *


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

# Others
def printMainMenu(t, p, r, m):
	choice = int(input("-- Chess Manager --\n1. Manage tournament\n2. Manage players\n3. Manage rounds\n4. Manage matches\n"))

	if choice == 1:
		choice = int(input("-- Tournament --\n1. Print tournament infos\n"))
		if choice == 1:
			printTournamentInfos(t)

	if choice == 2:
		choice = int(input("-- Player --\n1. Print players infos\n"))
		if choice == 1:
			printPlayerInfos(p)

	if choice == 3:
		choice = int(input("-- Rounds --\n1. Print rounds infos\n"))
		if choice == 1:
			printRoundsInfos(r)

	if choice == 4:
		choice = int(input("-- Matches --\n1. Print matches infos\n"))
		if choice == 1:
			printMatchInfos(m)
	# TODO: Switch case
