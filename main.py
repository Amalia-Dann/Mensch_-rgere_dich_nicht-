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

def transform_scale_keep_ratio(image, size):
    iwidth, iheight = image.get_size()
    scale = min(size[0] / iwidth, size[1] / iheight)
    #scale = max(size[0] / iwidth, size[1] / iheight)
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pg.transform.smoothscale(image, new_size)
    image_rect = scaled_image.get_rect(center = (size[0] // 2, size[1] // 2))
    return scaled_image, image_rect

def scaleImage(image, newWidth, newHeight):
    ursprüngliche_breite, ursprüngliche_höhe = image.get_size()
    vergrößertes_bild = pg.transform.scale(image, (newWidth, newHeight))
    return vergrößertes_bild

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



def gameLoop(player_list):
    pg.display.set_caption("Don't get ANGRY!")
    background_color = "#fcce8d"
    gamefield = pg.image.load("assets/gamefield.png")
    gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, screen.get_size())

    player1.setName(player_list[0])
    player2.setName(player_list[1])
    player3.setName(player_list[2])
    player4.setName(player_list[3])

    PLAY_BACK = Button(image=None, pos=(1165, 670),
                       text_input="BACK", font=get_font(30), base_color="Black", hovering_color="WHITE")

    DICE_BUTTON = Button(image=scaleImage(pg.image.load("assets/wuerfel.png"), 200, 200), pos=(1150, 90),
                         text_input="Roll the Dice",
                         font=get_font(10), base_color="BLACK", hovering_color="WHITE")

    # Printing the Names on the board
    name1_BUTTON = Button(image=None, pos=(366, 539), text_input=player_list[0], font=get_font(20),
                          base_color="#856c4a", hovering_color=None)
    name2_BUTTON = Button(image=None, pos=(366, 177), text_input=player_list[1], font=get_font(20),
                          base_color="#856c4a", hovering_color=None)
    name3_BUTTON = Button(image=None, pos=(908, 177), text_input=player_list[2], font=get_font(20),
                          base_color="#856c4a", hovering_color=None)
    name4_BUTTON = Button(image=None, pos=(908, 539), text_input=player_list[3], font=get_font(20),
                          base_color="#856c4a", hovering_color=None)

    image = None

    run = True

    while run:
        PLAY_MOUSE_POS = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if player1.winner() == True:
                winner(player1.getName())
                run = False
            if player2.winner() == True:
                winner(player2.getName())
                run = False
            if player3.winner() == True:
                winner(player3.getName())
                run = False
            if player4.winner() == True:
                winner(player4.getName())
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DICE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    dice = Dice()
                    dice_num = dice.roll_dice()
                    image = imageNumOfPoints(dice_num)

                # Buttons for Yellow Figures 1-4
                if FGE1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    fge1.setMoved(dice_num)
                    if fge1.finish() == True:
                        FGE1_BUTTON.updatePosition(zielfelder_list[3])
                        fge1.setPosition(zielfelder_list[3])
                        player_position["fge1"] = zielfelder_list[3]
                        player1.setFinish()
                    elif fge1.getMoved() > 43:
                        fge1.setMoved(dice_num * (-1))
                    else:
                        currentPos = makeMove(dice_num, fge1.getPosition(), "yellow", "fge1")
                        checkForOthers("fge1", currentPos)
                        FGE1_BUTTON.updatePosition(currentPos)
                        fge1.setPosition(currentPos)
                if FGE2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    fge2.setMoved(dice_num)
                    if fge2.finish() == True:
                        FGE2_BUTTON.updatePosition(zielfelder_list[2])
                        fge2.setPosition(zielfelder_list[2])
                        player_position["fge2"] = zielfelder_list[2]
                        player1.setFinish()
                    elif fge2.getMoved() > 43:
                        fge2.setMoved(dice_num * (-1))
                    else:
                        currentPos = makeMove(dice_num, fge2.getPosition(), "yellow", "fge2")
                        checkForOthers("fge2", currentPos)
                        FGE2_BUTTON.updatePosition(currentPos)
                        fge2.setPosition(currentPos)
                if FGE3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    fge3.setMoved(dice_num)
                    if fge3.finish() == True:
                        FGE3_BUTTON.updatePosition(zielfelder_list[1])
                        fge3.setPosition(zielfelder_list[1])
                        player_position["fge3"] = zielfelder_list[1]
                        player1.setFinish()
                    elif fge3.getMoved() > 43:
                        fge3.setMoved(dice_num * (-1))
                    else:
                        currentPos = makeMove(dice_num, fge3.getPosition(), "yellow", "fge3")
                        checkForOthers("fge3", currentPos)
                        FGE3_BUTTON.updatePosition(currentPos)
                        fge3.setPosition(currentPos)
                if FGE4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FGE4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fge4.setMoved(dice_num)
                        if fge4.finish() == True:
                            FGE4_BUTTON.updatePosition(zielfelder_list[0])
                            fge4.setPosition(zielfelder_list[0])
                            player_position["fge4"] = zielfelder_list[0]
                            player1.setFinish()
                        elif fge4.getMoved() > 43:
                            fge4.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fge4.getPosition(), "yellow", "fge4")
                            checkForOthers("fge4", currentPos)
                            FGE4_BUTTON.updatePosition(currentPos)
                            fge4.setPosition(currentPos)

                # Buttons for Green Figures 1-4
                if FGR1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FGR1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fgr1.setMoved(dice_num)
                        if fgr1.finish() == True:
                            FGR1_BUTTON.updatePosition(zielfelder_list[7])
                            fgr1.setPosition(zielfelder_list[7])
                            player_position["fgr1"] = zielfelder_list[7]
                            player2.setFinish()
                        elif fgr1.getMoved() > 43:
                            fgr1.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fgr1.getPosition(), "green", "fgr1")
                            checkForOthers("fgr1", currentPos)
                            FGR1_BUTTON.updatePosition(currentPos)
                            fgr1.setPosition(currentPos)
                if FGR2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FGR2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fgr2.setMoved(dice_num)
                        if fgr2.finish() == True:
                            FGR2_BUTTON.updatePosition(zielfelder_list[6])
                            fgr2.setPosition(zielfelder_list[6])
                            player_position["fgr2"] = zielfelder_list[6]
                            player2.setFinish()
                        elif fgr2.getMoved() > 43:
                            fgr2.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fgr2.getPosition(), "green", "fgr2")
                            checkForOthers("fgr2", currentPos)
                            FGR2_BUTTON.updatePosition(currentPos)
                            fgr2.setPosition(currentPos)
                if FGR3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FGR3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fgr3.setMoved(dice_num)
                        if fgr3.finish() == True:
                            FGR3_BUTTON.updatePosition(zielfelder_list[5])
                            fgr3.setPosition(zielfelder_list[5])
                            player_position["fgr3"] = zielfelder_list[5]
                            player2.setFinish()
                        elif fgr3.getMoved() > 43:
                            fgr3.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fgr3.getPosition(), "green", "fgr3")
                            checkForOthers("fgr3", currentPos)
                            FGR3_BUTTON.updatePosition(currentPos)
                            fgr3.setPosition(currentPos)
                if FGR4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FGR4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fgr4.setMoved(dice_num)
                        if fgr4.finish() == True:
                            FGR4_BUTTON.updatePosition(zielfelder_list[4])
                            fgr4.setPosition(zielfelder_list[4])
                            player_position["fgr4"] = zielfelder_list[4]
                            player2.setFinish()
                        elif fgr4.getMoved() > 43:
                            fgr4.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fgr4.getPosition(), "green", "fgr4")
                            checkForOthers("fgr4", currentPos)
                            FGR4_BUTTON.updatePosition(currentPos)
                            fgr4.setPosition(currentPos)

                # Buttons for Blue Figures 1-4
                if FB1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FB1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fb1.setMoved(dice_num)
                        if fb1.finish() == True:
                            FB1_BUTTON.updatePosition(zielfelder_list[11])
                            fb1.setPosition(zielfelder_list[11])
                            player_position["fb1"] = zielfelder_list[11]
                            player3.setFinish()
                        elif fb1.getMoved() > 43:
                            fb1.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fb1.getPosition(), "blue", "fb1")
                            checkForOthers("fb1", currentPos)
                            FB1_BUTTON.updatePosition(currentPos)
                            fb1.setPosition(currentPos)
                if FB2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FB2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fb2.setMoved(dice_num)
                        if fb2.finish() == True:
                            FB2_BUTTON.updatePosition(zielfelder_list[10])
                            fb2.setPosition(zielfelder_list[10])
                            player_position["fb2"] = zielfelder_list[10]
                            player3.setFinish()
                        elif fb2.getMoved() > 43:
                            fb2.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fb2.getPosition(), "blue", "fb2")
                            checkForOthers("fb2", currentPos)
                            FB2_BUTTON.updatePosition(currentPos)
                            fb2.setPosition(currentPos)
                if FB3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FB3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fb3.setMoved(dice_num)
                        if fb3.finish() == True:
                            FB3_BUTTON.updatePosition(zielfelder_list[9])
                            fb3.setPosition(zielfelder_list[9])
                            player_position["fb3"] = zielfelder_list[9]
                            player3.setFinish()
                        elif fb3.getMoved() > 43:
                            fb3.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fb3.getPosition(), "blue", "fb3")
                            checkForOthers("fb3", currentPos)
                            FB3_BUTTON.updatePosition(currentPos)
                            fb3.setPosition(currentPos)
                if FB4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FB4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fb4.setMoved(dice_num)
                        if fb4.finish() == True:
                            FB4_BUTTON.updatePosition(zielfelder_list[8])
                            fb4.setPosition(zielfelder_list[8])
                            player_position["fb4"] = zielfelder_list[8]
                            player3.setFinish()
                        elif fb4.getMoved() > 43:
                            fb4.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fb4.getPosition(), "blue", "fb4")
                            checkForOthers("fb4", currentPos)
                            FB4_BUTTON.updatePosition(currentPos)
                            fb4.setPosition(currentPos)

                # Buttons for Red Figures 1-4
                if FR1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FR1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fr1.setMoved(dice_num)
                        if fr1.finish() == True:
                            FR1_BUTTON.updatePosition(zielfelder_list[15])
                            fr1.setPosition(zielfelder_list[15])
                            player_position["fr1"] = zielfelder_list[15]
                            player4.setFinish()
                        elif fr1.getMoved() > 43:
                            fr1.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fr1.getPosition(), "red", "fr1")
                            checkForOthers("fr1", currentPos)
                            FR1_BUTTON.updatePosition(currentPos)
                            fr1.setPosition(currentPos)
                if FR2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FR2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fr2.setMoved(dice_num)
                        if fr2.finish() == True:
                            FR2_BUTTON.updatePosition(zielfelder_list[14])
                            fr2.setPosition(zielfelder_list[14])
                            player_position["fr2"] = zielfelder_list[14]
                            player4.setFinish()
                        elif fr2.getMoved() > 43:
                            fr2.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fr2.getPosition(), "red", "fr2")
                            checkForOthers("fr2", currentPos)
                            FR2_BUTTON.updatePosition(currentPos)
                            fr2.setPosition(currentPos)
                if FR3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FR3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fr3.setMoved(dice_num)
                        if fr3.finish() == True:
                            FR3_BUTTON.updatePosition(zielfelder_list[13])
                            fr3.setPosition(zielfelder_list[13])
                            player_position["fr3"] = zielfelder_list[13]
                            player4.setFinish()
                        elif fr3.getMoved() > 43:
                            fr3.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fr3.getPosition(), "red", "fr3")
                            checkForOthers("fr3", currentPos)
                            FR3_BUTTON.updatePosition(currentPos)
                            fr3.setPosition(currentPos)
                if FR4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if FR4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        fr4.setMoved(dice_num)
                        if fr4.finish() == True:
                            FR4_BUTTON.updatePosition(zielfelder_list[12])
                            fr4.setPosition(zielfelder_list[12])
                            player_position["fr4"] = zielfelder_list[12]
                            player4.setFinish()
                        elif fr4.getMoved() > 43:
                            fr4.setMoved(dice_num * (-1))
                        else:
                            currentPos = makeMove(dice_num, fr4.getPosition(), "red", "fr4")
                            checkForOthers("fr4", currentPos)
                            FR4_BUTTON.updatePosition(currentPos)
                            fr4.setPosition(currentPos)

            elif event.type == pg.VIDEORESIZE:
                window = pg.display.set_mode(event.size, pg.RESIZABLE)
                gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, window.get_size())

        screen.fill(background_color)
        screen.blit(gamefield, gamefield_rect)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        DICE_BUTTON.changeColor(PLAY_MOUSE_POS)
        DICE_BUTTON.update(screen)

        updateFigureButtons(PLAY_MOUSE_POS)

        name1_BUTTON.update(screen)
        name2_BUTTON.update(screen)
        name3_BUTTON.update(screen)
        name4_BUTTON.update(screen)

        if image is not None:
            newDiceImage = scaleImage(image, 120, 120)
            screen.blit(newDiceImage, (1093, 170))

        pg.display.update()


