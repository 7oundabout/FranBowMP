import pygame
from settings import *

platform_height = 32
platform_width = 32
platform_color = BLACK

class Platform(pygame.sprite.Sprite):
	def __init__(self, platform_x, platform_y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((platform_height, platform_width))
		self.image.fill(platform_color)
		self.rect = pygame.Rect(platform_x, platform_y, platform_width, platform_height)

		
