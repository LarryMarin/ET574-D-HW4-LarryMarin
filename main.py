# Name: Larry Marin
# QCC ID: 23656183
# ET574 HW4: Dice Game Simulator

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        #returns a random integer between 1 and the number of sides
        return random.randint(1, self.sides)
