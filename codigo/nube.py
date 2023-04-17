import random
class Nube():
    def __init__(self,animacion) -> None:
        self.generarNube()
        self.animacion = animacion
        self.velocidad = random.randint(2,4)
        
    def mover(self):
        if self.direccion == 'a':
            self.cordX += self.velocidad
            if self.cordX > 970:
                self.generarNube()
        else:
            self.cordX -= self.velocidad
            if self.cordX < -95:
                self.generarNube()
        
        self.animacion.dibujarNube(self.cordX,self.cordY)
    
    def generarNube(self):
        self.direccion = 'a' if random.randint(0,1) else 'd'
        if self.direccion == 'a':
            self.cordX = 0 - 89
        else:
            self.cordX = 960 + 2

        self.cordY = random.randint(96,543-52)
        self.velocidad = random.randint(2,4)
        

