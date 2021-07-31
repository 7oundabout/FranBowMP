import pygame
import random
from settings import *
from network import Network
from player import Player
print("Здравсствуйте, вас приветствует NVORON production. Это клиент игрока.")

ip = input("Вы хотите ввести свой ip или хотите взять из файла? Напишите ip или file: ")

if ip == "ip":
	server_input = input("Введите ip:")
	port = int(input("Введите порт:"))
	
elif ip == "file":
	print("Хорошо, ip сервера будет взят с файла ip-client.txt")
	file = open('ip-client.txt', 'r')
	data = file.read()
	server_input = ':'.join(data.split(':')[:-1])
	port = int(':'.join(data.split(':')[-1:]))
	print("Ip, к которому вы хотите присоединиться: "+data)
	
else:
	print("Ошибка")
	sys.exit()



pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fran Bow Multiplayer')


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