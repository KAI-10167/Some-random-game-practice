import pygame , sys , random

#General setup
pygame.mixer.pre_init(44100,-16,2,512)  #pre loading the sound so there are no delays(not looked into values)
pygame.init()   #initiating the game
clock = pygame.time.Clock()



screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))   #setting up the display window

pygame.display.set_caption("PONG")  #Display name

def ball_animation():
    global ball_speed_x,ball_speed_y , player_score , opponent_score , score_time,speed_int 
    
   
   

    ball.x += ball_speed_x  
    ball.y += ball_speed_y
      

    #scoring points
    if ball.left <= 0:
       pygame.mixer.Sound.play(Score_Sound) 
       player_score += 1
       score_time  = pygame.time.get_ticks()       #this checks time only when scored,ie,once
       
    
    if ball.right >= screen_width:
       pygame.mixer.Sound.play(Score_Sound)
       opponent_score += 1
       score_time  = pygame.time.get_ticks()
      
       

    if ball.top <= 0 or ball.bottom >= screen_height:
       ball_speed_y *= -1   
       pygame.mixer.Sound.play(pong_sound)     #sound





    if ball.colliderect(player) and ball_speed_x > 0:
       pygame.mixer.Sound.play(pong_sound) 
       if abs(ball.right - player.left) < 10:  #this is that if the difference between right of ball and left of ball is les than 10 the x axis is reversed
            ball_speed_x *= -1
       elif abs(ball.top - player.bottom) < 10 and ball_speed_y<0:    #this is differnce between bottom of player and top of ball and checking if the ball is coming from bottom
         ball_speed_y *= -1
       elif abs(ball.bottom - player.top) < 10 and ball_speed_y>0:    #this is differnce between bottom of ball and top of player and checking if the ball is coming from above
         ball_speed_y *= -1


    if  ball.colliderect(opponent) and ball_speed_x<0:
       pygame.mixer.Sound.play(pong_sound) 
       if abs(ball.left - opponent.right) < 10:
         ball_speed_x *= -1  
       elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y<0:    #this is differnce between bottom of player and top of ball and checking if the ball is coming from bottom
         ball_speed_y *= -1
       elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y>0:    #this is differnce between bottom of ball and top of player and checking if the ball is coming from above
         ball_speed_y *= -1


    



def victory():
 global score_time, player_score, opponent_score
 score_time = False
 restart_text = game_font.render(f"{"Would you like to restart?"}",False,white)
 screen.blit(restart_text,(440,500))
 restart_text_enter = game_font.render(f"{"Press Enter"}",False,white)
 screen.blit(restart_text_enter,(560,550))

 if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_KP_ENTER:
        player_score = opponent_score = 0
        score_time = True





def player_animation():
  player.y += player_speed
  if player.top <= 0:
       player.top = 0
  if player.bottom >= screen_height:
       player.bottom = screen_height 

def opponent_ai():
   opponent.y += opponent_speed
   if opponent.top <= 0:
       opponent.top = 0
   if opponent.bottom >= screen_height:
       opponent.bottom = screen_height 

def ball_restart():
   global ball_speed_x,ball_speed_y , current_time , score_time , ball_colour , speed_int , time
   current_time = pygame.time.get_ticks()             #this checks for time all the time
   ball.center = (screen_width/2,screen_height/2)

   time = current_time - score_time

   if 1400<current_time - score_time<2100:
      num_three = game_font.render(f"{1}",False,white)
      screen.blit(num_three,(screen_width/2-10,screen_height/2 + 50))
   if 700<current_time - score_time<1400:
      num_two = game_font.render(f"{2}",False,white)
      screen.blit(num_two,(screen_width/2-10,screen_height/2 +50))
   if current_time - score_time<700:
      num_one = game_font.render(f"{3}",False,white)
      screen.blit(num_one,(screen_width/2-10,screen_height/2 +50))      
 

   if time<2100:   #2100 is 2.1 secs
      ball_speed_x = ball_speed_y = 0
   else:
      ball_speed_x = speed_int* random.choice((-1,1))
      ball_speed_y = speed_int* random.choice((-1,1))
      score_time = None
      
       
   
  
      


ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)   # x-position, y-position,  width, height  screen_width/2 would make it the top left corner of the fourth quadrant, therefore, we subtract half of the object itself
player = pygame.Rect(screen_width - 30, screen_height/2 - 70, 20 , 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 20 , 140)

speed_int = 7  # speed of ball 


ball_speed_x = speed_int *random.choice((-1,1))
ball_speed_y = speed_int *random.choice((-1,1))
player_speed = 0
opponent_speed = 0


player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

#sound
pong_sound = pygame.mixer.Sound("pong.ogg")
Score_Sound = pygame.mixer.Sound("score.ogg")





score_time = True

#rgb
bg_colour = pygame.Color("grey12")  
red= (220,0,0)
blue = (0,0,220)
white = (255,255,255)
ball_colour = white

while True:   #checking for inputs
    for event in pygame.event.get():
      if event.type == pygame.QUIT:   #if the input is quit then 
         pygame.quit()                #Quit from pygame
         sys.exit()                   #Quit the application

         #player controls
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
            player_speed += 20  #speed
         if event.key == pygame.K_UP:
            player_speed -= 20   
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN:
            player_speed -= 20
         if event.key == pygame.K_UP:
            player_speed += 20 
            
            #opponent controls

      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_s:
            opponent_speed += 20
         if event.key == pygame.K_w:
            opponent_speed -= 20   

      if event.type == pygame.KEYUP:
         if event.key == pygame.K_s:
            opponent_speed -= 20
         if event.key == pygame.K_w:
            opponent_speed += 20        
         

    ball_animation()
    player_animation()
    opponent_ai()

    #visuals
    screen.fill(bg_colour)
    pygame.draw.rect(screen,red,player)
    pygame.draw.rect(screen,blue,opponent)
    pygame.draw.ellipse(screen,ball_colour,ball)     
    pygame.draw.aaline(screen,white,(screen_width/2,0),(screen_width/2,screen_height))   #for drawing a centre line where 3 is x1,y1 and 4 is x2,y2






    player_text = game_font.render(f"{player_score}",False,white)
    screen.blit(player_text,(710,400))

    opponent_text = game_font.render(f"{opponent_score}",False,white)
    screen.blit(opponent_text,(550,400))

    if score_time:
       ball_restart()
    

    #Winning text
    win_text = game_font.render(f"{"You Win"}",False,white)
    lose_text = game_font.render(f"{"You Lose"}",False,white)

    if player_score  == 10:
         victory()

    if opponent_score == 10:
       victory()

    if player_score == 10:
            screen.blit(win_text,(960,400))
            screen.blit(lose_text,(320,400))
    elif opponent_score == 10:
            screen.blit(win_text,(320,400))
            screen.blit(lose_text,(960,400))


     




    pygame.display.flip()  #draws screen from previous inputs
    clock.tick(60)         #Fps
  



