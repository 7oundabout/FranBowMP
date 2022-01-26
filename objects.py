import pygame
from settings import *

class Platform(pygame.sprite.Sprite):
	def __init__(self, platform_x, platform_y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((platform_height, platform_width))
		self.image = platform_texture
		self.rect = pygame.Rect(platform_x, platform_y, platform_width, platform_height)

class GridOb(pygame.sprite.Sprite):
	def __init__(self, grid_x, grid_y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((platform_height, platform_width), pygame.SRCALPHA)
		self.rect = pygame.Rect(grid_x, grid_y, platform_width, platform_height)
		pygame.draw.rect(self.image, RED, [0, 0, platform_width, platform_height], 1)