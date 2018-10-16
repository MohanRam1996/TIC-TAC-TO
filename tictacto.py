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
winner=''
pygame.time.delay(100)
run=True
end=True
draw=False
def playerX():
      global  player1
      global  player2
      global intro
      player1= 'x'
      player2= 'o'
      intro = False
      
def playerO():
      global  player1
      global  player2
      global intro
      player1 = 'o'
      player2 = 'x'
      intro = False
      
def run_false():
      global run
      global end
      end=False
      run=False
      

def run_true():
      global run
      global end
      end=False
      
      
      
     
# Get user input and Display
def get_input():
      win.fill((255,255,255))
      global X
      global O
      ram = True
      mylist=[' ', ' ' , ' ' , ' ' , ' ' , ' ' ,' ' , ' ' , ' ']
      alter=True
      key_pressed=True
      player=player1
      while ram:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()

            pygame.time.delay(10)
            
            pygame.draw.line(win, black, [200, 0], [200,610], 5)
            pygame.draw.line(win, black, [400, 0], [400,610], 5)
            pygame.draw.line(win, black, [0, 200], [610,200], 5)
            pygame.draw.line(win, black, [0, 400], [610,400], 5)
            # for the first time when this loop is executing key_pressed and alter is true
            # since player 1 plays first
            if key_pressed:
                  key_pressed=False
                  ram=game(mylist,player)
                  if alter :
                        if player1=='x':
                              flag=X 
                        else:
                              flag=O
                        player=player1
                        alter=False
                        
                  else:
                        if player2=='x':
                              flag=X
                        else:
                              flag=O
                        player=player2
                        alter=True

            #print(f'loop3{player}')
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

      
# game intro prerequestie
black = (0,0,0)
white = (255,255,255)
green= (0,225,0)
red=(255,0,0)
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None :
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

#game intro display
def game_intro():
    global intro
    intro= True

    while intro:
        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",75)
        TextSurf, TextRect = text_objects("Choose X or O !", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("X",135,450,100,50,white,green,playerX)
        button("0",385,450,100,50,white,green,playerO)

        pygame.display.update()
        clock.tick(7)

# game ending page

def game_end():
      global end
      end = True
      while end:
          for event in pygame.event.get():
              if event.type == pygame.QUIT: pygame.quit()
                            
          gameDisplay.fill(white)
          largeText = pygame.font.SysFont("comicsansms",65)
          TextSurf, TextRect = text_objects(f"{winner} won the match !!", largeText)
          TextRect.center = ((display_width/2),(display_height/2))
          gameDisplay.blit(TextSurf, TextRect)
          button("<-Restart",135,450,100,50,white,green,run_true)
          button("Quit->",385,450,100,50,white,red,run_false)
          pygame.time.delay(100)
          pygame.display.update()
          clock.tick(7)
                 
        
# game draw page

def game_draw():
      global draw
      global end
      end = True
      draw=False
      while end:
          for event in pygame.event.get():
              if event.type == pygame.QUIT: pygame.quit()
                            
          gameDisplay.fill(white)
          largeText = pygame.font.SysFont("comicsansms",63)
          TextSurf, TextRect = text_objects(f"Match is a Draw!!!", largeText)
          TextRect.center = ((display_width/2),(display_height/2))
          gameDisplay.blit(TextSurf, TextRect)
          button("<-Restart",135,450,100,50,white,green,run_true)
          button("Quit->",385,450,100,50,white,red,run_false)
          pygame.time.delay(100)
          pygame.display.update()
          clock.tick(7)
          

#solution     
def game(mylist1,player):
      global winner
      global draw
      #print(f"loop 4{player} {mylist1}")
      if mylist1.count(player)>2:
            win=[[0,1,2],[2,5,8],[6,7,8],[0,3,6],[0,4,8],[2,4,6],[3,4,5],[1,4,7]]
            indices = [i for i, x in enumerate(mylist1) if x == player]
            counter=0
            for n in win: 
                  for item in n:
                        try:
                              indices.index(item)
                              counter+=1
                        except ValueError:
                                 pass
                  if counter==3:
                      winner=player
                      return False
                  counter=0
     
      if mylist1.count(player)==5:
          draw=True
          return False
      return True
          

# main loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                  pygame.quit()

    game_intro()
    get_input()
    if draw:
        game_draw()
    else:
        game_end()
    

    
pygame.quit()
