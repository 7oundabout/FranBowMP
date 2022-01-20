import pygame
from levels import *
from objects import *


pf_x = pf_y = 0
platforms = [""]
platform_group = pygame.sprite.Group()

def platform_init(lvl): #функция инициализации платформ
	global pf_x
	global pf_y
	platform_group.empty() #сброс platform_group
	platforms.clear() #очистка листа
	pf_x = 0 ; pf_y = 0 #сброс pf_x, pf_y - позиций для инициализации
	for line in levels_map[lvl]:
		for symbol in line:
			if symbol == "1":
				pf = Platform(pf_x, pf_y)
				platform_group.add(pf)
				platforms.append(pf)
			pf_x += platform_width
		pf_y += platform_height
		pf_x = 0
		

