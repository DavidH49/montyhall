from numpy import random as rn


def get_money_door(doors):
    for i in range(0, len(doors)):
        if doors[i] == "money":
            return i


def get_open_door(da, dm):
    rnd = da
    while rnd == da or rnd == dm:
        rnd = rn.randint(3)
    
    return rnd


def print_game_data(gd):
    print("Switch: ", gd["switch"])
    print("Door Selected: ", gd["door"])
    print(f"User won {gd["n_wins"]} / {gd["iter"]} times")
    print("-" * 30)