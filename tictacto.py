# importing the pygame library
import pygame

# initialization of pygame
pygame.init()

# creating a window
win = pygame.display.set_mode((600,600))
win.fill((255,255,255))

# editing the name
pygame.display.set_caption("TIC TAC TO")

# defining the image
X = pygame.image.load('x.png')
O = pygame.image.load('o.png')

# image display size
display_width = 610
display_height = 610

gameDisplay = pygame.display.set_mode((display_width,display_height))

#coordinates
x=0
y=0

player1=''
player2=''
intro=False

def playerX():
      global  player1
      global  player2
      global intro
      player1= 'x'
      player2= 'o'
      intro = False
      print("x")
     
def playerO():
      global  player1
      global  player2
      global intro
      player1 = 'o'
      player2 = 'x'
      intro = False
      print("o")
     
# Get user input and Display
def get_input():
      global X
      global O
      ram = True
      mylist=[' ', ' ' , ' ' , ' ' , ' ' , ' ' ,' ' , ' ' , ' ']
      print(f"loop 2{player1}")
      alter=True
      key_pressed=True
      while ram:
            print('loop3')
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        
                        pygame.quit()
                        quit()
            pygame.time.delay(100)
            pygame.draw.line(win, black, [200, 0], [200,610], 5)
            pygame.draw.line(win, black, [400, 0], [400,610], 5)
            pygame.draw.line(win, black, [0, 200], [610,200], 5)
            pygame.draw.line(win, black, [0, 400], [610,400], 5)

            

            if alter and key_pressed:
                  key_pressed=False
                  if player1=='x':
                        flag=X
                        player=player1
                        alter=False
                  else:
                        flag=O
                        player=player1
                        alter=False
            elif  not alter and key_pressed:
                  key_pressed=False
                  if player2=='x':
                        flag=X
                        player=player2
                        alter=True
                  else:
                        flag=O
                        player=player2
                        alter=True


            keys=pygame.key.get_pressed()

            if keys[pygame.K_KP7] and mylist[6]==" ":
                  gameDisplay.blit(flag,(x,y))
                  mylist[6]=player
                  key_pressed= True
            elif keys[pygame.K_KP8]and mylist[7]==" ":
                  gameDisplay.blit(flag,(x+205,y))
                  mylist[7]=player
                  key_pressed= True
            elif keys[pygame.K_KP9]and mylist[8]==" ":
                  gameDisplay.blit(flag,(x+410,y))
                  mylist[8]=player
                  key_pressed= True
            elif keys[pygame.K_KP4]and mylist[3]==" ":
                  gameDisplay.blit(flag,(x,y+205))
                  mylist[3]=player
                  key_pressed= True
            elif keys[pygame.K_KP5]and mylist[4]==" ":
                  gameDisplay.blit(flag,(x+205,y+205))
                  mylist[4]=player
                  key_pressed= True
            elif keys[pygame.K_KP6]and mylist[5]==" ":
                  gameDisplay.blit(flag,(x+410,y+205))
                  mylist[5]=player
                  key_pressed= True
            elif keys[pygame.K_KP1]and mylist[0]==" ":
                  gameDisplay.blit(flag,(x,y+400))
                  mylist[0]=player
                  key_pressed= True
            elif keys[pygame.K_KP2]and mylist[1]==" ":
                  gameDisplay.blit(flag,(x+205,y+410))
                  mylist[1]=player
                  key_pressed= True
            elif keys[pygame.K_KP3]and mylist[2]==" ":
                  gameDisplay.blit(flag,(x+410,y+410))
                  mylist[2]=player
                  key_pressed= True
            else:
                  pass
            pygame.display.update()
            game(mylist)

      
# game intro
black = (0,0,0)
white = (255,255,255)
green= (0,225,0)
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():
      global intro
      intro= True

      while intro:
            
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",75)
        TextSurf, TextRect = text_objects("Choose X or O !", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("X",135,450,100,50,white,green,playerX)
        button("0",385,450,100,50,white,green,playerO)

        pygame.display.update()
        clock.tick(7)

#solution
def game(mylist):
      print(mylist)
      


# main loop
run=True
game_intro()
win.fill((255,255,255))
get_input()

while run :
      pygame.time.delay(100)
      print("loop 1")
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run=False
      
      
      
      
      
pygame.quit()      
