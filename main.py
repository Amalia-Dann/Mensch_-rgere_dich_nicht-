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
field_list = playground.fields()
hauser_list = playground.houses()
zielfelder_list = playground.finishFields()

player_position = { }
saved_name_rects = []

def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("assets/font.ttf", size)

# fonts
font = get_font(10)
input_font = get_font(15)

# This function scales an image while maintaining its aspect ratio.
def transform_scale_keep_ratio(image, size):
    iwidth, iheight = image.get_size()
    scale = min(size[0] / iwidth, size[1] / iheight)
    #scale = max(size[0] / iwidth, size[1] / iheight)
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pg.transform.smoothscale(image, new_size)
    image_rect = scaled_image.get_rect(center = (size[0] // 2, size[1] // 2))
    return scaled_image, image_rect # Return the scaled image and the centered rectangle.

# This function scales an image to a new width and height.
def scaleImage(image, newWidth, newHeight):
    original_width, original_height = image.get_size()  # Get the original width and height of the image.
    scaled_image = pg.transform.scale(image, (newWidth, newHeight))     # Scale the image to the new width and height.
    # Return the scaled image.
    return scaled_image

# This function represents the main menu of the game.
def main_menu():
    # Set the window caption.
    pg.display.set_caption("Don't get ANGRY!")

    # Load and scale the background image.
    BG = scaleImage(pg.image.load("assets/mainscreen.png"), 1280, 720)

    # Main menu loop
    while True:
        # Display the background on the screen.
        screen.blit(BG, (0, 0))  # Background on the screen

        # Get the current mouse position.
        MENU_MOUSE_POS = pg.mouse.get_pos()

        # Render the main menu title text.
        MENU_TEXT = get_font(75).render("Don't get ANGRY!", True, "#856c4a")  # Textfield
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        # Create buttons for play, rules, and quit.
        PLAY_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(340, 270),
                             text_input="PLAY", font=get_font(75), base_color="White", hovering_color="#fcce8d")
        RULES_BUTTON = Button(image=scaleImage(pg.image.load("assets/Play_Rect.png"), 430, 109), pos=(340, 420),
                              text_input="RULES", font=get_font(75), base_color="White", hovering_color="#fcce8d")
        QUIT_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(340, 570),
                             text_input="QUIT", font=get_font(75), base_color="White", hovering_color="#fcce8d")

        # Display the main menu title text.
        screen.blit(MENU_TEXT, MENU_RECT)

        # Update and render buttons.
        for button in [PLAY_BUTTON, RULES_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        # Event handling loop.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # Quit the game if the window is closed.
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # Check for button clicks and perform corresponding actions.
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()  # Run the play function
                if RULES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    rules()  # Run the rules function
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        # Update the display.
        pg.display.update()

# This function represents the rules screen of the game.
def rules():
    while True:
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()  # Get the current mouse position.

        screen.fill("#fcce8d")  # Fill the screen with a background color.
        #schrift = get_font(25)

        # Function to draw text on the screen.
        def draw_text(text):
            # Set up the font and initial position for drawing text.
            font = get_font(12)
            y_pos = 15
            x_pos = 20

            # Iterate over each line of the provided text and render it onto the screen.
            for line in text.splitlines():
                rendered_line = font.render(line, 1, (0, 0, 0))
                screen.blit(rendered_line, (x_pos, y_pos))

                # Update the y-position for the next line.
                y_pos += 21

        # Display the rules text.
        if __name__ == "__main__":
            text_to_display = (
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
            draw_text(text_to_display)

        # Create a button for returning to the main menu.
        RULES_BACK = Button(image=None, pos=(1200, 690),
                              text_input="BACK", font=get_font(20), base_color="Black", hovering_color="White")

        # Event handling loop.
        for event in pg.event.get():
            # Quit the game if the window is closed.
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # Check if the back button is clicked and return to the main menu if clicked.
                if RULES_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        # Update and render the back button.
        RULES_BACK.changeColor(OPTIONS_MOUSE_POS)
        RULES_BACK.update(screen)

        pg.display.update() # Update the display.

# This function represents the game's main menu where players can enter their names and start the game.
def play():
    # Set the window title
    pg.display.set_caption("Don't get ANGRY!")

    # Define background color
    background_color = "#fcce8d"

    # Load game field image and scale it to fit the screen
    gamefield = pg.image.load("assets/gamefield.png")
    gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, screen.get_size())

    # Define buttons for going back to the main menu and starting the game
    PLAY_BACK = Button(image=None, pos=(1165, 670),
                       text_input="BACK", font=get_font(30), base_color="Black", hovering_color="WHITE")

    GAME_ACTIVE = Button(image=None, pos=(135, 670), text_input="START", font=get_font(30),
                         base_color="Black", hovering_color="WHITE")

    # Text prompting the player to enter names
    prompt_text = ("Press Enter, to add a player")
    prompt_rect = pg.Rect(20, 50, 200, 40)

    # Input field parameters
    input_rect = pg.Rect(20, 100, 200, 40)
    input_text = ""
    cursor_active = False
    cursor_timer = 0  # Timer for cursor blink effect
    cursor_size = 2  # Size of the cursor

    # Saved player names
    max_players = 4
    saved_name_rects = [pg.Rect(20, 190 + i * 80, 200, 40) for i in range(max_players)]
    saved_name_texts = [""] * max_players

    # Variable for storing the background image
    image = None

    # Flag indicating whether the game is active
    active_play = False

    while True:
        # Get the current mouse position
        PLAY_MOUSE_POS = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Add player name when Enter is pressed
                    if not cursor_active:
                        cursor_active = True
                        prompt_text = "Enter player name"
                    else:
                        for i in range(len(saved_name_texts)):
                            if not saved_name_texts[i] and input_text:
                                saved_name_texts[i] = input_text
                                input_text = ""
                                cursor_timer = 0
                                if i == max_players - 1:
                                    cursor_active = False
                                    prompt_text = "All players registered"
                                else:
                                    prompt_text = "Enter player name"
                                break
                elif cursor_active:
                    # Handle input when cursor is active
                    if event.key == pg.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
            if event.type == pg.MOUSEBUTTONDOWN:
                # Check for button clicks
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if GAME_ACTIVE.checkForInput(PLAY_MOUSE_POS):
                    gameLoop(saved_name_texts)
            elif event.type == pg.VIDEORESIZE:
                # Resize the window and game field image
                window = pg.display.set_mode(event.size, pg.RESIZABLE)
                gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, window.get_size())

        # Fill the screen with background color
        screen.fill(background_color)
        # Draw the game field image
        screen.blit(gamefield, gamefield_rect)

        # Update and draw the back button
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        # Update and draw the start button
        GAME_ACTIVE.changeColor(PLAY_MOUSE_POS)
        GAME_ACTIVE.update(screen)

        # Display prompt text
        prompt_surface = font.render(prompt_text, True, black)
        screen.blit(prompt_surface, (prompt_rect.x + 5, prompt_rect.y + 5))

        # Draw input field if active
        if cursor_active:
            pg.draw.rect(screen, white, input_rect)
            pg.draw.rect(screen, black, input_rect, 2)
            input_surface = input_font.render(input_text, True, black)
            screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

            # Cursor blink effect
            if pg.time.get_ticks() % 1000 < 500:
                cursor_height = input_surface.get_height()
                cursor_rect = pg.Rect(input_rect.x + 5 + input_surface.get_width(), input_rect.y + 5, cursor_size,
                                      cursor_height)
                pg.draw.rect(screen, black, cursor_rect)

        # Display saved player names
        for i in range(len(saved_name_texts)):
            if saved_name_texts[i]:
                pg.draw.rect(screen, "#fcce8d", saved_name_rects[i])
                pg.draw.rect(screen, "#fcce8d", saved_name_rects[i], 2)
                saved_name_surface = font.render(saved_name_texts[i], True, "#856c4a")
                screen.blit(saved_name_surface, (saved_name_rects[i].x + 5, saved_name_rects[i].y + 5))

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
def gameLoop(player_list):
    # Set the window title
    pg.display.set_caption("Don't get ANGRY!")

    # Define background color
    background_color = "#fcce8d"

    # Load game field image and scale it to fit the screen
    gamefield = pg.image.load("assets/gamefield.png")
    gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, screen.get_size())

    # Set names for players
    player1.setName(player_list[0])
    player2.setName(player_list[1])
    player3.setName(player_list[2])
    player4.setName(player_list[3])

    # Define buttons for going back to the main menu and rolling the dice
    PLAY_BACK = Button(image=None, pos=(1165, 670),
                       text_input="BACK", font=get_font(30), base_color="Black", hovering_color="WHITE")
    DICE_BUTTON = Button(image=scaleImage(pg.image.load("assets/wuerfel.png"), 200, 200), pos=(1150, 90),
                         text_input="Roll the Dice",
                         font=get_font(10), base_color="BLACK", hovering_color="WHITE")

    # Display player names on the board
    name1_BUTTON = Button(image=None, pos=(366, 539), text_input=player_list[0], font=get_font(20),
                          base_color="#856c4a", hovering_color=None)
    name2_BUTTON = Button(image=None, pos=(366, 177), text_input=player_list[1], font=get_font(20),
                          base_color="#856c4a", hovering_color=None)
    name3_BUTTON = Button(image=None, pos=(908, 177), text_input=player_list[2], font=get_font(20),
                          base_color="#856c4a", hovering_color=None)
    name4_BUTTON = Button(image=None, pos=(908, 539), text_input=player_list[3], font=get_font(20),
                          base_color="#856c4a", hovering_color=None)

    # Variable for storing the background image
    image = None
    run = True

    while run:
        # Get the current mouse position
        PLAY_MOUSE_POS = pg.mouse.get_pos()

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
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    # If clicked, return to the main menu
                    main_menu()
                # Check if the "Roll the Dice" button is clicked
                if DICE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # If clicked, create a Dice object and roll the dice
                    dice = Dice()
                    dice_num = dice.roll_dice()
                    # Get the corresponding image of the dice number
                    image = imageNumOfPoints(dice_num)

                # Check if Yellow Figure 1 button is clicked
                if FGE1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fge1.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fge1.finish() == True:
                        # If yes, update its position to the finish line
                        FGE1_BUTTON.updatePosition(zielfelder_list[3])
                        fge1.setPosition(zielfelder_list[3])
                        player_position["fge1"] = zielfelder_list[3]
                        player1.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fge1.getMoved() > 43:
                        # If yes, move the figure backwards
                        fge1.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fge1.getPosition(), "yellow", "fge1")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fge1", currentPos)
                        # Update the position of the button representing the figure
                        FGE1_BUTTON.updatePosition(currentPos)
                        fge1.setPosition(currentPos)

                # Check if Yellow Figure 2 button is clicked
                if FGE2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fge2.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fge2.finish() == True:
                        # If yes, update its position to the finish line
                        FGE2_BUTTON.updatePosition(zielfelder_list[2])
                        fge2.setPosition(zielfelder_list[2])
                        player_position["fge2"] = zielfelder_list[2]
                        player1.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fge2.getMoved() > 43:
                        # If yes, move the figure backwards
                        fge2.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fge2.getPosition(), "yellow", "fge2")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fge2", currentPos)
                        # Update the position of the button representing the figure
                        FGE2_BUTTON.updatePosition(currentPos)
                        fge2.setPosition(currentPos)

                # Check if Yellow Figure 3 button is clicked
                if FGE3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fge3.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fge3.finish() == True:
                        # If yes, update its position to the finish line
                        FGE3_BUTTON.updatePosition(zielfelder_list[1])
                        fge3.setPosition(zielfelder_list[1])
                        player_position["fge3"] = zielfelder_list[1]
                        player1.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fge3.getMoved() > 43:
                        # If yes, move the figure backwards
                        fge3.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fge3.getPosition(), "yellow", "fge3")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fge3", currentPos)
                        # Update the position of the button representing the figure
                        FGE3_BUTTON.updatePosition(currentPos)
                        fge3.setPosition(currentPos)

                # Check if Yellow Figure 4 button is clicked
                if FGE4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fge4.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fge4.finish() == True:
                        # If yes, update its position to the finish line
                        FGE4_BUTTON.updatePosition(zielfelder_list[0])
                        fge4.setPosition(zielfelder_list[0])
                        player_position["fge4"] = zielfelder_list[0]
                        player1.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fge4.getMoved() > 43:
                        # If yes, move the figure backwards
                        fge4.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fge4.getPosition(), "yellow", "fge4")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fge4", currentPos)
                        # Update the position of the button representing the figure
                        FGE4_BUTTON.updatePosition(currentPos)
                        fge4.setPosition(currentPos)

                # Check if Green Figure 1 button is clicked
                if FGR1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fgr1.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fgr1.finish() == True:
                        # If yes, update its position to the finish line
                        FGR1_BUTTON.updatePosition(zielfelder_list[7])
                        fgr1.setPosition(zielfelder_list[7])
                        player_position["fgr1"] = zielfelder_list[7]
                        player2.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fgr1.getMoved() > 43:
                        # If yes, move the figure backwards
                        fgr1.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fgr1.getPosition(), "green", "fgr1")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fgr1", currentPos)
                        # Update the position of the button representing the figure
                        FGR1_BUTTON.updatePosition(currentPos)
                        fgr1.setPosition(currentPos)

                # Check if Green Figure 2 button is clicked
                if FGR2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fgr2.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fgr2.finish() == True:
                        # If yes, update its position to the finish line
                        FGR2_BUTTON.updatePosition(zielfelder_list[6])
                        fgr2.setPosition(zielfelder_list[6])
                        player_position["fgr2"] = zielfelder_list[6]
                        player2.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fgr2.getMoved() > 43:
                        # If yes, move the figure backwards
                        fgr2.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fgr2.getPosition(), "green", "fgr2")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fgr2", currentPos)
                        # Update the position of the button representing the figure
                        FGR2_BUTTON.updatePosition(currentPos)
                        fgr2.setPosition(currentPos)

                # Check if Green Figure 3 button is clicked
                if FGR3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fgr3.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fgr3.finish() == True:
                        # If yes, update its position to the finish line
                        FGR3_BUTTON.updatePosition(zielfelder_list[5])
                        fgr3.setPosition(zielfelder_list[5])
                        player_position["fgr3"] = zielfelder_list[5]
                        player2.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fgr3.getMoved() > 43:
                        # If yes, move the figure backwards
                        fgr3.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fgr3.getPosition(), "green", "fgr3")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fgr3", currentPos)
                        # Update the position of the button representing the figure
                        FGR3_BUTTON.updatePosition(currentPos)
                        fgr3.setPosition(currentPos)

                # Check if Green Figure 4 button is clicked
                if FGR4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fgr4.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fgr4.finish() == True:
                        # If yes, update its position to the finish line
                        FGR4_BUTTON.updatePosition(zielfelder_list[4])
                        fgr4.setPosition(zielfelder_list[4])
                        player_position["fgr4"] = zielfelder_list[4]
                        player2.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fgr4.getMoved() > 43:
                        # If yes, move the figure backwards
                        fgr4.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fgr4.getPosition(), "green", "fgr4")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fgr4", currentPos)
                        # Update the position of the button representing the figure
                        FGR4_BUTTON.updatePosition(currentPos)
                        fgr4.setPosition(currentPos)

                # Check if Blue Figure 1 button is clicked
                if FB1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fb1.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fb1.finish() == True:
                        # If yes, update its position to the finish line
                        FB1_BUTTON.updatePosition(zielfelder_list[11])
                        fb1.setPosition(zielfelder_list[11])
                        player_position["fb1"] = zielfelder_list[11]
                        player3.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fb1.getMoved() > 43:
                        # If yes, move the figure backwards
                        fb1.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fb1.getPosition(), "blue", "fb1")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fb1", currentPos)
                        # Update the position of the button representing the figure
                        FB1_BUTTON.updatePosition(currentPos)
                        fb1.setPosition(currentPos)

                # Check if Blue Figure 2 button is clicked
                if FB2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fb2.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fb2.finish() == True:
                        # If yes, update its position to the finish line
                        FB2_BUTTON.updatePosition(zielfelder_list[10])
                        fb2.setPosition(zielfelder_list[10])
                        player_position["fb2"] = zielfelder_list[10]
                        player3.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fb2.getMoved() > 43:
                        # If yes, move the figure backwards
                        fb2.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fb2.getPosition(), "blue", "fb2")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fb2", currentPos)
                        # Update the position of the button representing the figure
                        FB2_BUTTON.updatePosition(currentPos)
                        fb2.setPosition(currentPos)

                # Check if Blue Figure 3 button is clicked
                if FB3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fb3.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fb3.finish() == True:
                        # If yes, update its position to the finish line
                        FB3_BUTTON.updatePosition(zielfelder_list[9])
                        fb3.setPosition(zielfelder_list[9])
                        player_position["fb3"] = zielfelder_list[9]
                        player3.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fb3.getMoved() > 43:
                        # If yes, move the figure backwards
                        fb3.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fb3.getPosition(), "blue", "fb3")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fb3", currentPos)
                        # Update the position of the button representing the figure
                        FB3_BUTTON.updatePosition(currentPos)
                        fb3.setPosition(currentPos)

                # Check if Blue Figure 4 button is clicked
                if FB4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fb4.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fb4.finish() == True:
                        # If yes, update its position to the finish line
                        FB4_BUTTON.updatePosition(zielfelder_list[8])
                        fb4.setPosition(zielfelder_list[8])
                        player_position["fb4"] = zielfelder_list[8]
                        player3.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fb4.getMoved() > 43:
                        # If yes, move the figure backwards
                        fb4.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fb4.getPosition(), "blue", "fb4")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fb4", currentPos)
                        # Update the position of the button representing the figure
                        FB4_BUTTON.updatePosition(currentPos)
                        fb4.setPosition(currentPos)

                # Buttons for Red Figures 1-4
                # Check if Red Figure 1 button is clicked
                if FR1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fr1.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fr1.finish() == True:
                        # If yes, update its position to the finish line
                        FR1_BUTTON.updatePosition(zielfelder_list[15])
                        fr1.setPosition(zielfelder_list[15])
                        player_position["fr1"] = zielfelder_list[15]
                        player4.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fr1.getMoved() > 43:
                        # If yes, move the figure backwards
                        fr1.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fr1.getPosition(), "red", "fr1")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fr1", currentPos)
                        # Update the position of the button representing the figure
                        FR1_BUTTON.updatePosition(currentPos)
                        fr1.setPosition(currentPos)

                # Check if Red Figure 2 button is clicked
                if FR2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fr2.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fr2.finish() == True:
                        # If yes, update its position to the finish line
                        FR2_BUTTON.updatePosition(zielfelder_list[14])
                        fr2.setPosition(zielfelder_list[14])
                        player_position["fr2"] = zielfelder_list[14]
                        player4.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fr2.getMoved() > 43:
                        # If yes, move the figure backwards
                        fr2.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fr2.getPosition(), "red", "fr2")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fr2", currentPos)
                        # Update the position of the button representing the figure
                        FR2_BUTTON.updatePosition(currentPos)
                        fr2.setPosition(currentPos)

                # Check if Red Figure 3 button is clicked
                if FR3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fr3.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fr3.finish() == True:
                        # If yes, update its position to the finish line
                        FR3_BUTTON.updatePosition(zielfelder_list[13])
                        fr3.setPosition(zielfelder_list[13])
                        player_position["fr3"] = zielfelder_list[13]
                        player4.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fr3.getMoved() > 43:
                        # If yes, move the figure backwards
                        fr3.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fr3.getPosition(), "red", "fr3")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fr3", currentPos)
                        # Update the position of the button representing the figure
                        FR3_BUTTON.updatePosition(currentPos)
                        fr3.setPosition(currentPos)

                # Check if Red Figure 4 button is clicked
                if FR4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    # Set the moved attribute of the figure to the rolled dice number
                    fr4.setMoved(dice_num)
                    # Check if the figure has reached the finish line
                    if fr4.finish() == True:
                        # If yes, update its position to the finish line
                        FR4_BUTTON.updatePosition(zielfelder_list[12])
                        fr4.setPosition(zielfelder_list[12])
                        player_position["fr4"] = zielfelder_list[12]
                        player4.setFinish()
                    # Check if the figure has moved beyond the finish line
                    elif fr4.getMoved() > 43:
                        # If yes, move the figure backwards
                        fr4.setMoved(dice_num * (-1))
                    else:
                        # Otherwise, calculate the new position of the figure after moving it
                        currentPos = makeMove(dice_num, fr4.getPosition(), "red", "fr4")
                        # Check for other players on the new position and adjust accordingly
                        checkForOthers("fr4", currentPos)
                        # Update the position of the button representing the figure
                        FR4_BUTTON.updatePosition(currentPos)
                        fr4.setPosition(currentPos)

            # Handle event for resizing the window
            elif event.type == pg.VIDEORESIZE:
                # Set the window size to the new size while keeping it resizable
                window = pg.display.set_mode(event.size, pg.RESIZABLE)
                # Scale the gamefield image to fit the new window size while maintaining aspect ratio
                gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, window.get_size())

        # Fill the screen with the background color and blit the gamefield image onto it
        screen.fill(background_color)
        screen.blit(gamefield, gamefield_rect)

        # Update and draw the BACK button
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        # Update and draw the DICE button
        DICE_BUTTON.changeColor(PLAY_MOUSE_POS)
        DICE_BUTTON.update(screen)

        # Update and draw the figure buttons for all players
        updateFigureButtons(PLAY_MOUSE_POS)

        # Update and draw the name buttons for all players
        name1_BUTTON.update(screen)
        name2_BUTTON.update(screen)
        name3_BUTTON.update(screen)
        name4_BUTTON.update(screen)

        # If there is a new dice roll, display the corresponding dice image
        if image is not None:
            newDiceImage = scaleImage(image, 120, 120)
            screen.blit(newDiceImage, (1093, 170))

        # Update the display to show all changes
        pg.display.update()


