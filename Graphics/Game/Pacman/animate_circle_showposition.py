import pygame

pygame.init()

# Window (slightly increased size)
width, height = 900, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Circle Animation")

# Colors (changed)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)   # added for text

# Circle properties
radius = 70
x, y = 0, 0   # start at top-left

# Different increments
dx = 3   # x increment
dy = 2   # y increment

# -------------------------------
# Font setup (ADDED)
# -------------------------------
font_sm = pygame.font.SysFont("Arial", 28)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw circle
    pygame.draw.circle(screen, BLUE, (x, y), radius)

    # -------------------------------
    # Display x and y (ADDED)
    # -------------------------------
    text = f"x = {x}, y = {y}"
    text_surface = font_sm.render(text, True, BLACK)
    screen.blit(text_surface, (20, 20))

    # Move circle
    x += dx
    y += dy

    pygame.display.flip()

    clock.tick(60)

pygame.quit()