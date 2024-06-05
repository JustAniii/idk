#variablen
kl: float = 0
x: float = 0
y: float = 0
x05 = 0
y05 = 0
pins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
end = 0
end1 = 0

def calc(x: float, kl: float, pins: list, start: int):
    pins_new = None
    pins_new = pins
    if x <= kl / 8 * 1:
        pins_new[start] = pins_new[start] + 1
    elif x <= kl / 8 * 2:
        pins_new[start + 1] = pins_new[start + 1] + 1
    elif x <= kl / 8 * 3:
        pins_new[start + 2] = pins_new[start + 2] + 1
    elif x <= kl / 8 * 4:
        pins_new[start + 3] = pins_new[start + 3] + 1
    elif x <= kl / 8 * 5:
        pins_new[start + 4] = pins_new[start + 4] + 1
    elif x <= kl / 8 * 6:
        pins_new[start + 5] = pins_new[start + 5] + 1
    elif x <= kl / 8 * 7:
        pins_new[start + 6] = pins_new[start + 6] + 1
    else:
        pins_new[start + 7] = pins_new[start + 7] + 1
    return pins_new

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
        pins = calc(x, kl, pins, 0)
    elif y <= kl / 8 * 2:
        pins = calc(x, kl, pins, 8)
    elif y <= kl / 8 * 3:
        pins = calc(x, kl, pins, 16)
    elif y <= kl / 8 * 4:
        pins = calc(x, kl, pins, 24)
    elif y <= kl / 8 * 5:
        pins = calc(x, kl, pins, 32)
    elif y <= kl / 8 * 6:
        pins = calc(x, kl, pins, 40)
    elif y <= kl / 8 * 7:
        pins = calc(x, kl, pins, 48)
    else:
        pins = calc(x, kl, pins, 56)

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
    
