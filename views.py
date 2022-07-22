from models import Player


# TODO: print infos about players
# TODO: print infos about tournaments
# TODO: print infos about matches
# TODO: print infos about rounds

# Players
def printPlayerList():
		l = []
		for p in Player.instances:
			l.append(vars(p))
		print(l)
