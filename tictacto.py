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
      
      pygame.draw.line(win, black, [200, 0], [200,610], 5)
      pygame.draw.line(win, black, [400, 0], [400,610], 5)
      pygame.draw.line(win, black, [0, 200], [610,200], 5)
      pygame.draw.line(win, black, [0, 400], [610,400], 5)
      
      keys=pygame.key.get_pressed()

      if keys[pygame.K_KP7]:
          gameDisplay.blit(X,(x,y))
      elif keys[pygame.K_KP8]:
          gameDisplay.blit(X,(x+205,y))
      elif keys[pygame.K_KP9]:
          gameDisplay.blit(X,(x+410,y))
      elif keys[pygame.K_KP4]:
          gameDisplay.blit(X,(x,y+205))
      elif keys[pygame.K_KP5]:
          gameDisplay.blit(X,(x+205,y+205))
      elif keys[pygame.K_KP6]:
          gameDisplay.blit(X,(x+410,y+205))
      elif keys[pygame.K_KP1]:
          gameDisplay.blit(X,(x,y+400))
      elif keys[pygame.K_KP2]:
          gameDisplay.blit(X,(x+205,y+410))
      elif keys[pygame.K_KP3]:
          gameDisplay.blit(X,(x+410,y+410))
      else:
            pass


      pygame.display.update()

      
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

# main loop
run=True
game_intro()
win.fill((255,255,255))
while run :
      pygame.time.delay(100)
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run=False
      
      for _ in range(8):
            print(_)
            get_input()
      
      
      
      
pygame.quit()      
