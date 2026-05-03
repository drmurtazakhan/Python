# =============================================================================
# pacman_basic.py
# SDEV140 - Module 8 Programming Assignment
# Based on: https://hackr.io/blog/how-to-create-a-python-pac-man-game
# No enhancements — this is the clean base version with clear comments.
# =============================================================================

# ── Step 1: Import libraries ──────────────────────────────────────────────────
import pygame   # the game library — handles graphics, input, and window
import random   # used to make ghost movement random each frame

# ── Step 2: Initialize Pygame ─────────────────────────────────────────────────
pygame.init()   # must be called before using any pygame function

# ── Step 3: Constants ─────────────────────────────────────────────────────────
# Window size
WIDTH, HEIGHT = 600, 600   # game window is 600 x 600 pixels

# Grid size — each cell in the maze is 30 x 30 pixels
GRID_SIZE = 30

# Calculate how many rows and columns fit in the window
ROWS = HEIGHT // GRID_SIZE   # 600 // 30 = 20 rows
COLS = WIDTH  // GRID_SIZE   # 600 // 30 = 20 columns

# Colors — each is a tuple of (Red, Green, Blue) values from 0 to 255
WHITE  = (255, 255, 255)   # pellets and text
BLACK  = (  0,   0,   0)   # background
YELLOW = (255, 255,   0)   # Pac-Man
RED    = (255,   0,   0)   # ghosts
BLUE   = (  0,   0, 255)   # walls

# ── Step 4: Create the game window ───────────────────────────────────────────
screen = pygame.display.set_mode((WIDTH, HEIGHT))   # open the window
pygame.display.set_caption("Pac-Man")               # set the title bar text
clock  = pygame.time.Clock()                         # used to control FPS
font   = pygame.font.SysFont("Arial", 24)            # font for score and lives

# ── Step 5: The Maze ──────────────────────────────────────────────────────────
# The maze is a 2D list (list of lists).
# Each number represents what is in that cell:
#   1 = Wall  (blue block)
#   0 = Empty path (Pac-Man and ghosts can walk here)
#   2 = Pellet (small dot — worth 10 points)
#   3 = Ghost  (red circle)
#   4 = Pac-Man (yellow circle — starting position)

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 3, 1, 0, 1, 3, 0, 0, 0, 0, 1, 3, 1, 0, 1, 3, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# ── Step 6: Track pellet positions separately ─────────────────────────────────
# We store pellet positions in a separate list so that when a ghost walks
# over a pellet cell, the pellet is not permanently erased from the display.
# List comprehension: scans every cell and collects (row, col) for each pellet.
pellet_positions = [
    (row_idx, col_idx)
    for row_idx, row in enumerate(maze)
    for col_idx, cell in enumerate(row)
    if cell == 2
]

# ── Step 7: Find starting positions for Pac-Man and ghosts ───────────────────
def get_positions():
    """
    Scan the maze grid and return:
      pacman_pos    — [row, col] of the cell containing 4 (Pac-Man)
      ghost_positions — list of [row, col] for every cell containing 3 (ghost)
    """
    pacman_pos = None      # will hold Pac-Man's [row, col]
    ghost_positions = []   # will hold a list of ghost [row, col] pairs

    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == 4:
                pacman_pos = [row_idx, col_idx]       # found Pac-Man
            elif cell == 3:
                ghost_positions.append([row_idx, col_idx])  # found a ghost

    return pacman_pos, ghost_positions

# Get the starting positions
pacman_pos, ghost_positions = get_positions()

# Starting game values
score = 0
lives = 3

# ── Step 8: Draw the maze ─────────────────────────────────────────────────────
def draw_maze(screen):
    """
    Loop through every cell in the maze grid and draw the correct shape.
    This function is called every frame to refresh the display.
    """
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            # Calculate the top-left pixel position of this cell
            x = col_idx * GRID_SIZE
            y = row_idx * GRID_SIZE

            if cell == 1:
                # Draw a blue filled rectangle for the wall
                pygame.draw.rect(screen, BLUE, (x, y, GRID_SIZE, GRID_SIZE))

            elif cell == 2:
                # Draw a small white circle for a pellet (at the cell center)
                cx = x + GRID_SIZE // 2   # center x of the cell
                cy = y + GRID_SIZE // 2   # center y of the cell
                pygame.draw.circle(screen, WHITE, (cx, cy), 5)

            elif cell == 3:
                # Draw a red circle for a ghost
                cx = x + GRID_SIZE // 2
                cy = y + GRID_SIZE // 2
                pygame.draw.circle(screen, RED, (cx, cy), 12)

            elif cell == 4:
                # Draw a yellow circle for Pac-Man
                cx = x + GRID_SIZE // 2
                cy = y + GRID_SIZE // 2
                pygame.draw.circle(screen, YELLOW, (cx, cy), 12)

