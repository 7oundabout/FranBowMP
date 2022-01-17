import pygame
import random
from settings import *
from network import Network
from player import Player
from objects import *
from levels import *

pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FBMP')
pygame.display.set_icon(ico_game)
platform_group = pygame.sprite.Group()
players = [Player(), Player()]
my_group = pygame.sprite.Group(players)
n = Network()
p = n.getP()
clock = pygame.time.Clock()
running = True

while running:
	
	clock.tick(FPS) #установление фпс
	
	p2 = n.send(p) #отправка пакета p и возвращение p2
	
	for event in pygame.event.get(): # блок евентов
		if event.type == pygame.QUIT: 
			running = False
	
	sc.fill(SKY) #закрашивание фона
	sc.blit(backgrounds[players[0].level], [0,0]) #закрашивание фона бэкграундом
	
	players[0].rect.x = p[0] ; players[0].rect.y = p[1] ; players[0].direction = p[2] ; players[0].detector = p[3] ; players[0].index = p[4] ; players[0].level = p[5] #передача полученных переменных в локалку p
	players[1].rect.x = p2[0] ; players[1].rect.y = p2[1] ; players[1].direction = p2[2] ; players[1].detector = p2[3] ; players[1].index = p2[4] ; players[1].level = p2[5] #передача полученных переменных в локалку p2
	players[0].move()
	players[0].switch()

	if players[0].level < 1:
		platform_group.draw(sc) #отрисовка платформ
	
	if players[0].level == players[1].level:
		my_group.update() #обновление группы игроков
		my_group.draw(sc)
	else:
		players[0].update()
		sc.blit(players[0].image, players[0])

	p[0] = players[0].rect.x ; p[1] = players[0].rect.y ; p[2] = players[0].direction ; p[3] = players[0].detector ; p[4] = players[0].index ; p[5] = players[0].level #передача измененной локалки p на сервер
	
	pygame.display.flip() #обновление экрана


pygame.quit()