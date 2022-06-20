class Player():
	def __init__(self, name) -> None:
		self.name = name

	def getName(self):
		return self.name

class Tournament():
	def __init__(self, player_list) -> None:
		self.player_list = player_list

	def listPlayers(self):
		for player in self.player_list:
			print(player.name)

class Match(Tournament):
	def __init__(self) -> None:
		pass

class Round(Match):
	def __init__(self) -> None:
		pass

if __name__ == "__main__":
	test = []
	test_tournament = Tournament(test)
	test.append(Player(name="Mac"))
	test.append(Player(name="Rose"))

	test_tournament.listPlayers()
