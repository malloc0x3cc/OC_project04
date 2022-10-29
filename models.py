class Player:
    def __init__(self, firstname, lastname, elo_rank):
        self.firstname = firstname
        self.lastname = lastname
        self.elo_rank = elo_rank

    def update_rank(self, new_rank):
        self.elo_rank = new_rank


class Tournament:
    round_list = []

    def __init__(self, name, location, date) -> None:
        self.name = name
        self.location = location
        self.date = date
        self.nb_of_rounds = 0

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
