import pygame
from settings import *

#Объекты

class Redis(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = 300
		self.y = HEIGHT // 2 - 40

	def redis_draw(self, sc, player_x, player_y):
		pygame.transform.flip(redis, True, False)
		if player_x > self.x:
			sc.blit(redis, [self.x, self.y])
		else:
			sc.blit(pygame.transform.flip(redis, True, False), [self.x, self.y])
