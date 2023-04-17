import pygame
class Sonido():
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.music.load(".\\sound\\sountrack_general.mp3")
        self.efectoDisparo = pygame.mixer.Sound(".\\sound\\Efecto_disparo.wav")
        self.efectoItem = pygame.mixer.Sound(".\\sound\\efecto_pop.wav")
    
    def iniciarMusica(self):
        pygame.mixer.music.play(5)
    def iniciarDisparo(self):
        self.efectoDisparo.play()
    def iniciarItem(self):
        self.efectoItem.play()
        