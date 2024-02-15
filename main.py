import pygame as pg
import sys
from src.button.button import Button
from src.dice.dice import Dice
from src.figure.figure import Figure
from src.gamefield.gameField import GameField
from src.player.player import Player

pg.init()

# Start screen:
screen = pg.display.set_mode((1280,720))
pg.display.set_caption("Don't get ANGRY!")

clock = pg.time.Clock()

# colors
white = (255, 255, 255)
black = (0, 0, 0)

#create Object
playground = GameField()
fieldList = playground.fields()
hauserList = playground.houses()
zielfelderList = playground.finishFields()

playerPosition = { }
savedNameRects = []

def getFont(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("assets/font.ttf", size)

# fonts
font = getFont(10)
inputFont = getFont(15)

# This function scales an image while maintaining its aspect ratio.
def transformScaleKeepRatio(image, size):
    iwidth, iheight = image.get_size()
    scale = min(size[0] / iwidth, size[1] / iheight)
    #scale = max(size[0] / iwidth, size[1] / iheight)
    newSize = (round(iwidth * scale), round(iheight * scale))
    scaledImage = pg.transform.smoothscale(image, newSize)
    imageRect = scaledImage.get_rect(center = (size[0] // 2, size[1] // 2))
    return scaledImage, imageRect # Return the scaled image and the centered rectangle.

# This function scales an image to a new width and height.
def scaleImage(image, newWidth, newHeight):
    originalWidth, originalHeight = image.get_size()  # Get the original width and height of the image.
    scaledImage = pg.transform.scale(image, (newWidth, newHeight))     # Scale the image to the new width and height.
    # Return the scaled image.
    return scaledImage

# This function represents the main menu of the game.
def mainMenu():
    # Set the window caption.
    pg.display.set_caption("Don't get ANGRY!")

    # Load and scale the background image.
    BG = scaleImage(pg.image.load("assets/mainscreen.png"), 1280, 720)

    # Main menu loop
    while True:
        # Display the background on the screen.
        screen.blit(BG, (0, 0))  # Background on the screen

        # Get the current mouse position.
        menuMousePos = pg.mouse.get_pos()

        # Render the main menu title text.
        menuText = getFont(75).render("Don't get ANGRY!", True, "#856c4a")  # Textfield
        menuRect = menuText.get_rect(center=(640, 100))

        # Create buttons for play, rules, and quit.
        playButton = Button(image=pg.image.load("assets/PlayRect.png"), pos=(340, 270),
                            textInput="PLAY", font=getFont(75), baseColor="White", hoveringColor="#fcce8d")
        rulesButton  = Button(image=scaleImage(pg.image.load("assets/PlayRect.png"), 430, 109), pos=(340, 420),
                              textInput="RULES", font=getFont(75), baseColor="White", hoveringColor="#fcce8d")
        quitButton = Button(image=pg.image.load("assets/PlayRect.png"), pos=(340, 570),
                            textInput="QUIT", font=getFont(75), baseColor="White", hoveringColor="#fcce8d")

        # Display the main menu title text.
        screen.blit(menuText, menuRect)

        # Update and render buttons.
        for button in [playButton, rulesButton , quitButton]:
            button.changeColor(menuMousePos)
            button.update(screen)

        # Event handling loop.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # Quit the game if the window is closed.
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # Check for button clicks and perform corresponding actions.
                if playButton.checkForInput(menuMousePos):
                    play()  # Run the play function
                if rulesButton .checkForInput(menuMousePos):
                    rules()  # Run the rules function
                if quitButton.checkForInput(menuMousePos):
                    pg.quit()
                    sys.exit()

        # Update the display.
        pg.display.update()

# This function represents the rules screen of the game.
def rules():
    while True:
        OptionsMousePos = pg.mouse.get_pos()  # Get the current mouse position.

        screen.fill("#fcce8d")  # Fill the screen with a background color.

        # Function to draw text on the screen.
        def drawText(text):
            # Set up the font and initial position for drawing text.
            font = getFont(12)
            yPos = 15
            xPos = 20

            # Iterate over each line of the provided text and render it onto the screen.
            for line in text.splitlines():
                renderedLine = font.render(line, 1, (0, 0, 0))
                screen.blit(renderedLine, (xPos, yPos))

                # Update the y-position for the next line.
                yPos += 21

        # Display the rules text.
        if __name__ == "__main__":
            textToDisplay = (
                "Your pieces always start in the starting circle and are moved in the direction of the arrow \n"
                "towards the finish. \n"
                "On your turn, you roll the dice and can move your figure according to the result of the dice, \n"
                "beginning with the starting figure. \n"
                "Then it is the next player's turn. \n\n"
                "During the course of the game, you may roll a number that could theoretically place you on a \n"
                "square that is already occupied. \n"
                "Place your piece on this square to beat your opponent. \n"
                "They will have to place it back in the starting circle and will be moved one step backwards. \n\n"
                "If one of you rolls a 6, he gets another roll and has to bring another piece from the starting \n"
                "circle into play and use the second free roll to \n"
                "place it further, according to the eyes. \n"
                "If, on the other hand, you roll a 5, for example, you must move another piece. \n"
                "If you roll a 6, but have already moved all 4 pieces, or have already partially reached the goal, \n"
                "you can move any piece 6 spaces further. \n"
                "He then has one more free roll. If you have no other piece on the square, you must roll a 6. \n"
                "If you fail to do so, you must discard the die. \n"
                "If you land on a square that already contains another piece, the other piece is knocked off the square.\n"
                "Once a piece has completely circled the outer cross, it moves onto the circles of its color \n"
                "to the finish line. \n"
                "To reach the goal, a number must be rolled that moves the piece to any square within the goal. \n"
                "If you roll a number above this, \n"
                "you must discard the die. \n\n"
                "Goal: \n"
                "The first player to get their 4 pieces to the finish line wins. \n"
                "The others can decide for themselves whether the game ends or whether they still want to play \n"
                "for the lower places")
            drawText(textToDisplay)

        # Create a button for returning to the main menu.
        RulesBack = Button(image=None, pos=(1200, 690),
                           textInput="BACK", font=getFont(20), baseColor="Black", hoveringColor="White")

        # Event handling loop.
        for event in pg.event.get():
            # Quit the game if the window is closed.
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # Check if the back button is clicked and return to the main menu if clicked.
                if RulesBack.checkForInput(OptionsMousePos):
                    mainMenu()

        # Update and render the back button.
        RulesBack.changeColor(OptionsMousePos)
        RulesBack.update(screen)

        pg.display.update() # Update the display.

# This function represents the game's main menu where players can enter their names and start the game.
def play():
    # Set the window title
    pg.display.set_caption("Don't get ANGRY!")

    # Define background color
    backgroundColor = "#fcce8d"

    # Load game field image and scale it to fit the screen
    gamefield = pg.image.load("assets/gamefield.png")
    gamefield, gamefieldRect = transformScaleKeepRatio(gamefield, screen.get_size())

    # Define buttons for going back to the main menu and starting the game
    PlayBack = Button(image=None, pos=(1165, 670),
                      textInput="BACK", font=getFont(30), baseColor="Black", hoveringColor="WHITE")

    gameActive = Button(image=None, pos=(135, 670), textInput="START", font=getFont(30),
                         baseColor="Black", hoveringColor="WHITE")

    # Text prompting the player to enter names
    promptText = ("Press Enter, to add a player")
    promptRect = pg.Rect(20, 50, 200, 40)

    # Input field parameters
    inputRect = pg.Rect(20, 100, 200, 40)
    inputText = ""
    cursorActive = False
    cursorTimer = 0  # Timer for cursor blink effect
    cursorSize = 2  # Size of the cursor

    # Saved player names
    maxPlayers = 4
    savedNameRects = [pg.Rect(20, 190 + i * 80, 200, 40) for i in range(maxPlayers)]
    savedNameTexts = [""] * maxPlayers

    # Variable for storing the background image
    image = None

    # Flag indicating whether the game is active
    activePlay = False

    while True:
        # Get the current mouse position
        playMousePos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Add player name when Enter is pressed
                    if not cursorActive:
                        cursorActive = True
                        promptText = "Enter player name"
                    else:
                        for i in range(len(savedNameTexts)):
                            if not savedNameTexts[i] and inputText:
                                savedNameTexts[i] = inputText
                                inputText = ""
                                cursorTimer = 0
                                if i == maxPlayers - 1:
                                    cursorActive = False
                                    promptText = "All players registered"
                                else:
                                    promptText = "Enter player name"
                                break
                elif cursorActive:
                    # Handle input when cursor is active
                    if event.key == pg.K_BACKSPACE:
                        inputText = inputText[:-1]
                    else:
                        inputText += event.unicode
            if event.type == pg.MOUSEBUTTONDOWN:
                # Check for button clicks
                if PlayBack.checkForInput(playMousePos):
                    mainMenu()
                if gameActive.checkForInput(playMousePos):
                    gameLoop(savedNameTexts)
            elif event.type == pg.VIDEORESIZE:
                # Resize the window and game field image
                window = pg.display.set_mode(event.size, pg.RESIZABLE)
                gamefield, gamefieldRect = transformScaleKeepRatio(gamefield, window.get_size())

        # Fill the screen with background color
        screen.fill(backgroundColor)
        # Draw the game field image
        screen.blit(gamefield, gamefieldRect)

        # Update and draw the back button
        PlayBack.changeColor(playMousePos)
        PlayBack.update(screen)

        # Update and draw the start button
        gameActive.changeColor(playMousePos)
        gameActive.update(screen)

        # Display prompt text
        promptSurface = font.render(promptText, True, black)
        screen.blit(promptSurface, (promptRect.x + 5, promptRect.y + 5))

        # Draw input field if active
        if cursorActive:
            pg.draw.rect(screen, white, inputRect)
            pg.draw.rect(screen, black, inputRect, 2)
            inputSurface = inputFont.render(inputText, True, black)
            screen.blit(inputSurface, (inputRect.x + 5, inputRect.y + 5))

            # Cursor blink effect
            if pg.time.get_ticks() % 1000 < 500:
                cursorHeight = inputSurface.get_height()
                cursorRect = pg.Rect(inputRect.x + 5 + inputSurface.get_width(), inputRect.y + 5, cursorSize,
                                      cursorHeight)
                pg.draw.rect(screen, black, cursorRect)

        # Display saved player names
        for i in range(len(savedNameTexts)):
            if savedNameTexts[i]:
                pg.draw.rect(screen, "#fcce8d", savedNameRects[i])
                pg.draw.rect(screen, "#fcce8d", savedNameRects[i], 2)
                savedNameSurface = font.render(savedNameTexts[i], True, "#856c4a")
                screen.blit(savedNameSurface, (savedNameRects[i].x + 5, savedNameRects[i].y + 5))

        # Update the display
        pg.display.update()


# This function returns the image corresponding to the given dice number.
def imageNumOfPoints(dice_num):
    # Load the image based on the dice number.
    if dice_num == 1:
        diceImage = pg.image.load("assets/Augenzahl1.png")
    elif dice_num == 2:
        diceImage = pg.image.load("assets/Augenzahl2.png")
    elif dice_num == 3:
        diceImage = pg.image.load("assets/Augenzahl3.png")
    elif dice_num == 4:
        diceImage = pg.image.load("assets/Augenzahl4.png")
    elif dice_num == 5:
        diceImage = pg.image.load("assets/Augenzahl5.png")
    elif dice_num == 6:
        diceImage = pg.image.load("assets/Augenzahl6.png")
    else:
        # If the dice number is not valid, return None.
        diceImage = None

    return diceImage


# This function represents the main game loop where players take turns rolling the dice and moving their pieces.
def gameLoop(playerList):
    # Set the window title
    pg.display.set_caption("Don't get ANGRY!")

    # Define background color
    backgroundColor = "#fcce8d"

    # Load game field image and scale it to fit the screen
    gamefield = pg.image.load("assets/gamefield.png")
    gamefield, gamefieldRect = transformScaleKeepRatio(gamefield, screen.get_size())

    # Set names for players
    player1.setName(playerList[0])
    player2.setName(playerList[1])
    player3.setName(playerList[2])
    player4.setName(playerList[3])

    # Define buttons for going back to the main menu and rolling the dice
    playBack = Button(image=None, pos=(1165, 670),
                       textInput="BACK", font=getFont(30), baseColor="Black", hoveringColor="WHITE")
    diceButton= Button(image=scaleImage(pg.image.load("assets/wuerfel.png"), 200, 200), pos=(1150, 90),
                         textInput="Roll the Dice",
                         font=getFont(10), baseColor="BLACK", hoveringColor="WHITE")

    # Display player names on the board
    name1Buttom = Button(image=None, pos=(366, 539), textInput=playerList[0], font=getFont(20),
                          baseColor="#856c4a", hoveringColor=None)
    name2Button = Button(image=None, pos=(366, 177), textInput=playerList[1], font=getFont(20),
                          baseColor="#856c4a", hoveringColor=None)
    name3Button = Button(image=None, pos=(908, 177), textInput=playerList[2], font=getFont(20),
                          baseColor="#856c4a", hoveringColor=None)
    name4Button = Button(image=None, pos=(908, 539), textInput=playerList[3], font=getFont(20),
                          baseColor="#856c4a", hoveringColor=None)

    # Variable for storing the background image
    image = None
    run = True

    while run:
        # Get the current mouse position
        playMousePos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                # Quit the game if the window is closed
                pg.quit()
                sys.exit()
            # Check if player 1 has won the game
            if player1.winner() == True:
                # If player 1 has won, display the winner and stop the game loop
                winner(player1.getName())
                run = False
            # Check if player 2 has won the game
            if player2.winner() == True:
                # If player 2 has won, display the winner and stop the game loop
                winner(player2.getName())
                run = False
            # Check if player 3 has won the game
            if player3.winner() == True:
                # If player 3 has won, display the winner and stop the game loop
                winner(player3.getName())
                run = False
            # Check if player 4 has won the game
            if player4.winner() == True:
                # If player 4 has won, display the winner and stop the game loop
                winner(player4.getName())
                run = False

            # Check if a mouse button is clicked
            if event.type == pg.MOUSEBUTTONDOWN:
                # Check if the "BACK" button is clicked
                if playBack.checkForInput(playMousePos):
                    # If clicked, return to the main menu
                    mainMenu()
                # Check if the "Roll the Dice" button is clicked
                if diceButton.checkForInput(playMousePos):
                    # If clicked, create a Dice object and roll the dice
                    dice = Dice()
                    diceNum = dice.rollDice()
                    # Get the corresponding image of the dice number
                    image = imageNumOfPoints(diceNum)

                # Check if Yellow Figure 1 button is clicked
                if fge1Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fge1.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fge1.finish() == True:
                        # If yes, update its position to the finish line
                        fge1Button.updatePosition(zielfelderList[3])
                        fge1.setPosition(zielfelderList[3])
                        playerPosition["fge1"] = zielfelderList[3]
                        player1.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fge1.getMoved() > 43:
                        # If yes, move the figure backwards
                        fge1.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fge1.getPosition(), "yellow", "fge1")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fge1", currentPos)
                        # Update the position of the button representing the figure
                        fge1Button.updatePosition(currentPos)
                        fge1.setPosition(currentPos)

                # Check if Yellow Figure 2 button is clicked
                if fge2Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fge2.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fge2.finish() == True:
                        # If yes, update its position to the finish line
                        fge2Button.updatePosition(zielfelderList[2])
                        fge2.setPosition(zielfelderList[2])
                        playerPosition["fge2"] = zielfelderList[2]
                        player1.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fge2.getMoved() > 43:
                        # If yes, move the figure backwards
                        fge2.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fge2.getPosition(), "yellow", "fge2")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fge2", currentPos)
                        # Update the position of the button representing the figure
                        fge2Button.updatePosition(currentPos)
                        fge2.setPosition(currentPos)

                # Check if Yellow Figure 3 button is clicked
                if fge3Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fge3.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fge3.finish() == True:
                        # If yes, update its position to the finish line
                        fge3Button.updatePosition(zielfelderList[1])
                        fge3.setPosition(zielfelderList[1])
                        playerPosition["fge3"] = zielfelderList[1]
                        player1.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fge3.getMoved() > 43:
                        # If yes, move the figure backwards
                        fge3.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fge3.getPosition(), "yellow", "fge3")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fge3", currentPos)
                        # Update the position of the button representing the figure
                        fge3Button.updatePosition(currentPos)
                        fge3.setPosition(currentPos)

                # Check if Yellow Figure 4 button is clicked
                if fge4Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fge4.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fge4.finish() == True:
                        # If yes, update its position to the finish line
                        fge4Button.updatePosition(zielfelderList[0])
                        fge4.setPosition(zielfelderList[0])
                        playerPosition["fge4"] = zielfelderList[0]
                        player1.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fge4.getMoved() > 43:
                        # If yes, move the figure backwards
                        fge4.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fge4.getPosition(), "yellow", "fge4")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fge4", currentPos)
                        # Update the position of the button representing the figure
                        fge4Button.updatePosition(currentPos)
                        fge4.setPosition(currentPos)

                # Check if Green Figure 1 button is clicked
                if fgr1Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fgr1.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fgr1.finish() == True:
                        # If yes, update its position to the finish line
                        fgr1Button.updatePosition(zielfelderList[7])
                        fgr1.setPosition(zielfelderList[7])
                        playerPosition["fgr1"] = zielfelderList[7]
                        player2.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fgr1.getMoved() > 43:
                        # If yes, move the figure backwards
                        fgr1.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fgr1.getPosition(), "green", "fgr1")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fgr1", currentPos)
                        # Update the position of the button representing the figure
                        fgr1Button.updatePosition(currentPos)
                        fgr1.setPosition(currentPos)

                # Check if Green Figure 2 button is clicked
                if fgr2Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fgr2.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fgr2.finish() == True:
                        # If yes, update its position to the finish line
                        fgr2Button.updatePosition(zielfelderList[6])
                        fgr2.setPosition(zielfelderList[6])
                        playerPosition["fgr2"] = zielfelderList[6]
                        player2.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fgr2.getMoved() > 43:
                        # If yes, move the figure backwards
                        fgr2.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fgr2.getPosition(), "green", "fgr2")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fgr2", currentPos)
                        # Update the position of the button representing the figure
                        fgr2Button.updatePosition(currentPos)
                        fgr2.setPosition(currentPos)

                # Check if Green Figure 3 button is clicked
                if fgr3Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fgr3.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fgr3.finish() == True:
                        # If yes, update its position to the finish line
                        fgr3Button.updatePosition(zielfelderList[5])
                        fgr3.setPosition(zielfelderList[5])
                        playerPosition["fgr3"] = zielfelderList[5]
                        player2.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fgr3.getMoved() > 43:
                        # If yes, move the figure backwards
                        fgr3.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fgr3.getPosition(), "green", "fgr3")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fgr3", currentPos)
                        # Update the position of the button representing the figure
                        fgr3Button.updatePosition(currentPos)
                        fgr3.setPosition(currentPos)

                # Check if Green Figure 4 button is clicked
                if fgr4Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fgr4.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fgr4.finish() == True:
                        # If yes, update its position to the finish line
                        fgr4Button.updatePosition(zielfelderList[4])
                        fgr4.setPosition(zielfelderList[4])
                        playerPosition["fgr4"] = zielfelderList[4]
                        player2.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fgr4.getMoved() > 43:
                        # If yes, move the figure backwards
                        fgr4.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fgr4.getPosition(), "green", "fgr4")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fgr4", currentPos)
                        # Update the position of the button representing the figure
                        fgr4Button.updatePosition(currentPos)
                        fgr4.setPosition(currentPos)

                # Check if Blue Figure 1 button is clicked
                if fb1Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fb1.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fb1.finish() == True:
                        # If yes, update its position to the finish line
                        fb1Button.updatePosition(zielfelderList[11])
                        fb1.setPosition(zielfelderList[11])
                        playerPosition["fb1"] = zielfelderList[11]
                        player3.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fb1.getMoved() > 43:
                        # If yes, move the figure backwards
                        fb1.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fb1.getPosition(), "blue", "fb1")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fb1", currentPos)
                        # Update the position of the button representing the figure
                        fb1Button.updatePosition(currentPos)
                        fb1.setPosition(currentPos)

                # Check if Blue Figure 2 button is clicked
                if fb2Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fb2.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fb2.finish() == True:
                        # If yes, update its position to the finish line
                        fb2Button.updatePosition(zielfelderList[10])
                        fb2.setPosition(zielfelderList[10])
                        playerPosition["fb2"] = zielfelderList[10]
                        player3.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fb2.getMoved() > 43:
                        # If yes, move the figure backwards
                        fb2.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fb2.getPosition(), "blue", "fb2")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fb2", currentPos)
                        # Update the position of the button representing the figure
                        fb2Button.updatePosition(currentPos)
                        fb2.setPosition(currentPos)

                # Check if Blue Figure 3 button is clicked
                if fb3Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fb3.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fb3.finish() == True:
                        # If yes, update its position to the finish line
                        fb3Button.updatePosition(zielfelderList[9])
                        fb3.setPosition(zielfelderList[9])
                        playerPosition["fb3"] = zielfelderList[9]
                        player3.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fb3.getMoved() > 43:
                        # If yes, move the figure backwards
                        fb3.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fb3.getPosition(), "blue", "fb3")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fb3", currentPos)
                        # Update the position of the button representing the figure
                        fb3Button.updatePosition(currentPos)
                        fb3.setPosition(currentPos)

                # Check if Blue Figure 4 button is clicked
                if fb4Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fb4.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fb4.finish() == True:
                        # If yes, update its position to the finish line
                        fb4Button.updatePosition(zielfelderList[8])
                        fb4.setPosition(zielfelderList[8])
                        playerPosition["fb4"] = zielfelderList[8]
                        player3.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fb4.getMoved() > 43:
                        # If yes, move the figure backwards
                        fb4.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fb4.getPosition(), "blue", "fb4")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fb4", currentPos)
                        # Update the position of the button representing the figure
                        fb4Button.updatePosition(currentPos)
                        fb4.setPosition(currentPos)

                # Buttons for Red Figures 1-4
                # Check if Red Figure 1 button is clicked
                if fr1Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fr1.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fr1.finish() == True:
                        # If yes, update its position to the finish line
                        fr1Button.updatePosition(zielfelderList[15])
                        fr1.setPosition(zielfelderList[15])
                        playerPosition["fr1"] = zielfelderList[15]
                        player4.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fr1.getMoved() > 43:
                        # If yes, move the figure backwards
                        fr1.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fr1.getPosition(), "red", "fr1")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fr1", currentPos)
                        # Update the position of the button representing the figure
                        fr1Button.updatePosition(currentPos)
                        fr1.setPosition(currentPos)

                # Check if Red Figure 2 button is clicked
                if fr2Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fr2.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fr2.finish() == True:
                        # If yes, update its position to the finish line
                        fr2Button.updatePosition(zielfelderList[14])
                        fr2.setPosition(zielfelderList[14])
                        playerPosition["fr2"] = zielfelderList[14]
                        player4.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fr2.getMoved() > 43:
                        # If yes, move the figure backwards
                        fr2.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fr2.getPosition(), "red", "fr2")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fr2", currentPos)
                        # Update the position of the button representing the figure
                        fr2Button.updatePosition(currentPos)
                        fr2.setPosition(currentPos)

                # Check if Red Figure 3 button is clicked
                if fr3Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fr3.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fr3.finish() == True:
                        # If yes, update its position to the finish line
                        fr3Button.updatePosition(zielfelderList[13])
                        fr3.setPosition(zielfelderList[13])
                        playerPosition["fr3"] = zielfelderList[13]
                        player4.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fr3.getMoved() > 43:
                        # If yes, move the figure backwards
                        fr3.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fr3.getPosition(), "red", "fr3")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fr3", currentPos)
                        # Update the position of the button representing the figure
                        fr3Button.updatePosition(currentPos)
                        fr3.setPosition(currentPos)

                # Check if Red Figure 4 button is clicked
                if fr4Button.checkForInput(playMousePos):
                    # Set the moved attribute of the figure to the rolled dice number
                    fr4.setMoved(diceNum)
                    # Check if the figure has reached the finish line
                    if fr4.finish() == True:
                        # If yes, update its position to the finish line
                        fr4Button.updatePosition(zielfelderList[12])
                        fr4.setPosition(zielfelderList[12])
                        playerPosition["fr4"] = zielfelderList[12]
                        player4.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fr4.getMoved() > 43:
                        # If yes, move the figure backwards
                        fr4.setMoved(diceNum * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(diceNum, fr4.getPosition(), "red", "fr4")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fr4", currentPos)
                        # Update the position of the button representing the figure
                        fr4Button.updatePosition(currentPos)
                        fr4.setPosition(currentPos)

            # Handle event for resizing the window
            elif event.type == pg.VIDEORESIZE:
                # Set the window size to the new size while keeping it resizable
                window = pg.display.set_mode(event.size, pg.RESIZABLE)
                # Scale the gamefield image to fit the new window size while maintaining aspect ratio
                gamefield, gamefieldRect = transformScaleKeepRatio(gamefield, window.get_size())

        # Fill the screen with the background color and blit the gamefield image onto it
        screen.fill(backgroundColor)
        screen.blit(gamefield, gamefieldRect)

        # Update and draw the BACK button
        playBack.changeColor(playMousePos)
        playBack.update(screen)

        # Update and draw the DICE button
        diceButton.changeColor(playMousePos)
        diceButton.update(screen)

        # Update and draw the figure buttons for all players
        updateFigureButtons(playMousePos)

        # Update and draw the name buttons for all players
        name1Buttom.update(screen)
        name2Button.update(screen)
        name3Button.update(screen)
        name4Button.update(screen)

        # If there is a new dice roll, display the corresponding dice image
        if image is not None:
            newDiceImage = scaleImage(image, 120, 120)
            screen.blit(newDiceImage, (1093, 170))

        # Update the display to show all changes
        pg.display.update()


# Update the state and appearance of all figure buttons based on the mouse position
def updateFigureButtons(PLAY_MOUSE_POS):
    # Update and change color for yellow player's figure buttons
    fge1Button.update(screen)
    fge1Button.changeColor(playMousePos)
    fge2Button.update(screen)
    fge2Button.changeColor(playMousePos)
    fge3Button.update(screen)
    fge3Button.changeColor(playMousePos)
    fge4Button.update(screen)
    fge4Button.changeColor(playMousePos)

    # Update and change color for green player's figure buttons
    fgr1Button.update(screen)
    fgr1Button.changeColor(playMousePos)
    fgr2Button.update(screen)
    fgr2Button.changeColor(playMousePos)
    fgr3Button.update(screen)
    fgr3Button.changeColor(playMousePos)
    fgr4Button.update(screen)
    fgr4Button.changeColor(playMousePos)

    # Update and change color for red player's figure buttons
    fr1Button.update(screen)
    fr1Button.changeColor(playMousePos)
    fr2Button.update(screen)
    fr2Button.changeColor(playMousePos)
    fr3Button.update(screen)
    fr3Button.changeColor(playMousePos)
    fr4Button.update(screen)
    fr4Button.changeColor(playMousePos)

    # Update and change color for blue player's figure buttons
    fb1Button.update(screen)
    fb1Button.changeColor(playMousePos)
    fb2Button.update(screen)
    fb2Button.changeColor(playMousePos)
    fb3Button.update(screen)
    fb3Button.changeColor(playMousePos)
    fb4Button.update(screen)
    fb4Button.changeColor(playMousePos)


# This function checks if the new position is already occupied by another player
def checkForOthers(playerName, newPosition):
    # Iterate over each player's name and position in the playerosition dictionary
    for otherPlayer, position in playerPosition.items():
        # Check if the player is not the current player and if their position matches the new position
        if other_player != player_name and position == new_position:
            # Reset the other player's position to their starting position
            playerPosition[otherPlayer] = hauserList[0]

            # Update the position and state of the other player's figure buttons based on their name
            if other_player == "fge1":
                # Set the position of the figure to the starting position of the corresponding color
                fge1.setPosition(hauserList[0])
                # Update the position of the figure button on the screen
                fge1Button.updatePosition(hauserList[0])
                # Reset the moved state of the figure
                fge1.resetMoved()
            # The logic for updating the position and state of the figure buttons is the same for all players.
            # Iterate over each player and perform the same actions based on their name.
            if otherPlayer == "fge2":
                fge2.setPosition(hauserList[1])
                fge2Button.updatePosition(hauserList[1])
                fge2.resetMoved()
            if otherPlayer == "fge3":
                fge3.setPosition(hauserList[2])
                fge3Button.updatePosition(hauserList[2])
                fge3.resetMoved()
            if otherPlayer == "fge4":
                fge4.setPosition(hauserList[3])
                fge4Button.updatePosition(hauserList[3])
                fge4.resetMoved()

            if otherPlayer == "fr1":
                fr1.setPosition(hauserList[12])
                fr1Button.updatePosition(hauserList[12])
                fr1.resetMoved()
            if otherPlayer == "fr2":
                fr2.setPosition(hauserList[13])
                fr2Button.updatePosition(hauserList[13])
                fr2.resetMoved()
            if otherPlayer == "fr3":
                fr3.setPosition(hauserList[14])
                fr3Button.updatePosition(hauserList[14])
                fr3.resetMoved()
            if otherPlayer == "fr4":
                fr4.setPosition(hauserList[15])
                fr4Button.updatePosition(hauserList[15])
                fr4.resetMoved()

            if otherPlayer == "fb1":
                fb1.setPosition(hauserList[8])
                fb1Button.updatePosition(hauserList[8])
                fb1.resetMoved()
            if otherPlayer == "fb2":
                fb2.setPosition(hauserList[9])
                fb2Button.updatePosition(hauserList[9])
                fb2.resetMoved()
            if otherPlayer == "fb3":
                fb3.setPosition(hauserList[10])
                fb3Button.updatePosition(hauserList[10])
                fb3.resetMoved()
            if otherPlayer == "fb4":
                fb4.setPosition(hauserList[11])
                fb4Button.updatePosition(hauserList[11])
                fb4.resetMoved()

            if otherPlayer == "fgr1":
                fgr1.setPosition(hauserList[4])
                fgr1Button.updatePosition(hauserList[4])
                fgr1.resetMoved()
            if otherPlayer == "fgr2":
                fgr2.setPosition(hauserList[5])
                fgr2Button.updatePosition(hauserList[5])
                fgr2.resetMoved()
            if otherPlayer == "fgr3":
                fgr3.setPosition(hauserList[6])
                fgr3Button.updatePosition(hauserList[6])
                fgr3.resetMoved()
            if otherPlayer == "fgr4":
                fgr4.setPosition(hauserList[7])
                fgr4Button.updatePosition(hauserList[7])
                fgr4.resetMoved()
            break

    # Update the position of the current player in the player_position dictionary
    playerPosition[playerName] = newPosition

# This function makes a move on the game board based on the dice roll, current position, player color, and current figure.
def makeMove(dice_num, position, color, currentFigure):
    # Check if the player is yellow
    if color == "yellow":
        # Check if the current position is one of the yellow starting positions
        if position in hauserList[0:4]:
            # If a 6 is rolled, move to the first position on the fieldList
            if diceNum == 6:
                position = fieldList[0]
            else:
                # Otherwise, print a message indicating no 6 was rolled and move to the next player's turn
                print("No 6 rolled. Next player's turn")
        else:
            # If not in the starting positions, calculate the new position based on the dice roll
            for i in range(0, 40):
                if position == fieldList[i]:
                    counter = i + diceNum
                    if counter > 39:
                        counter = counter - 40
                    position = fieldList[counter]
                    break

    # Check if the player is green
    elif color == "green":
        if position in hauserList[4:8]:
            if diceNum == 6:
                position = fieldList[10]
            else:
                print("No 6 rolled. Next player's turn")
        else:
            for i in range(0, 40):
                if position == fieldList[i]:
                    counter = i + diceNum
                    if counter > 39:
                        counter = counter - 40
                    position = fieldList[counter]
                    break

    # Check if the player is blue
    elif color == "blue":
        if position in hauserList[8:12]:
            if diceNum == 6:
                position = fieldList[20]
            else:
                print("No 6 rolled. Next player's turn")
        else:
            for i in range(0, 40):
                if position == fieldList[i]:
                    counter = i + diceNum
                    if counter > 39:
                        counter = counter - 40
                    position = fieldList[counter]
                    break

    # Check if the player is red
    elif color == "red":
        if position in hauserList[12:16]:
            if diceNum == 6:
                position = fieldList[30]
            else:
                print("No 6 rolled. Next player's turn")
        else:
            for i in range(0, 40):
                if position == fieldList[i]:
                    counter = i + diceNum
                    if counter > 39:
                        counter = counter - 40
                    position = fieldList[counter]
                    break

    # Return the updated position after the move
    return position


# This function displays the winner of the game.
def winner(winPlayer):
    # Set the window caption.
    pg.display.set_caption("Don't get ANGRY!")

    # Load and scale the background image.
    BG = scaleImage(pg.image.load("assets/mainscreen.png"), 1280, 720)

    # Create a button for quitting the game.
    quitButton = Button(image=pg.image.load("assets/PlayRect.png"), pos=(640, 550),
                         textInput="QUIT", font=getFont(75), baseColor="White", hoveringColor="#fcce8d")

    # Winner screen loop
    while True:
        # Display the background on the screen.
        screen.blit(BG, (0, 0))  # Background on the screen

        # Get the current mouse position.
        ENDSCREEN_MOUSE_POS = pg.mouse.get_pos()

        # Render the text displaying the winner.
        endscreenText = getFont(30).render("The winner is player " + str(winPlayer), True, "#856c4a")  # Textfield
        endScreenRect = endscreenText.get_rect(center=(640, 150))

        # Display the winner text.
        screen.blit(ENDSCREEN_TEXT, ENDSCREEN_RECT)

        # Update the display.
        pg.display.update()

        # Event handling loop.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # Quit the game if the window is closed.
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # Check if the quit button is clicked and quit the game if clicked.
                if QUIT_BUTTON.checkForInput(ENDSCREEN_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        # Update and render the quit button.
        QUIT_BUTTON.changeColor(ENDSCREEN_MOUSE_POS)
        QUIT_BUTTON.update(screen)

# Create Figure-Objects
fge1 = Figure(position=hauserList[0], color="yellow")
fge2 = Figure(position=hauserList[1], color="yellow")
fge3 = Figure(position=hauserList[2], color="yellow")
fge4 = Figure(position=hauserList[3], color="yellow")

fgr1 = Figure(position=hauserList[4], color="green")
fgr2 = Figure(position=hauserList[5], color="green")
fgr3 = Figure(position=hauserList[6], color="green")
fgr4 = Figure(position=hauserList[7], color="green")

fb1 = Figure(position=hauserList[8], color="blue")
fb2 = Figure(position=hauserList[9], color="blue")
fb3 = Figure(position=hauserList[10], color="blue")
fb4 = Figure(position=hauserList[11], color="blue")

fr1 = Figure(position=hauserList[12], color="red")
fr2 = Figure(position=hauserList[13], color="red")
fr3 = Figure(position=hauserList[14], color="red")
fr4 = Figure(position=hauserList[15], color="red")

# Create Player Objects
player1 = Player("", "")
player2 = Player("", "")
player3 = Player("", "")
player4 = Player("", "")

#Create Figures as Buttons

# Yellow Figures:
fge1Button = Button(image=pg.image.load("assets/figyellow.png"), pos=(hauserList[0]), textInput="1", font=getFont(10),
                    baseColor="BLACK", hoveringColor="WHITE")

fge2Button = Button(image=pg.image.load("assets/figyellow.png"), pos=(hauserList[1]), textInput="2", font=getFont(10),
                    baseColor="BLACK", hoveringColor="WHITE")
fge3Button = Button(image=pg.image.load("assets/figyellow.png"), pos=(hauserList[2]), textInput="3", font=getFont(10),
                    baseColor="BLACK", hoveringColor="WHITE")
fge4Button = Button(image=pg.image.load("assets/figyellow.png"), pos=(hauserList[3]), textInput="4", font=getFont(10),
                    baseColor="BLACK", hoveringColor="WHITE")
#Red Figures:
fr1Button = Button(image=pg.image.load("assets/figred.png"), pos=(hauserList[12]), textInput="1", font=getFont(10),
                   baseColor="BLACK", hoveringColor="WHITE")
fr2Button = Button(image=pg.image.load("assets/figred.png"), pos=(hauserList[13]), textInput="2", font=getFont(10),
                   baseColor="BLACK", hoveringColor="WHITE")
fr3Button = Button(image=pg.image.load("assets/figred.png"), pos=(hauserList[14]), textInput="3", font=getFont(10),
                   baseColor="BLACK", hoveringColor="WHITE")
fr4Button = Button(image=pg.image.load("assets/figred.png"), pos=(hauserList[15]), textInput="4", font=getFont(10),
                   baseColor="BLACK", hoveringColor="WHITE")
#Blue Figures:
fb1Button = Button(image=pg.image.load("assets/figblue.png"), pos=(hauserList[8]), textInput="1", font=getFont(10),
                   baseColor="BLACK", hoveringColor="WHITE")
fb2Button = Button(image=pg.image.load("assets/figblue.png"), pos=(hauserList[9]), textInput="2", font=getFont(10),
                   baseColor="BLACK", hoveringColor="WHITE")
fb3Button = Button(image=pg.image.load("assets/figblue.png"), pos=(hauserList[10]), textInput="3", font=getFont(10),
                   baseColor="BLACK", hoveringColor="WHITE")
fb4Button = Button(image=pg.image.load("assets/figblue.png"), pos=(hauserList[11]), textInput="4", font=getFont(10),
                   baseColor="BLACK", hoveringColor="WHITE")

#Green Figures:
fgr1Button = Button(image=pg.image.load("assets/figgreen.png"), pos=(hauserList[4]), textInput="1", font=getFont(10),
                    baseColor="BLACK", hoveringColor="WHITE")
fgr2Button = Button(image=pg.image.load("assets/figgreen.png"), pos=(hauserList[5]), textInput="2", font=getFont(10),
                    baseColor="BLACK", hoveringColor="WHITE")
fgr3Button = Button(image=pg.image.load("assets/figgreen.png"), pos=(hauserList[6]), textInput="3", font=getFont(10),
                    baseColor="BLACK", hoveringColor="WHITE")
fgr4Button = Button(image=pg.image.load("assets/figgreen.png"), pos=(hauserList[7]), textInput="4", font=getFont(10),
                    baseColor="BLACK", hoveringColor="WHITE")

mainMenu()