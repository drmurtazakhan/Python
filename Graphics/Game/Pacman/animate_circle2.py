import pygame

pygame.init()

# Window
width, height = 900, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Circle Animation")

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Circle
radius = 30
x, y = 0, 0

# --- compute exact movement ---
steps = 300   # total frames to reach destination
dx = (width - radius) / steps
dy = (height - radius) / steps

clock = pygame.time.Clock()

running = True
for i in range(steps):   # run exactly 'steps' frames
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not running:
        break

    screen.fill(WHITE)

    pygame.draw.circle(screen, BLUE, (int(x), int(y)), radius)

    x += dx
    y += dy

    pygame.display.flip()
    clock.tick(60)

# Final exact position (guaranteed bottom-right)
screen.fill(WHITE)
pygame.draw.circle(screen, BLUE, (width - radius, height - radius), radius)
pygame.display.flip()

# wait until close
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()