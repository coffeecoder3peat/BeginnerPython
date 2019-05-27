import random

class Dice:
    """A simple attempt to creat a class for dice."""

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))

normal_dice = Dice()

for num in range(1, 11):
    normal_dice.roll_die()