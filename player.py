import pygame
from settings import *

player_img = [pygame.image.load('sprites/panimation/1.png'), pygame.image.load('sprites/panimation/2.png'), pygame.image.load('sprites/panimation/3.png'), pygame.image.load('sprites/panimation/4.png'), pygame.image.load('sprites/panimation/5.png'), pygame.image.load('sprites/panimation/6.png')]
player_img_inverted = []
for i in range(len(player_img)):
	player_img_inverted.append(pygame.transform.flip(player_img[i], True, False))
img_counter = 0

class Player(pygame.sprite.Sprite):
	def __init__(self, player_x, player_y, player_direction, player_detector):
		pygame.sprite.Sprite.__init__(self)
		self.x = player_x
		self.y = player_y
		self.speed = 4	
		self.direction = player_direction
		self.detector = player_detector

	def draw(self, sc):
		global img_counter
		if img_counter +1 == 36:
						img_counter = 0

		if self.detector == 1:
			if self.direction:
				img_counter += 1
				sc.blit(player_img[img_counter // 6], (self.x, self.y))
			else:
				img_counter += 1
				sc.blit(player_img_inverted[img_counter // 6], (self.x, self.y))
		else:
			if self.direction:
				img_counter += 1
				sc.blit(player_img[5], (self.x, self.y))
			else:
				img_counter += 1
				sc.blit(player_img_inverted[5], (self.x, self.y))

	def move(self, sc):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
			self.detector = 1
			img_counter =0
			self.draw(sc)
		else:
			self.detector = 0
			self.draw(sc)

		if keys[pygame.K_LEFT]:
			self.direction = 1
			self.x -= self.speed
		if keys[pygame.K_RIGHT]:
			self.direction = 0
			self.x += self.speed
		if keys[pygame.K_UP]:
			self.y -= self.speed
		if keys[pygame.K_DOWN]:
			self.y += self.speed

'''переключатель
class Switch(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

	def draw(self):
		pygame.draw.polygon(sc, BLUE, points=[(WIDTH - 50, HEIGHT // 2 - 30), (WIDTH - 20, HEIGHT // 2), (WIDTH - 50,HEIGHT // 2 + 30)])
'''