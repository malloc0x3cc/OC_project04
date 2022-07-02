class Player():
	instances = []
	def __init__(self, firstname="n/a", lastname="n/a", gender="n/a", rank="n/a") -> None:
		self.firstname = firstname
		self.lastname = lastname
		self.gender = gender
		self.rank = rank
		self.__class__.instances.append(self)

	def updateRank(self):
		pass

class Tournament():
	def __init__(self, name="n/a", location="n/a", start_date="n/a", end_date="n/a") -> None:
		self.name = name
		self.start_date = start_date
		self.end_date = end_date

	def playerList(self):
		for p in Player.instances:
			print(vars(p))

class Match():
	def __init__(self, name="n/a", start_date="n/a", end_date="n/a") -> None:
		self.name = name
		self.start_date = start_date
		self.end_date = end_date

class Round():
	def __init__(self, number="n/a", start_date="n/a", end_date="n/a") -> None:
		self.name = name
		self.start_date = start_date
		self.end_date = end_date

if __name__ == "__main__":
	p1 = Player(firstname="John", lastname="Doe", gender="Male")
	p2 = Player(firstname="Jane", lastname="Doe", gender="Female")
	t = Tournament()
	t.playerList()