def updateFigureButtons(PLAY_MOUSE_POS):
    FGE1_BUTTON.update(screen)
    FGE1_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGE2_BUTTON.update(screen)
    FGE2_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGE3_BUTTON.update(screen)
    FGE3_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGE4_BUTTON.update(screen)
    FGE4_BUTTON.changeColor(PLAY_MOUSE_POS)

    FGR1_BUTTON.update(screen)
    FGR1_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGR2_BUTTON.update(screen)
    FGR2_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGR3_BUTTON.update(screen)
    FGR3_BUTTON.changeColor(PLAY_MOUSE_POS)
    FGR4_BUTTON.update(screen)
    FGR4_BUTTON.changeColor(PLAY_MOUSE_POS)

    FR1_BUTTON.update(screen)
    FR1_BUTTON.changeColor(PLAY_MOUSE_POS)
    FR2_BUTTON.update(screen)
    FR2_BUTTON.changeColor(PLAY_MOUSE_POS)
    FR3_BUTTON.update(screen)
    FR3_BUTTON.changeColor(PLAY_MOUSE_POS)
    FR4_BUTTON.update(screen)
    FR4_BUTTON.changeColor(PLAY_MOUSE_POS)

    FB1_BUTTON.update(screen)
    FB1_BUTTON.changeColor(PLAY_MOUSE_POS)
    FB2_BUTTON.update(screen)
    FB2_BUTTON.changeColor(PLAY_MOUSE_POS)
    FB3_BUTTON.update(screen)
    FB3_BUTTON.changeColor(PLAY_MOUSE_POS)
    FB4_BUTTON.update(screen)
    FB4_BUTTON.changeColor(PLAY_MOUSE_POS)

