import pygame

player_animation = [pygame.image.load('sprites/panimation/1.png'), pygame.image.load('sprites/panimation/2.png'), pygame.image.load('sprites/panimation/3.png'), pygame.image.load('sprites/panimation/4.png'), pygame.image.load('sprites/panimation/5.png'), pygame.image.load('sprites/panimation/6.png'), pygame.image.load('sprites/panimation/7.png'), pygame.image.load('sprites/panimation/8.png'), pygame.image.load('sprites/panimation/9.png'), pygame.image.load('sprites/panimation/10.png'), pygame.image.load('sprites/panimation/11.png'), pygame.image.load('sprites/panimation/12.png')]
backgrounds = [pygame.image.load('backgrounds/1.png'), pygame.image.load('backgrounds/2.png'), pygame.image.load('backgrounds/3.png'), pygame.image.load('backgrounds/4.png'), pygame.image.load('backgrounds/5.png')]
platform_texture = pygame.image.load('sprites/objects/platform.png')

WIDTH = 800
HEIGHT = 400
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKY = (135, 206, 235)