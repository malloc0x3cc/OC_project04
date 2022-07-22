from datetime import datetime
from models import Round


# TODO: Swiss algorithm:
	# [ ]: BubbleSort/InsertionSort by ELO ranks ( Time: O(n), Space: O(1) )
	# [ ]: pair players by closest ELO

# Rounds
def createRound(nb):
	name = f"Round {nb + 1}"
	start_date = datetime.now()
	end_date = ""

	r = Round(name, start_date, end_date)
	return r