# Update the state and appearance of all figure buttons based on the mouse position
def updateFigureButtons(PLAY_MOUSE_POS):
    # Update and change color for yellow player's figure buttons
    FGE1_BUTTON.update(screen)
    FGE1_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGE2_BUTTON.update(screen)
    FGE2_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGE3_BUTTON.update(screen)
    FGE3_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGE4_BUTTON.update(screen)
    FGE4_BUTTON.changeColor(PLAY_MOUSE_POS)

    # Update and change color for green player's figure buttons
    FGR1_BUTTON.update(screen)
    FGR1_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGR2_BUTTON.update(screen)
    FGR2_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGR3_BUTTON.update(screen)
    FGR3_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGR4_BUTTON.update(screen)
    FGR4_BUTTON.changeColor(PLAY_MOUSE_POS)

    # Update and change color for red player's figure buttons
    FR1_BUTTON.update(screen)
    FR1_BUTTON.changeColor(PLAY_MOUSE_POS)
    FR2_BUTTON.update(screen)
    FR2_BUTTON.changeColor(PLAY_MOUSE_POS)
    FR3_BUTTON.update(screen)
    FR3_BUTTON.changeColor(PLAY_MOUSE_POS)
    FR4_BUTTON.update(screen)
    FR4_BUTTON.changeColor(PLAY_MOUSE_POS)

    # Update and change color for blue player's figure buttons
    FB1_BUTTON.update(screen)
    FB1_BUTTON.changeColor(PLAY_MOUSE_POS)
    FB2_BUTTON.update(screen)
    FB2_BUTTON.changeColor(PLAY_MOUSE_POS)
    FB3_BUTTON.update(screen)
    FB3_BUTTON.changeColor(PLAY_MOUSE_POS)
    FB4_BUTTON.update(screen)
    FB4_BUTTON.changeColor(PLAY_MOUSE_POS)


