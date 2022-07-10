from models import Player


def printPlayerList():
		l = []
		for p in Player.instances:
			l.append(vars(p))
		print(l)
