import pygame
import random
from settings import *
from network import Network
from player import Player
from objects import *

pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FBMP')
platform_group = pygame.sprite.Group()
players = [Player(), Player()]
my_group = pygame.sprite.Group(players)
n = Network()
p = n.getP()
clock = pygame.time.Clock()

levels_number =[[ #уровни
		"-------------------------", 
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"-------------------------", 
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"------------------------1"],
		[ 
		"-------------------------", 
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"-------------------------", 
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"-------------------------",
		"-------------------------"]]

pf_x = pf_y = 0
platforms = []

def platform_init(lvl): #функция инициализации платформ
	global pf_x, pf_y
	for line in levels_number[lvl]:
		for symbol in line:
			if symbol == "1":
				pf = Platform(pf_x, pf_y)
				platform_group.add(pf)
				platforms.append(pf)
			pf_x += platform_width
		pf_y += platform_height
		pf_x = 0

platform_init(players[0].level)

running = True
while running:
	
	clock.tick(FPS) #установление фпс
	
	p2 = n.send(p) #отправка пакета p и возвращение p2
	
	for event in pygame.event.get(): # блок евентов
		if event.type == pygame.QUIT: 
			running = False
	
	sc.fill(SKY) #закрашивание фона
	sc.blit(background, [0,0]) #закрашивание фона бэкграундом
	
	players[0].rect.x = p[0] ; players[0].rect.y = p[1] ; players[0].direction = p[2] ; players[0].detector = p[3] ; players[0].index = p[4] ; players[0].level = p[5] #передача полученных переменных в локалку p
	players[1].rect.x = p2[0] ; players[1].rect.y = p2[1] ; players[1].direction = p2[2] ; players[1].detector = p2[3] ; players[1].index = p2[4] ; players[1].level = p2[5] #передача полученных переменных в локалку p2
	players[0].move()

	if players[0].rect.x > WIDTH: #блок переключения на другой уровень
		players[0].level += 1
		players[0].rect.x = 0 #сброс позиции игрока
		platform_group.empty() #сброс platform_group
		platforms.clear() #очистка листа
		pf_x = 0 ; pf_y = 0 #сброс pf_x, pf_y - позиций для инициализации
		platform_init(players[0].level) #цикл инициализации

	my_group.update() #обновление группы игроков
	my_group.draw(sc) #отрисовка группы игроков
	platform_group.draw(sc) #отрисовка платформ

	p[0] = players[0].rect.x ; p[1] = players[0].rect.y ; p[2] = players[0].direction ; p[3] = players[0].detector ; p[4] = players[0].index ; p[5] = players[0].level #передача измененной локалки p на сервер
	
	pygame.display.flip() #обновление экрана


pygame.quit()