# This function checks if the new position is already occupied by another player
def checkForOthers(player_name, new_position):
    # Iterate over each player's name and position in the player_position dictionary
    for other_player, position in player_position.items():
        # Check if the player is not the current player and if their position matches the new position
        if other_player != player_name and position == new_position:
            # Reset the other player's position to their starting position
            player_position[other_player] = hauser_list[0]

            # Update the position and state of the other player's figure buttons based on their name
            if other_player == "fge1":
                # Set the position of the figure to the starting position of the corresponding color
                fge1.setPosition(hauser_list[0])
                # Update the position of the figure button on the screen
                FGE1_BUTTON.updatePosition(hauser_list[0])
                # Reset the moved state of the figure
                fge1.resetMoved()
            # The logic for updating the position and state of the figure buttons is the same for all players.
            # Iterate over each player and perform the same actions based on their name.
            if other_player == "fge2":
                fge2.setPosition(hauser_list[1])
                FGE2_BUTTON.updatePosition(hauser_list[1])
                fge2.resetMoved()
            if other_player == "fge3":
                fge3.setPosition(hauser_list[2])
                FGE3_BUTTON.updatePosition(hauser_list[2])
                fge3.resetMoved()
            if other_player == "fge4":
                fge4.setPosition(hauser_list[3])
                FGE4_BUTTON.updatePosition(hauser_list[3])
                fge4.resetMoved()

            if other_player == "fr1":
                fr1.setPosition(hauser_list[12])
                FR1_BUTTON.updatePosition(hauser_list[12])
                fr1.resetMoved()
            if other_player == "fr2":
                fr2.setPosition(hauser_list[13])
                FR2_BUTTON.updatePosition(hauser_list[13])
                fr2.resetMoved()
            if other_player == "fr3":
                fr3.setPosition(hauser_list[14])
                FR3_BUTTON.updatePosition(hauser_list[14])
                fr3.resetMoved()
            if other_player == "fr4":
                fr4.setPosition(hauser_list[15])
                FR4_BUTTON.updatePosition(hauser_list[15])
                fr4.resetMoved()

            if other_player == "fb1":
                fb1.setPosition(hauser_list[8])
                FB1_BUTTON.updatePosition(hauser_list[8])
                fb1.resetMoved()
            if other_player == "fb2":
                fb2.setPosition(hauser_list[9])
                FB2_BUTTON.updatePosition(hauser_list[9])
                fb2.resetMoved()
            if other_player == "fb3":
                fb3.setPosition(hauser_list[10])
                FB3_BUTTON.updatePosition(hauser_list[10])
                fb3.resetMoved()
            if other_player == "fb4":
                fb4.setPosition(hauser_list[11])
                FB4_BUTTON.updatePosition(hauser_list[11])
                fb4.resetMoved()

            if other_player == "fgr1":
                fgr1.setPosition(hauser_list[4])
                FGR1_BUTTON.updatePosition(hauser_list[4])
                fgr1.resetMoved()
            if other_player == "fgr2":
                fgr2.setPosition(hauser_list[5])
                FGR2_BUTTON.updatePosition(hauser_list[5])
                fgr2.resetMoved()
            if other_player == "fgr3":
                fgr3.setPosition(hauser_list[6])
                FGR3_BUTTON.updatePosition(hauser_list[6])
                fgr3.resetMoved()
            if other_player == "fgr4":
                fgr4.setPosition(hauser_list[7])
                FGR4_BUTTON.updatePosition(hauser_list[7])
                fgr4.resetMoved()
            break

    # Update the position of the current player in the player_position dictionary
    player_position[player_name] = new_position

