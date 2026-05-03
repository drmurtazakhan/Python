# =============================================================================
# SDEV140 - Module 8 Programming Assignment
# Pac-Man Style Arcade Game
# Built with Python and Pygame
#
# HOW I MADE IT MY OWN:
#   1. Larger, more complex maze (20 rows x 22 cols vs the original 10x20)
#   2. Added a lives system (3 lives before game over)
#   3. Added power pellets - eating one lets Pac-Man eat ghosts temporarily
#   4. Ghosts turn blue and slow down during power pellet mode
#   5. Added a proper Game Over / You Win / Restart screen
#   6. Added a score bonus when eating a ghost while powered-up
#   7. Color-coded multiple ghosts (red, pink, orange, cyan)
# =============================================================================

import pygame   # The game library — handles graphics, sound, and input
import random   # Used to make ghost movement unpredictable


# -----------------------------------------------------------------------------
# STEP 1: Initialize Pygame and set up constants
# -----------------------------------------------------------------------------
pygame.init()

# --- Window & Grid constants -------------------------------------------------
GRID_SIZE   = 30          # Each cell in the maze is 30x30 pixels
COLS        = 22          # Number of columns in our maze
ROWS        = 20          # Number of rows in our maze
WIDTH       = COLS * GRID_SIZE   # Window width in pixels
HEIGHT      = ROWS * GRID_SIZE   # Window height in pixels

# --- Color constants (R, G, B) -----------------------------------------------
BLACK       = (0,   0,   0)
WHITE       = (255, 255, 255)
YELLOW      = (255, 220, 0)
BLUE        = (30,  80,  255)
DARK_BLUE   = (0,   0,   160)
RED         = (220, 30,  30)
PINK        = (255, 150, 200)
ORANGE      = (255, 165, 0)
CYAN        = (0,   220, 220)
GHOST_BLUE  = (50,  50,  200)   # Color ghosts turn when Pac-Man is powered up
PELLET_CLR  = (200, 200, 200)   # Normal pellet color (small dot)
POWER_CLR   = (255, 100, 0)     # Power pellet color (big dot)

# --- Game timing constants ---------------------------------------------------
FPS             = 10    # Frames per second (controls overall game speed)
GHOST_MOVE_RATE = 2     # Ghosts move every N frames (lower = faster)
POWER_DURATION  = 50    # Number of frames power pellet mode lasts

# --- Maze grid codes ---------------------------------------------------------
# Each cell in the MAZE list is one of these values:
WALL   = 1   # Blue wall block
EMPTY  = 0   # Open path (no pellet)
PELLET = 2   # Normal small pellet (+10 points)
POWER  = 5   # Power pellet — temporarily lets Pac-Man eat ghosts (+50 pts)


