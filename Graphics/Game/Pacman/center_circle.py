import pygame

pygame.init()

# Window setup
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Center Circle")

# Colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

radius = 50 # Circle radius

# Center position
center_x = width // 2
center_y = height // 2

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill(BLACK)

    # Draw circle (centered)
    pygame.draw.circle(screen, GREEN, (center_x, center_y), radius)
    #pygame.draw.circle(screen, GREEN, (0, 0), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()