import pygame
from pygame import display, fastevent, time, transform
from pygame.font import Font
from pygame.sprite import Group
from .ruby_choco import RubyWindow, RubyChoco, ChocolatesGanhoClick, BotaoMelhorias, Window

class Engine():
    def __init__(self):
        display.init()
        fastevent.init()
        pygame.font.init()
        self.FPS_TICK = time.Clock()
        self.tela = display.set_mode([66*4, 84*4])
        display.set_caption("Ruby Clicker")
        self.GAMELOOP = True
        self.chocolates = 0
        self.chocolate_font = Font("res/font/AvenuePixel-Regular.ttf", 40)

    def new_game(self):
        self.grupo_ruby = Group()
        self.Window = Window(self.grupo_ruby)
        self.RubyClicker = RubyWindow(self.grupo_ruby)
        self.RubyChoco = RubyChoco(self.grupo_ruby)
        self.Botao = BotaoMelhorias(self.grupo_ruby)

    def verifica_evento(self):
        for event in fastevent.get():
            if event.type == pygame.QUIT:
                self.GAMELOOP = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if event.pos[0] > 16*4+4 and event.pos[1] > 16*4+12 and event.pos[0] < 16*12+4 and event.pos[1] < 16*12+12:
                    ChocolatesGanhoClick(event.pos, self.grupo_ruby)
                    self.chocolates+=1
                if event.pos[0] > 12 and  event.pos[1] > (16*16)+12 and event.pos[0] < 67  and event.pos[1] < 324:
                    self.Botao.click()

    def update(self):
        self.grupo_ruby.update()
        pygame.display.flip()

    def draw(self):
        self.grupo_ruby.draw(self.tela)
        self.chocolate_text = self.chocolate_font.render(f"{self.chocolates}", False, (255, 255, 255))
        self.tela.blit(self.chocolate_text, (10*4,3))

    def run_loop(self):
        self.new_game()
        while self.GAMELOOP:
            self.verifica_evento()
            self.update()
            self.draw()
            self.FPS_TICK.tick(60)
