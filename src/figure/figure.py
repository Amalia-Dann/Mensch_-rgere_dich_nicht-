class Figure:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.counter = 0
        self.moved = True

    def moved(self):
        return self.moved

    def setPosition(self, currentPosition):
        self.position = currentPosition

    # gets the current position of the figure
    def getPosition(self):
        return self.position

    # checks whether the figure has entered the target-fields
    def finish(self):
        if self.counter >=41 and self.position <= 44:
            return True
        else:
            return False # if the figure overshoots the target, it must remain stationary