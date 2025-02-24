import matplotlib.pyplot as plt
import numpy as np
from numpy import random as rn
from icecream import ic

from util import *


def game(door: int, switch: bool) -> bool:
    doors = np.array(["goat", "goat", "money"])
    rn.shuffle(doors)

    # Sets all the door indices
    door_user = door
    door_money = get_money_door(doors)
    door_open = get_open_door(door_user, door_money)
    door_switch = get_open_door(door_user, door_open)

    # Switches the user's door if they choose so
    if switch:
        door_user = door_switch

    # Returns True if the user's door is the money door
    return door_user == door_money


def run_game(switch: bool, iter: int, door: int) -> int:
    outcomes = []

    # Plays the game 'iter' times
    for i in range(iter):
        out = game(door, switch)
        outcomes.append(out)
    
    # Filters the array to get the total amount of wins
    filter_outcomes = []
    for ob in outcomes:
        if ob:
            filter_outcomes.append(True)

    # Returns the total amount of wins
    return len(filter_outcomes)


def main():
    ITER = 10000
    
    # Prepares lists for both cases
    li_switch = []
    li_noswitch = []

    # Plays the game many times
    for i in range(3):
        # Always switches
        out_sw = run_game(True, ITER, i)
        # Never switches
        out_nos = run_game(False, ITER, i)

        # Appends the outcomes to the prepared lists
        li_switch.append(out_sw)
        li_noswitch.append(out_nos)
    
    li_labels = np.array([0, 1, 2])

    # Plot Bars
    plt.bar(li_labels, li_switch)
    plt.bar(li_labels, li_noswitch)

    # Plot Settings
    plt.ylim((0, ITER))
    plt.ylabel('N Wins')
    plt.xlabel('Door Chosen')
    plt.legend(["Switched", "No Switch"])

    plt.show()
    
if __name__ == "__main__":
    main()