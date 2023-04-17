import random
class Zanahoria():
    def __init__(self) -> None:
        self.cordX = 128
        self.cordY = 192
        self.tamanio = 40
        self.coordenadas = ((128,96),(160,96),(128,128),(160,128),(128,192),(160,192),(416,192),(544,192),(608,416),(736,416),(800,96),(800,512))

    def restablecer(self):
        self.cordX , self.cordY = self.coordenadas[random.randint(0,11)]
        