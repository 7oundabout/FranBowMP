import pygame
from settings import *



class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.index = 0
		self.image = player_animation[self.index]
		self.rect = pygame.Rect(5, 5, 59, 186)
		self.speed = 5
		self.rect.x = WIDTH // 2
		self.rect.y = HEIGHT // 2 - 30
		self.direction = False 
		self.detector = False

	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
			pygame.detector = True
		else:
			pygame.detector = False

		if keys[pygame.K_w]:
			self.rect.y -= self.speed
		if keys[pygame.K_s]:
			self.rect.y += self.speed
		if keys[pygame.K_a]:
			self.direction = False
			self.rect.x -= self.speed
		if keys[pygame.K_d]:
			self.direction = True
			self.rect.x += self.speed

	def update(self):
		if self.detector:
			if self.direction:
				if self.index < 15:
					self.index += 1
					self.image = player_animation[self.index // 6]
			else:
				if self.index < 35:
					self.index += 1
					self.image = player_animation[self.index // 6]
		else:
			if self.direction:
				self.image = player_animation[10]
			else:
				self.image = player_animation[11]
