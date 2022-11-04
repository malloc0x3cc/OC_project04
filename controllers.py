import math
import datetime
import main
import models


# Players
def add_player():
    player = models.Player(
        firstname=input("First name: "),
        lastname=input("Last name: "),
        elo=int(input("ELO: "))
    )
    main.playersTable.insert(player.__dict__)


# Tournaments
def create_tournament():
    # TODO: Input date (blank for datetime now)
    tournament = models.Tournament(
        name=input("Name: "),
        location=input("Location: "),
        date=str(datetime.datetime.now())
    )
    main.tournamentTable.insert(tournament.__dict__)


def swiss(player_list):
    # Bubble sort
    swap = True
    length = len(player_list) - 1
    while swap:
        i = 0
        swap = False
        while i < length:
            if player_list[i]['elo'] > player_list[i + 1]['elo']:
                buffer = player_list[i]
                player_list[i] = player_list[i + 1]
                player_list[i + 1] = buffer
                swap = True
            i += 1
        length -= 1

    # Pairing
    i = 0
    pairs = []
    while i < (len(player_list) - 1):
        pairs.append([player_list[i], player_list[i + 1]])
        i += 2

    return pairs


def start_tournament():
    rounds = []
    players = [p for p in main.playersTable]
    # NOTE: logarithm base 2 to figure the amount of rounds.
    for n in range(math.ceil(math.log2(len(main.playersTable)))):
        rounds.append(
            models.Round(
                nb=n + 1,
                start_date=str(datetime.datetime.now()),
                end_date=str(datetime.datetime.now())
                + str(datetime.timedelta(hours=1))
            )
        )
        print(f"-- Round {rounds[-1].nb} --\n{players}")

        matches = [models.Match(paired_players=_) for _ in swiss(players)]
        players = []

        for match in matches:
            for p in enumerate(match.paired_players):
                print(f"{p[0]}: {p[1]['firstname']} {p[1]['lastname']}")
            match.winner = match.paired_players[int(input("winner: "))]

            players.append(match.winner)
            main.matchesTable.insert(match.__dict__)

        print(f"Winners for Round {rounds[-1].nb}:")
        for player in players:
            print(f"{player['firstname']} {player['lastname']}")

    for round in rounds:
        main.roundsTable.insert(round.__dict__)
