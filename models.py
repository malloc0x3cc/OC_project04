from tinydb import TinyDB


class Player():
	instances = []
	def __init__(self, firstname, lastname, birthdate, gender, rank) -> None:
		self.firstname = firstname
		self.lastname = lastname
		self.birthdate = birthdate
		self.gender = gender
		self.rank = rank
		self.__class__.instances.append(self)

	def updateRank(self, new_rank):
		self.rank = new_rank

class Tournament():
	def __init__(self, name, location, description, time_control, date, nb_of_rounds) -> None:
		self.name = name
		self.location = location
		self.description = description
		self.time_control = time_control
		self.date = date
		self.nb_of_rounds = nb_of_rounds
		self.player_list = []
		self.round_list = []

	def addPlayersToList(self, player):
		self.player_list.append(player)

	def addRoundToList(self, round):
		self.round_list.append(round)

class Round():
	def __init__(self, name, start_date, end_date) -> None:
		self.name = name
		self.start_date = start_date
		self.end_date = end_date
