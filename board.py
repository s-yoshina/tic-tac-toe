import random

class Board:
    BOARD_SIZE = 3
    PLAYER = 0
    COMPUTER = 1
    WIN = 3

    def __init__(self):
        self.board = []
        self._initialize_board()
        self.human_symbol = ""
        self.computer_symbol = ""
        self.board_coordinate_map = {}
        self._conduct_board_mapping()

    def set_symbols(self, first_player):
        '''Sets the symbols used by the players on the board.

        [Arguments]
        first_player: int
        '''
        if first_player == self.PLAYER:
            self.human_symbol = "O"
            self.computer_symbol = "X"
        else:
            self.human_symbol = "X"
            self.computer_symbol = "O"

    def get_available_moves(self) -> list:
        '''Checks for the availabe moves on the board
            and returns them as a list.
        [Returns] -> list
        '''
        available_moves = []
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if type(self.board[i][j]) is int:
                    available_moves.append(self.board[i][j])
        return available_moves

    def apply_move(self, move, symbol):
        '''Applies the move of a player onto the board.

        [Arguments]
        move: int
        symbol: str
        '''
        x, y = self.board_coordinate_map[move]
        self.board[x][y] = symbol

    def print_board(self):
        '''Displays the board on the screen.
           ***Currently doesn't self_adjust with regards to the size of the integers in the squares'''
        def border_print():
            '''Displays the border of each row onto the screen'''
            for i in range(self.BOARD_SIZE-1):
                print('+---', end='')
            print('+---+')
        border_print()
        # Loop to print the non-border rows.
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE-1):
                print('| %s ' % (self.board[i][j]), end='')
            print('| ' + str(self.board[i][self.BOARD_SIZE-1]) + ' |')
            border_print()

    def is_column_win(self, symbol, col) -> bool:
        symbol_count = 0
        for row in range(Board.BOARD_SIZE):
            if symbol_count == Board.WIN:
                return True
            if self.board[row][col] != symbol:
                return False
            symbol_count += 1
        return True

    def win_check(self, symbol) -> bool:
        '''Checks whether a player has won or not by returning a boolean.

        [Arguments]
        symbol: str
        '''
        # Row and column check
        for i, row in enumerate(self.board):
            if row == [symbol]*Board.WIN: # Row check
                return True
            if self.is_column_win(symbol, i): # Column check
                return True

        # Diagonal checks for three in a row
        tr_diag_count = 0 # Diagonal from the top left to the bottom right
        tl_diag_count = 0 # Diagonal from the top right to the bottom left
        for i in range(self.BOARD_SIZE):
            if self.board[i][self.BOARD_SIZE-1-i] == symbol:
                tr_diag_count += 1
            if self.board[i][i] == symbol:
                tl_diag_count += 1
            if tr_diag_count == Board.WIN or tl_diag_count == 3:
                return True
        return False

    def reset_board(self):
        '''Resets the board to its initial state.'''
        square_number = 1
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                self.board[i][j] = square_number
                square_number += 1

    def _initialize_board(self):
        '''Initializes the board array.'''
        for i in range(1, (self.BOARD_SIZE**2)+1, self.BOARD_SIZE):
            self.board.append([j for j in range(i, i+self.BOARD_SIZE)])

    def _conduct_board_mapping(self):
        '''Maps the board coordinates to array coordinates for the board array.'''
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                self.board_coordinate_map[self.board[i][j]] = (i,j)

if __name__ == "__main__":
    board = Board()
    board.set_symbols(Board.PLAYER)
    board.print_board()
