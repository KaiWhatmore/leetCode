from random import shuffle
from secrets import choice


def secret_santa(players):
    not_giving_anything_yet = players[:]
    not_receiving_anything_yet = players[:]

    result = []
    while len(not_giving_anything_yet) > 0:
        shuffle(not_giving_anything_yet)
        giver = not_giving_anything_yet[0]

        if giver in not_receiving_anything_yet:
            not_receiving_anything_yet.remove(giver)
            gift_receiver = choice(not_receiving_anything_yet)
            not_receiving_anything_yet.append(giver)
        else:
            gift_receiver = choice(not_receiving_anything_yet)

        not_giving_anything_yet.remove(giver)
        not_receiving_anything_yet.remove(gift_receiver)
        result.append([giver, gift_receiver])

    return result


players = ["bob", "sam", "kai", "edd", "jon", "bam bam"]
print(secret_santa(players))
