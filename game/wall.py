import os
import pygame

from .config import *

class Wall(pygame.sprite.Sprite):

    def __init__(self, left, bottom, dir_images):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(dir_images, 'wall.png'))

        self.rect = self.image.get_rect() # Obtengo el rectangulo
        # Posiciono el rectangulo
        self.rect.left = left 
        self.rect.bottom = bottom

        self.vel_x = SPEED

        self.rect_top = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 1) # Rectangulo en la parte superior de los obstaculos

    def update(self):
        self.rect.left -= self.vel_x
        self.rect_top.x = self.rect.x # Con esto nos cercioramos que el rectangulo se encuentre en la parte superior
    
    def stop(self): # Detiene el movimiento de nuestro obstaculo
        self.vel_x = 0