# This function makes a move on the game board based on the dice roll, current position, player color, and current figure.
def makeMove(dice_num, position, color, currentFigure):
    # Check if the player is yellow
    if color == "yellow":
        # Check if the current position is one of the yellow starting positions
        if position in hauser_list[0:4]:
            # If a 6 is rolled, move to the first position on the field_list
            if dice_num == 6:
                position = field_list[0]
            else:
                # Otherwise, print a message indicating no 6 was rolled and move to the next player's turn
                print("No 6 rolled. Next player's turn")
        else:
            # If not in the starting positions, calculate the new position based on the dice roll
            for i in range(0, 40):
                if position == field_list[i]:
                    counter = i + dice_num
                    if counter > 39:
                        counter = counter - 40
                    position = field_list[counter]
                    break

    # Check if the player is green
    elif color == "green":
        if position in hauser_list[4:8]:
            if dice_num == 6:
                position = field_list[10]
            else:
                print("No 6 rolled. Next player's turn")
        else:
            for i in range(0, 40):
                if position == field_list[i]:
                    counter = i + dice_num
                    if counter > 39:
                        counter = counter - 40
                    position = field_list[counter]
                    break

    # Check if the player is blue
    elif color == "blue":
        if position in hauser_list[8:12]:
            if dice_num == 6:
                position = field_list[20]
            else:
                print("No 6 rolled. Next player's turn")
        else:
            for i in range(0, 40):
                if position == field_list[i]:
                    counter = i + dice_num
                    if counter > 39:
                        counter = counter - 40
                    position = field_list[counter]
                    break

    # Check if the player is red
    elif color == "red":
        if position in hauser_list[12:16]:
            if dice_num == 6:
                position = field_list[30]
            else:
                print("No 6 rolled. Next player's turn")
        else:
            for i in range(0, 40):
                if position == field_list[i]:
                    counter = i + dice_num
                    if counter > 39:
                        counter = counter - 40
                    position = field_list[counter]
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
    QUIT_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(640, 550),
                         text_input="QUIT", font=get_font(75), base_color="White", hovering_color="#fcce8d")

    # Winner screen loop
    while True:
        # Display the background on the screen.
        screen.blit(BG, (0, 0))  # Background on the screen

        # Get the current mouse position.
        ENDSCREEN_MOUSE_POS = pg.mouse.get_pos()

        # Render the text displaying the winner.
        ENDSCREEN_TEXT = get_font(30).render("The winner is player " + str(winPlayer), True, "#856c4a")  # Textfield
        ENDSCREEN_RECT = ENDSCREEN_TEXT.get_rect(center=(640, 150))

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
fge1 = Figure(position=hauser_list[0], color="yellow")
fge2 = Figure(position=hauser_list[1], color="yellow")
fge3 = Figure(position=hauser_list[2], color="yellow")
fge4 = Figure(position=hauser_list[3], color="yellow")

