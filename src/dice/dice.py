import random
class Dice:
    # initializing dice
    def __init__(self):
        self.number = self.rollDice()
    def rollDice(self):
        diceNum = random.randint(1,6)
        self.number = diceNum # saving the number of the dice
        return diceNum # returning the number of the dice