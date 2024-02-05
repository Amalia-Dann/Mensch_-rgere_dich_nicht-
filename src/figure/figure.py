


class Figure:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.counter = 0

    def movedFields(self, dice_num):
        self.counter += dice_num
        return self.counter

    def setPosition(self, currentPosition):
        self.position = currentPosition
    def getPosition(self):
        return self.position
    def finish(self):
        if self.counter >=41 and self.position <= 44:
            return True
        else:
            return False