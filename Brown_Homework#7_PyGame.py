"""
Jaden Brown
3/12/25
Assignment #9
Description: Adding win/lose conditions, adding collision with cars, adding win/lose screens, adding functions
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
c1_pos = [-100,45] #black car
c2_pos = [600,125] #purple car
c3_pos = [-100,225] #red car
c4_pos = [600,305] #blue car

#score
score = 0

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
    c1_pos[0] += 15
  #car2
  if c2_pos[0] < -100:
    c2_pos[0] = 600
  else:
    c2_pos[0] -= 15
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

  #Win Condition
  if cur_pos[1] < 40:
    print("You Win!")
    running = False
  #Lose Condition
    #Car collision with frog
  if cur_pos[0] > c1_pos[0] and cur_pos[0] < c1_pos[0] + 100 and cur_pos[1] > c1_pos[1] - 10 and cur_pos[1] < c1_pos[1] + 60:
    print("YOU LOSE")
    running = False
  if cur_pos[0] > c2_pos[0] and cur_pos[0] < c2_pos[0] + 100 and cur_pos[1] > c2_pos[1] - 10 and cur_pos[1] < c2_pos[1] + 60:
    print("YOU LOSE")
    running = False
  if cur_pos[0] > c3_pos[0] and cur_pos[0] < c3_pos[0] + 100 and cur_pos[1] > c3_pos[1] - 10 and cur_pos[1] < c3_pos[1] + 60:
    print("YOU LOSE")
    running = False
  if cur_pos[0] > c4_pos[0] and cur_pos[0] < c4_pos[0] + 100 and cur_pos[1] > c4_pos[1] - 10 and cur_pos[1] < c4_pos[1] + 60:
    print("YOU LOSE")
    running = False
  
  #Score
  if cur_pos[1] < 40 and score < 1:
    score += 1
  if cur_pos[1] < 80 and score < 1:
    score += 1
  if cur_pos[1] < 120 and score < 1:
    score += 1
  if cur_pos[1] < 160 and score < 1:
    score += 1
  if cur_pos[1] < 200 and score < 1:
    score += 1
  if cur_pos[1] < 240 and score < 1:
    score += 1
  if cur_pos[1] < 280 and score < 1:
    score += 1
  if cur_pos[1] < 320 and score < 1:
    score += 1
  if cur_pos[1] < 360 and score < 1:
    score += 1
  if cur_pos[1] < 400 and score < 1:
    score += 1
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
  for body in c1_pos:
    pygame.draw.rect(screen, "black", pygame.Rect((c1_pos[0],c1_pos[1]), (100, 50)),body)
  for body in c2_pos:
    pygame.draw.rect(screen, "purple", pygame.Rect((c2_pos[0],c2_pos[1]), (100, 50)),body)
  for body in c3_pos:
    pygame.draw.rect(screen, "red", pygame.Rect((c3_pos[0],c3_pos[1]), (100, 50)),body)
  for body in c4_pos:
    pygame.draw.rect(screen, "blue", pygame.Rect((c4_pos[0],c4_pos[1]), (100, 50)),body)

  #frog
  for body in cur_pos:
    pygame.draw.circle(screen, "#0ba300", cur_pos, 20, body)
  
  # update screen
  pygame.display.flip()
  # fps
  dt = clock.tick(speed) / 1000
# quit pygame
pygame.quit()
