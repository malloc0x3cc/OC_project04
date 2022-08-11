from datetime import datetime
from models import Round


def swiss(playerList):
	# Bubblesort
	swap = True
	length = len(playerList) - 1
	while (swap):
		i = 0
		swap = False
		while (i < length):
			if (playerList[i].elo_rank > playerList[i + 1].elo_rank):
				buffer = playerList[i]
				playerList[i] = playerList[i + 1]
				playerList[i + 1] = buffer
				swap = True
			i += 1
		length -= 1

	# Pairing
	i = 0
	pairs = []
	while (i < len(playerList) - 1):
		pairs.append([playerList[i], playerList[i + 1]])
		i += 2

	return(pairs)

# Rounds
def createRound(nb):
	nb = f"Round {nb + 1}"
	start_date = datetime.now()
	end_date = ""

	r = Round(nb, start_date, end_date)
	return r
