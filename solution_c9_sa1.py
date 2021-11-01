import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
bird=pygame.Rect(100,250,30,30)

# Creating a variable 'groundx' and initializing to 0.
groundx=0

while True:
    
  screen.blit(images["bg"],[0,0])
  # Decrementing 'groundx'by 5
  groundx-=5
  # Checking if 'groundx' becomes less than -550
  if groundx<-550:
      # Resetting the value of 'groundx' back to 0
      groundx=0
      
  screen.blit(images["ground"],[groundx,550])
  screen.blit(images["bird"],bird)
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
        
  
  pygame.display.update()
  pygame.time.Clock().tick(30)
