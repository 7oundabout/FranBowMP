import pygame
from settings import player_animation, WIDTH, HEIGHT

class player(pygame.sprite.Sprite):
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
		self.level = 0

	def keymove(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
			self.detector = True
		else:
			self.detector = False

		if keys[pygame.K_w]:
			self.move_up()
		else:
			pass

		if keys[pygame.K_s]:
			self.move_down()
		else:
			pass

		if keys[pygame.K_a]:
			self.move_left()
		else:
			pass

		if keys[pygame.K_d]:
			self.move_right()
		else:
			pass

		if keys[pygame.K_q]:
			return True
		else:
			return False

	def move_up(self):
		if self.rect.y > 0:
			self.rect.y -= self.speed
		else:
			pass
	
	def move_down(self):
		if self.rect.y < HEIGHT - 186:
			self.rect.y += self.speed
		else:
			pass
	
	def move_left(self):
		self.direction = True
		if self.rect.x < 5 and self.level == 0:
			pass
		else:
			self.rect.x -= self.speed
	
	def move_right(self):
		self.direction = False
		if self.rect.x > WIDTH - 74 and self.level == 5:
			pass
		else:
			self.rect.x += self.speed
				
	def switch(self, initial_redirected):
		if self.rect.x > WIDTH - 59: #блок переключения на другой уровень
			self.level += 1
			self.rect.x = 0 #сброс позиции игрока
			initial_redirected.platform_init(self.level)
		elif self.rect.x < 0:
			self.rect.x = WIDTH - 59
			self.level -= 1
			initial_redirected.platform_init(self.level)

	def update(self):
		if self.detector:
			if self.direction:
				if self.index < 19:
					self.index += 1
					self.image = player_animation[self.index // 4]
				else:
					self.index = 0


			else:
				if self.index < 38 and self.index > 19:
					self.index += 1
					self.image = player_animation[self.index // 4]
				else:
					self.index = 20

		else:
			if self.direction:
				self.image = player_animation[10]
			else:
				self.image = player_animation[11]