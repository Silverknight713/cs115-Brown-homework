"""
Jaden Brown
3/3/25
Assignment #8
Description: Reworking the background of the game to fit segments, then adding movement and boundaries to keep the frog within the screen.
"""
import pygame
from pygame.constants import KEYDOWN

#initialize pygame
pygame.init()

#window dimensions and display
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("frogger")

# fps
clock = pygame.time.Clock()
dt = 0
speed = 10

#Frog Position
cur_pos = [300,380]

#Car Positions
c1_pos = [0,45] #black car
c2_pos = [600,125] #purple car
c3_pos = [0,225] #red car
c4_pos = [600,305] #blue car

"""game loop"""
running = True
while running:
  """Handle events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == KEYDOWN:
      if event.key == pygame.K_ESCAPE: #escape key
        running = False
      if event.key == pygame.K_w: #moving up
        cur_pos[1] -= 20
      if event.key == pygame.K_s: #moving down
        cur_pos[1] += 20
      if event.key == pygame.K_a: # moving left 
        cur_pos[0] -= 20
      if event.key == pygame.K_d: # moving right
        cur_pos[0] += 20
  """Car Movements"""
  #car1
  if c1_pos[0] > 600:
    c1_pos[0] = -100
  else:
    c1_pos[0] += 10
  #car2
  if c2_pos[0] < -200:
    c2_pos[0] = 600
  else:
    c1_pos[0] -= 10
"""I have no idea why the first 2 cars don't move, I've looked through the code and have no idea what the issue might be"""
  #car3
  if c3_pos[0] > 600:
    c3_pos[0] = -100
  else:
    c3_pos[0] += 10
  #car4
  if c4_pos[0] < -100:
    c4_pos[0] = 600
  else:
    c4_pos[0] -= 10
  """update our game state"""
    
  #update bounds
  if cur_pos[0] < 20: #x direction bounds
    cur_pos[0] = 20
  if cur_pos[0] > width - 20:
    cur_pos[0] = width - 20
  if cur_pos[1] < 20: #y direction bounds
    cur_pos[1] = 20
  if cur_pos[1] > height - 20:
    cur_pos[1] = height - 20
  
  """ draw to our screen """
  # clear screen
  screen.fill("white")

  # Beginning & End Grass zones
  pygame.draw.rect(screen, "green", pygame.Rect((0, 0), (600, 40)))
  pygame.draw.rect(screen, "green", pygame.Rect((0, 360), (600, 40)))
  #Road
  pygame.draw.rect(screen, "grey", pygame.Rect((0, 40), (600, 320)))
  #Middle Grass Zone & Road Lines
  pygame.draw.rect(screen, "green", pygame.Rect((0, 180), (600, 40)))
  pygame.draw.rect(screen, "yellow", pygame.Rect((0, 100), (600, 20)))
  pygame.draw.rect(screen, "yellow", pygame.Rect((0, 280), (600, 20)))
  

  #cars
  pygame.draw.rect(screen, "black", pygame.Rect((c1_pos[0],c1_pos[1]), (100, 50)))
  pygame.draw.rect(screen, "purple", pygame.Rect((c2_pos[0],c2_pos[1]), (200, 50)))
  pygame.draw.rect(screen, "red", pygame.Rect((c3_pos[0],c3_pos[1]), (100, 50)))
  pygame.draw.rect(screen, "blue", pygame.Rect((c4_pos[0],c4_pos[1]), (100, 50)))

  #frog
  pygame.draw.circle(screen, "#0ba300", (cur_pos[0],cur_pos[1]), 20)
  
  # update screen
  pygame.display.flip()
  # fps
  dt = clock.tick(speed) / 1000
# quit pygame
pygame.quit()
