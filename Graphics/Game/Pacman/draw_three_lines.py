import pygame

pygame.init()

# Window setup
width, height = 800, 600
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
    pygame.draw.line(screen, RED,   (100, 100), (700, 100), 5)  # Top line
    pygame.draw.line(screen, GREEN, (100, 250), (700, 250), 5)  # Middle line
    pygame.draw.line(screen, BLUE,  (100, 400), (700, 400), 5)  # Bottom line

    pygame.display.flip()
    clock.tick(60)

pygame.quit()