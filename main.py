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
pg.display.set_caption("Menü")
BG = pg.image.load("assets/background.png")

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
    pg.display.set_caption("Mensch ärger Dich nicht")
    background_color = "#fcce8d"
    gamefield = pg.image.load("assets/gamefield.png")
    gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, screen.get_size())

    PLAY_BACK = Button(image=None, pos=(1165, 670),
                       text_input="BACK", font=get_font(30), base_color="Black", hovering_color="WHITE")

    GAME_ACTIVE = Button(image=None, pos=(100, 670), text_input="START", font=get_font(40),
                         base_color="Black", hovering_color="WHITE")

    # Text für Spieler-Aufforderung
    prompt_text = "Press Enter, to add a player"
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
                        prompt_text = "Spieler Namen eingeben"
                    else:
                        for i in range(len(saved_name_texts)):
                            if not saved_name_texts[i] and input_text:
                                saved_name_texts[i] = input_text
                                input_text = ""
                                cursor_timer = 0
                                if i == max_players - 1:
                                    cursor_active = False
                                    prompt_text = "Alle Spieler eingetragen"
                                else:
                                    prompt_text = "Spieler Namen eingeben"
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
    pg.display.set_caption("Mensch ärger Dich nicht")
    background_color = "#fcce8d"
    gamefield = pg.image.load("assets/gamefield.png")
    gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, screen.get_size())

    PLAY_BACK = Button(image=None, pos=(1165, 670),
                       text_input="BACK", font=get_font(30), base_color="Black", hovering_color="WHITE")

    DICE_BUTTON = Button(image=scaleImage(pg.image.load("assets/wuerfel.png"), 200, 200), pos=(1150, 90),
                         text_input="Roll the Dice",
                         font=get_font(10), base_color="BLACK", hovering_color="WHITE")

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
                    #FGE1_BUTTON.updatePosition(field_list[1])
                if DICE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    dice = Dice()
                    dice_num = dice.roll_dice()
                    image = imageNumOfPoints(dice_num)
            elif event.type == pg.VIDEORESIZE:
                window = pg.display.set_mode(event.size, pg.RESIZABLE)
                gamefield, gamefield_rect = transform_scale_keep_ratio(gamefield, window.get_size())

        screen.fill(background_color)
        screen.blit(gamefield, gamefield_rect)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        DICE_BUTTON.changeColor(PLAY_MOUSE_POS)
        DICE_BUTTON.update(screen)

        FGE1_BUTTON.update(screen)
        FGE2_BUTTON.update(screen)
        FGE3_BUTTON.update(screen)
        FGE4_BUTTON.update(screen)

        if image is not None:
            newDiceImage = scaleImage(image, 150, 150)
            screen.blit(newDiceImage, (1100, 150))

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
    pg.display.set_caption("Menü")

    while True:
        screen.blit(BG, (0,0))  #Background on the screen

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")  # Textfield
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        RULES_BUTTON = Button(image=pg.image.load("assets/Rules_Rect.png"), pos=(640, 400),
                                text_input="Rules", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pg.image.load("assets/Quit_Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

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

# Yellow Figures:
FGE1_BUTTON = Button(image=scaleImage(pg.image.load("assets/figyellow.png"), 50, 50), pos=(hauser_list[0]),
                     text_input="", font=get_font(0),
                     base_color="BLACK", hovering_color="BLACK")
FGE2_BUTTON = Button(image=scaleImage(pg.image.load("assets/figyellow.png"), 50, 50), pos=(hauser_list[1]),
                     text_input="", font=get_font(0),
                     base_color="BLACK", hovering_color="BLACK")
FGE3_BUTTON = Button(image=scaleImage(pg.image.load("assets/figyellow.png"), 50, 50), pos=(hauser_list[2]),
                     text_input="", font=get_font(0),
                     base_color="BLACK", hovering_color="BLACK")
FGE4_BUTTON = Button(image=scaleImage(pg.image.load("assets/figyellow.png"), 50, 50), pos=(hauser_list[3]),
                     text_input="", font=get_font(0),
                     base_color="BLACK", hovering_color="BLACK")

main_menu()