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
		self.level = 3

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
		if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
			self.detector = 1
			img_counter =0
			self.draw(sc)
		else:
			self.detector = 0
			self.draw(sc)
		if keys[pygame.K_a]:
			if self.x >= 0:
				self.direction = 1
				self.x -= self.speed
			else:
				if self.level >= 1:
					self.level -= 1
					self.x = WIDTH - 83
				else:
					pass
		if keys[pygame.K_d]:
			if self.x <= WIDTH - 59:
				self.direction = 0
				self.x += self.speed
			else:
				if self.level <= 3:
					self.level += 1
					self.x = 20
				else:
					pass
		if keys[pygame.K_w]:
			if self.y >= 25:
				self.y -= self.speed
		if keys[pygame.K_s]:
			if self.y <= HEIGHT - 186:
				self.y += self.speed

