import pygame

# Initialize pygame
pygame.init()

# -------------------------------
# Screen setup
# -------------------------------
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Display Text Example")

# -------------------------------
# Colors
# -------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# -------------------------------
# Font setup
# -------------------------------
font_sm = pygame.font.SysFont("Arial", 30)

# Create text surface
text_surface = font_sm.render("Hello, Pygame!", True, WHITE)

# -------------------------------
# Game loop
# -------------------------------
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(BLACK)

    # Draw text
    screen.blit(text_surface, (300, 200))

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()