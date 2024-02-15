class Player:
    # Class Player represents a player in the game, characterized by a name and color. It contains methods for initializing the player,
    # setting and retrieving the player's name and color, managing a list of figures on target fields, determining if the player has won
    # by having all figures on target fields.

    # initializing the player
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.figureList = []

    # setting the name
    def setName(self, newName):
        self.name = newName

    # getting and returning the name
    def getName(self):
        return self.name

    def setColor(self, newColor):
        self.color = newColor

    # getting and returning the color
    def getColor(self):
        return self.color

    # memorizing which figures are on the target-fields
    def setFinish(self):
        self.figureList.append(True)

    # returning the figureList
    def getFinish(self):
        return self.figureList

    # declaring the winner
    def winner(self):
        return self.figureList.count(True) == 4