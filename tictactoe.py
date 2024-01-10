from ai import AI
from player import Player
from board import Board
from random import randint

class TicTacToe:
    HUMAN = 0
    COMPUTER = 1

    def __init__(self):
        self.turns_played = 0
        self.first_move = TicTacToe.HUMAN
        self.score = {'勝ち': 0, '負け': 0, '引き分け': 0}
        self.board = Board()
        self.ai = AI()
        self.player = Player()

    def main(self):
        while True:
            self.player.select_difficulty(self.ai)
            self._set_game_settings()
            if self.first_move == self.HUMAN:
                self.play_game(self.player.players_turn, self.ai.play_move)
            else:
                self.play_game(self.ai.play_move, self.player.players_turn)
            self._print_score()
            command = self.player.play_again()
            if command == "y":
                self._reset_board()
            else:
                break

    def _set_game_settings(self):
        self._select_first_player()
        self.board.set_symbols(self.first_move)

    def _select_first_player(self):
        self.first_move = self.HUMAN if randint(0, 1) == self.HUMAN else self.COMPUTER

    def first_move_setup(self) -> tuple:
        if self.first_move == TicTacToe.HUMAN:
            input("プレイヤーが先攻です。↲")
            return self.board.human_symbol, self.board.computer_symbol
        else:
            input("コンピューターが先攻です。↲")
            return self.board.computer_symbol, self.board.human_symbol

    def is_player_win(self, symbol) -> bool:
        '''Checks if player1 has won.'''
        if self.board.win_check(symbol):
            return True
        return False

    def player_wins(self, symbol):
        self.board.print_board()
        if symbol == self.board.human_symbol:
            input("あなたの勝ち！↲")
            self.score['勝ち'] += 1
        else:
            input("コンピューターの勝ち↲")
            self.score['負け'] += 1

    def player_turn(self, player_func, symbol) -> str:
        """Plays the players turn and returns "break" if the player has won"""
        if symbol == self.board.human_symbol:
            self.board.print_board()
        player_func(self.board)
        if self.is_player_win(symbol):
            self.player_wins(symbol)
            return "break"
        return None

    def is_draw(self) -> bool:
        '''Checks if the game is drawn.'''
        if self.turns_played == 4:
            return True
        return False

    def _draw(self):
        """Initiates draw"""
        self.board.print_board()
        input("引き分け↲")
        self.score['引き分け'] += 1

    def play_game(self, player1_func, player2_func):
        """Plays the game"""
        player1_symbol, player2_symbol = self.first_move_setup()
        while True:
            if self.player_turn(player1_func, player1_symbol) == "break":
                break
            if self.is_draw():
                self._draw()
                break
            if self.player_turn(player2_func, player2_symbol) == "break":
                break
            self.turns_played += 1

    def _reset_board(self):
        self.board.reset_board()
        self.turns_played = 0

    def _print_score(self):
        print('-'*11)
        print("成績")
        print('-'*11)
        [print(f"{key}: {value}") for key, value in self.score.items()]
        print('-'*11)

if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.main()
