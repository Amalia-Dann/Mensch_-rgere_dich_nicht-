class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.figure_list = []

    def setName(self, newName):
        self.name = newName
    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def setFinish(self):
        self.figure_list.append(True)

    def getFinish(self):
        return self.figure_list

    def winner(self):
        return self.figure_list.count(True) == 4