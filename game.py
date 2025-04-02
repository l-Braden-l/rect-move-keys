# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 
import random
def init_game (): 
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True



# -- Draw Rectangle -- #
def draw_rectangle(screen,color,x,y,width,height): 
   pygame.draw.rect(screen, color, (x, y, width, height))



def main():
   screen = init_game()

   # -- Create Font Object -- #
   font = pygame.font.Font(None,36) # default font, size 36

   # -- Rectangle 1 -- #
   color1 = config.RED
   x1, y1 = 395,125
   width1 = 250
   height1 = 125

   # -- Rectangle 2 -- #
   color2 = config.BLUE
   x2, y2 = 195,425
   width2 = 150
   height2 = 190

   clock = pygame.time.Clock() # Initialize the clock here

   running = True
   while running:
      running = handle_events()

      # -- Change border -- #
      increase = 1

      # -- How many pixels to move -- #
      value = 1

      # -- Render text -- #
      text_surface1 = font.render('Use arrow keys to move the red rectangle!', True, config.BLACK)
      text_surface2 = font.render('Use W,A,S,D to move the blue rectangle!', False, config.BLACK)
      

      # -- Key Pressed (Red Rectangle) -- #
      key = pygame.key.get_pressed()
      if key[pygame.K_LEFT]: # Move left
         x1 -= value
      if key[pygame.K_RIGHT]: # Move right
         x1 += value
      if key[pygame.K_UP]: # Move up
         y1 -= value
      if key[pygame.K_DOWN]: # Move down
         y1 += value

         # -- Key Pressed (Blue Rectangle) -- #
      key = pygame.key.get_pressed()
      if key[pygame.K_a]: # Move left
         x2 -= value
      if key[pygame.K_d]: # Move right
         x2 += value
      if key[pygame.K_w]: # Move up
         y2 -= value
      if key[pygame.K_s]: # Move down
         y2 += value

         # -- Change Both Shapes -- # 
      if key[pygame.K_1]:
         height1 += value
         height2 += value
      if key[pygame.K_2]:
         width1 += value
         width2 += value
      if key[pygame.K_3]:
         width1 -= value
         width2 -= value
      if key[pygame.K_4]:
         height1 -= value
         height2 -= value
      if key[pygame.K_r]:
         color1 = random.randint((0,255)(0,255)(0,255))
         color2 = random.randint((0,255)(0,255)(0,255))
      

      screen.fill(config.WHITE) # Use color from config

      # -- Draw Shapes -- #
      draw_rectangle(screen,color1, x1, y1, width1, height1) # Draw Red Rectangle
      draw_rectangle(screen, color2, x2, y2, width2, height2) # Draw Blue Rectangle

   
      # -- How Many Pixels Wide (Text) -- #
         # -- Text one -- #
      text_width1 = text_surface1.get_width() 
      text1_x = 250
      # -- Set Fixed y-coordinate for text -- #
      text1_y = 50 

         # -- Text Two -- #
      text_width2 = text_surface2.get_width() 
      text2_x = 30
      # -- Set Fixed y-coordinate for text -- #
      text2_y = 300 

      # -- Blit Text(s) -- #
      screen.blit(text_surface1, (text1_x, text1_y))
      screen.blit(text_surface2, (text2_x, text2_y))

      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()