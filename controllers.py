from datetime import datetime
from models import Round


def bubbleSort(playerlist):
	swap = True

	while (swap):
		i = 0
		swap = False
		while (i < len(playerlist) - 1):
			if (playerlist[i].elo_rank > playerlist[i + 1].elo_rank):
				buffer = playerlist[i]
				playerlist[i] = playerlist[i + 1]
				playerlist[i + 1] = buffer
				swap = True
			print(playerlist)
			i += 1

def swiss(playerlist):
	# TODO: Swiss algorithm:
		# [x]: Sort all players by ELO ranks
		# [ ]: pair players by closest ELO
	bubbleSort(playerlist)

# Rounds
def createRound(nb):
	name = f"Round {nb + 1}"
	start_date = datetime.now()
	end_date = ""

	r = Round(name, start_date, end_date)
	return r
