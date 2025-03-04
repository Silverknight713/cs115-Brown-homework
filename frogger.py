import pygame
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
"""game loop"""
running = True
while running:
  """Handle events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  """update our game state"""
  """ draw to our screen """
  # clear screen
  screen.fill("white")

  # Grass zones
  pygame.draw.rect(screen, "green", pygame.Rect((0, 0), (600, 50)))
  pygame.draw.rect(screen, "green", pygame.Rect((0, 350), (600, 50)))
  #Road
  pygame.draw.rect(screen, "grey", pygame.Rect((0, 50), (600, 300)))
  pygame.draw.rect(screen, "yellow", pygame.Rect((0, 190), (600, 20)))

  #cars
  pygame.draw.rect(screen, "black", pygame.Rect((0, 65), (100, 50)),10)
  pygame.draw.rect(screen, "purple", pygame.Rect((0, 125), (200, 50)),10)
  pygame.draw.rect(screen, "red", pygame.Rect((0, 225), (100, 50)),10)
  pygame.draw.rect(screen, "blue", pygame.Rect((0, 285), (100, 50)),10)

  #frog
  pygame.draw.circle(screen, "#0ba300", (300,375), 25)
  
  # update screen
  pygame.display.flip()
  # fps
  dt = clock.tick(speed) / 1000
# quit pygame
pygame.quit()
