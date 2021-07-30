import pygame
import random
from settings import *
from network import Network
from player import Player

server_input = input("Введите ip:")
port = int(input("Введите порт:"))

pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FBMP')


bg = [pygame.image.load('backgrounds//1.png'), pygame.image.load('backgrounds//2.png'), pygame.image.load('backgrounds//3.png'), pygame.image.load('backgrounds//4.png'), pygame.image.load('backgrounds//5.png')]
#switch = Switch()

n = Network(server_input, port)
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
	sc.blit(bg[p.level], [0,0])
#	switch.draw()
	p.move(sc)
	p2.draw(sc)
	pygame.display.flip()


pygame.quit()