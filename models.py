import math


class Player:
	instances = []

	def __init__(self, player_id, firstname, lastname, birthdate, gender, elo_rank) -> None:
		self.id = player_id
		self.firstname = firstname
		self.lastname = lastname
		self.birthdate = birthdate
		self.gender = gender
		self.elo_rank = elo_rank
		self.__class__.instances.append(self)

	# FIXME: https://fr.wikipedia.org/wiki/Classement_Elo#Th%C3%A9orie_math%C3%A9matique
	def update_rank(self, new_rank):
		self.elo_rank = new_rank


class Tournament:
	round_list = []

	def __init__(self, name, location, description, date) -> None:
		self.name = name
		self.location = location
		self.description = description
		self.date = date
		# NOTE: logarithm base 2 to figure the amount of rounds to determine a single winner.
		self.nb_of_rounds = math.ceil(math.log2(len(Player.instances)))

	def add_round_to_list(self, chess_round):
		self.__class__.round_list.append(chess_round)


class Round:
	def __init__(self, nb, start_date, end_date) -> None:
		self.nb = nb
		self.start_date = start_date
		self.end_date = end_date


class Match:
	def __init__(self, paired_players_ids) -> None:
		self.paired_players_ids = paired_players_ids
		self.winner = None

	def end(self, winner=None):
		self.winner = winner
