import pygame
import sys
import random as rnd
from pygame.locals import *

#Imagens;

LockImage = pygame.image.load("./Images/Lock.jpeg", "LockImage")

KeyImage = pygame.image.load("./Images/Key.png", "KeyImage")

WallImage = pygame.image.load("./Images/Wall.png", "Wall")

ExitImage = pygame.image.load("./Images/Exit.png")

WinImage = pygame.image.load("./Images/You win!.png")

PlayerImage = [pygame.image.load("./Images/player_0.png", "Player1"),
               pygame.image.load("./Images/player_1.png", "Player2"),
               pygame.image.load("./Images/player_2.png", "Player3"),
               pygame.image.load("./Images/player_3.png", "Player4"),
               
               pygame.image.load("./Images/player_4.png", "Player1fl"),
               pygame.image.load("./Images/player_5.png", "Player2fl"),
               pygame.image.load("./Images/player_6.png", "Player3fl"),
               pygame.image.load("./Images/player_7.png", "Player4fl"),]



EnemyImage = [pygame.image.load("./Images/scorpion_0.png", "Scorpion1"),
              pygame.image.load("./Images/scorpion_1.png", "Scorpion2"),
              pygame.image.load("./Images/scorpion_2.png", "Scorpion1fl"),
              pygame.image.load("./Images/scorpion_3.png", "Scorpion2fl"),]

#Música


pygame.mixer.init()
MainTheme = pygame.mixer.music.load("./desert chase.mp3", "DesertChase")




world =[["  ","lB","  ","  ","  "],
        ["  ","l9","lA","  ","  "],
        ["  ","l8","l7","  ","  "],
        ["  ","  ","l6","  ","l5"],
        ["  ","l2","l1","l3","l4"]]


#Quartos


l1 = [["X","X","X","X","L","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," ","X"," "," "," ","X"," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      [" "," ","X"," "," "," ","X"," "," "],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," ","X"," "," "," ","X"," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X","X","X","X","X","X"]]

l2 = [["X","X","X","X","X","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," ","K"," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," "," "],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," ","X"," ","X"," ","X"," ","X"],
      ["X","E","X"," ","X"," ","X"," ","X"],
      ["X","X","X","X","X","X","X","X","X"]]

l3 = [["X","X","X","X","X","X","X","X","X"],
      ["X","X","X","X","X","X","X","X","X"],
      ["X","X","X","X","X","X","X","X","X"],
      ["X","X","X","X","X","X","X","X","X"],
      [" "," "," "," "," "," "," "," "," "],
      ["X","X","X","X","X","X","X","X","X"],
      ["X","X","X","X","X","X","X","X","X"],
      ["X","X","X","X","X","X","X","X","X"],
      ["X","X","X","X","X","X","X","X","X"]]

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
      ["X","X","E"," "," "," ","E","X","X"],
      ["X","X"," "," "," "," "," ","X","X"],
      ["X","X"," "," "," "," "," ","X","X"],
      ["X","X"," "," ","K"," "," ","X","X"],
      ["X","X"," "," "," "," "," ","X","X"],
      ["X","X"," "," "," "," "," ","X","X"],
      ["X","X"," "," "," "," "," ","X","X"],
      ["X","X","X","X"," ","X","X","X","X"]]

l6 = [["X"," "," ","X"," ","X","X","X","X"],
      ["X"," "," ","X"," "," "," "," ","X"],
      ["X"," "," ","X"," "," ","X"," ","X"],
      ["X"," "," ","X"," "," "," "," ","X"],
      ["X","K"," ","X"," "," ","X"," ","X"],
      ["X"," "," ","X"," "," "," "," ","X"],
      ["X"," "," ","X"," "," ","X"," ","X"],
      ["X"," "," ","X"," "," "," "," ","X"],
      ["X","X","X","X"," ","X","X","X","X"]]

