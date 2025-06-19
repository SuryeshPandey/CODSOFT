# game/ai.py

import math
from copy import deepcopy

class AI:
    def __init__(self, ai_player='O', human_player='X'):
        self.ai_player = ai_player
        self.human_player = human_player

    def get_best_move(self, board_obj):
        best_score = -math.inf
        best_move = None

        for row, col in board_obj.get_empty_cells():
            new_board = deepcopy(board_obj)
            new_board.make_move(row, col, self.ai_player)
            score = self.minimax(new_board, False)
            if score > best_score:
                best_score = score
                best_move = (row, col)
        return best_move

    def minimax(self, board_obj, is_maximizing):
        if board_obj.current_winner == self.ai_player:
            return 1
        elif board_obj.current_winner == self.human_player:
            return -1
        elif board_obj.is_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for row, col in board_obj.get_empty_cells():
                new_board = deepcopy(board_obj)
                new_board.make_move(row, col, self.ai_player)
                score = self.minimax(new_board, False)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for row, col in board_obj.get_empty_cells():
                new_board = deepcopy(board_obj)
                new_board.make_move(row, col, self.human_player)
                score = self.minimax(new_board, True)
                best_score = min(best_score, score)
            return best_score
