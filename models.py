import math


class Player():
	instances = []
	def __init__(self, firstname, lastname, birthdate, gender, elo_rank) -> None:
		self.firstname = firstname
		self.lastname = lastname
		self.birthdate = birthdate
		self.gender = gender
		self.elo_rank = elo_rank
		self.__class__.instances.append(self)

	# FIXME: Implement the actual math for ELO ranking: https://fr.wikipedia.org/wiki/Classement_Elo
	def updateRank(self, new_rank):
		self.elo_rank = new_rank

class Tournament():
	def __init__(self, name, location, description, date) -> None:
		self.name = name
		self.location = location
		self.description = description
		self.date = date
		# NOTE: Because a chess game is 2 players, use logarithm base 2 to figure the amount of rounds to determine a single winner.
		self.nb_of_rounds = math.ceil(math.log2(len(Player.instances)))
		self.round_list = []

	def addRoundToList(self, round):
		self.round_list.append(round)

class Round():
	def __init__(self, nb, start_date, end_date) -> None:
		self.nb = nb
		self.start_date = start_date
		self.end_date = end_date

class Match():
	def __init__(self, pair_of_players) -> None:
		self.players = pair_of_players
		self.winner = None

	def end(self, winner=None):
		self.winner = winner