l7 = [["X","X","X","X","K","X","X","X","X"],
      ["X","X","X","X","X","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," "," "," ","E"," "," "," ","X"],
      ["L"," "," "," "," "," "," "," ","X"],
      ["X"," "," ","X","X","X","X"," ","X"],
      ["X"," "," ","X"," "," "," "," ","X"],
      ["X"," "," ","X"," "," "," "," ","X"],
      ["X"," "," ","X"," ","X","X","X","X"]]

l8 = [["X","X","X","X","L","X","X","X","X"],
      ["X"," "," "," "," ","X","X","X","X"],
      ["X","X","X"," "," ","X","X","X","X"],
      ["X"," "," "," "," ","X","X","X","X"],
      ["X","X","X"," "," "," "," "," "," "],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X"," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X","X","X","X","X","X"]]

l9 = [["X","X","X","X","L","X","X","X","X"],
      ["X"," "," ","X"," "," "," "," "," "],
      ["X"," "," ","X"," "," "," "," "," "],
      ["X","X"," ","x","X","X","X","X","X"],
      ["X"," "," "," "," "," "," "," "," "],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X"," "," "," "," "," "," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X","X","X","X"," ","X","X","X","X"]]

lA = [["X","X","X","X","X","X","X","X","X"],
      [" "," "," "," "," "," "," "," ","X"],
      [" "," "," "," "," "," "," "," ","X"],
      ["X","X","X"," "," ","X","X"," ","X"],
      [" "," "," "," "," ","X"," "," ","X"],
      ["X"," "," ","X","X","X"," "," ","X"],
      ["X"," "," ","X"," "," "," "," ","X"],
      ["X"," "," ","X"," "," "," ","E","X"],
      ["X","X","X","X"," ","X","X","X","X"]]

lB = [["X","X","X","X","W","X","X","X","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," ","X"," "," "," ","X"," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," ","X"," "," "," ","X"," ","X"],
      ["X"," "," "," "," "," "," "," ","X"],
      ["X"," ","X"," "," "," ","X"," ","X"],
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


def e_dstr(atk,e,t):                  #Função de destruir o inimigo: exclui objeto da lista caso em colisão com objeto de ataque
    for i in range(len(e)):
        if atk.colliderect(e[i]):
            e.pop(i)
            t += 600

def p_atk(pl,state):                      #Função de ataque: Spawna a "arma" do jogador caso certa tecla for pressionada
    k = pygame.key.get_pressed()
    if k[K_SPACE]:
        if state == "Left":
            dagger = pygame.Rect(pl.x-32,pl.y-32,32,96)
        else:
            dagger = pygame.Rect(pl.x+pl.width,pl.y-32,32,96)
    else:
        dagger = pygame.Rect(0,0,0,0)
    
    pygame.draw.rect(win, RED, dagger)
    return dagger

def mov_check():
    if pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_RIGHT]:                    #Função de estado: detecta se o jogador está virado para a esquerda ou direita
        k = pygame.key.get_pressed()
        if k[K_LEFT]:
            state = "Left"
            return state
        elif k[K_RIGHT]:
            state = "Right"
            return state




#---------------------#

#Funções de colisão----#

def tilecolset(lyt):                       #Função de colisão das paredes: cria uma lista com todas as posições com paredes (0 para X e 1 para Y)
    
    scl = []
    sclX = []
    sclY = []


    for i in range(len(lyt)):
        for k in range(len(lyt[i])):
            if lyt[i][k] == "X" or lyt[i][k] == "L":
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


def lock_set(lyt):


    for i in range(len(lyt)):
        for k in range(len(lyt[i])):
            if lyt[i][k] == "L":
                lock = pygame.Rect(k*32,i*32, 32, 32)
                return lock
   
def lock_col_set(lyt,scl):


    for i in range(len(lyt)):
        for k in range(len(lyt[i])):
            if lyt[i][k] == "L":
                scl[0].append(k*32)
                scl[1].append(i*32)
   


def key_set(lyt):

    for i in range(len(lyt)):
        for k in range(len(lyt[i])):
            if lyt[i][k] == "K":
                key = (pygame.Rect(k*32,i*32, 32, 32))
                return key

def keyroom(lyt):

   for i in range(len(lyt)):
        for k in range(len(lyt[i])):
            if lyt[i][k] == "K":
                keyroom = True
                return keyroom

def lockroom(lyt):

   for i in range(len(lyt)):
        for k in range(len(lyt[i])):
            if lyt[i][k] == "L":
                lockroom = True
                return lockroom            


#Funções gráficas-----#

def render(lyt, e, fr):    #Função de renderização: de acordo com a váriavel de matriz fornecida, preenche a cena com tiles
    if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_DOWN] or pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_RIGHT]:
        if pygame.key.get_pressed()[K_LEFT]:
            win.blit(PlayerImage[fr//15], square)
        else:
            win.blit(PlayerImage[4+(fr//15)], square)
    else:
        win.blit(PlayerImage[5], square)            
    







    for i in range(len(lyt)):
        for k in range(len(lyt[i])):
            if lyt[i][k] == "X":
                win.blit(WallImage, pygame.Rect(k*32, i *32, 32, 32))
            if lyt[i][k] == "L":
                win.blit(LockImage, pygame.Rect(k*32, i *32, 32, 32))
            if lyt[i][k] == "K":
                win.blit(KeyImage, pygame.Rect(k*32, i *32, 32, 32))
            if lyt[i][k] == "W":
                win.blit(ExitImage, pygame.Rect(k*32, i *32, 32, 32))               
    
    for i in e:         #Renderiza Inimigos
        if i.x > square.x:
            win.blit(EnemyImage[fr//30], i)
        else:
            win.blit(EnemyImage[2+(fr//30)],i)
    
    pygame.display.flip()   #No final de tudo, atualiza a imagem


def atk_render(atk):        #Função de renderização de ataque: renderiza o ataque
    pygame.draw.rect(win, RED, atk)

def image_transform():
    LockImage.convert(WHT, 0)

#---------------------#

#Funções de chave e cadeado#

def key_collect(key, obj, lyt,pk):

    if obj.colliderect(key):
        lyt[key.y//32][key.x//32] = " "
        key = []
        pk +=1
        key_set(lyt)

def lock_delete(lck, obj, lyt,pk):

    if obj.colliderect(lck) and pk > 0:
        lyt[lck.y//32][lck.x//32] = " "
        lck = []
        pk -=1
        lock_col_set(lyt, [colX,colY])



#Outras funções-------#


time = 100*60
pygame.font.init()
font = pygame.font.SysFont(pygame.font.get_default_font(), 36)

def timerender(t, c):

    time_text = font.render(f"Time: {t//60}", True, c)
    win.blit(time_text, (winW-100,realH-30))

def keyrender(k):
    key_text = font.render(f"Keys: {k}", True, WHT)
    win.blit(key_text, (10,realH-30))

    







clock = pygame.time.Clock() #FPS

#Define altura e largura da tela
winW = 288
winH = 288
realH = 320
win = pygame.display.set_mode((winW,realH))


#Cores

WHT = (255,255,255)
BLK = (0,0,0)
RED = (255, 0, 0)
BLU = (0, 0, 255)
GRN = (0, 255, 0)
BRN = (25, 16, 9)

currentframe = 0

#Posição e tamanho do objeto

sqrInitPosX = winW/2
sqrInitPosY = winW/2

square = pygame.Rect(winW/2,winH/2,30,30)

pkeys = 0 #Essa variável são as chaves do jogador

weapon_time = 0 #Variável para o tempo do ataque

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



pygame.mixer.music.play(0,0,0)



run = True
w = False

while run:  #Loop de entrada: repete toda vez que o jogador entra em um quarto novo

    if w:
        run = False

    

    currentRoom = vardict[world[ly][lx]]
    localrun = True

    enemies = enemylist(currentRoom)
    locks = lock_set(currentRoom)
    keys = key_set(currentRoom)
   
    

    while localrun:  #Loop de quarto: repete o tempo todo

        if time == 1:   #Sair se o tempo for igual a zero
            localrun =False
            run = False

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

        #Subtrai o tempo
        time -= 1

        #Detecta colisão com a chave
        if keyroom(vardict[world[ly][lx]]):
            if square.colliderect(keys):
                vardict[world[ly][lx]][keys.y//32][keys.x//32] = " "
                keys = []
                pkeys +=1
        key_set(vardict[world[ly][lx]])
        #Detecta colisão com cadeado
        if lockroom(vardict[world[ly][lx]]):
            if square.colliderect(locks) and pkeys > 0:
                vardict[world[ly][lx]][locks.y//32][locks.x//32] = " "
                locks = []
                pkeys -=1
                lock_col_set(vardict[world[ly][lx]], [colX,colY])

        
        #Detecta o ataque do jogador
        
        #weapon = p_atk(square,mov_check())


        #Detecta colisão de ataque com inimigo
        #e_dstr(weapon,enemies,time)
        timecolor = WHT
        #Detecta a colisão do jogador com inimigos
        for e in enemies:
            if square.colliderect(e):
                time -= 1
                timecolor = RED

        currentframe += 1     #Váriavel para indicar o atual frame do jogo
        if currentframe  == 60:
            currentframe = 0        

        #Renderiza os objetos
        win.fill(BLK)
        pygame.draw.rect(win, BRN, (0, 0, winW, winH))   #Preenche o fundo
        timerender(time, timecolor)
        keyrender(pkeys)
        #atk_render(weapon)
        render(currentRoom, enemies, currentframe)
        

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

    
        elif square.y < 0:                                #...por cima
            if ly == 0:
                w = True
                localrun = False
                run = False             #Vence o jogo se sair de lB 
            sqrInitPosX = square.x
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


while w:
    for e in pygame.event.get():    #Código para sair do jogo
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
    gameover = pygame.font.SysFont(pygame.font.get_default_font(), 40)
    gameover_text = font.render("YOU WIN! :)", True, BLK)
    win.fill(WHT)

    win.blit(WinImage, pygame.Rect(0,0,0,0))
    win.blit(gameover_text, (0,winH))
    pygame.display.flip()   




while time  == 0:

    for e in pygame.event.get():    #Código para sair do jogo
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
    gameover = pygame.font.SysFont(pygame.font.get_default_font(), 40)
    gameover_text = font.render("YOUR TIME HAS ENDED", True, RED)
    win.fill(BLK)
    win.blit(gameover_text, (0,realH/2))
    pygame.display.flip()
    
