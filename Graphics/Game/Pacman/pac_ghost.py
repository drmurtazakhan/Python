import pygame
import random   # Used to generate random movement for ghost

# Initialize pygame
pygame.init()

# -------------------------------
# Screen setup
# -------------------------------
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man with Simple Ghost")

# -------------------------------
# Colors
# -------------------------------
BLACK = (0, 0, 0)
YELLOW = (255, 220, 0)
RED = (255, 0, 0)

# -------------------------------
# Pac-Man properties
# -------------------------------
pac_x = WIDTH // 2
pac_y = HEIGHT // 2
radius = 20
speed = 5   # Pac-Man speed (5 pixels per key press)

# -------------------------------
# Ghost properties
# -------------------------------
ghost_x = 100
ghost_y = 100
ghost_speed = 15  # Ghost speed (pixels in a direction)

# Used to control how often ghost moves
ghost_move_delay = 0

# -------------------------------
# Game loop control
# -------------------------------
running = True
clock = pygame.time.Clock()

# ===============================
# MAIN LOOP
# ===============================
while running:
    clock.tick(60)   # Run at 60 frames per second

    # ---------------------------
    # Handle window events
    # ---------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------------------
    # Keyboard input for Pac-Man
    # ---------------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        pac_y -= speed   # Move UP: decrease y by 5 pixels

    if keys[pygame.K_DOWN]:
        pac_y += speed   # Move DOWN: increase y by 5 pixels

    if keys[pygame.K_LEFT]:
        pac_x -= speed   # Move LEFT: decrease x by 5 pixels

    if keys[pygame.K_RIGHT]:
        pac_x += speed   # Move RIGHT: increase x by 5 pixels

    # ---------------------------
    # Keep Pac-Man inside screen
    # ---------------------------
    if pac_x < radius:
        pac_x = radius
    if pac_x > WIDTH - radius:
        pac_x = WIDTH - radius
    if pac_y < radius:
        pac_y = radius
    if pac_y > HEIGHT - radius:
        pac_y = HEIGHT - radius

    # ---------------------------
    # Ghost random movement
    # ---------------------------
    ghost_move_delay += 1   # Increase counter every frame

    if ghost_move_delay % 15 == 0:
        # Move ghost only every 15 frames 

        direction = random.choice([
            (-1, 0),   # up
            (1, 0),    # down
            (0, -1),   # left
            (0, 1)     # right
        ])

        dx, dy = direction

        # Update ghost position
        ghost_x += dx * ghost_speed   # Move in x direction
        ghost_y += dy * ghost_speed   # Move in y direction

    # ---------------------------
    # Keep Ghost inside screen
    # ---------------------------
    if ghost_x < radius:
        ghost_x = radius
    if ghost_x > WIDTH - radius:
        ghost_x = WIDTH - radius
    if ghost_y < radius:
        ghost_y = radius
    if ghost_y > HEIGHT - radius:
        ghost_y = HEIGHT - radius

    # ---------------------------
    # Collision detection
    # ---------------------------
    distance = ((pac_x - ghost_x)**2 + (pac_y - ghost_y)**2) ** 0.5

    if distance < radius * 2:
        # If distance between centers is less than sum of radii,
        # Pac-Man and ghost have collided
        print("Game Over: Pac-Man caught!")
        running = False   # End the game

    # ---------------------------
    # Drawing
    # ---------------------------
    screen.fill(BLACK)

    # Draw Pac-Man (yellow circle)
    pygame.draw.circle(screen, YELLOW, (pac_x, pac_y), radius)

    # Draw Ghost (red circle)
    pygame.draw.circle(screen, RED, (ghost_x, ghost_y), radius)

    pygame.display.flip()   # Update screen

# Quit pygame
pygame.quit()