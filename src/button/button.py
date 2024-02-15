class Button():
    # initializing the buttons
    def __init__(self, image, pos, textInput, font, baseColor, hoveringColor):
        self.image = image
        self.xPos = pos[0]
        self.yPos = pos[1]
        self.currentPosition = [self.xPos, self.yPos]
        self.font = font
        self.baseColor, self.hoveringColor = baseColor, hoveringColor
        self.textInput = textInput
        self.text = self.font.render(self.textInput, True, self.baseColor)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.xPos, self.yPos))
        self.textRect = self.text.get_rect(center=(self.xPos, self.yPos))

    # puts button on the screen
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)

    # updates the positon of the button on the screen
    def updatePosition(self, newPos):
        self.xPos = newPos[0]
        self.yPos = newPos[1]

        self.rect.center = (self.xPos, self.yPos)
        self.textRect.center = (self.xPos, self.yPos)

    # gets the current position of the button
    def getPosition(self):
        return self.currentPosition

    # checks whether the mouse is on the button
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    # changes the color to the hovering-color if the mouse is on the button
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.textInput, True, self.hoveringColor)
        else:
            self.text = self.font.render(self.textInput, True, self.baseColor)