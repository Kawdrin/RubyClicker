import pygame
from pygame import Surface, image

class SpriteSheet(object):
    def __init__(self, arquivo):
        self.sheet = image.load(arquivo)

    def get_sprite(self, x, y, largura, altura):
        image = Surface((largura, altura), pygame.SRCALPHA)
        image.blit(self.sheet, (0,0), (x, y, largura, altura))
        return image
