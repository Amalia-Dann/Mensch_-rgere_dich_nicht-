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
gray = (200, 200, 200)
blue = (0, 128, 255)

# fonts
font = pg.font.Font(None, 36)
input_font = pg.font.Font(None, 32)

#create Object
playground = GameField()
field_list = playground.fields()
hauser_list = playground.houses()
zielfelder_list = playground.finishFields()

player_position = { }


def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("assets/font.ttf", size)

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

def imageNumOfPoints(dice_num):
    if dice_num == 1:
        diceImage = pg.image.load("assets/Augenzahl1.png")
        return diceImage
    if dice_num == 2:
        diceImage = pg.image.load("assets/Augenzahl2.png")
        return diceImage
    if dice_num == 3:
        diceImage = pg.image.load("assets/Augenzahl3.png")
        return diceImage
    if dice_num == 4:
        diceImage = pg.image.load("assets/Augenzahl4.png")
        return diceImage
    if dice_num == 5:
        diceImage = pg.image.load("assets/Augenzahl5.png")
        return diceImage
    if dice_num == 6:
        diceImage = pg.image.load("assets/Augenzahl6.png")
        return diceImage
def play():
    pg.display.set_caption("Don't get ANGRY!")
    background_color = "#fcce8d"
    gamefield = pg.image.load("assets/gamefield.png")
    gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, screen.get_size())

    PLAY_BACK = Button(image=None, pos=(1165, 670),
                       text_input="BACK", font=get_font(30), base_color="Black", hovering_color="WHITE")


    GAME_ACTIVE = Button(image = None, pos = (135, 670), text_input = "START", font = get_font(30),
                         base_color = "Black", hovering_color = "WHITE")

    # Text für Spieler-Aufforderung
    prompt_text = ("Press Enter, to add a player")
    prompt_rect = pg.Rect(20, 50, 200, 40)

    # Eingabefeld
    input_rect = pg.Rect(20, 100, 200, 40)
    input_text = ""
    cursor_active = False
    cursor_timer = 0  # Timer für den Cursor-Blinkeffekt

    # Größe des Cursors
    cursor_size = 2

    # Gespeicherte Namen
    max_players = 4
    saved_name_rects = [pg.Rect(20, 190 + i * 80, 200, 40) for i in range(max_players)]
    saved_name_texts = [""] * max_players


    image = None
    active_play = False

    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
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
                    if event.key == pg.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if GAME_ACTIVE.checkForInput(PLAY_MOUSE_POS):
                    gameLoop(saved_name_texts)
            elif event.type == pg.VIDEORESIZE:
                window = pg.display.set_mode(event.size, pg.RESIZABLE)
                gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, window.get_size())

        screen.fill(background_color)
        screen.blit(gamefield, gamefield_rect)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        GAME_ACTIVE.changeColor(PLAY_MOUSE_POS)
        GAME_ACTIVE.update(screen)

        # Spieler-Aufforderung anzeigen
        prompt_surface = font.render(prompt_text, True, black)
        screen.blit(prompt_surface, (prompt_rect.x + 5, prompt_rect.y + 5))

        # Eingabefeld zeichnen, wenn aktiv
        if cursor_active:
            pg.draw.rect(screen, gray, input_rect)
            pg.draw.rect(screen, black, input_rect, 2)
            input_surface = input_font.render(input_text, True, black)
            screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

            # Cursor-Blinkeffekt
            if pg.time.get_ticks() % 1000 < 500:
                cursor_height = input_surface.get_height()
                cursor_rect = pg.Rect(input_rect.x + 5 + input_surface.get_width(), input_rect.y + 5, cursor_size,
                                      cursor_height)
                pg.draw.rect(screen, black, cursor_rect)

        # Gespeicherte Namen anzeigen
        for i in range(len(saved_name_texts)):
            if saved_name_texts[i]:
                pg.draw.rect(screen, blue, saved_name_rects[i])
                pg.draw.rect(screen, "#fcce8d", saved_name_rects[i], 2)
                saved_name_surface = font.render(saved_name_texts[i], True, black)
                screen.blit(saved_name_surface, (saved_name_rects[i].x + 5, saved_name_rects[i].y + 5))


        pg.display.update()

