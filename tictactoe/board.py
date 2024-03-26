WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from typing import Optional
from enum import Enum

Square = int


class Symbol(Enum):
    CIRCLE = "O"
    CROSS = "X"
    EMPTY = "#"


class Board:
    """Responsible for storing current state, making and validating moves, and updating the game

    Attributes:
        first_move (Symbol): Symbol to make the first move, alternate after every match
        p1_score (int): First player's score
        p2_score (int): Second player's score
        size (int): Board dimension     
        squares (dict[[int,int],Square]): Container to convert row,col into Square
        table (list[Symbol]): Container to store the current board state, use Square as index 
        turn (Symbol): Current turn to make a move
        win_conditions (list[list[Square]]): All possible connections to win the game
    """

    def __init__(self, size: int = 3):
        """Creating a board with given size

        Args:
            size (int, optional): Board dimension
        """
       
    def get_win_conditions(self) -> list[list[Square]]:
        """Get all winning connections, for all board sizes

        Returns:
            list[list[Square]]: list of rows, cols, diagonals 
        """
    
        return rows + cols + diagonals

    def get_squares(self) -> dict[[int, int], Square]:
        """Create a dictionary containing all squares

        Returns:
            dict[[int, int], Square]: (row,col) as key, square name as value
        """
        return {(r, c): r * self.size + c
                for r in range(self.size) for c in range(self.size)}

    def get_table(self) -> list[Symbol]:
        """Table to store the current board state

        Returns:
            list[Symbol]: List of tiles filled with empty Symbol
        """
        return [Symbol.EMPTY for _ in range(self.size**2)]

    def get_rows_cols(self) -> tuple[list[Square], list[Square]]:
        """Group squares into corresponding rows and columns

        Returns:
            tuple[list[Square], list[Square]]: lists of rows and cols
        """
     
        return rows, columns

    def get_diagonals(self) -> list[list[Square]]:
        """Calculate diagonal squares for all board sizes

        Returns:
            list[list[Square]]: list of diagonals
        """
  
        return diagonals

    @property
    def empty_squares(self) -> list[Square]:
        """Get all empty squares

        Returns:
            list[Square]: list of empty squres
        """
        return [
            square for square in self.squares.values() if self.is_empty(square)
        ]

    def reset(self):
        """Reset the board and change the turn
        """
        self.table = self.get_table()
        self.first_move = Symbol.CROSS if self.first_move == Symbol.CIRCLE else Symbol.CIRCLE
        self.turn = self.first_move

    def square_pos(self, square: Square) -> Optional[tuple[int, int]]:
        """Get row, col of the square

        Args:
            square (Square): Square number

        Returns:
            Optional[tuple[int, int]]: (row, col) if square exists
        """
        for pos, sq in self.squares.items():
            if sq == square:
                return pos
        return None

    def square_name(self, row: int, col: int) -> Square:
        """Convert row, col into square

        Returns:
            Square: corresponding number
        """
        return self.squares[(row, col)]

    def square_value(self, square: Square) -> Symbol:
        """Get the symbol of the square

        Args:
            square (Square): Square name

        Returns:
            Symbol: Symbol of the square
        """
        return self.table[square]

    def is_empty(self, square: Square) -> bool:
        """Check if square is empty

        Args:
            square (Square): square name

        Returns:
            bool: True if empty symbol
        """
        return self.table[square] == Symbol.EMPTY

    def get_connection(self) -> list[Square]:
        """Check for connected tiles

        Returns:
            list[Square]: List of connected squares
        """
        for row in self.win_conditions:
            checklist = []
            for square in row:
                if self.is_empty(square):
                    continue
                checklist.append(self.square_value(square))
            if len(checklist) == self.size and len(set(checklist)) == 1:
                return row
        return []

    def is_draw(self) -> bool:
        """Check for draw

        Returns:
            bool: True if board is filled and no connection
        """
        if len(self.empty_squares) == 0 and len(self.get_connection()) == 0:
            return True
        return False

    def winner(self) -> Optional[Symbol]:
        """Get the winner of the match

        Returns:
            Optional[Symbol]: Symbol of connected tiles if exists
        """
        connection = self.get_connection()
        if len(connection) == 0:
            return None
        elif self.square_value(connection[0]) == Symbol.CIRCLE:
            return Symbol.CIRCLE
        else:
            return Symbol.CROSS

    def is_gameover(self) -> bool:
        """Check for gameover

        Returns:
            bool: True if there's winner or draw
        """
        return self.winner() is not None or self.is_draw()

    def _update(self):
        """Update the turn and score if there's winner
        """
        self.turn = Symbol.CROSS if self.turn == Symbol.CIRCLE else Symbol.CIRCLE
        if self.winner() == Symbol.CIRCLE:
            self.p1_score += 1
        elif self.winner() == Symbol.CROSS:
            self.p2_score += 1

    def push(self, square: Square, value: Symbol):
        """Store the symbol into the square

        Args:
            square (Square): square name
            value (Symbol): symbol
        """
        self.table[square] = value

    def undo(self, square: Square):
        """Change the square's value to empty

        Args:
            square (Square): square name
        """
        self.table[square] = Symbol.EMPTY

    def move(self, square: Square):
        """Mark the square with symbol of current turn if valid and update the board

        Args:
            square (Square): square name
        """
        if square >= self.size**2 or square < 0 or not self.is_empty(square):
            print("Invalid move!")
            return
        self.push(square, self.turn)
        self._update()

    def print(self):
        """Represent the board in string
        """
      


if __name__ == "__main__":
    # CLI game for two player mode
    board = Board()
    print("Tic Tac Toe - Duel")
    print("##################")
    board.print()
    running = True
    while running:
 
