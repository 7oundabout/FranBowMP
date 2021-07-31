import pygame
import random
from settings import *
from network import Network
from player import Player
from objects import *

server_input = input("Введите ip:")
port = int(input("Введите порт:"))

pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FBMP')

#Переключение уровней
class Levels():
	def __init__(self):
		pass

	def level1_draw(self):
		r = Redis()
		r.redis_draw(sc, p.x, p.y)		

n = Network(server_input, port)
p = n.getP()
l = Levels()
clock = pygame.time.Clock()

running = True
while running:
	clock.tick(FPS)
	p2 = n.send(p)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	sc.fill(SKY)
	sc.blit(bg[p.level], [0,0])
	if p.level == 2:
		l.level1_draw()
	else:
		pass
	p.move(sc)
	if p.level == p2.level:
		p2.draw(sc)
	pygame.display.flip()


pygame.quit()