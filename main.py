import pygame
import random
from settings import *
from network import Network
from player import Player
from objects import *
import linecache

print("Здравствуйте. Это клиент игрока.")

ip = input("Вы хотите ввести свой ip или хотите взять из файла? Напишите ip или file: ")

if ip == "ip":
	input_ip = input("Введите ip: ")
	server_input = ':'.join(input_ip.split(':')[:-1])
	port = int(':'.join(input_ip.split(':')[-1:]))

	save = input("Хотите сохранить ip? Напишите Y или N. ")
	
	if save.upper() == "Y":
		print("Ip был сохранён в ip-client.txt")
		data = '\n' + input_ip
		open('ip-client.txt', 'a').write(data)
	
	
	elif save.upper() == "N":
		print("Ip не был сохранён")
		
		
	else:
		print("Ошибка")
		sys.exit()


elif ip == "file":
	print("Хорошо, ip сервера будет взят с файла ip-client.txt")
	print("Выберите ip: ")
	
	f = open("ip-client.txt","r")
	listing = f.read()
	print(listing)
	choose = int(input())
	data = linecache.getline('ip-client.txt', choose)
	server_input = ':'.join(data.split(':')[:-1])
	port = int(':'.join(data.split(':')[-1:]))
	print("Ip, к которому вы хотите присоединиться: "+ data)
	f.close()
	
else:
	print("Ошибка")
	sys.exit()

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