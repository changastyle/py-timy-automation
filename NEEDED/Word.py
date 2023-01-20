class Word:

    nombre = ""
    x = -1
    y = -1
    h = -1
    w = -1

    def __init__(self, nombre , x, y, h, w):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.h = h
        self.w = w

    def anchoFinal(self):
        final = self.x + self.w
        return final

    def altoFinal(self):
        final = self.y + self.h
        return final

    def medio(self):
        finalX = self.anchoFinal()
        finalY = self.altoFinal()

        medioX = int(self.x + ((finalX - self.x)/2))
        medioY = int(self.y + ((finalY - self.y)/2))

        return [medioX, medioY]

    def __str__(self):
        return "WORD(" + str(self.nombre) +"): POS (" + str(self.x) +"," + str(self.y) + ") -> " + str(self.h) + "x" + str(self.w) + " -> FINAL: (" + str(self.anchoFinal()) +"," + str(self.altoFinal()) +") -> MEDIO: " + str(self.medio())