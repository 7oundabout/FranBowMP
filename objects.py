import pygame
from settings import *

platform_height = 20
platform_width = 20
platform_color = BLACK

class Platform(pygame.sprite.Sprite):
	def __init__(self, platform_x, platform_y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((platform_height, platform_width))
		self.image = platform_texture
		self.rect = pygame.Rect(platform_x, platform_y, platform_width, platform_height)

		
class World_border(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(())
		self.rect = pygame.Rect(x, y, width, height)