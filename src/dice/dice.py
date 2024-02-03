import random
class Dice:
    def __init__(self):
        self.number = self.roll_dice()
    def roll_dice(self):
        rand = random.randint(1,6)
        self.number = rand
        return rand


#dice = Dice()
#dice.roll_dice()
#print(dice.imageNumOfPoints())