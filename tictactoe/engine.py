WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from tictactoe.board import Board
import random

Square = int
Score = int


class Engine:

    def __init__(self, ai: str, foe: str, level: int):
        self.ai = ai
        self.foe = foe
        self.level = level

    def minimax(self, board: Board, ai_turn: bool, depth: int, alpha: float,
                beta: float) -> tuple:
       

    def evaluate_board(self, board: Board, depth: int) -> Score:
        

    def evaluate_best_move(self, board: Board) -> Square:
        