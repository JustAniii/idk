#variablen
kl: float = 0
x: float = 0
y: float = 0
x05 = 0
y05 = 0
pins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
end = 0
end1 = 0

while end < 1:
    # messwerte werden importiert
    m1 = float(input("Messwert 1 eingeben: "))
    m2 = float(input("Messwert 2 eingeben: "))
    m3 = float(input("Messwert 3 eingeben: "))
    m4 = float(input("Messwert 4 eingeben: "))
    kl = float(input("Kantenlänge eingeben(cm): "))

    gm = m1 + m2 + m3 + m4 #berechnung der gesamt kraft
    x = kl * (m2 +m4) / gm #berechnung der x-achsen
    y = kl * (m3 +m4) / gm #berechnung der y-achse

    m1p = m1 * 100 / gm
    m2p = m2 * 100 / gm
    m3p = m3 * 100 / gm
    m4p = m4 * 100 / gm

    print("kraft an sensor 1 = " + str(m1) + "  (" + str(m1p) + "%)")
    print("kraft an sensor 2 = " + str(m2) + "  (" + str(m2p) + "%)")
    print("kraft an sensor 3 = " + str(m3) + "  (" + str(m3p) + "%)")
    print("kraft an sensor 4 = " + str(m4) + "  (" + str(m4p) + "%)")
    print("gesamte kraft: " + str(gm))
    print("x = " + str(x)) #darstellung der x-achse
    print("y = " + str(y)) #darstellung der y-achse
    print(" ")
