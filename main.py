import pygame
import random
from settings import *
from network import Network
from player import Player

pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FBMP')


background = pygame.image.load('backgrounds//1.png')
#switch = Switch()

n = Network()
p = n.getP()
clock = pygame.time.Clock()
players = [Player(), Player()]
my_group = pygame.sprite.Group(players)

running = True
while running:
	clock.tick(FPS)
	p2 = n.send(p)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	sc.fill(BLACK)
	sc.blit(background, [0,0])
#	switch.draw()
	players[0].rect.x = p[0] ; players[0].rect.y = p[1] ; players[0].direction = p[2], players[0].detector = p[3]
	players[1].rect.x = p2[0] ; players[1].rect.y = p2[1] ; players[1].direction = p2[2], players[1].detector = p2[3]
	players[0].move()
	p[0] = players[0].rect.x ; p[1] = players[0].rect.y ; p[2] = players[0].direction ; p[3] = players[0].detector
	my_group.update()
	my_group.draw(sc)
	pygame.display.flip()


pygame.quit()