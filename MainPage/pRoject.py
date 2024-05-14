import pygame
from random import randrange as rnd
from tanks import Tanks
from tetris import Tetris
from xo import Xo
from kapriz import Kapriz

pygame.init()
screen = pygame.display.set_mode((626, 417))
pygame.display.set_caption("MiniGames")
pygame.display.set_icon(pygame.image.load('pristavka.jpeg'))

x0 = pygame.font.Font('Fonts/static/Playfair_144pt-Medium.ttf', 20)
xo = x0.render('X & 0', False, 'white')
tetris = pygame.font.Font('Fonts/static/Playfair_144pt-Medium.ttf', 20)
tetriss = tetris.render('Tetris', False, 'white')
tank = pygame.font.Font('Fonts/static/Playfair_144pt-Medium.ttf', 20)
tanks = tank.render('Tanks', False, 'white')
arcanoid = pygame.font.Font('Fonts/static/Playfair_144pt-Medium.ttf', 20)
arcanoidd = arcanoid.render('Arkanoid', False, 'white')

bg = pygame.image.load('Icons/bacgraund.jpg').convert()

while True:

    screen.blit(bg, (0, 0))

    screen.blit(pygame.image.load('icons/icon_x_o_.jpg').convert(), (40, 158))
    screen.blit(xo, (60, 130))
    screen.blit(pygame.image.load('icons/icon_tetris.jpeg').convert_alpha(), (170, 158))
    screen.blit(tetriss, (210, 130))
    screen.blit(pygame.image.load('icons/icon_tanks.jpeg').convert_alpha(), (330, 158))
    screen.blit(tanks, (365, 130))
    screen.blit(pygame.image.load('icons/icon_arkanoid.png').convert_alpha(), (480, 158))
    screen.blit(arcanoidd, (490, 130))

    xoRect = pygame.image.load('icons/icon_x_o_.jpg').get_rect(topleft=(40, 158))
    tetrisRect = pygame.image.load('icons/icon_tetris.jpeg').get_rect(topleft=(170, 158))
    tankRect = pygame.image.load('icons/icon_tanks.jpeg').get_rect(topleft=(330, 158))
    arcanoidRect = pygame.image.load('icons/icon_arkanoid.png').get_rect(topleft=(480, 158))


    mouse = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] and xoRect.collidepoint(mouse):
        Xo.xo_run()
    if pygame.mouse.get_pressed()[0] and tankRect.collidepoint(mouse):
        Tanks.tanks_run()
    if pygame.mouse.get_pressed()[0] and tetrisRect.collidepoint(mouse):
        Tetris.tetris_run()
    if pygame.mouse.get_pressed()[0] and arcanoidRect.collidepoint(mouse):
        Kapriz.kapriz_run()
        # pass

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
