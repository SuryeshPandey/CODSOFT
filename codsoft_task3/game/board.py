# game/board.py

class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.grid = [['' for _ in range(3)] for _ in range(3)]
        self.current_winner = None

    def make_move(self, row, col, player):
        if self.grid[row][col] == '':
            self.grid[row][col] = player
            if self.check_winner(row, col, player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, row, col, player):
        # Check row
        if all(self.grid[row][c] == player for c in range(3)):
            return True
        # Check column
        if all(self.grid[r][col] == player for r in range(3)):
            return True
        # Check diagonals
        if row == col and all(self.grid[i][i] == player for i in range(3)):
            return True
        if row + col == 2 and all(self.grid[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != '' for row in self.grid for cell in row) and self.current_winner is None

    def get_empty_cells(self):
        return [(r, c) for r in range(3) for c in range(3) if self.grid[r][c] == '']

    def print_board(self):
        for row in self.grid:
            print(row)
