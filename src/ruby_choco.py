from pygame.sprite import Sprite
from pygame.transform import scale, rotate, rotozoom
from pygame import Rect
from .SpriteSheet import SpriteSheet


spritesheet = SpriteSheet("res/ruby.png")

class RubyWindow(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global spritesheet
        self.image = spritesheet.get_sprite(0,0,16*4, 16*5+2)
        self.image = scale(self.image, ((16*4)*4, (16*5+2)*4))
        self.rect = Rect(0, 0, 16*4*4, 16*5+2)

    def update(self):
        ...

class RubyChoco(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global spritesheet
        self.sprite = spritesheet.get_sprite(64, 112, 32, 32)
        self.image = scale(self.sprite, [16*2*4, 16*2*4])
        self.rect = Rect(16*4, 16*4, 16*12,16*12)
        self.rota = 0
        self.scala = 0

    def update(self):
        self.image = rotate(self.sprite, self.rota)
        self.image = scale(self.image, [16*2*4, 16*2*4])
        if self.scala >= 10:
            self.scala = 0
        self.scala += 0.1

        if self.rota >= 360:
            self.rota = 0
        self.rota += 0.90

    def animation(self):
        ...
