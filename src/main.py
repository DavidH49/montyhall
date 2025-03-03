import matplotlib.pyplot as plt
from numpy import random as rn
from icecream import ic
import time


NDOOR = 3
ITERATIONS = 1000000


## Gets the one remaining door which doesn't contain money
def find_door(exa: int, exb: int) -> int:
    d = 0

    while d == exa or d == exb:
        d += 1
    
    return d


## Plays the game once with specified settings
def game(door_sel: int, switch: bool) -> bool:
    # Sets all the door indices
    door_money = rn.randint(NDOOR)
    door_open = find_door(door_sel, door_money)
    door_switch = find_door(door_sel, door_open)

    # Switches the user's door if they choose so
    if switch:
        door_sel = door_switch

    # Returns True if the user's door is the money door
    return door_sel == door_money


## Plays the game 'iter' times with specified settings
def run_game(switch: bool, iter: int, door: int) -> int:
    outcomes = []

    # Plays the game 'iter' times
    for i in range(iter):
        out = game(door, switch)
        outcomes.append(out)
    
    # Filters the array to get the total amount of wins
    filter_outcomes = filter(
        lambda ob: not not ob,
        outcomes
    )

    # Returns the total amount of wins
    return len(list(filter_outcomes))


## Main Function
def main():
    # Prepares lists for both cases
    li_switch = []
    li_noswitch = []

    t_start = time.process_time()

    # Plays the game many times
    for i in range(NDOOR):
        # Always switches
        out_sw = run_game(True, ITERATIONS, i)
        # Never switches
        out_nos = run_game(False, ITERATIONS, i)

        # Appends the outcomes to the prepared lists
        li_switch.append(out_sw)
        li_noswitch.append(out_nos)
    
    t_end = time.process_time()
    t_elapsed = t_end - t_start
    print("Processing time:", t_elapsed, "s")

    li_labels = [0, 1, 2]

    # Plot Bars
    plt.bar(li_labels, li_switch)
    plt.bar(li_labels, li_noswitch)

    # Plot Settings
    plt.ylim((0, ITERATIONS))
    plt.title("")
    plt.ylabel("N Wins")
    plt.xlabel("Door Chosen")
    plt.legend(["Always Switch", "Never Switch"])

    plt.show()
    
if __name__ == "__main__":
    main()