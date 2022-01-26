import pygame
from objects import *

platform_group = pygame.sprite.Group() 
grid_group = pygame.sprite.Group()

class objects_initialization():
	def __init__(self):
		self.pf_x = 0 ; self.pf_y = 0
		self.levels_map = None

	def platform_init(self, lvl): #функция инициализации платформ
		platform_group.empty() #сброс platform_group
		self.pf_x = 0 ; self.pf_y = 0 #сброс pf_x, pf_y - позиций для инициализации
		
		for line in self.levels_map[lvl]:
			for symbol in line:
				if symbol == "1":
					pf = Platform(self.pf_x, self.pf_y)
					platform_group.add(pf)
				self.pf_x += platform_width
			self.pf_y += platform_height
			self.pf_x = 0
	
	def grid_init(self):
		for x in range(0, WIDTH, platform_width):
			for y in range(0, HEIGHT, platform_height):
				grid_object = GridOb(x, y)
				grid_group.add(grid_object)