def gameLoop(player_list):
    pg.display.set_caption("Don't get ANGRY!")
    background_color = "#fcce8d"
    gamefield = pg.image.load("assets/gamefield.png")
    gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, screen.get_size())

    PLAY_BACK = Button(image=None, pos=(1165, 670),
                       text_input="BACK", font=get_font(30), base_color="Black", hovering_color="WHITE")

    DICE_BUTTON = Button(image=scaleImage(pg.image.load("assets/wuerfel.png"), 200, 200), pos=(1150, 90),
                         text_input="Roll the Dice",
                         font=get_font(10), base_color="BLACK", hovering_color="WHITE")

    counter_fge1 = 0

    image = None


    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DICE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    dice = Dice()
                    dice_num = dice.roll_dice()
                    image = imageNumOfPoints(dice_num)

                #Buttons for Yellow Figures 1-4
                if FGE1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fge1.getPosition(), "yellow", "fge1")
                    checkForOthers("fge1", currentPos)
                    FGE1_BUTTON.updatePosition(currentPos)
                    fge1.setPosition(currentPos)
                    #yellowFigure_list[0] += dice_num
                if FGE2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fge2.getPosition(), "yellow", "fge2")
                    checkForOthers("fge2", currentPos)
                    FGE2_BUTTON.updatePosition(currentPos)
                    fge2.setPosition(currentPos)
                if FGE3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fge3.getPosition(), "yellow", "fge3")
                    checkForOthers("fge3", currentPos)
                    FGE3_BUTTON.updatePosition(currentPos)
                    fge3.setPosition(currentPos)
                if FGE4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fge4.getPosition(), "yellow", "fge4")
                    checkForOthers("fge4", currentPos)
                    FGE4_BUTTON.updatePosition(currentPos)
                    fge4.setPosition(currentPos)

                # Buttons for Green Figures 1-4
                if FGR1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fgr1.getPosition(), "green", "fgr1")
                    checkForOthers("fgr1", currentPos)
                    FGR1_BUTTON.updatePosition(currentPos)
                    fgr1.setPosition(currentPos)
                if FGR2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fgr2.getPosition(), "green", "fgr2")
                    checkForOthers("fgr2", currentPos)
                    FGR2_BUTTON.updatePosition(currentPos)
                    fgr2.setPosition(currentPos)
                if FGR3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fgr3.getPosition(), "green", "fgr3")
                    checkForOthers("fgr3", currentPos)
                    FGR3_BUTTON.updatePosition(currentPos)
                    fgr3.setPosition(currentPos)
                if FGR4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fgr4.getPosition(), "green", "fgr4")
                    checkForOthers("fgr4", currentPos)
                    FGR4_BUTTON.updatePosition(currentPos)
                    fgr4.setPosition(currentPos)

                # Buttons for Blue Figures 1-4
                if FB1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fb1.getPosition(), "blue", "fb1")
                    checkForOthers("fb1", currentPos)
                    FB1_BUTTON.updatePosition(currentPos)
                    fb1.setPosition(currentPos)
                if FB2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fb2.getPosition(), "blue", "fb2")
                    checkForOthers("fb2", currentPos)
                    FB2_BUTTON.updatePosition(currentPos)
                    fb2.setPosition(currentPos)
                if FB3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fb3.getPosition(), "blue", "fb3")
                    checkForOthers("fb3", currentPos)
                    FB3_BUTTON.updatePosition(currentPos)
                    fb3.setPosition(currentPos)
                if FB4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fb4.getPosition(), "blue", "fb4")
                    checkForOthers("fb4", currentPos)
                    FB4_BUTTON.updatePosition(currentPos)
                    fb4.setPosition(currentPos)

                # Buttons for Red Figures 1-4
                if FR1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fr1.getPosition(), "red", "fr1")
                    checkForOthers("fr1", currentPos)
                    FR1_BUTTON.updatePosition(currentPos)
                    fr1.setPosition(currentPos)
                if FR2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fr2.getPosition(), "red", "fr2")
                    checkForOthers("fr2", currentPos)
                    FR2_BUTTON.updatePosition(currentPos)
                    fr2.setPosition(currentPos)
                if FR3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    currentPos = makeMove(dice_num, fr3.getPosition(), "red", "fr3")
                    checkForOthers("fr3", currentPos)
                    FR3_BUTTON.updatePosition(currentPos)
                    fr3.setPosition(currentPos)
                if FR4_BUTTON.checkForInput(PLAY_MOUSE_POS):
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
            if other_player == "fge2":
                fge2.setPosition(hauser_list[1])
                FGE2_BUTTON.updatePosition(hauser_list[1])
            if other_player == "fge3":
                fge3.setPosition(hauser_list[2])
                FGE3_BUTTON.updatePosition(hauser_list[2])
            if other_player == "fge4":
                fge4.setPosition(hauser_list[3])
                FGE4_BUTTON.updatePosition(hauser_list[3])

            if other_player == "fr1":
                fr1.setPosition(hauser_list[12])
                FR1_BUTTON.updatePosition(hauser_list[12])
            if other_player == "fr2":
                fr2.setPosition(hauser_list[13])
                FR2_BUTTON.updatePosition(hauser_list[13])
            if other_player == "fr3":
                fr3.setPosition(hauser_list[14])
                FR3_BUTTON.updatePosition(hauser_list[14])
            if other_player == "fr4":
                fr4.setPosition(hauser_list[15])
                FR4_BUTTON.updatePosition(hauser_list[15])

            if other_player == "fb1":
                fb1.setPosition(hauser_list[8])
                FB1_BUTTON.updatePosition(hauser_list[8])
            if other_player == "fb2":
                fb2.setPosition(hauser_list[9])
                FB2_BUTTON.updatePosition(hauser_list[9])
            if other_player == "fb3":
                fb3.setPosition(hauser_list[10])
                FB3_BUTTON.updatePosition(hauser_list[10])
            if other_player == "fb4":
                fb4.setPosition(hauser_list[11])
                FB4_BUTTON.updatePosition(hauser_list[11])

            if other_player == "fgr1":
                fgr1.setPosition(hauser_list[4])
                FGR1_BUTTON.updatePosition(hauser_list[4])
            if other_player == "fgr2":
                fgr2.setPosition(hauser_list[5])
                FGR2_BUTTON.updatePosition(hauser_list[5])
            if other_player == "fgr3":
                fgr3.setPosition(hauser_list[6])
                FGR3_BUTTON.updatePosition(hauser_list[6])
            if other_player == "fgr4":
                fgr4.setPosition(hauser_list[7])
                FGR4_BUTTON.updatePosition(hauser_list[7])

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

