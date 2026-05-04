import pygame

# Initialize pygame
pygame.init()

# -------------------------------
# Screen setup
# -------------------------------
WIDTH, HEIGHT = 600, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Maze (No Ghost)")

# -------------------------------
# Grid / Maze settings
# -------------------------------
GRID_SIZE = 30
ROWS = HEIGHT // GRID_SIZE
COLS = WIDTH // GRID_SIZE

# -------------------------------
# Colors
# -------------------------------
BLACK  = (0, 0, 0)
YELLOW = (255, 220, 0)
BLUE   = (0, 0, 255)
WHITE  = (200, 200, 200)

# -------------------------------
# Maze cell types
# -------------------------------
WALL   = 1   # Blue wall block
EMPTY  = 0   # Open path
PELLET = 2   # Small pellet

# -------------------------------
# Simple maze layout
# -------------------------------
MAZE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,1],
    [1,2,1,1,1,2,1,2,1,1,1,1,2,1,2,1,1,1,2,1],
    [1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,1,2,2,2,1],
    [1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,2,1],
    [1,2,2,2,2,2,1,2,2,0,0,2,2,1,2,2,2,2,2,1],
    [1,1,1,1,1,2,1,1,2,0,0,2,1,1,2,1,1,1,1,1],
    [1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,1,2,2,2,1],
    [1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1],
    [1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1],
    [1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# -------------------------------
# Pac-Man properties (pixel-based)
# -------------------------------
pac_x = GRID_SIZE * 9 + GRID_SIZE // 2
pac_y = GRID_SIZE * 7 + GRID_SIZE // 2
radius = GRID_SIZE // 2 - 2
speed = 3   # pixels per frame

# -------------------------------
# Game loop control
# -------------------------------
running = True
clock = pygame.time.Clock()

# ===============================
# MAIN LOOP
# ===============================
while running:
    clock.tick(60)

    # ---------------------------
    # Handle window events
    # ---------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------------------
    # Keyboard input (continuous)
    # ---------------------------
    keys = pygame.key.get_pressed()

    new_x = pac_x
    new_y = pac_y

    if keys[pygame.K_UP]:
        new_y -= speed

    if keys[pygame.K_DOWN]:
        new_y += speed

    if keys[pygame.K_LEFT]:
        new_x -= speed

    if keys[pygame.K_RIGHT]:
        new_x += speed

    # ----------------------------------------------------
    # Convert pixel position → grid position
    # This tells us which maze cell Pac-Man is entering
    # ----------------------------------------------------
    row = new_y // GRID_SIZE
    col = new_x // GRID_SIZE

    # ----------------------------------------------------
    # Move only if NOT a wall
    # ----------------------------------------------------
    if 0 <= row < ROWS and 0 <= col < COLS:
        if MAZE[row][col] != WALL:
            pac_x = new_x
            pac_y = new_y

            # --------------------------------------------
            # Eat pellet (remove it from maze)
            # --------------------------------------------
            if MAZE[row][col] == PELLET:
                MAZE[row][col] = EMPTY

    # ---------------------------
    # Drawing
    # ---------------------------
    screen.fill(BLACK)

    # Draw maze
    for r in range(ROWS):
        for c in range(COLS):
            x = c * GRID_SIZE
            y = r * GRID_SIZE

            if MAZE[r][c] == WALL:
                pygame.draw.rect(screen, BLUE, (x, y, GRID_SIZE, GRID_SIZE))

            elif MAZE[r][c] == PELLET:
                cx = x + GRID_SIZE // 2
                cy = y + GRID_SIZE // 2
                pygame.draw.circle(screen, WHITE, (cx, cy), 4)

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, (pac_x, pac_y), radius)

    pygame.display.flip()

# Quit pygame
pygame.quit()