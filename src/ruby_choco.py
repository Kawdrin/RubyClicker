from pygame.sprite import Sprite
from pygame.font import Font
from pygame import display
from pygame.transform import scale, rotate, rotozoom
from pygame import Rect
from .SpriteSheet import SpriteSheet


spritesheet = SpriteSheet("res/rubyyyy.png")

class Window(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global spritesheet
        self.image = spritesheet.get_sprite(0, 240, 160, 144)
        self.image = scale(self.image, [160*4,  144*4])
        self.rect = Rect(0, 0, 16*4, 16*4)

    def update(self):
        ...

class RubyWindow(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global spritesheet
        self.image = spritesheet.get_sprite(1, 1, 64, 82)
        self.image = scale(self.image, ((16*4)*4, (16*5+2)*4))
        self.rect = Rect(4, 4, 16*4*4, 16*5+2)

    def update(self):
        ...

class RubyChoco(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global spritesheet
        self.sprite = spritesheet.get_sprite(160, 0, 32, 32)
        self.image = scale(self.sprite, [16*2*4, 16*2*4])
        self.rect = Rect(16*4, 16*4, 16*12,16*12)
        self.rota = 0
        self.scala = 0

    def update(self):
        self.image = rotate(self.sprite, self.rota)
        self.image = scale(self.image, [16*2*4, 16*2*4])
        if self.rota >= 360:
            self.rota = 0
        self.rota += 0.90

class BotaoMelhorias(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global spritesheet
        self.image = spritesheet.get_sprite(1, 145, 14, 14)
        self.image = scale(self.image, [14*4, 14*4])
        self.rect = Rect(12, (16*16)+12, 14, 14)


    def update(self):
        ...
    def click(self):
        a = display.init()
        janela = display.set_mode([514, 514])

class Calculator(Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        texto = Font("res/font/AvenuePixel-Regular.ttf", 36)
        self.image = texto.render("10000+", False, (255,255,255))
        self.rect = Rect(pos[0], pos[1], 15, 15)
        self.pos = pos[1]
        self.rect.x -= 14


    def update(self):
        self.rect.y -= 1

        if self.pos - self.rect.y == 30:
            self.kill()
