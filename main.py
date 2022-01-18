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
p = [[WIDTH // 2 - 30, HEIGHT // 2 - 30, False, False, 0, 1, 0, 0], [WIDTH // 2 - 30, HEIGHT // 2 - 30, False, False, 0, 2, 1]]
p[0] = n.getP()

clock = pygame.time.Clock()
running = True

pf_x = pf_y = 0
platforms = [""]

def platform_init(lvl): #функция инициализации платформ
	global pf_x, pf_y

	if lvl < 2:
		for line in levels_map[lvl]:
			for symbol in line:
				if symbol == "1":
					pf = Platform(pf_x, pf_y)
					platform_group.add(pf)
					platforms.append(pf)
				pf_x += platform_width
			pf_y += platform_height
			pf_x = 0
	else:
		platform_group.empty() #сброс platform_group
		platforms.clear() #очистка листа
		pf_x = 0 ; pf_y = 0 #сброс pf_x, pf_y - позиций для инициализации


while running:
	
	clock.tick(FPS) #установление фпс
	
	p[1] = n.send(p[0]) #отправка пакета p и возвращение p2
	
	for event in pygame.event.get(): # блок евентов
		if event.type == pygame.QUIT: 
			running = False
	
	sc.fill(SKY) #закрашивание фона
	sc.blit(backgrounds[players[p[0][6]].level], [0,0]) #закрашивание фона бэкграундом



	players[p[0][6]].rect.x = p[0][0] ; players[p[0][6]].rect.y = p[0][1] ; players[p[0][6]].direction = p[0][2] ; players[p[0][6]].detector = p[0][3] ; players[p[0][6]].index = p[0][4] ; players[p[0][6]].level = p[0][5]  #передача полученных переменных в локалку p
	players[p[1][6]].rect.x = p[1][0] ; players[p[1][6]].rect.y = p[1][1] ; players[p[1][6]].direction = p[1][2] ; players[p[1][6]].detector = p[1][3] ; players[p[1][6]].index = p[1][4] ; players[p[1][6]].level = p[1][5] #передача полученных переменных в локалку p2
	players[p[0][6]].move()
	players[p[0][6]].switch()
	platform_init(players[0].level)
	platform_group.draw(sc) #отрисовка платформ
	

	if players[p[0][6]].level == players[p[1][6]].level:
		my_group.update() #обновление группы игроков
		my_group.draw(sc)
	else:
		players[p[0][6]].update()
		sc.blit(players[p[0][6]].image, players[p[0][6]])

	p[0][0] = players[p[0][6]].rect.x ; p[0][1] = players[p[0][6]].rect.y ; p[0][2] = players[p[0][6]].direction ; p[0][3] = players[p[0][6]].detector ; p[0][4] = players[p[0][6]].index ; p[0][5] = players[p[0][6]].level #передача измененной локалки p на сервер

	pygame.display.flip() #обновление экрана


pygame.quit()