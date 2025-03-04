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
  # update screen
  pygame.display.flip()
  # fps
  dt = clock.tick(speed) / 1000
# quit pygame
pygame.quit()
