import pygame , sys , random
from pygame.locals import *
from pygame.sprite import Group

#Initialising
pygame.init()

#clock
clock = pygame.time.Clock()

screen_width = 540
screen_height = 800

#display
screen = pygame.display.set_mode((screen_width,screen_height))

# Name
pygame.display.set_caption("FLAPPY BIRD")


#variables and constants
scroll_speed = 2
backgroundimg = pygame.image.load('background.png')
baseimg = pygame.image.load('base1.png')
base_x = 0
pipe_gap = 200
pipe_frequency = 1700
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pipe_pass = False
game_font = pygame.font.SysFont('Bauhaus 93',60)
black = (255,255,255)

#creating flappy
class bird(pygame.sprite.Sprite):
   def __init__(self, x,y):
      pygame.sprite.Sprite.__init__(self)
      
      self.images = []
      self.index = 0
      self.counter = 0
      for num in range(1,4):   #Adding the images to the list
         img = pygame.image.load(f'bird{num}.png')
         self.images.append(img)


      self.image = self.images[self.index]  #choosing the image 
      self.rect = self.image.get_rect()      #borders of the image
      self.rect.center =[x,y]
      self.velocity  = 0
      self.clicked = False


   def update(self):
      
     #gravity
     if flying == True:
            self.velocity += 0.5       
            if self.velocity > 8:  #limiting the gravity
                self.velocity = 8 
            if self.rect.bottom < 700:
                self.rect.y += int(self.velocity)
            
     if game_over == False:        
         if pygame.mouse.get_pressed()[0] == True and self.clicked == False:   #[0] means the left mouse button
             self.clicked = True
             self.velocity = -10
                #when the mouse is not clicked
         if pygame.mouse.get_pressed()[0] == False:
             self.clicked = False
                #this is so that it does not keep increasing when the mouse is pressed down




         if self.rect.top <= 0 : #limiting on top of screen
             self.rect.top = 0
        



         if flying == True:

                #Animation
                self.counter += 1
                flap_cooldown = 5

                if self.counter > flap_cooldown:  #for changing the index
                        self.counter = 0
                        self.index += 1
                        if self.index >= len(self.images):  #if the index is greater than num of images
                            self.index = 0
                        self.image = self.images[self.index]
                

            #rotation of the bird
         self.image = pygame.transform.rotate(self.images[self.index], (self.velocity * -2))
     else:
         self.image = pygame.transform.rotate(self.images[self.index], -90)
              
    

class pipes(pygame.sprite.Sprite):
  def __init__(self,x,y,position):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load('pipe-green.png')
    self.rect = self.image.get_rect()
 #positon 1 is for top and -1 is for bottom
    if position == 1:
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect.bottomleft = [x,y - int(pipe_gap/2)]
    if position == -1:
      self.rect.topleft = [x,y + int(pipe_gap/2)]    



  def update(self):
    self.rect.x -= scroll_speed   
    if self.rect.right < 0 :
        self.kill()








bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()


flappy = bird(50,int(screen_height/2))
bird_group.add(flappy)



#Run
run = True
game_over = False
flying = False

while run:   

 screen.blit(backgroundimg,(0,0))   

 pipe_group.draw(screen)
 

 screen.blit(baseimg,(base_x,700))

 if flappy.rect.bottom >= 700:
     game_over = True
     flying = False
      
 bird_group.draw(screen)
 bird_group.update()
    
 #collison
 if pygame.sprite.groupcollide(bird_group,pipe_group,False,False):  #false means do not kill
      game_over = True
  

 if game_over == False and flying == True:
     #generating new pipes
     time_now = pygame.time.get_ticks()
     if time_now - last_pipe > pipe_frequency:  
            pipe_height = random.randint(-200,200)       
            bottom_pipe = pipes(screen_width,int(screen_height/2)+pipe_height,-1)
            top_pipe = pipes(screen_width,int(screen_height/2)+pipe_height,1)
            pipe_group.add(bottom_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

         

     #scrolling
     base_x -= scroll_speed
     if abs(base_x) > 140:
         base_x = 0

     pipe_group.update()
 



 if len(pipe_group)>0:
     if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.left < pipe_group.sprites()[0].rect.right and pipe_pass == False:
         pipe_pass = True
     if pipe_pass == True:
         if  bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
             score += 1
             pipe_pass = False

              

 for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
         flying = True
    if event.type == pygame.QUIT:   #if the input is quit then 
         pygame.quit()                #Quit from pygame
         sys.exit() 

    
 score_text = game_font.render(f"{score}",False,black)
 screen.blit(score_text,(250,65))
    



 pygame.display.flip()    
    #game speed
 clock.tick(60)         