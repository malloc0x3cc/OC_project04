from datetime import datetime
from models import Round


def swiss(player_list):
    # Bubble sort
    swap = True
    length = len(player_list) - 1
    while swap:
        i = 0
        swap = False
        while i < length:
            if player_list[i].elo_rank > player_list[i + 1].elo_rank:
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
        pairs.append([player_list[i].id, player_list[i + 1].id])
        i += 2

    return pairs


# Rounds
def create_round(nb):
    nb = f"Round {nb + 1}"
    start_date = datetime.now()
    end_date = ""

    r = Round(nb, start_date, end_date)
    return r
