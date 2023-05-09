import pygame
import numpy as np

# Define some constants
WIDTH, HEIGHT = 750, 750
ROWS, COLS = 75, 75
CELL_SIZE = WIDTH // ROWS

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Create a numpy array to store the state of the cells
board = np.zeros((ROWS, COLS), dtype=int)

# Draw the cells
def draw_cells():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, GRAY, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Update the state of the cells
def update_cells():
    global board
    new_board = np.zeros((ROWS, COLS), dtype=int)
    for row in range(1, ROWS-1):
        for col in range(1, COLS-1):
            # Count the number of live neighbors
            neighbors = np.sum(board[row-1:row+2, col-1:col+2]) - board[row][col]
            if board[row][col] == 1 and (neighbors == 2 or neighbors == 3):
                new_board[row][col] = 1
            elif board[row][col] == 0 and neighbors == 3:
                new_board[row][col] = 1
    del board
    board = new_board

# Reset the board back to 0s
def reset_board():
    global board
    board = np.zeros((ROWS, COLS), dtype=int)

# Paint board position on click
def handle_click(event):
    x, y = event.pos
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    board[row][col] = 1 - board[row][col]

def randomize_board():
    global board
    board = np.zeros((ROWS, COLS), dtype=int)
    for row in range(ROWS):
        for col in range(COLS):
            if np.random.rand() < 0.4:
                board[row][col] = 1

def main():
    running = True  
    clock = pygame.time.Clock()
    playing = False

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(event)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = ~playing
                elif event.key == pygame.K_BACKSPACE:
                    reset_board()
                elif event.key == pygame.K_r:
                    randomize_board()

        if(playing):
            update_cells()

        # Clear the screen
        screen.fill(BLACK)
        draw_cells()

        # Update the screen
        pygame.display.flip()
        # Limit the frame rate
        clock.tick(10)
    # Quit pygame
    pygame.quit()

if __name__ == '__main__':
    main()