# ── Step 9: Move Pac-Man ──────────────────────────────────────────────────────
def move_pacman(direction, screen):
    """
    Move Pac-Man one cell in the given direction if the target cell is not a wall.
    direction — a string: "UP", "DOWN", "LEFT", or "RIGHT"
    Also checks if Pac-Man eats a pellet and calls collision detection.
    """
    global pacman_pos, score   # we modify these module-level variables

    row, col = pacman_pos      # current position
    new_row, new_col = row, col  # start with the same position

    # Calculate the new position based on direction
    if direction == "UP":
        new_row -= 1   # moving up decreases the row number
    elif direction == "DOWN":
        new_row += 1   # moving down increases the row number
    elif direction == "LEFT":
        new_col -= 1   # moving left decreases the column number
    elif direction == "RIGHT":
        new_col += 1   # moving right increases the column number

    # Only move if the target cell is NOT a wall (value 1)
    if maze[new_row][new_col] != 1:

        # Check if Pac-Man is moving onto a pellet
        if (new_row, new_col) in pellet_positions:
            pellet_positions.remove((new_row, new_col))  # remove eaten pellet
            score += 10                                  # add 10 points

        maze[row][col] = 0              # clear Pac-Man from old cell
        maze[new_row][new_col] = 4      # place Pac-Man in new cell
        pacman_pos = [new_row, new_col] # update the position tracker

    check_collision(screen)  # check if Pac-Man is now on the same cell as a ghost

# ── Step 10: Move Ghosts ──────────────────────────────────────────────────────
def move_ghosts(screen):
    """
    Move each ghost one cell in a random valid direction.
    Ghosts can only move onto empty cells (0) or pellet cells (2).
    If a ghost moves away from a pellet cell, the pellet is restored.
    """
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    for ghost in ghost_positions:
        row, col = ghost
        random.shuffle(directions)  # pick a random order to try directions

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            # Ghosts can only move onto empty paths (0) or pellets (2)
            if maze[new_row][new_col] in [0, 2]:

                maze[row][col] = 0   # clear ghost from old cell

                # If the ghost was standing on a pellet, restore it
                if (row, col) in pellet_positions:
                    maze[row][col] = 2

                # Place ghost in the new cell
                ghost[0], ghost[1] = new_row, new_col
                maze[new_row][new_col] = 3

                break  # stop trying directions after a successful move

    check_collision(screen)  # check if any ghost is now on Pac-Man's cell

# ── Step 11: Collision Detection ─────────────────────────────────────────────
def check_collision(screen):
    """
    Check if Pac-Man and any ghost are on the same cell.
    If yes — lose a life, reset positions, or end the game.
    """
    global lives, pacman_pos, ghost_positions

    for ghost in ghost_positions:
        if ghost[0] == pacman_pos[0] and ghost[1] == pacman_pos[1]:
            # Pac-Man and a ghost are on the same cell
            lives -= 1   # lose one life

            if lives == 0:
                # No lives left — show Game Over and stop
                draw_game_over(screen)
            else:
                # Still has lives — reset positions for another try
                reset_positions()

# ── Step 12: Reset Positions ──────────────────────────────────────────────────
def reset_positions():
    """
    Reset Pac-Man and all ghosts back to their original starting positions
    in the maze. Called after Pac-Man loses a life.
    """
    global pacman_pos, ghost_positions

    # Clear all current character positions from the maze
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell in [3, 4]:
                maze[row_idx][col_idx] = 0  # replace with empty path

    # Re-read starting positions from the original maze values
    # (We have to re-scan because we cleared them above)
    # Place Pac-Man back at row 1, col 1 (its original starting cell)
    maze[1][1] = 4
    pacman_pos = [1, 1]

    # Place ghosts back at their original positions
    ghost_starts = [[3, 3], [3, 7], [3, 13], [3, 17]]
    ghost_positions = []
    for pos in ghost_starts:
        maze[pos[0]][pos[1]] = 3
        ghost_positions.append(pos)

