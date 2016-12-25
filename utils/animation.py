import pygame
from pygame import Rect
import os

MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]


def load_image(file=None, width=None, number=18):
    # file = os.path.join(MAIN_DIR, 'data/image', file)
    file = "D:/Projects/Python/3.5.2/PlantsVSZombies/src/_0008_shujing.png"

    try:
        # surface = pygame.image.load(file).convert_alpha()
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    if width == None:
        return surface
    height = surface.get_height()

    return [surface.subsurface(
        Rect((i * width, 0), (width, height))
    ) for i in range(number)]


class SunFlower(pygame.sprite.Sprite):
    _width = 82
    _height = 77
    _number = 18
    images = []

    def __init__(self):
        self.order = 0
        pygame.sprite.Sprite.__init__(self)
        if len(self.images) == 0:
            self.images = load_image("D:/Projects/Python/3.5.2/PlantsVSZombies/src/_0008_shujing.png", self._width,
                                     self._number)
        self.image = self.images[self.order]
        self.rect = Rect(0, 0, self._width, self._height)

    def update(self):
        if self.order >= self._number - 1:
            self.order = -1
        self.order += 1
        self.image = self.images[self.order]
