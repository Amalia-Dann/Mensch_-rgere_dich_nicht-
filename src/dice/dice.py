import random
class Dice:
    # initializing dice
    def __init__(self):
        self.number = self.roll_dice()
    def roll_dice(self):
        rand = random.randint(1,6)
        self.number = rand # saving the number of the dice
        return rand # returning the number of the dice