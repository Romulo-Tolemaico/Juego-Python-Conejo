import pygame
class Control():
    def __init__(self,jugador,colision,animacion) -> None:
        self.colision = colision
        self.jugador = jugador
        self.animacion = animacion
    
    def confirmar(self,teclas):
        if teclas[pygame.K_h]:
            return True

    def movimiento(self,teclas):
        if teclas[pygame.K_a]:
            self.animacion.aPW = self.animacion.aPD = self.animacion.aPS = 1
            self.jugador.moverIzq()
            self.colision.colisionA()
            self.animacion.dibujarPA()
        if teclas[pygame.K_d]:
            self.animacion.aPW = self.animacion.aPA = self.animacion.aPS = 1
            self.jugador.moverDer()
            self.colision.colisionD()
            self.animacion.dibujarPD()
        if teclas[pygame.K_w]:
            self.animacion.aPD = self.animacion.aPA = self.animacion.aPS = 1
            self.jugador.moverArr()
            self.colision.colisionW()
            self.animacion.dibujarPW()
        if teclas[pygame.K_s]:
            self.animacion.aPW = self.animacion.aPA = self.animacion.aPD = 1
            self.jugador.moverAbj()
            self.colision.colisionS()
            self.animacion.dibujarPS()
        

