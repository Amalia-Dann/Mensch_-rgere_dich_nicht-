class GameField:
    def __init__(self):
        self.fieldList = self.fields()

    def fields(self):
        # initializing the fields

        # fields 1-5
        f1 = [577, 660] # starting field yellow
        f2 = [577, 600]
        f3 = [577, 539]
        f4 = [577, 479]
        f5 = [577, 418]

        # fields 6-9
        f6 = [517, 418]
        f7 = [457, 418]
        f8 = [397, 418]
        f9 = [335, 418]

        # fields 10-11
        f10 = [335, 358]
        f11 = [335, 297] # starting field green

        # fields 12-15
        f12 = [397, 297]
        f13 = [457, 297]
        f14 = [517, 297]
        f15 = [577, 297]

        # fields 16-19
        f16 = [577, 237]
        f17 = [577, 177]
        f18 = [577, 116]
        f19 = [577, 56]

        # fields 20-21
        f20 = [637, 56]
        f21 = [697, 56] # starting field blue

        # fields 22-25
        f22 = [697, 116]
        f23 = [697, 177]
        f24 = [697, 237]
        f25 = [697, 297]

        # fields 26-29
        f26 = [757, 297]
        f27 = [817, 297]
        f28 = [878, 297]
        f29 = [938, 297]

        # fields 30-31
        f30 = [938, 358]
        f31 = [938, 418] # starting field red

        # fields 32-35
        f32 = [878, 418]
        f33 = [817, 418]
        f34 = [757, 418]
        f35 = [697, 418]

        # fields 36-39
        f36 = [697, 479]
        f37 = [697, 539]
        f38 = [697, 600]
        f39 = [697, 660]

        # fields 40
        f40 = [637, 660]

        # list of fields
        fieldList = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21,
                      f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39,
                      f40]
        return fieldList

    def houses(self):
        # Coordinates for houses

        # Yellow houses
        hge1 = [335, 600]
        hge2 = [395, 600]
        hge3 = [335, 660]
        hge4 = [395, 660]

        # green houses
        hgr1 = [335, 56]
        hgr2 = [395, 56]
        hgr3 = [335, 116]
        hgr4 = [395, 116]

        # blue houses
        hb1 = [878, 56]
        hb2 = [938, 56]
        hb3 = [878, 116]
        hb4 = [938, 116]

        # red houses
        hr1 = [878, 600]
        hr2 = [938, 600]
        hr3 = [878, 660]
        hr4 = [938, 660]

        # list of houses
        hauserList = [hge1, hge2, hge3, hge4, hgr1, hgr2, hgr3, hgr4, hb1, hb2, hb3, hb4, hr1, hr2, hr3, hr4]
        return hauserList

    def finishFields(self):
        # target fields

        # Yellow target fields
        zge1 = [637, 599]
        zge2 = [637, 539]
        zge3 = [637, 478]
        zge4 = [637, 418]

        # green target fields
        zgr1 = [397, 357]
        zgr2 = [457, 357]
        zgr3 = [517, 357]
        zgr4 = [577, 357]

        # blue target fields
        zb1 = [636, 116]
        zb2 = [636, 176]
        zb3 = [636, 237]
        zb4 = [636, 297]

        # red target fields
        zr1 = [878, 357]
        zr2 = [817, 357]
        zr3 = [757, 357]
        zr4 = [697, 357]

        # list of target fields
        zielfelderList = [zge1, zge2, zge3, zge4, zgr1, zgr2, zgr3, zgr4, zb1, zb2, zb3, zb4, zr1, zr2, zr3, zr4]
        return zielfelderList

    # defining the starting fields of the colors
    def startPosition(self, color):
        if color == "yellow":
            return self.field_list[0]
        elif color == "green":
            return self.field_list[10]
        elif color == "blue":
            return self.field_list[20]
        elif color == "red":
            return self.field_list[30]