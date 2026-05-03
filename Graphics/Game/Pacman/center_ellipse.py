import pygame

pygame.init()

# Window setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Ellipse")

# Colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Ellipse size
ellipse_width = 200
ellipse_height = 100

# Center position (like rectangle logic)
ellipse_x = (width - ellipse_width) // 2
ellipse_y = (height - ellipse_height) // 2

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill(BLACK)

    # Draw ellipse (inside a rectangle area)
    pygame.draw.ellipse(screen, YELLOW, (ellipse_x, ellipse_y, ellipse_width, ellipse_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()