#berechnung der richtigen reihe
    if y <= kl / 8 * 1: #berechnung der richtigen spalte
        if x <= kl / 8 * 1:
            pins[0] = pins[0] + 1
        elif x <= kl / 8 * 2:
            pins[1] = pins[1] + 1
        elif x <= kl / 8 * 3:
            pins[2] = pins[2] + 1
        elif x <= kl / 8 * 4:
            pins[3] = pins[3] + 1
        elif x <= kl / 8 * 5:
            pins[4] = pins[4] + 1
        elif x <= kl / 8 * 6:
            pins[5] = pins[5] + 1
        elif x <= kl / 8 * 7:
            pins[6] = pins[6] + 1
        else:
            pins[7] = pins[7] + 1

    elif y <= kl / 8 * 2:
        if x <= kl / 8 * 1:
            pins[8] = pins[8] + 1
        elif x <= kl / 8 * 2:
            pins[9] = pins[9] + 1
        elif x <= kl / 8 * 3:
            pins[10] = pins[10] + 1
        elif x <= kl / 8 * 4:
            pins[11] = pins[11] + 1
        elif x <= kl / 8 * 5:
            pins[12] = pins[12] + 1
        elif x <= kl / 8 * 6:
            pins[13] = pins[13] + 1
        elif x <= kl / 8 * 7:
            pins[14] = pins[14] + 1
        else:
            pins[15] = pins[15] + 1

    elif y <= kl / 8 * 3:
        if x <= kl / 8 * 1:
            pins[16] = pins[16] + 1
        elif x <= kl / 8 * 2:
            pins[17] = pins[17] + 1
        elif x <= kl / 8 * 3:
            pins[18] = pins[18] + 1
        elif x <= kl / 8 * 4:
            pins[19] = pins[19] + 1
        elif x <= kl / 8 * 5:
            pins[20] = pins[20] + 1
        elif x <= kl / 8 * 6:
            pins[21] = pins[21] + 1
        elif x <= kl / 8 * 7:
            pins[22] = pins[22] + 1
        else:
            pins[23] = pins[23] + 1

    elif y <= kl / 8 * 4:
        if x <= kl / 8 * 1:
            pins[24] = pins[24] + 1
        elif x <= kl / 8 * 2:
            pins[25] = pins[25] + 1
        elif x <= kl / 8 * 3:
            pins[26] = pins[26] + 1
        elif x <= kl / 8 * 4:
            pins[27] = pins[27] + 1
        elif x <= kl / 8 * 5:
            pins[28] = pins[28] + 1
        elif x <= kl / 8 * 6:
            pins[29] = pins[29] + 1
        elif x <= kl / 8 * 7:
            pins[30] = pins[30] + 1
        else:
            pins[31] = pins[31] + 1

    elif y <= kl / 8 * 5:
        if x <= kl / 8 * 1:
            pins[32] = pins[32] + 1
        elif x <= kl / 8 * 2:
            pins[33] = pins[33] + 1
        elif x <= kl / 8 * 3:
            pins[34] = pins[34] + 1
        elif x <= kl / 8 * 4:
            pins[35] = pins[35] + 1
        elif x <= kl / 8 * 5:
            pins[36] = pins[36] + 1
        elif x <= kl / 8 * 6:
            pins[37] = pins[37] + 1
        elif x <= kl / 8 * 7:
            pins[38] = pins[38] + 1
        else:
            pins[39] = pins[39] + 1

    elif y <= kl / 8 * 6:
        if x <= kl / 8 * 1:
            pins[40] = pins[40] + 1
        elif x <= kl / 8 * 2:
            pins[41] = pins[41] + 1
        elif x <= kl / 8 * 3:
            pins[42] = pins[42] + 1
        elif x <= kl / 8 * 4:
            pins[43] = pins[43] + 1
        elif x <= kl / 8 * 5:
            pins[44] = pins[44] + 1
        elif x <= kl / 8 * 6:
            pins[45] = pins[45] + 1
        elif x <= kl / 8 * 7:
            pins[46] = pins[46] + 1
        else:
            pins[47] = pins[47] + 1

    elif y <= kl / 8 * 7:
        if x <= kl / 8 * 1:
            pins[48] = pins[48] + 1
        elif x <= kl / 8 * 2:
            pins[49] = pins[49] + 1
        elif x <= kl / 8 * 3:
            pins[50] = pins[50] + 1
        elif x <= kl / 8 * 4:
            pins[51] = pins[51] + 1
        elif x <= kl / 8 * 5:
            pins[52] = pins[52] + 1
        elif x <= kl / 8 * 6:
            pins[53] = pins[53] + 1
        elif x <= kl / 8 * 7:
            pins[54] = pins[54] + 1
        else:
            pins[55] = pins[55] + 1

    else:
        if x <= kl / 8 * 1:
            pins[56] = pins[56] + 1
        elif x <= kl / 8 * 2:
            pins[57] = pins[57] + 1
        elif x <= kl / 8 * 3:
            pins[58] = pins[58] + 1
        elif x <= kl / 8 * 4:
            pins[59] = pins[59] + 1
        elif x <= kl / 8 * 5:
            pins[60] = pins[60] + 1
        elif x <= kl / 8 * 6:
            pins[61] = pins[61] + 1
        elif x <= kl / 8 * 7:
            pins[62] = pins[62] + 1
        else:
            pins[63] = pins[63] + 1

    #darstellung der werte in einer tabelle
    print("     1 2 3 4   5 6 7 8 ")
    print("     - - - -   - - - -")
    print("R1 = " + str(pins[0]) + " " + str(pins[1]) + " " + str(pins[2]) + " " + str(pins[3]) + "   " + str(pins[4]) + " " + str(pins[5]) + " " + str(pins[6]) + " " + str(pins[7]) + " " )
    print("R2 = " + str(pins[8]) + " " + str(pins[9]) + " " + str(pins[10]) + " " + str(pins[11]) + "   " + str(pins[12]) + " " + str(pins[13]) + " " + str(pins[14]) + " " + str(pins[15]) + " " )
    print("R3 = " + str(pins[16]) + " " + str(pins[17]) + " " + str(pins[18]) + " " + str(pins[19]) + "   " + str(pins[20]) + " " + str(pins[21]) + " " + str(pins[22]) + " " + str(pins[23]) + " " )
    print("R4 = " + str(pins[24]) + " " + str(pins[25]) + " " + str(pins[26]) + " " + str(pins[27]) + "   " + str(pins[28]) + " " + str(pins[29]) + " " + str(pins[30]) + " " + str(pins[31]) + " " )
    print(" ")
    print("R5 = " + str(pins[32]) + " " + str(pins[33]) + " " + str(pins[34]) + " " + str(pins[35]) + "   " +  str(pins[36]) + " " + str(pins[37]) + " " + str(pins[38]) + " " + str(pins[39]) + " " )
    print("R6 = " + str(pins[40]) + " " + str(pins[41]) + " " + str(pins[42]) + " " + str(pins[43]) + "   " +  str(pins[44]) + " " + str(pins[45]) + " " + str(pins[46]) + " " + str(pins[47]) + " " )
    print("R7 = " + str(pins[48]) + " " + str(pins[49]) + " " + str(pins[50]) + " " + str(pins[51]) + "   " + str(pins[52]) + " " + str(pins[53]) + " " + str(pins[54]) + " " + str(pins[55]) + " "  )
    print("R8 = " + str(pins[56]) + " " + str(pins[57]) + " " + str(pins[58]) + " " + str(pins[59]) + "   " + str(pins[60]) + " " + str(pins[61]) + " " + str(pins[62]) + " " + str(pins[63]) + " " )
    
