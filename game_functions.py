# game_functions.py
import random
import pygame
import sys

# Constants
WIDTH = 400
HEIGHT = 400
TILE_SIZE = 100

# Colors
BACKGROUND_COLOR = (187, 173, 160)
EMPTY_TILE_COLOR = (205, 193, 180)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def draw_board(screen, board):
    screen.fill(BACKGROUND_COLOR)

    for i in range(4):
        for j in range(4):
            tile_value = board[i][j]
            tile_color = TILE_COLORS.get(tile_value, EMPTY_TILE_COLOR)
            pygame.draw.rect(screen, tile_color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))

            if tile_value != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(tile_value), True, (0, 0, 0))
                text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)

    pygame.display.flip()



def move(board, direction):
    # Helper function to merge tiles in a row or column
    def merge(row):
        new_row = [0] * 4
        index = 0

        for value in row:
            if value != 0:
                if new_row[index] == 0:
                    new_row[index] = value
                elif new_row[index] == value:
                    new_row[index] *= 2
                    index += 1
                else:
                    index += 1
                    new_row[index] = value
        return new_row

    # Helper function to rotate the board
    def rotate_board(board):
        return [list(row) for row in zip(*board[::-1])]

    # Helper function to update the board after a move
    def update_board(board, new_board):
        for i in range(4):
            for j in range(4):
                board[i][j] = new_board[i][j]

    # Perform the move based on the specified direction
    if direction == "W":  # Move up
        rotated_board = rotate_board(board)
        new_board = [merge(row) for row in rotated_board]
        update_board(board, rotate_board(new_board))
    elif direction == "A":  # Move left
        new_board = [merge(row) for row in board]
        update_board(board, new_board)
    elif direction == "S":  # Move down
        rotated_board = rotate_board(board)
        rotated_board.reverse()
        new_board = [merge(row) for row in rotated_board]
        update_board(board, rotate_board(new_board))
    elif direction == "D":  # Move right
        reversed_board = [row[::-1] for row in board]
        new_board = [merge(row) for row in reversed_board]
        update_board(board, [row[::-1] for row in new_board])
    else:
        return False  # Invalid direction

    return True

# You can add more functions for game logic as needed
