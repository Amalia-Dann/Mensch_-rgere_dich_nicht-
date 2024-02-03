class Figure:

    def __init__(self, position, color):
        self.postion = position
        self.color = color

    def makeMove(self, dice_num):
        self.position += dice_num
        return self.postion

    def finish(self):
        if self.postion >=41 and self.postion <= 44:
            return True
        else:
            return False