# ── Step 13: Display Score and Lives ─────────────────────────────────────────
def draw_hud(screen, score, lives):
    """
    Render the score and remaining lives as text on the screen.
    HUD = Heads Up Display — the information overlay shown during play.
    """
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))             # top-left corner
    screen.blit(lives_text, (WIDTH - 130, 10))    # top-right corner

# ── Step 14: Game Over Screen ─────────────────────────────────────────────────
def draw_game_over(screen):
    """
    Show a Game Over message and final score, then wait 3 seconds and quit.
    """
    screen.fill(BLACK)
    msg1 = font.render("GAME OVER", True, RED)
    msg2 = font.render(f"Final Score: {score}", True, WHITE)
    msg3 = font.render("Closing in 3 seconds...", True, WHITE)

    # Center the text on the screen
    screen.blit(msg1, (WIDTH // 2 - msg1.get_width() // 2, HEIGHT // 2 - 60))
    screen.blit(msg2, (WIDTH // 2 - msg2.get_width() // 2, HEIGHT // 2))
    screen.blit(msg3, (WIDTH // 2 - msg3.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.flip()   # push the game over screen to the display
    pygame.time.wait(3000)  # pause for 3 seconds (3000 milliseconds)
    pygame.quit()
    exit()

# ── Step 15: You Win Screen ───────────────────────────────────────────────────
def draw_you_win(screen):
    """
    Show a You Win message when all pellets have been collected.
    """
    screen.fill(BLACK)
    msg1 = font.render("YOU WIN!", True, YELLOW)
    msg2 = font.render(f"Final Score: {score}", True, WHITE)
    msg3 = font.render("Closing in 3 seconds...", True, WHITE)

    screen.blit(msg1, (WIDTH // 2 - msg1.get_width() // 2, HEIGHT // 2 - 60))
    screen.blit(msg2, (WIDTH // 2 - msg2.get_width() // 2, HEIGHT // 2))
    screen.blit(msg3, (WIDTH // 2 - msg3.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    exit()

# ── Step 16: Main Game Loop ───────────────────────────────────────────────────
def main():
    """
    The main game loop. Runs continuously until the player quits.
    Each iteration:
      1. Handles events  (keyboard input, window close)
      2. Updates game logic  (move ghosts, check win)
      3. Draws everything to the screen
    """
    direction = None   # stores the current movement direction ("UP", "DOWN", etc.)
    running = True
    frame_count = 0 

    while running:
        clock.tick(3)   # limit the game loop to 10 frames per second

        # ── Phase 1: Handle Events ────────────────────────────────────────────
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # Player clicked the X button on the window
                running = False

            elif event.type == pygame.KEYDOWN:
                # A key was pressed — update the movement direction
                if event.key == pygame.K_UP:
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT:
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"

        # ── Phase 2: Update Game Logic ────────────────────────────────────────
        if direction:
            move_pacman(direction, screen)  # move Pac-Man if a key has been pressed

        if frame_count % 5 == 0:   # ghosts move every 5 frames, not every frame
            move_ghosts(screen)

        move_ghosts(screen)  # move ghosts every frame

        # Check win condition — all pellets collected
        if len(pellet_positions) == 0:
            draw_you_win(screen)

        # ── Phase 3: Draw Everything ──────────────────────────────────────────
        screen.fill(BLACK)              # clear the screen with black
        draw_maze(screen)               # draw walls, pellets, ghosts, Pac-Man
        draw_hud(screen, score, lives)  # draw score and lives
        pygame.display.flip()           # push the drawn frame to the screen

    pygame.quit()   # clean up pygame before exiting

# ── Entry Point ───────────────────────────────────────────────────────────────
# This is standard Python — only call main() when this file is run directly,
# not when it is imported by another file.
if __name__ == "__main__":
    main()