def winner(counter):
    if player1.winner(yellowFigure_list) == True:
        print("Gelb hat gewonnen")
        while True:
            screen.fill("#fcce8d")
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            pg.display.update()


def rules():
    while True:
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()

        screen.fill("#fcce8d")
        #schrift = pg.font.SysFont('Arial', 24)
        schrift = get_font(25)

        def draw_text(text):
            #font = pg.font.SysFont("arial", 25)
            font = get_font(12)
            y_pos = 15
            x_pos = 20

            for line in text.splitlines():
                rendered_line = font.render(line, 1, (0, 0, 0))
                screen.blit(rendered_line, (x_pos, y_pos))
                #pg.display.update()

                # Aktualisiere die y-Position für die nächste Zeile
                y_pos += 21

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
                "The player jumps over their own and enemy pieces standing in the way, but the occupied square \n"
                "is also counted. \n\n"
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

        RULES_BACK = Button(image=None, pos=(1200, 690),
                              text_input="BACK", font=get_font(20), base_color="Black", hovering_color="White")

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if RULES_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        RULES_BACK.changeColor(OPTIONS_MOUSE_POS)
        RULES_BACK.update(screen)

        pg.display.update()

def main_menu():
    pg.display.set_caption("Don't get ANGRY!")
    BG = scaleImage(pg.image.load("assets/mainscreen.png"), 1280, 720)
    while True:
        screen.blit(BG, (0,0))  #Background on the screen

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = get_font(75).render("Don't get ANGRY!", True, "#856c4a")  # Textfield
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(340, 270),
                             text_input="PLAY", font=get_font(75), base_color="White", hovering_color="#fcce8d")
        RULES_BUTTON = Button(image=scaleImage(pg.image.load("assets/Play_Rect.png"),430,109 ), pos=(340, 420),
                                text_input="RULES", font=get_font(75), base_color="White", hovering_color="#fcce8d")
        QUIT_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(340, 570),
                             text_input="QUIT", font=get_font(75), base_color="White", hovering_color="#fcce8d")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, RULES_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()  #run play function
                if RULES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    rules() #run options function
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()

# Create Figure-Objects
fge1 = Figure(position=hauser_list[0], color="yellow")
fge2 = Figure(position=hauser_list[1], color="yellow")
fge3 = Figure(position=hauser_list[2], color="yellow")
fge4 = Figure(position=hauser_list[3], color="yellow")
yellowFigure_list = [0, 0, 0, 0]

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
player1 = Player("Horst", "yellow", yellowFigure_list)

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