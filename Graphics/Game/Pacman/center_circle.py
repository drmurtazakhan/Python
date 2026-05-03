import pygame

pygame.init()

# Window setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Center Circle")

# Colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Circle radius
radius = 50

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
    pygame.draw.circle(screen, YELLOW, (center_x, center_y), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()