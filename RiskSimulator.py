import numpy as np


def three_dice_two_dice():
    counter = 0
    player1 = 0
    player2 = 0
    new_num = 0
    player1_score, player2_score = 0, 0
    while counter < 1000000:
        for number in range(3):
            new_num = np.random.randint(1, 7)
            if new_num > player1:
                player1 = new_num
        for number in range(2):
            new_num = np.random.randint(1, 7)
            if new_num > player1:
                player2 = new_num
        if player1 > player2:
            player1_score += 1
        else:
            player2_score += 1
        counter += 1
        player1 = 0
        player2 = 0
    print(player1_score/counter)


def until_failure(attacker_amt, defender_amt, print_results):
    while attacker_amt > 1 and defender_amt > 0:
        attacker_roll = []
        defender_roll = []
        # create rolls based on how many each player has left
        for i in range(attacker_amt - 1):
            if len(attacker_roll) < 3:
                attacker_roll.append(np.random.randint(1, 7))
        for i in range(defender_amt):
            if len(defender_roll) < 2:
                defender_roll.append(np.random.randint(1, 7))

        # remove pieces based on rolls
        if max(attacker_roll) > max(defender_roll):
            defender_amt -= 1
        else:
            attacker_amt -= 1
        attacker_roll.remove(max(attacker_roll))
        defender_roll.remove(max(defender_roll))
        if len(attacker_roll) > 0 and len(defender_roll) > 0:
            if max(attacker_roll) > max(defender_roll):
                defender_amt -= 1
            else:
                attacker_amt -= 1
        if print_results:
            print(attacker_amt)
            print(defender_amt)
    if attacker_amt > 1:
        if print_results:
            print("The attacker won and has", attacker_amt, "units left")
        return 1
    else:
        if print_results:
            print("The defender won and has", defender_amt, "units left")
        return 0


counter = 0
percent_chance = 0
while counter < 100000:
    percent_chance += until_failure(8, 5, print_results=False)
    counter += 1
percent_chance *= 100
print("Attacker has a", percent_chance/counter, "% chance of winning")
