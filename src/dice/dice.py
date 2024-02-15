import random
class Dice:
    #Class Dice represents a six-sided dice used in games. It includes a method for initializing the dice and rolling it
    # to generate a random number between 1 and 6, which is then stored and returned.

    # initializing dice
    def __init__(self):
        self.number = self.rollDice()
    def rollDice(self):
        diceNum = random.randint(1,6)
        self.number = diceNum # saving the number of the dice
        return diceNum # returning the number of the dice