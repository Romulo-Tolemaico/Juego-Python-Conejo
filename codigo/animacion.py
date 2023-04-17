import pygame
class Animacion():
    def __init__(self,ventana,jugador) -> None:
        self.ventana = ventana
        self.jugador = jugador
        self.aPW = 1
        self.aPS = 1
        self.aPA = 1
        self.aPD = 1
        self.direccion = ".\\img\\conejo\\caminarIzq\\"+str(self.aPD)+".png"

    def dibujarBackGround1(self):
        self.ventana.blit(pygame.image.load(".\\img\\background\\background1.png").convert(),(0,0))
        
    def dibujarBackGround2(self):
        self.ventana.blit(pygame.image.load(".\\img\\background\\background2.png").convert(),(0,0))
    
    def dibujarBackGround3(self):
        self.ventana.blit(pygame.image.load(".\\img\\background\\background3.png").convert(),(0,0))

    def dibujarBackGround4(self):
        self.ventana.blit(pygame.image.load(".\\img\\background\\background4.png").convert(),(0,0))
    
    def dibujarPA(self):
        self.direccion = ".\\img\\conejo\\caminarIzq\\"+str(self.aPA)+".png"
        self.aPA += 1
        if self.aPA == 9:
            self.aPA = 1
    
    def dibujarPD(self):
        self.direccion = ".\\img\\conejo\\caminarDer\\"+str(self.aPD)+".png"
        self.aPD += 1
        if self.aPD == 9:
            self.aPD = 1
    
    def dibujarPW(self):
        self.direccion = ".\\img\\conejo\\caminarArr\\"+str(self.aPW)+".png"
        self.aPW += 1
        if self.aPW == 9:
            self.aPW = 1
    
    def dibujarPS(self):
        self.direccion = ".\\img\\conejo\\caminarAbj\\"+str(self.aPS)+".png"
        self.aPS += 1
        if self.aPS == 9:
            self.aPS = 1

    def dibujarMiraOne(self,x,y):
        self.ventana.blit(pygame.image.load(".\\img\\punto_mira\\1.png"),(x,y))

    def dibujarMiraTwo(self,x,y):
        self.ventana.blit(pygame.image.load(".\\img\\punto_mira\\2.png"),(x,y))
    
    def dibujarZanahoria(self,x,y):
        self.ventana.blit(pygame.image.load(".\\img\\zanahoria_item\\1.png"),(x,y))

    def dibujarNube(self,x,y):
        self.ventana.blit(pygame.image.load(".\\img\\nube\\1.png"),(x,y))

    

    