def checkForOthers(player_name, new_position):
    # Überprüfen, ob das neue Feld bereits von einem anderen Spieler belegt ist
    for other_player, position in player_position.items():
        if other_player != player_name and position == new_position:
            print(f"The field {new_position} is already occupied by {other_player} !")
            player_position[other_player] = hauser_list[0]
            if other_player == "fge1":
                fge1.setPosition(hauser_list[0])
                FGE1_BUTTON.updatePosition(hauser_list[0])
                fge1.resetMoved()
                #yellowFigure_list[0] = 0
            if other_player == "fge2":
                fge2.setPosition(hauser_list[1])
                FGE2_BUTTON.updatePosition(hauser_list[1])
                fge2.resetMoved()
                #yellowFigure_list[1] = 0
            if other_player == "fge3":
                fge3.setPosition(hauser_list[2])
                FGE3_BUTTON.updatePosition(hauser_list[2])
                fge3.resetMoved()
                #yellowFigure_list[2] = 0
            if other_player == "fge4":
                fge4.setPosition(hauser_list[3])
                FGE4_BUTTON.updatePosition(hauser_list[3])
                fge4.resetMoved()
                #yellowFigure_list[3] = 0

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

    # Aktualisiere die Position des aktuellen Spielers
    player_position[player_name] = new_position

