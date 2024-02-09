class Player:
    # initializing the player
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.figure_list = []

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
        self.figure_list.append(True)

    # returning the figure-list
    def getFinish(self):
        return self.figure_list

    # declaring the winner
    def winner(self):
        return self.figure_list.count(True) == 4