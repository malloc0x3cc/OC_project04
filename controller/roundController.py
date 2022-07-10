from datetime import datetime
from ..models import Round


def createRound(nb):
	name = f"Round {nb + 1}"
	start_date = datetime.now()
	end_date = ""

	r = Round(name, start_date, end_date)
	return r
