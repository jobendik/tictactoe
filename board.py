class Board:
    def __init__(self):
        self.board = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]

        self.game_over = False

    def move(self, move, sign, name):

        if move == 0 and self.board[0][0] != 'X' and self.board[0][0] != 'O' and not self.check_winner(sign, name):
            self.board[0].pop(0)
            self.board[0].insert(0, sign)
            return self.board

        elif move == 1 and self.board[0][1] != 'X' and self.board[0][1] != 'O' and not self.check_winner(sign, name):
            self.board[0].pop(1)
            self.board[0].insert(1, sign)
            return self.board

        elif move == 2 and self.board[0][2] != 'X' and self.board[0][2] != 'O' and not self.check_winner(sign, name):
            self.board[0].pop(2)
            self.board[0].insert(2, sign)
            return self.board

        elif move == 3 and self.board[1][0] != 'X' and self.board[1][0] != 'O' and not self.check_winner(sign, name):
            self.board[1].pop(0)
            self.board[1].insert(0, sign)
            return self.board

        elif move == 4 and self.board[1][1] != 'X' and self.board[1][1] != 'O' and not self.check_winner(sign, name):
            self.board[1].pop(1)
            self.board[1].insert(1, sign)
            return self.board

        elif move == 5 and self.board[1][2] != 'X' and self.board[1][2] != 'O' and not self.check_winner(sign, name):
            self.board[1].pop(2)
            self.board[1].insert(2, sign)
            return self.board

        elif move == 6 and self.board[2][0] != 'X' and self.board[2][0] != 'O' and not self.check_winner(sign, name):
            self.board[2].pop(0)
            self.board[2].insert(0, sign)
            return self.board

        elif move == 7 and self.board[2][1] != 'X' and self.board[2][1] != 'O' and not self.check_winner(sign, name):
            self.board[2].pop(1)
            self.board[2].insert(1, sign)
            return self.board

        elif move == 8 and self.board[2][2] != 'X' and self.board[2][2] != 'O' and not self.check_winner(sign, name):
            self.board[2].pop(2)
            self.board[2].insert(2, sign)
            return self.board

        if self.check_winner(sign, name):
            self.print_board()
            print(f'We have a winner: {name} wins!')
            self.game_over = True
            return name

        else:
            return 200

    def check_winner(self, sign, name):
        if self.board[0][0] == sign and self.board[0][1] == sign and self.board[0][2] == sign or \
                self.board[1][0] == sign and self.board[1][1] == sign and self.board[1][2] == sign or \
                self.board[2][0] == sign and self.board[2][1] == sign and self.board[2][2] == sign:
            return name

        if self.board[0][0] == sign and self.board[1][0] == sign and self.board[2][0] == sign or \
                self.board[0][1] == sign and self.board[1][1] == sign and self.board[2][1] == sign or \
                self.board[0][2] == sign and self.board[1][2] == sign and self.board[2][2] == sign:
            return name

        if self.board[0][0] == sign and self.board[1][1] == sign and self.board[2][2] == sign or \
                self.board[2][0] == sign and self.board[1][1] == sign and self.board[0][2] == sign:
            return name

    def print_board(self):
        for i in self.board:
            print(i)
