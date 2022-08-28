import datetime
import random
from tinydb import TinyDB
from faker import Faker
from controllers import swiss
from views import *


if __name__ == "__main__":
    # TODO: Check if DB already exists
    db = TinyDB("db.json", sort_keys=True, indent=4)
    tournamentTable = db.table("Tournament")
    playersTable = db.table("Players")
    roundsTable = db.table("Rounds")
    matchesTable = db.table("Matches")

    rounds = matches = []

    # Menu
    print("-- Players --")
    players = [
        Player(
            player_id=_,
            firstname=Faker().first_name(),
            lastname=Faker().last_name(),
            # gender=random.choice(["M", "F"]),
            birthdate=str(Faker().date_of_birth()),
            elo_rank=random.randint(1200, 1400)) for _ in range(8)
    ]
    print_player_list()

    print("-- Tournament --")
    tournament = Tournament(
        name=input("Name: "),
        location=input("Location: "),
        description=input("Description: "),
        date=str(datetime.datetime.now())
    )
    print_tournament_infos(tournament)

    print("-- Rounds --")
    for n in range(tournament.nb_of_rounds):
        rounds.append(
            Round(
                n + 1,
                str(datetime.datetime.now()),
                str(datetime.datetime.now()) + str(datetime.timedelta(hours=1))
            )
        )
        print("-- Matches --")
        matches = [Match(paired_players_ids=[_]) for _ in swiss(players)]

    # Serialization
    players_dict = []
    rounds_dict = []
    matches_dict = []

    for _ in players:
        players_dict.append(_.__dict__)
    for _ in rounds:
        rounds_dict.append(_.__dict__)
    for _ in matches:
        matches_dict.append(_.__dict__)

    # db insert
    tournamentTable.insert(tournament.__dict__)
    playersTable.insert_multiple(players_dict)
    roundsTable.insert_multiple(rounds_dict)
    matchesTable.insert_multiple(matches_dict)
