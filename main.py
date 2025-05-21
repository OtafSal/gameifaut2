import pygame
from pygame.locals import *



l1 = [["X","X"," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
      ]

#Funções do jogador---#

def movement(obj, spd):             #Função de movimento: Jogador se move a uma determinada velocidade de acordo com as teclas
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and obj.x > 0:
        obj.move_ip(-spd,0)
    if keys[K_RIGHT] and obj.right < winW:
        obj.move_ip(spd,0)
    if keys[K_UP] and obj.y > 0:
        obj.move_ip(0,-spd)
    if keys[K_DOWN] and obj.bottom < winH:
        obj.move_ip(0,spd)

#---------------------#

#Funções gráficas-----#

def render():    #Função de renderização: de acordo com a váriavel de matriz fornecida, preenche a cena com tiles
    win.fill(BLK)   #Preenche o fundo
    pygame.draw.rect(win, WHT, square)
    pygame.display.flip()
'''
    for i in range(len(lyt)):
        for k in range(len(lyt[i])):
            if lyt[i][k] == "X":
                wall = pygame.rect(k*32, i *32, 32, 32)
                pygame.draw.rect(win, WHT, wall)
'''

#---------------------#

#Outras funções-------#









clock = pygame.time.Clock() #FPS

#Define altura e largura da tela
winW = 512
winH = 512
win = pygame.display.set_mode((winW,winH))


#Cores

WHT = (255,255,255)
BLK = (0,0,0)

#Posição e tamanho do objeto

square = pygame.Rect(winW/2,winH/2,32,32)

#Loop de jogo
run = True

while run:
    
    for e in pygame.event.get():    #Código para sair do jogo
        if e.type == QUIT:
            run = False

    
    #Mover o quadrado
    movement(square, 2)

    #Renderiza os objetos
    render()

    #Define o FPS
    clock.tick(60)
