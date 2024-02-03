from random import random


class GameField:
    # Koordinaten der Felder
    # Koordinaten der Figuren
    # figurbewegen
    # figurschlagen
    # startpositon --> Koordinaten setzen
    # hat gewonnen

    def __init__(self):
        self.field_list = self.fields()
        #self.figure_list = figures
        #self.dice = dice

    def fields(self):
        # Koordinaten für Felder

        # Felder 1-5 (Startfeld gelb --> hoch)
        f1 = [577, 660] # gelbes Startfeld
        f2 = [577, 600]
        f3 = [577, 539]
        f4 = [577, 479]
        f5 = [577, 418]

        # Felder 6-9 (nach links)
        f6 = [517, 418]
        f7 = [457, 418]
        f8 = [397, 418]
        f9 = [335, 418]

        # Felder 10-11 (hoch)
        f10 = [335, 358]
        f11 = [335, 297] # grünes Startfeld

        # Felder 12-15 (nach rechts)
        f12 = [397, 297]
        f13 = [457, 297]
        f14 = [517, 297]
        f15 = [577, 297]

        # Felder 16-19 (nach oben)
        f16 = [577, 237]
        f17 = [577, 177]
        f18 = [577, 116]
        f19 = [577, 56]

        # Felder 20-21 (nach rechts)
        f20 = [637, 56]
        f21 = [697, 56] # blaues Startfeld

        # Felder 22-25 (nach unten)
        f22 = [697, 116]
        f23 = [697, 177]
        f24 = [697, 237]
        f25 = [697, 297]

        # Felder 26-29 (nach rechts)
        f26 = [757, 297]
        f27 = [817, 297]
        f28 = [878, 297]
        f29 = [938, 297]

        # Felder30-31 (nach unten)
        f30 = [938, 358]
        f31 = [938, 418] # rotes Startfeld

        # Felder 32-35 (nach links)
        f32 = [878, 418]
        f33 = [817, 418]
        f34 = [757, 418]
        f35 = [697, 418]

        # Felder 36-39 (nach unten)
        f36 = [697, 479]
        f37 = [697, 539]
        f38 = [697, 600]
        f39 = [697, 660]

        # Feld 40 (nach links)
        f40 = [637, 660]
        field_list = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21,
                      f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39,
                      f40]
        return field_list

    def houses(self):
        # Koordinaten für Häuser

        # Gelbe Häuser
        hge1 = [335, 600]
        hge2 = [395, 600]
        hge3 = [335, 660]
        hge4 = [395, 660]

        # Grüne Häuser
        hgr1 = [335, 56]
        hgr2 = [395, 56]
        hgr3 = [335, 116]
        hgr4 = [395, 116]

        # Blaue Häuser
        hb1 = [878, 56]
        hb2 = [938, 56]
        hb3 = [878, 116]
        hb4 = [938, 116]

        # Rote Häuser
        hr1 = [878, 600]
        hr2 = [938, 600]
        hr3 = [878, 660]
        hr4 = [938, 660]

        hauser_list = [hge1, hge2, hge3, hge4, hgr1, hgr2, hgr3, hgr4, hb1, hb2, hb3, hb4, hr1, hr2, hr3, hr4]
        return hauser_list

    def finishFields(self):
        # Zielfelder

        # Gelbe Zielfelder
        zge1 = [636, 600]
        zge2 = [636, 539]
        zge3 = [636, 479]
        zge4 = [636, 418]

        # Grüne Zielfelder
        zgr1 = [397, 358]
        zgr2 = [457, 358]
        zgr3 = [517, 358]
        zgr4 = [577, 358]

        # Blaue Zielfelder
        zb1 = [636, 116]
        zb2 = [636, 177]
        zb3 = [636, 237]
        zb4 = [636, 297]

        # Rote zielfelder
        zr1 = [878, 358]
        zr2 = [817, 358]
        zr3 = [757, 358]
        zr4 = [697, 358]

        zielfelder_list = [zge1, zge2, zge3, zge4, zgr1, zgr2, zgr3, zgr4, zb1, zb2, zb3, zb4, zr1, zr2, zr3, zr4]
        return zielfelder_list

    def startPosition(self, color):
        if color == "yellow":
            return self.field_list[0]
        elif color == "green":
            return self.field_list[10]
        elif color == "blue":
            return self.field_list[20]
        elif color == "red":
            return self.field_list[30]

    #def coordinatesFigures(self):


#spielfeld = GameField()
#this_list = spielfeld.felder()
#print(spielfeld.startPosition("yellow"))


