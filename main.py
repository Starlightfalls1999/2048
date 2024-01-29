import pygame
from pygame.locals import QUIT
import sys
from game_functions import initialize_board, add_new_tile, draw_board, move

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("2048 Game")

    board = initialize_board()
    add_new_tile(board)
    add_new_tile(board)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        draw_board(screen, board)

        direction = input("Enter move (W/A/S/D): ").upper()

        if direction not in ['W', 'A', 'S', 'D']:
            print("Invalid input. Use WASD to MOVE.")
            continue

        if move(board, direction):
            add_new_tile(board)
        else:
            print("Invalid move. Try again.")

        if is_game_over(board):
            print("Game Over!")
            break



def is_game_over(board):
    # Helper function to check for any empty cells on the board
    def has_empty_cells(board):
        return any(0 in row for row in board)

    # Helper function to check for adjacent equal values in rows or columns
    def has_adjacent_equal_values(row):
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                return True
        return False

    # Check for valid moves in rows
    for row in board:
        if has_empty_cells(board) or has_adjacent_equal_values(row):
            return False

    # Check for valid moves in columns
    for col in range(4):
        column_values = [board[row][col] for row in range(4)]
        if has_adjacent_equal_values(column_values):
            return False

    return True


if __name__ == "__main__":
    main()
