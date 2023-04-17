class Jugador():
    def __init__(self,x,y) -> None:
        self.cordX = x
        self.cordY = y
        self.hp = 25
        self.velocidad = 3
        self.tamanio = 31
        self.vivo = True

    def moverDer(self):
        self.cordX = self.cordX + self.velocidad
    def moverIzq(self):
        self.cordX = self.cordX - self.velocidad
    def moverArr(self):
        self.cordY = self.cordY - self.velocidad
    def moverAbj(self):
        self.cordY = self.cordY + self.velocidad

    

    