def makeMove(dice_num, position, color, currentFigure):
    if color == "yellow":
        if position == hauser_list[0] or position == hauser_list[1] or position == hauser_list[2] or position == hauser_list[3]:
            if dice_num == 6:
                position = field_list[0]
            else:
                print("Keine 6 gewürfelt. Nächster Spieler")
        else:
            for i in range(0, 40):
                if position == field_list[i]:
                    counter = i + dice_num
                    if counter > 39:
                        counter = counter - 40
                    position = field_list[counter]
                    break

    elif color == "green":
        if position == hauser_list[4] or position == hauser_list[5] or position == hauser_list[6] or position == hauser_list[7]:
            if dice_num == 6:
                position = field_list[10]
            else:
                print("Keine 6 gewürfelt. Nächster Spieler")
        else:
            for i in range(0, 40):
                if position == field_list[i]:
                    counter = i + dice_num
                    if counter > 39:
                        counter = counter - 40
                    position = field_list[counter]
                    break

    elif color == "blue":
        if position == hauser_list[8] or position == hauser_list[9] or position == hauser_list[10] or position == hauser_list[11]:
            if dice_num == 6:
                position = field_list[20]
            else:
                print("Keine 6 gewürfelt. Nächster Spieler")
        else:
            for i in range(0, 40):
                if position == field_list[i]:
                    counter = i + dice_num
                    if counter > 39:
                        counter = counter - 40
                    position = field_list[counter]
                    break

    elif color == "red":
        if position == hauser_list[12] or position == hauser_list[13] or position == hauser_list[14] or  position == hauser_list[15]:
            if dice_num == 6:
                position = field_list[30]
            else:
                print("Keine 6 gewürfelt. Nächster Spieler")
        else:
            for i in range(0, 40):
                if position == field_list[i]:
                    counter = i + dice_num
                    if counter > 39:
                        counter = counter - 40
                    position = field_list[counter]
                    break

    #checkForOthers(currentFigure, position)
    return position

def winner(winPlayer):
    pg.display.set_caption("Don't get ANGRY!")
    BG = scaleImage(pg.image.load("assets/mainscreen.png"), 1280, 720)


    QUIT_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(640, 550),
                         text_input="QUIT", font=get_font(75), base_color="White", hovering_color="#fcce8d")

    while True:
        screen.blit(BG, (0, 0))  # Background on the screen

        ENDSCREEN_MOUSE_POS = pg.mouse.get_pos()

        ENDSCREEN_TEXT = get_font(30).render("The winner is player " + str(winPlayer) , True, "#856c4a")  # Textfield
        ENDSCREEN_RECT = ENDSCREEN_TEXT.get_rect(center=(640, 150))

        screen.blit(ENDSCREEN_TEXT, ENDSCREEN_RECT)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
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