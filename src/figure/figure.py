class Figure:
    #Class Figure represents a game figure with position and color attributes. It includes methods for initializing the figure's position and color,
    #resetting its movement counter, updating the movement counter based on dice rolls, getting the current position and movement counter, setting the
    #position of the figure, and determining if the figure has reached the target fields.

    # initializing the figure
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.counter = -6   #with a six you come out of the house

    # resetting the counter to 0
    def resetMoved(self):
        self.counter = -6

    # add the current number of dice to the counter
    def setMoved(self, dice_num):
        self.counter += dice_num

    # returns the number of the counter
    def getMoved(self):
        return self.counter

    # sets the position of the current figure
    def setPosition(self, currentPosition):
        self.position = currentPosition

    # gets the current position of the figure
    def getPosition(self):
        return self.position

    # checks whether the figure has entered the target-fields
    def finish(self):
        if self.counter >=40 and self.counter <= 43:
            return True
        else:
            return False # if the figure overshoots the target, it must remain stationary