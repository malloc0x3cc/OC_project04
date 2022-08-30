import datetime
import random
from tinydb import TinyDB
from faker import Faker
from controllers import swiss
from views import *


if __name__ == "__main__":
    database_file = "db.json"
    open(database_file, 'w').close()
    # TODO: Check if DB already exists
    db = TinyDB(database_file, sort_keys=True, indent=4)
    db.clear_cache()
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
            elo_rank=random.randint(1200, 1400)
        ) for _ in range(2)
    ]
    players_dict = []
    for _ in players:
        players_dict.append(_.__dict__)
    playersTable.insert_multiple(players_dict)

    print("-- Tournament --")
    tournament = Tournament(
        name=input("Name: "),
        location=input("Location: "),
        description=input("Description (optional): "),
        date=str(datetime.datetime.now())
    )
    tournamentTable.insert(tournament.__dict__)

    print("-- Rounds --")
    for n in range(tournament.nb_of_rounds):
        rounds.append(
            Round(
                n + 1,
                str(datetime.datetime.now()),
                str(datetime.datetime.now()) + str(datetime.timedelta(hours=1))
            )
        )
        print(f"Round {rounds[-1].nb}")
        print("-- Matches --")
        matches = [
            Match(paired_players_ids=_) for _ in swiss(players)
        ]
        matches_dict = []

        print(matches)

        for _ in matches:
            print(_.paired_players_ids)
            _.end(int(input("winner: ")))
            for p in players:
                if _.winner == p.id:
                    players.remove(p)
            matches_dict.append(_.__dict__)
            matchesTable.insert_multiple(matches_dict)

    rounds_dict = []
    for _ in rounds:
        rounds_dict.append(_.__dict__)
    roundsTable.insert_multiple(rounds_dict)
