import pygame

pygame.init()

# Window setup
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Three Lines")

# Colors
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill(BLACK)

    # Draw three lines
    pygame.draw.line(screen, RED,   (100, 50), (300, 50), 5)    # Top line
    pygame.draw.line(screen, GREEN, (100, 150), (300, 150), 5)  # Middle line
    pygame.draw.line(screen, BLUE,  (100, 250), (300, 250), 5)  # Bottom line

    pygame.display.flip()
    clock.tick(60)

pygame.quit()