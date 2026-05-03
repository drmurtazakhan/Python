import pygame

pygame.init()

# Window (slightly increased size)
width, height = 900, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Circle Animation")

# Colors (changed)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Circle properties
radius = 30
x, y = 0, 0   # start at top-left

# Different increments
dx = 3   # x increment
dy = 2   # y increment

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw circle
    pygame.draw.circle(screen, BLUE, (x, y), radius)

    # Move circle
    x += dx
    y += dy

    pygame.display.flip()

    clock.tick(60)

pygame.quit()