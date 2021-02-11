import pygame
from pygame import display, fastevent, time

class Engine():
    def __init__(self):
        display.init()
        fastevent.init()
        self.FPS_TICK = time.Clock()
        self.tela = display.set_mode([210,210])
        self.GAMELOOP = True

    def verifica_evento(self):
        for event in fastevent.get():
            if event.type == pygame.QUIT:
                self.GAMELOOP = False
                display.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    print("+ 5 ruby choco")


    def run_loop(self):
        self.verifica_evento()
        self.FPS_TICK.tick(60)

Engine()
