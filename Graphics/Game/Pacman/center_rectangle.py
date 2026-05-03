import pygame

pygame.init()

# Window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Center Rectangle")

# Colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Rectangle size
rect_width = 200
rect_height = 100

# Center position
rect_x = (width - rect_width) // 2
rect_y = (height - rect_height) // 2

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.draw.rect(screen, YELLOW, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()   # IMPORTANT

    clock.tick(60)

pygame.quit()