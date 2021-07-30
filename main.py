import pygame
import random
from settings import *
from network import Network
from player import Player

server_input = input("Введите ip:")

pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FBMP')


background = pygame.image.load('backgrounds//1.png')
#switch = Switch()

n = Network(server_input)
p = n.getP()
clock = pygame.time.Clock()

running = True
while running:
	clock.tick(FPS)
	p2 = n.send(p)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	sc.fill(SKY)
	sc.blit(background, [0,0])
#	switch.draw()
	p.move(sc)
	p2.draw(sc)
	pygame.display.flip()


pygame.quit()