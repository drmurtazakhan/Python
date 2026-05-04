import pygame

# Initialize pygame
pygame.init()

# -------------------------------
# Screen setup
# -------------------------------
WIDTH, HEIGHT = 600, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Maze (Modular)")

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
WALL   = 1
EMPTY  = 0
PELLET = 2

# -------------------------------
# Maze layout
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
# Pac-Man properties
# -------------------------------
pac_x = GRID_SIZE * 9 + GRID_SIZE // 2
pac_y = GRID_SIZE * 7 + GRID_SIZE // 2
radius = GRID_SIZE // 2 - 2
speed = 3

# -------------------------------
# FUNCTION: Handle movement input
# -------------------------------
def move_pacman(pac_x, pac_y):
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

    return new_x, new_y

# -------------------------------
# FUNCTION: Check wall collision
# -------------------------------
def can_move(new_x, new_y):
    row = new_y // GRID_SIZE
    col = new_x // GRID_SIZE

    if 0 <= row < ROWS and 0 <= col < COLS:
        return MAZE[row][col] != WALL
    return False

# -------------------------------
# FUNCTION: Eat pellet
# -------------------------------
def eat_pellet(pac_x, pac_y):
    row = pac_y // GRID_SIZE
    col = pac_x // GRID_SIZE

    if MAZE[row][col] == PELLET:
        MAZE[row][col] = EMPTY

# -------------------------------
# FUNCTION: Draw maze
# -------------------------------
def draw_maze():
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

# -------------------------------
# FUNCTION: Draw Pac-Man
# -------------------------------
def draw_pacman(pac_x, pac_y):
    pygame.draw.circle(screen, YELLOW, (pac_x, pac_y), radius)

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
    # Handle events
    # ---------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------------------
    # Movement
    # ---------------------------
    new_x, new_y = move_pacman(pac_x, pac_y)

    if can_move(new_x, new_y):
        pac_x, pac_y = new_x, new_y
        eat_pellet(pac_x, pac_y)

    # ---------------------------
    # Drawing
    # ---------------------------
    screen.fill(BLACK)
    draw_maze()
    draw_pacman(pac_x, pac_y)

    pygame.display.flip()

pygame.quit()