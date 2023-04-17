import pygame,sys
from .control import Control
from .jugador import Jugador
from .colision import Colision
from .zanahoria import Zanahoria
from .animacion import Animacion
from .NPCmira import Mira
from .sonido import Sonido
from .nube import Nube
from .record import Record
import random

class Juego():
    def __init__(self) -> None:
        self.dimensionX = 960
        self.dimensionY = 640
        self.jugador = Jugador(417,416)
        self.zanahoria = Zanahoria()
        self.mira1 = Mira()
        self.mira2 = Mira()
        self.mira3 = Mira()
        self.mira4 = Mira()
        self.mira5 = Mira()
        self.mira6 = Mira()
        self.sonido = Sonido()
        self.ventana = pygame.display.set_mode((self.dimensionX,self.dimensionY))
        self.animacion = Animacion(self.ventana,self.jugador)
        self.record = Record()
        self.colision = Colision(self.jugador,self.zanahoria,self.animacion,self.sonido,self.record)
        self.control = Control(self.jugador,self.colision,self.animacion)
        self.nube1 = Nube(self.animacion)
        self.nube2 = Nube(self.animacion)
        self.nube3 = Nube(self.animacion)
        self.nube4 = Nube(self.animacion)
        self.nube5 = Nube(self.animacion)
        self.nube6 = Nube(self.animacion)
        self.nube7 = Nube(self.animacion)
        self.nube8 = Nube(self.animacion)
        self.nube9 = Nube(self.animacion)
        self.nube10 = Nube(self.animacion)
        self.accion = 1
        
        

    def iniciarJuego(self):
        pygame.init()
        self.iniciarComponentes()
        self.correrJuego()
        
    def iniciarComponentes(self):
        self.sonido.iniciarMusica()

    def actualizar(self):
        if self.accion == 1:
            self.ecenario1()
        if self.accion == 2:
            self.ecenario2()
        if self.accion == 3:
            self.ecenario3()

    def nubes(self):
        self.nube1.mover()
        self.nube2.mover()
        self.nube3.mover()
        self.nube4.mover()
        self.nube5.mover()
        self.nube6.mover()
        self.nube7.mover()
        self.nube8.mover()
        self.nube9.mover()


    def accionesNPC(self):
        self.colision.detectarMira(self.mira1)
        self.mira1.mover()
        self.colision.detectarMira(self.mira2)
        self.mira2.mover()
        self.colision.detectarMira(self.mira3)
        self.mira3.mover()
        self.colision.detectarMira(self.mira4)
        self.mira4.mover()
        self.colision.detectarMira(self.mira5)
        self.mira5.mover()
        self.colision.detectarMira(self.mira6)
        self.mira6.mover()
        self.colision.detectarChoqueMuroGeneralMira(self.mira1)
        self.colision.detectarChoqueMuroGeneralMira(self.mira2)
        self.colision.detectarChoqueMuroGeneralMira(self.mira3)
        self.colision.detectarChoqueMuroGeneralMira(self.mira4)
        self.colision.detectarChoqueMuroGeneralMira(self.mira5)
        self.colision.detectarChoqueMuroGeneralMira(self.mira6)
        self.mira1.cargarAtaque()
        self.mira2.cargarAtaque()
        self.mira3.cargarAtaque()
        self.mira4.cargarAtaque()
        self.mira5.cargarAtaque()
        self.mira6.cargarAtaque()

    def ecenario1(self):
        self.animacion.dibujarBackGround3()
        if random.randint(0,1) == 0:
            self.ventana.blit(pygame.font.Font(None,80).render(str("Presione H para jugar"),False,(200,60,80)),(180,350))
        self.accion = 2 if self.control.confirmar(pygame.key.get_pressed()) else 1


    def ecenario2(self):
        #BackGround
        self.animacion.dibujarBackGround1()

        #Texto score
        self.ventana.blit(pygame.font.Font(None,40).render("Score: "+str(self.record.puntaje),False,(255,255,255)),(40,40))
        #Texto vida
        self.ventana.blit(pygame.font.Font(None,40).render("HP: "+str(self.jugador.hp),False,(255,255,255)),(40,80))

        #Zanahoria
        self.animacion.dibujarZanahoria(self.zanahoria.cordX,self.zanahoria.cordY)

        #Personaje

        self.control.movimiento(pygame.key.get_pressed())

        #Personaje
        self.ventana.blit(pygame.image.load(self.animacion.direccion),(self.jugador.cordX,self.jugador.cordY-19))
        self.accionesNPC()
        #Nube
        self.nubes()
        self.colision.detectarMuro()
        self.colision.detectarItem()
        self.accion = 3 if not self.jugador.vivo else 2

    def ecenario3(self):
        self.animacion.dibujarBackGround4()
        if random.randint(0,1) == 0:
            self.ventana.blit(pygame.font.Font(None,50).render(str("Presione H para salir"),False,(200,60,80)),(280,500))
        self.accion = 4 if self.control.confirmar(pygame.key.get_pressed()) else 3

    def correrJuego(self):
        while True and self.accion != 4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.actualizar()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
        
    
