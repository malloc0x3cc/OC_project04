class Player:
    def __init__(self, firstname, lastname, elo):
        self.firstname = firstname
        self.lastname = lastname
        self.elo = elo

    def update_rank(self, new_rank):
        self.elo = new_rank


class Tournament:
    def __init__(self, name, location, date) -> None:
        self.name = name
        self.location = location
        self.date = date
        self.nb_of_rounds = 0


class Round:
    def __init__(self, nb, start_date, end_date) -> None:
        self.nb = nb
        self.start_date = start_date
        self.end_date = end_date


class Match:
    def __init__(self, paired_players) -> None:
        self.paired_players = paired_players
        self.winner = None
