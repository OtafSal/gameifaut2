import pygame
from pygame.locals import *

world =[["  ","lB","  ","  ","  "],
        ["  ","l9","lA","  ","  "],
        ["  ","l8","l7","  ","  "],
        ["  ","  ","l6","  ","l5"],
        ["  ","l2","l1","l3","l4"]]


#Quartos


l1 = [["X","X","X","X"," ","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," ","X"," ","E"," ","X"," ","X"],
      ["X"," "," "," "," ","E"," "," ","X"],
      [" "," ","X"," "," "," ","X"," "," "],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," ","X"," "," "," ","X"," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X"," ","X","X","X","X"]]

l2 = [["X","X","X","X","X","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," ","E"," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," "," "],
      ["X"," ","X"," "," "," "," "," ","X"],
      ["X"," ","X"," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X","X","X","X","X","X"]]

l3 = [[" "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "],
      ["X","X","X","X","X","X","X","X","X"],
      [" "," "," "," "," "," "," "," "," "],
      ["X","X","X","X","X","X","X","X","X"],
      [" "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "],
      [" "," "," "," "," "," "," "," "," "]]

l4 = [["X","X","X","X"," ","X","X","X","X"],
      ["X"," "," "," "," ","X","X","X","X"],
      ["X"," "," "," "," ","X","X","X","X"],
      ["X"," "," "," "," ","X","X","X","X"],
      [" "," "," "," "," ","X","X","X","X"],
      ["X","X","X","X","X","X","X","X","X"],
      ["X","X","X","X","X","X","X","X","X"],
      ["X","X","X","X","X","X","X","X","X"],
      ["X","X","X","X","X","X","X","X","X"]]

l5 = [["X","X","X","X","X","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X"," ","X","X","X","X"]]

l6 = [["X","X","X","X"," ","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      [" "," "," "," "," "," "," "," "," "],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X"," ","X","X","X","X"]]

l7 = [["X","X","X","X"," ","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      [" "," "," "," "," "," "," "," "," "],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X"," ","X","X","X","X"]]

l8 = [["X","X","X","X"," ","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      [" "," "," "," "," "," "," "," "," "],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X"," ","X","X","X","X"]]

l9 = [["X","X","X","X"," ","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      [" "," "," "," "," "," "," "," "," "],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X"," ","X","X","X","X"]]

lA = [["X","X","X","X"," ","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      [" "," "," "," "," "," "," "," "," "],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X"," ","X","X","X","X"]]

lB = [["X","X","X","X"," ","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      [" "," "," "," "," "," "," "," "," "],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X"," ","X","X","X","X"]]






#Funções do jogador---#

def movement(obj, spd):             #Função de movimento: Jogador se move a uma determinada velocidade de acordo com as teclas
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and tilecoldetect(colX,colY, pygame.Rect(obj.x ,obj.y+2 , 1, 27)) == False:
        obj.move_ip(-spd,0)
    if keys[K_RIGHT] and tilecoldetect(colX,colY, pygame.Rect(obj.right ,obj.y+2 , 1, 27)) == False:
        obj.move_ip(spd,0)
    if keys[K_UP] and tilecoldetect(colX,colY, pygame.Rect(obj.x+2 ,obj.y , 27, 1)) == False:
        obj.move_ip(0,-spd)
    if keys[K_DOWN] and tilecoldetect(colX,colY, pygame.Rect(obj.x+2 ,obj.bottom , 27, 1)) == False:
        obj.move_ip(0,spd)






#---------------------#

#Funções de colisão----#

def tilecolset(lyt):                       #Função de colisão das paredes: cria uma lista com todas as posições com paredes (0 para X e 1 para Y)
    
    scl = []
    sclX = []
    sclY = []


    for i in range(len(lyt)):
        for k in range(len(lyt[i])):
            if lyt[i][k] == "X":
                sclX.append(k*32)
                sclY.append(i*32)
    
    scl = [sclX, sclY]
    return scl
                
def tilecoldetect(X, Y, obj):               #2° Função de colião das paredes: detecta se há uma colisão entre o objeto especificado e cada uma das paredes

    rtn = False

    for i in range(len(X)):
        if obj.colliderect(pygame.Rect(X[i], Y[i], 32, 32)):
            rtn = True
    return rtn
            
#---------------------#

#Funções de sprites---#

def enemylist(lyt):
    enms = []
    for i in range(len(lyt)):
        for k in range(len(lyt[i])):
            if lyt[i][k] == "E":
                enms.append(pygame.Rect(k*32,i*32, 32, 32))
    
    return enms

def mov(self, player):
    if self.x != player.x and self.y != player.y:
        self.move_ip((player.x-self.x)/abs(player.x-self.x),(player.y-self.y)/abs(player.y-self.y))
    else:
        self.move_ip((player.x-self.x+1)/abs(player.x-self.x+1),(player.y-self.y+1)/abs(player.y-self.y+1))



                


#Funções gráficas-----#

def render(lyt, e):    #Função de renderização: de acordo com a váriavel de matriz fornecida, preenche a cena com tiles
    win.fill(BLK)   #Preenche o fundo
    pygame.draw.rect(win, WHT, square)
    

    for i in range(len(lyt)):
        for k in range(len(lyt[i])):
            if lyt[i][k] == "X":
                pygame.draw.rect(win, GRN, pygame.Rect(k*32, i *32, 32, 32))
    
    for i in e:         #Renderiza Inimigos
        pygame.draw.rect(win, RED, i)
    
    pygame.display.flip()   #No final de tudo, atualiza a imagem


#---------------------#

#Outras funções-------#











clock = pygame.time.Clock() #FPS

#Define altura e largura da tela
winW = 288
winH = 288
win = pygame.display.set_mode((winW,winH))


#Cores

WHT = (255,255,255)
BLK = (0,0,0)
RED = (255, 0, 0)
BLU = (0, 0, 255)
GRN = (0, 255, 0)



#Posição e tamanho do objeto

sqrInitPosX = winW/2
sqrInitPosY = winW/2

square = pygame.Rect(winW/2,winH/2,30,30)



#Coordenadas do quarto:

vardict = {"l1": l1,
           "l2": l2,
           "l3": l3,
           "l4": l4,
           "l5": l5,
           "l6": l6,
           "l7": l7,
           "l8": l8,
           "l9": l9,
           "lA": lA,
           "lB": lB}    #Usado para converter texto em variáveis


lx = 2
ly = 4






run = True

while run:  #Loop de entrada: repete toda vez que o jogador entra em um quarto novo

    

    currentRoom = vardict[world[ly][lx]]
    localrun = True

    enemies = enemylist(currentRoom)
    

    while localrun:  #Loop de quarto: repete o tempo todo
    
        for e in pygame.event.get():    #Código para sair do jogo
            if e.type == QUIT:
                localrun = False
                run = False

        colX = tilecolset(currentRoom)[0]           #Define colisões X e Y
        colY = tilecolset(currentRoom)[1] 

    
        #Mover o quadrado
        movement(square, 2)

        for i in range(len(enemies)):   #Movimenta os inimigos
            mov(enemies[i], square)


        #Renderiza os objetos
        render(currentRoom, enemies)

        #Checa a saída do quarto
        if square.x < 0:                #Sair do quarto...
            sqrInitPosX = winW - square.width               #...pela esquerda
            sqrInitPosY = square.y
            square = pygame.Rect(sqrInitPosX,sqrInitPosY,30,30)
            lx -= 1
            localrun = False
  

        elif square.right > winW:                
            sqrInitPosX = 0                                #...pela direita
            sqrInitPosY = square.y
            square = pygame.Rect(sqrInitPosX,sqrInitPosY,30,30)
            lx += 1
            localrun = False

    
        elif square.y < 0:                
            sqrInitPosX = square.x                                #...por cima
            sqrInitPosY = winH - square.height
            square = pygame.Rect(sqrInitPosX,sqrInitPosY,30,30)
            ly -= 1
            localrun = False

    
        elif square.bottom > winH:                
            sqrInitPosX = square.x                                #...por cima
            sqrInitPosY = 0
            square = pygame.Rect(sqrInitPosX,sqrInitPosY,30,30)
            ly += 1
            localrun = False


        #Define o FPS
        clock.tick(60)

 
