import pygame

# Initialize pygame (starts all pygame modules)
pygame.init()

# -------------------------------
# Screen setup
# -------------------------------
WIDTH, HEIGHT = 600, 400   # Width and height of the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the window
pygame.display.set_caption("Simple Pac-Man Movement")  # Window title

# -------------------------------
# Define colors using RGB format
# -------------------------------
BLACK = (0, 0, 0)          # Background color
YELLOW = (255, 220, 0)     # Pac-Man color

# -------------------------------
# Pac-Man initial position
# -------------------------------
pac_x = WIDTH // 2   # Start at horizontal center of screen
pac_y = HEIGHT // 2  # Start at vertical center of screen

radius = 20          # Size of Pac-Man (circle radius)
speed = 5            # Movement speed (5 pixels per key press)

# -------------------------------
# Game loop control
# -------------------------------
running = True       # This keeps the game running

# Clock controls how fast the game updates
clock = pygame.time.Clock()

# ===============================
# MAIN GAME LOOP
# ===============================
while running:
    clock.tick(60)   # Run the loop 60 times per second (smooth motion)

    # ---------------------------
    # Handle events (like closing window)
    # ---------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   # Stop the loop if window is closed

    # ---------------------------
    # Detect which keys are pressed
    # ---------------------------
    keys = pygame.key.get_pressed()

    # ---------------------------
    # Move Pac-Man using arrow keys
    # ---------------------------
    if keys[pygame.K_UP]:
        pac_y -= speed   # Move UP: decrease y-position by 5 pixels

    if keys[pygame.K_DOWN]:
        pac_y += speed   # Move DOWN: increase y-position by 5 pixels

    if keys[pygame.K_LEFT]:
        pac_x -= speed   # Move LEFT: decrease x-position by 5 pixels

    if keys[pygame.K_RIGHT]:
        pac_x += speed   # Move RIGHT: increase x-position by 5 pixels

    # ---------------------------
    # Keep Pac-Man inside the screen
    # ---------------------------
    if pac_x < radius:
        pac_x = radius   # Prevent moving beyond left boundary

    if pac_x > WIDTH - radius:
        pac_x = WIDTH - radius   # Prevent moving beyond right boundary

    if pac_y < radius:
        pac_y = radius   # Prevent moving beyond top boundary

    if pac_y > HEIGHT - radius:
        pac_y = HEIGHT - radius   # Prevent moving beyond bottom boundary

    # ---------------------------
    # Drawing section
    # ---------------------------
    screen.fill(BLACK)   # Clear the screen with black color

    # Draw Pac-Man as a yellow circle at (pac_x, pac_y)
    pygame.draw.circle(screen, YELLOW, (pac_x, pac_y), radius)

    pygame.display.flip()   # Update the screen to show changes

# -------------------------------
# Quit pygame when loop ends
# -------------------------------
pygame.quit()