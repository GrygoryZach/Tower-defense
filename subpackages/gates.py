from math import degrees, atan2, sqrt, cos, sin, radians
from pygame import sprite
from pygame.sprite import Group
from pygame import Surface
from pygame import mask
from pygame import SRCALPHA
from pygame import transform
from pygame import time
from pygame import mouse

from typing import Any, Tuple, Optional, List

from .functions import load_image



class Gate(sprite.Sprite):
    image_n = load_image("assets/gate/gate_N.png")
    image_e = load_image("assets/gate/gate_E.png")

    def __init__(self, coords: List, facing: str, gate_group: Group) -> None:
        super().__init__(gate_group)
        self.image = {'N': Gate.image_n, 'E': Gate.image_e}[facing]
        self.rect = self.image.get_rect(center=coords)
        self.rect.center = coords

        self.mask = mask.from_surface(self.image)

    def update(self, screen: Surface, enemy_group: Group) -> None:
        screen.blit(self.image, self.rect)
        for enemy in enemy_group:
            if sprite.collide_mask(self, enemy):
                enemy.die("gate")
                self.die()
                break

    def die(self):
        self.kill()