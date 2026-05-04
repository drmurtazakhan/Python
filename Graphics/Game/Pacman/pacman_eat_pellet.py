import pygame

pygame.init()

# ------------------------------------------------------------
# Window & Grid constants 
# ------------------------------------------------------------
GRID_SIZE = 30 # Each cell in the maze is 30x30 pixels
ROWS = 15      # Number of rows in our maze  
COLS = 20      # Number of columns in our maze

WIDTH = COLS * GRID_SIZE    # Window width in pixels
HEIGHT = ROWS * GRID_SIZE   # Window height in pixels 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Basic + Maze")

clock = pygame.time.Clock()

# ------------------------------------------------------------
# COLORS
# ------------------------------------------------------------
BLACK  = (0, 0, 0)
BLUE   = (0, 0, 255)
YELLOW = (255, 220, 0)
WHITE  = (200, 200, 200)

# ------------------------------------------------------------
# MAZE CELL TYPES
# ------------------------------------------------------------
WALL   = 1   # Blue wall block
EMPTY  = 0   # Open path (no pellet)
PELLET = 2   # Normal small pellet

# ------------------------------------------------------------
# SIMPLE MAZE 
# 1 = wall, 2 = pellet, 0 = empty
# ------------------------------------------------------------
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

# ------------------------------------------------------------
# PACMAN START POSITION (row, col)
# ------------------------------------------------------------
pac_row = 7
pac_col = 9

# ------------------------------------------------------------
# FUNCTION: Check if Pacman can move into a cell
# ------------------------------------------------------------
def can_move(row, col):
    # Stay inside grid AND not hit a wall
    if 0 <= row < ROWS and 0 <= col < COLS:
        return MAZE[row][col] != WALL
    return False

# ------------------------------------------------------------
# FUNCTION: Draw maze (walls + pellets)
# ------------------------------------------------------------
def draw_maze():
    for r in range(ROWS):
        for c in range(COLS):
            x = c * GRID_SIZE
            y = r * GRID_SIZE

            if MAZE[r][c] == WALL:
                # Draw wall
                pygame.draw.rect(screen, BLUE, (x, y, GRID_SIZE, GRID_SIZE))

            elif MAZE[r][c] == PELLET:
                # Draw pellet (small dot)
                cx = x + GRID_SIZE // 2
                cy = y + GRID_SIZE // 2
                pygame.draw.circle(screen, WHITE, (cx, cy), 4)

# ------------------------------------------------------------
# FUNCTION: Draw Pacman
# ------------------------------------------------------------
def draw_pacman(row, col):
    cx = col * GRID_SIZE + GRID_SIZE // 2
    cy = row * GRID_SIZE + GRID_SIZE // 2
    pygame.draw.circle(screen, YELLOW, (cx, cy), GRID_SIZE // 2 - 2)

# ------------------------------------------------------------
# MAIN GAME LOOP
# ------------------------------------------------------------
running = True

while running:
    clock.tick(10)  # Control speed

    # --------------------------------------------------------
    # INPUT HANDLING (same structure as your basic version)
    # --------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            # Current position
            new_row = pac_row
            new_col = pac_col

            # Determine movement direction
            if event.key == pygame.K_UP:
                new_row -= 1
            elif event.key == pygame.K_DOWN:
                new_row += 1
            elif event.key == pygame.K_LEFT:
                new_col -= 1
            elif event.key == pygame.K_RIGHT:
                new_col += 1

            # Move only if NOT a wall
            if can_move(new_row, new_col):
                pac_row = new_row
                pac_col = new_col

                # ------------------------------------------------
                # EAT PELLET (very simple logic)
                # ------------------------------------------------
                if MAZE[pac_row][pac_col] == PELLET:
                    MAZE[pac_row][pac_col] = EMPTY  # remove pellet

    # --------------------------------------------------------
    # DRAWING
    # --------------------------------------------------------
    screen.fill(BLACK)

    draw_maze()
    draw_pacman(pac_row, pac_col)

    pygame.display.flip()

pygame.quit()