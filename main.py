import pygame
import random
from settings import *
from network import network
from player import player
from objects import *
from objects_initialization import *

pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FBMP')
pygame.display.set_icon(ico_game)
players = [player(), player()]
my_group = pygame.sprite.Group(players)
n = network()
p = [[WIDTH // 2 - 30, HEIGHT // 2 - 30, False, False, 0, 1, 0, None, None], [WIDTH // 2 - 30, HEIGHT // 2 - 30, False, False, 0, 2, 1 , None, None]]
p[0] = n.getP()
initial = objects_initialization()
clock = pygame.time.Clock()

class mainrun():
	def __init__(self):
		self.running = True
		self.key = False
		self.package = False
		self.column = None ; self.row = None
		self.first_run()
		initial.grid_init()
		while self.running == True:
			self.main()


	def main(self):
		clock.tick(FPS) #установление фпс
		p[1] = n.send(p[0]) #отправка пакета p и возвращение p2
		for event in pygame.event.get(): # блок евентов
			if event.type == pygame.QUIT: 
				running = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.key == True:
					pos = pygame.mouse.get_pos()
					self.column = pos[0] // platform_width
					self.row = pos[1] // platform_height
					self.package = True
				else:
					pass

		sc.fill(SKY) #закрашивание фона
		players[p[0][6]].rect.x = p[0][0] ; players[p[0][6]].rect.y = p[0][1] ; players[p[0][6]].direction = p[0][2] ; players[p[0][6]].detector = p[0][3] ; players[p[0][6]].index = p[0][4] ; players[p[0][6]].level = p[0][5] ; players[p[0][6]].package = p[0][7]  #передача полученных переменных в локалку p
		players[p[1][6]].rect.x = p[1][0] ; players[p[1][6]].rect.y = p[1][1] ; players[p[1][6]].direction = p[1][2] ; players[p[1][6]].detector = p[1][3] ; players[p[1][6]].index = p[1][4] ; players[p[1][6]].level = p[1][5] ; players[p[0][6]].package = p[0][7] #передача полученных переменных в локалку p2
		sc.blit(backgrounds[players[p[0][6]].level], [0,0]) #закрашивание фона бэкграундом
		
		if p[1][8] == None:
			pass
		else:
			initial.levels_map = p[1][8]
			initial.platform_init(p[0][5])
			p[0][8] = None


		self.key = players[p[0][6]].keymove()

		players[p[0][6]].switch(initial)
		platform_group.draw(sc) #отрисовка платформ
		
		if players[p[0][6]].level == players[p[1][6]].level:
			my_group.update() #обновление группы игроков
			my_group.draw(sc)
		else:
			players[p[0][6]].update()
			sc.blit(players[p[0][6]].image, players[p[0][6]])
		
		if p[0][7] == None:
			if self.key == True:
				grid_group.draw(sc)
				if self.package == True:
					p[0][7] = [players[p[0][6]].level, self.row, self.column]
					self.package = False
			else:
				pass
		else:
			p[0][7] = None

		p[0][0] = players[p[0][6]].rect.x ; p[0][1] = players[p[0][6]].rect.y ; p[0][2] = players[p[0][6]].direction ; p[0][3] = players[p[0][6]].detector ; p[0][4] = players[p[0][6]].index ; p[0][5] = players[p[0][6]].level ; p[0][7] = p[0][7] ; p[0][8] = None #передача измененной локалки p на сервер
		pygame.display.flip() #обновление экрана
	
	def first_run(self):
		if p[0][8] == None:
			pass
		else:
			initial.levels_map = p[0][8]
			initial.platform_init(p[0][5])
			p[0][8] = None

if __name__ == "__main__":
    mainrun()