import pygame

# Initialize pygame (starts all pygame modules)
pygame.init()

# -------------------------------
# Screen setup
# -------------------------------
WIDTH, HEIGHT = 600, 400   # Width and height of the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the window
pygame.display.set_caption("Simple Circle Movement")  # Window title

# -------------------------------
# Define colors using RGB format
# -------------------------------
BLACK = (0, 0, 0)          # Background color
YELLOW = (255, 220, 0)     # Circle color

# -------------------------------
# Circle initial position
# -------------------------------
x = WIDTH // 2   # Start at horizontal center of screen
y = HEIGHT // 2  # Start at vertical center of screen

radius = 20          # Size of Circle (circle radius)


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
    
    # Handle events (like closing window)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   # Stop the loop if window is closed
    
    # Detect which keys are pressed
    keys = pygame.key.get_pressed()
    
    # Move Circle using arrow keys    
    if keys[pygame.K_UP]:
        y -= 5   # Move UP: decrease y-position by 5 pixels

    if keys[pygame.K_DOWN]:
        y += 5   # Move DOWN: increase y-position by 5 pixels

    if keys[pygame.K_LEFT]:
        x -= 5   # Move LEFT: decrease x-position by 5 pixels

    if keys[pygame.K_RIGHT]:
        x += 5   # Move RIGHT: increase x-position by 5 pixels

    # ---------------------------
    # Keep Circle inside the screen
    # ---------------------------
    if x < radius:
        x = radius   # Prevent moving beyond left boundary

    if x > WIDTH - radius:
        x = WIDTH - radius   # Prevent moving beyond right boundary

    if y < radius:
        y = radius   # Prevent moving beyond top boundary

    if y > HEIGHT - radius:
        y = HEIGHT - radius   # Prevent moving beyond bottom boundary

    # ---------------------------
    # Drawing section
    # ---------------------------
    screen.fill(BLACK)   # Clear the screen with black color

    # Draw Circle as a yellow circle at (x, y)
    pygame.draw.circle(screen, YELLOW, (x, y), radius)

    pygame.display.flip()   # Update the screen to show changes

# -------------------------------
# Quit pygame when loop ends
# -------------------------------
pygame.quit()