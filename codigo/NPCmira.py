import random as rd
class Mira():
    def __init__(self) -> None:
        self.cordX = rd.randint(128,831)
        self.cordY = rd.randint(96,543)
        self.tamanio = 31
        self.danio = 5
        self.velocidad = 3
        self.direccionX = 'a' if rd.randint(0,1) else 'd'
        self.direccionY = 'w' if rd.randint(0,1) else 's'
        self.tiempoEspera = 100
    
    def mover(self):
        if self.direccionX == 'a':
            self.cordX -= self.velocidad
        elif self.direccionX == 'd':
            self.cordX += self.velocidad
        
        if self.direccionY == 'w':
            self.cordY -= self.velocidad
        elif self.direccionY == 's':
            self.cordY += self.velocidad
    
    def atacar(self):
        return self.tiempoEspera == 0

    def cargarAtaque(self):
        if self.tiempoEspera > 0:
            self.tiempoEspera -= 1