# -----------------------------------------------------------------------------
# STEP 2: Design the maze
# Each row is a list of numbers. 1=wall, 0=open, 2=pellet, 5=power pellet.
# Pac-Man and ghosts start on EMPTY (0) cells defined in START positions below.
# -----------------------------------------------------------------------------
MAZE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,5,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,5,1],
    [1,2,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,2,1],
    [1,2,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,2,1,2,1,1,1,1,1,1,1,1,2,1,2,1,1,2,1],
    [1,2,2,2,2,1,2,2,2,2,1,1,2,2,2,2,1,2,2,2,2,1],
    [1,1,1,1,2,1,1,1,0,1,1,1,1,1,0,1,1,1,2,1,1,1],
    [1,1,1,1,2,1,1,1,0,1,0,0,0,1,0,1,1,1,2,1,1,1],
    [1,1,1,1,2,1,0,0,0,0,0,0,0,0,0,0,0,1,2,1,1,1],
    [1,1,1,1,2,1,0,1,1,0,0,0,0,1,1,0,1,1,2,1,1,1],
    [1,1,1,1,2,1,0,1,1,0,0,0,0,1,1,0,1,1,2,1,1,1],
    [1,1,1,1,2,1,0,0,0,0,0,0,0,0,0,0,0,1,2,1,1,1],
    [1,1,1,1,2,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,2,1],
    [1,5,2,1,2,2,2,2,0,2,2,2,2,0,2,2,2,2,1,2,5,1],
    [1,1,2,1,2,1,2,1,1,1,1,1,1,1,1,2,1,2,1,2,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# --- Starting positions (row, col) -------------------------------------------
PACMAN_START  = (16, 8)          # Pac-Man starts near the bottom-center
GHOST_STARTS  = [
    (9,  10),   # Ghost 1 — red
    (10, 10),   # Ghost 2 — pink
    (11, 10),   # Ghost 3 — orange
    (11, 11),   # Ghost 4 — cyan
]
GHOST_COLORS  = [RED, PINK, ORANGE, CYAN]


# -----------------------------------------------------------------------------
# STEP 3: Set up the Pygame window and clock
# -----------------------------------------------------------------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man — SDEV140 Edition")

clock  = pygame.time.Clock()
font_sm = pygame.font.SysFont("Arial", 20, bold=True)
font_lg = pygame.font.SysFont("Arial", 40, bold=True)


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def build_fresh_maze():
    """Return a deep copy of the original maze so we can reset cleanly."""
    return [row[:] for row in MAZE]


def collect_pellets(maze):
    """
    Scan the maze and return a set of (row, col) for every pellet cell.
    We track pellets separately so ghosts don't erase them when they walk over.
    """
    positions = set()
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == PELLET or cell == POWER:
                positions.add((r, c))
    return positions


def draw_maze(maze, pellets):
    """
    Draw the entire maze grid to the screen.
    Called every frame from the main game loop.
    """
    for r in range(ROWS):
        for c in range(COLS):
            x = c * GRID_SIZE   # pixel x position of this cell
            y = r * GRID_SIZE   # pixel y position of this cell
            cell = maze[r][c]

            if cell == WALL:
                # Draw a wall block with a slightly lighter border for a 3D look
                pygame.draw.rect(screen, BLUE, (x, y, GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, DARK_BLUE, (x, y, GRID_SIZE, GRID_SIZE), 2)

            elif (r, c) in pellets:
                # Normal pellet — small grey dot
                cx = x + GRID_SIZE // 2
                cy = y + GRID_SIZE // 2
                if maze[r][c] == POWER:
                    # Power pellet — larger orange dot
                    pygame.draw.circle(screen, POWER_CLR, (cx, cy), 8)
                else:
                    pygame.draw.circle(screen, PELLET_CLR, (cx, cy), 4)


def draw_pacman(row, col):
    """Draw Pac-Man as a yellow circle."""
    cx = col * GRID_SIZE + GRID_SIZE // 2
    cy = row * GRID_SIZE + GRID_SIZE // 2
    pygame.draw.circle(screen, YELLOW, (cx, cy), GRID_SIZE // 2 - 2)


def draw_ghosts(ghosts, powered_up):
    """
    Draw each ghost. If Pac-Man is powered up, ghosts turn blue (scared).
    ghosts — list of [row, col] positions
    powered_up — bool, True when Pac-Man ate a power pellet
    """
    for i, (gr, gc) in enumerate(ghosts):
        cx = gc * GRID_SIZE + GRID_SIZE // 2
        cy = gr * GRID_SIZE + GRID_SIZE // 2
        color = GHOST_BLUE if powered_up else GHOST_COLORS[i]
        pygame.draw.circle(screen, color, (cx, cy), GRID_SIZE // 2 - 2)
        # Draw two small "eyes"
        eye_color = WHITE if powered_up else WHITE
        pygame.draw.circle(screen, eye_color, (cx - 5, cy - 4), 4)
        pygame.draw.circle(screen, eye_color, (cx + 5, cy - 4), 4)
        pygame.draw.circle(screen, BLACK, (cx - 5, cy - 4), 2)
        pygame.draw.circle(screen, BLACK, (cx + 5, cy - 4), 2)


def draw_hud(score, lives):
    """Draw the score and lives at the top-left and top-right of the screen."""
    score_text = font_sm.render(f"Score: {score}", True, WHITE)
    lives_text = font_sm.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 5))
    screen.blit(lives_text, (WIDTH - 110, 5))


def draw_message(line1, line2=""):
    """Draw a centered message overlay — used for Game Over / Win screens."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))          # Semi-transparent dark background
    screen.blit(overlay, (0, 0))

    t1 = font_lg.render(line1, True, YELLOW)
    t2 = font_sm.render(line2, True, WHITE)
    screen.blit(t1, t1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
    screen.blit(t2, t2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))


def find_positions(maze):
    """
    Scan the maze and return:
      pac_pos — (row, col) of Pac-Man (cell value 4)
    We store ghost/pacman positions separately, not in the maze grid,
    so this is mainly used to verify starting positions are valid.
    """
    for r in range(ROWS):
        for c in range(COLS):
            if maze[r][c] == 4:
                return (r, c)
    return None


def can_move(maze, row, col):
    """
    Return True if the cell at (row, col) is a valid position to move into.
    A cell is valid if it's inside the grid AND not a wall.
    """
    if 0 <= row < ROWS and 0 <= col < COLS:
        return maze[row][col] != WALL
    return False


def move_ghosts(maze, ghosts, powered_up, frame_count):
    """
    Move each ghost one step in a random valid direction.
    When powered_up is True, ghosts move less frequently (they're scared).
    frame_count — used to skip movement frames when appropriate.
    """
    # Scared ghosts move every 4 frames instead of every 2
    move_interval = GHOST_MOVE_RATE * 2 if powered_up else GHOST_MOVE_RATE
    if frame_count % move_interval != 0:
        return

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # up, down, left, right

    for ghost in ghosts:
        gr, gc = ghost
        random.shuffle(directions)          # Try directions in random order
        for dr, dc in directions:
            nr, nc = gr + dr, gc + dc
            if can_move(maze, nr, nc):
                ghost[0] = nr
                ghost[1] = nc
                break                       # Move to the first valid direction


# =============================================================================
# GAME RESET FUNCTION
# Reset all game state — called at start and after losing a life (or all lives)
# =============================================================================

def reset_game():
    """Return a fresh game state dictionary."""
    maze   = build_fresh_maze()
    pellets = collect_pellets(maze)
    ghosts = [list(pos) for pos in GHOST_STARTS]
    return {
        "maze":       maze,
        "pellets":    pellets,
        "pac":        list(PACMAN_START),
        "ghosts":     ghosts,
        "score":      0,
        "lives":      3,
        "powered_up": False,
        "power_timer": 0,
        "frame":      0,
        "state":      "playing",   # "playing", "dead", "gameover", "win"
    }


# =============================================================================
# MAIN GAME LOOP
# =============================================================================

def main():
    g = reset_game()           # g is the game state dictionary
    running = True

    while running:
        clock.tick(FPS)        # Cap the loop at FPS frames per second
        g["frame"] += 1

        # -----------------------------------------------------------------
        # EVENT HANDLING — keyboard and window close
        # -----------------------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                # Allow restart from any non-playing screen
                if g["state"] in ("gameover", "win"):
                    if event.key == pygame.K_r:
                        g = reset_game()
                    continue

                # Pac-Man movement — arrow keys
                pr, pc = g["pac"]
                move = None
                if   event.key == pygame.K_UP:    move = (-1, 0)
                elif event.key == pygame.K_DOWN:  move = (1, 0)
                elif event.key == pygame.K_LEFT:  move = (0, -1)
                elif event.key == pygame.K_RIGHT: move = (0, 1)

                if move:
                    dr, dc = move
                    nr, nc = pr + dr, pc + dc
                    if can_move(g["maze"], nr, nc):
                        g["pac"] = [nr, nc]

        # -----------------------------------------------------------------
        # GAME LOGIC (only when playing)
        # -----------------------------------------------------------------
        if g["state"] == "playing":

            pr, pc = g["pac"]

            # --- Check if Pac-Man eats a pellet --------------------------
            if (pr, pc) in g["pellets"]:
                cell = g["maze"][pr][pc]
                g["pellets"].discard((pr, pc))

                if cell == POWER:
                    # Power pellet: ghosts become scared
                    g["score"]      += 50
                    g["powered_up"]  = True
                    g["power_timer"] = POWER_DURATION
                else:
                    # Normal pellet
                    g["score"] += 10

            # --- Count down power pellet timer ---------------------------
            if g["powered_up"]:
                g["power_timer"] -= 1
                if g["power_timer"] <= 0:
                    g["powered_up"] = False

            # --- Move ghosts every GHOST_MOVE_RATE frames ----------------
            move_ghosts(g["maze"], g["ghosts"], g["powered_up"], g["frame"])

            # --- Collision: Pac-Man meets a ghost ------------------------
            for i, ghost in enumerate(g["ghosts"]):
                if ghost[0] == pr and ghost[1] == pc:
                    if g["powered_up"]:
                        # Pac-Man eats the ghost — send it back to start
                        g["score"] += 200
                        g["ghosts"][i] = list(GHOST_STARTS[i])
                    else:
                        # Ghost catches Pac-Man — lose a life
                        g["lives"] -= 1
                        if g["lives"] <= 0:
                            g["state"] = "gameover"
                        else:
                            # Reset positions but keep score and remaining maze
                            g["pac"]        = list(PACMAN_START)
                            g["ghosts"]     = [list(p) for p in GHOST_STARTS]
                            g["powered_up"] = False
                            g["power_timer"] = 0
                        break

            # --- Check win condition: all pellets eaten -------------------
            if len(g["pellets"]) == 0:
                g["state"] = "win"

        # -----------------------------------------------------------------
        # DRAWING — runs every frame regardless of game state
        # -----------------------------------------------------------------
        screen.fill(BLACK)                               # Clear screen
        draw_maze(g["maze"], g["pellets"])               # Draw walls & pellets
        draw_ghosts(g["ghosts"], g["powered_up"])        # Draw ghosts
        draw_pacman(g["pac"][0], g["pac"][1])            # Draw Pac-Man
        draw_hud(g["score"], g["lives"])                 # Draw score & lives

        # Overlay messages for non-playing states
        if g["state"] == "gameover":
            draw_message("GAME OVER", f"Score: {g['score']}  |  Press R to restart")
        elif g["state"] == "win":
            draw_message("YOU WIN!", f"Score: {g['score']}  |  Press R to restart")
        elif g["powered_up"]:
            # Small reminder when powered up
            msg = font_sm.render("POWERED UP!", True, ORANGE)
            screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, 5))

        pygame.display.flip()   # Push everything we drew to the screen

    pygame.quit()


# Standard Python entry point — only run main() when this file is executed directly
if __name__ == "__main__":
    main()