fgr1 = Figure(position=hauser_list[4], color="green")
fgr2 = Figure(position=hauser_list[5], color="green")
fgr3 = Figure(position=hauser_list[6], color="green")
fgr4 = Figure(position=hauser_list[7], color="green")

fb1 = Figure(position=hauser_list[8], color="blue")
fb2 = Figure(position=hauser_list[9], color="blue")
fb3 = Figure(position=hauser_list[10], color="blue")
fb4 = Figure(position=hauser_list[11], color="blue")

fr1 = Figure(position=hauser_list[12], color="red")
fr2 = Figure(position=hauser_list[13], color="red")
fr3 = Figure(position=hauser_list[14], color="red")
fr4 = Figure(position=hauser_list[15], color="red")

# Create Player Objects
player1 = Player("", "")
player2 = Player("", "")
player3 = Player("", "")
player4 = Player("", "")

#Create Figures as Buttons

# Yellow Figures:
FGE1_BUTTON = Button(image=pg.image.load("assets/figyellow.png"), pos=(hauser_list[0]), text_input="1", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")

FGE2_BUTTON = Button(image=pg.image.load("assets/figyellow.png"), pos=(hauser_list[1]), text_input="2", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")
FGE3_BUTTON = Button(image=pg.image.load("assets/figyellow.png"), pos=(hauser_list[2]), text_input="3", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")
FGE4_BUTTON = Button(image=pg.image.load("assets/figyellow.png"), pos=(hauser_list[3]), text_input="4", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")
#Red Figures:
FR1_BUTTON = Button(image=pg.image.load("assets/figred.png"), pos=(hauser_list[12]), text_input="1", font=get_font(10),
                    base_color="BLACK", hovering_color="WHITE")
FR2_BUTTON = Button(image=pg.image.load("assets/figred.png"), pos=(hauser_list[13]), text_input="2", font=get_font(10),
                    base_color="BLACK", hovering_color="WHITE")
FR3_BUTTON = Button(image=pg.image.load("assets/figred.png"), pos=(hauser_list[14]), text_input="3", font=get_font(10),
                    base_color="BLACK", hovering_color="WHITE")
FR4_BUTTON = Button(image=pg.image.load("assets/figred.png"), pos=(hauser_list[15]), text_input="4", font=get_font(10),
                    base_color="BLACK", hovering_color="WHITE")
#Blue Figures:
FB1_BUTTON = Button(image=pg.image.load("assets/figblue.png"), pos=(hauser_list[8]), text_input="1", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")
FB2_BUTTON = Button(image=pg.image.load("assets/figblue.png"), pos=(hauser_list[9]), text_input="2", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")
FB3_BUTTON = Button(image=pg.image.load("assets/figblue.png"), pos=(hauser_list[10]), text_input="3", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")
FB4_BUTTON = Button(image=pg.image.load("assets/figblue.png"), pos=(hauser_list[11]), text_input="4", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")

#Green Figures:
FGR1_BUTTON = Button(image=pg.image.load("assets/figgreen.png"), pos=(hauser_list[4]), text_input="1", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")
FGR2_BUTTON = Button(image=pg.image.load("assets/figgreen.png"), pos=(hauser_list[5]), text_input="2", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")
FGR3_BUTTON = Button(image=pg.image.load("assets/figgreen.png"), pos=(hauser_list[6]), text_input="3", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")
FGR4_BUTTON = Button(image=pg.image.load("assets/figgreen.png"), pos=(hauser_list[7]), text_input="4", font=get_font(10),
                     base_color="BLACK", hovering_color="WHITE")

main_menu()