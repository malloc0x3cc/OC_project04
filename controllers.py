from datetime import datetime
from models import Round


def swiss(tournamentPlayerlist):
	# Bubblesort
	swap = True
	length = len(tournamentPlayerlist) - 1
	while (swap):
		i = 0
		swap = False
		while (i < length):
			if (tournamentPlayerlist[i].elo_rank > tournamentPlayerlist[i + 1].elo_rank):
				buffer = tournamentPlayerlist[i]
				tournamentPlayerlist[i] = tournamentPlayerlist[i + 1]
				tournamentPlayerlist[i + 1] = buffer
				swap = True
			i += 1
		length -= 1

	# Pairing
	i = 0
	pairs = []
	while (i < len(tournamentPlayerlist) - 1):
		pairs.append([tournamentPlayerlist[i], tournamentPlayerlist[i + 1]])
		i += 2

	print("Players matched !")
	return(pairs)

# Rounds
def createRound(nb):
	name = f"Round {nb + 1}"
	start_date = datetime.now()
	end_date = ""

	r = Round(name, start_date, end_date)
	return r
