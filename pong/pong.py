import pygame , sys , random

#General setup
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))   #setting up the display window

pygame.display.set_caption("PONG")  #Display name

def ball_animation():
    global ball_speed_x,ball_speed_y , player_score , opponent_score , score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #collison
    if ball.left <= 0:
       player_score += 1
       score_time  = pygame.time.get_ticks()       #this checks time only when scored,ie,once
        
    
    if ball.right >= screen_width:
       opponent_score += 1
       score_time  = pygame.time.get_ticks()
       

    if ball.top <= 0 or ball.bottom >= screen_height:
       ball_speed_y *= -1   

    if ball.colliderect(player) or ball.colliderect(opponent):
       ball_speed_x *= -1
   


def player_animation():
  player.y += player_speed
  if player.top <= 0:
       player.top = 0
  if player.bottom >= screen_height:
       player.bottom = screen_height 

def opponent_ai():
   if opponent.top < ball.y:
      opponent.top += opponent_speed         
   if opponent.bottom > ball.y:
      opponent.bottom -= opponent_speed
   if opponent.top <= 0:
       opponent.top = 0
   if opponent.bottom >= screen_height:
       opponent.bottom = screen_height 

def ball_restart():
   global ball_speed_x,ball_speed_y , current_time , score_time
   current_time = pygame.time.get_ticks()             #this checks for time all the time
   ball.center = (screen_width/2,screen_height/2)

   if 1400<current_time - score_time<2100:
      num_three = game_font.render(f"{1}",False,white)
      screen.blit(num_three,(screen_width/2-10,screen_height/2 + 50))
   if 700<current_time - score_time<1400:
      num_two = game_font.render(f"{2}",False,white)
      screen.blit(num_two,(screen_width/2-10,screen_height/2 +50))
   if current_time - score_time<700:
      num_one = game_font.render(f"{3}",False,white)
      screen.blit(num_one,(screen_width/2-10,screen_height/2 +50))      
      





   if current_time - score_time<2100:   #2100 is 2.1 secs
      ball_speed_x = ball_speed_y = 0
   else:
      ball_speed_x = 7* random.choice((-1,1))
      ball_speed_y = 8* random.choice((-1,1))
      score_time = None
 
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)   # x-position, y-position,  width, height  screen_width/2 would make it the top left corner of the fourth quadrant, therefore, we subtract half of the object itself
player = pygame.Rect(screen_width - 30, screen_height/2 - 70, 20 , 140)
opponent = pygame.Rect(20, screen_height/2 - 70, 20 , 140)


ball_speed_x = 7 *random.choice((-1,1))
ball_speed_y = 8 *random.choice((-1,1))
player_speed = 0
opponent_speed = 12


player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)


score_time = True

#rgb
bg_colour = pygame.Color("grey12")  
red= (220,0,0)
blue = (0,0,220)
white = (255,255,255)


while True:   #checking for inputs
    for event in pygame.event.get():
      if event.type == pygame.QUIT:   #if the input is quit then 
         pygame.quit()                #Quit from pygame
         sys.exit()                   #Quit the application
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
            player_speed += 10
         if event.key == pygame.K_UP:
            player_speed -= 10   
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN:
            player_speed -= 10
         if event.key == pygame.K_UP:
            player_speed += 10  
         

    ball_animation()
    player_animation()
    opponent_ai()

    #visuals
    screen.fill(bg_colour)
    pygame.draw.rect(screen,red,player)
    pygame.draw.rect(screen,blue,opponent)
    pygame.draw.ellipse(screen,white,ball)     
    pygame.draw.aaline(screen,white,(screen_width/2,0),(screen_width/2,screen_height))   #for drawing a centre line where 3 is x1,y1 and 4 is x2,y2






    player_text = game_font.render(f"{player_score}",False,white)
    screen.blit(player_text,(660,400))

    opponent_text = game_font.render(f"{opponent_score}",False,white)
    screen.blit(opponent_text,(600,400))

    if score_time:
       ball_restart()

    pygame.display.flip()  #draws screen from previous inputs
    clock.tick(60)         #Fps
  



