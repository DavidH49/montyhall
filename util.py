from numpy import random as rn


def get_money_door(doors: list) -> int:
    for i in range(0, len(doors)):
        if doors[i] == "money":
            return i


# Possibly horrible way of finding a door, but functional
def get_open_door(da: int, db: int) -> int:
    rnd = da
    while rnd == da or rnd == db:
        rnd = rn.randint(3)
    
    return rnd