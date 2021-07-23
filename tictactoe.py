from player import Player
from board import Board
import sys

player, opponent = 'X', 'O'


def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False


def calculate(b):
    for row in range(3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == player:
                return 10
            elif b[row][0] == opponent:
                return -10

    for col in range(3):

        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:

            if b[0][col] == player:
                return 10
            elif b[0][col] == opponent:
                return -10

    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

        if b[0][0] == player:
            return 10
        elif b[0][0] == opponent:
            return -10

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

        if b[0][2] == player:
            return 10
        elif b[0][2] == opponent:
            return -10

    return 0


def minimax(board, depth, isMax):
    # hvis isMax = True: da er vi 'X'
    # Funksjonen gir 10, -10 eller 0

    score = calculate(board)
    # Hvis vi er ferdige med spillet:
    if score == 10:
        return score

    if score == -10:
        return score

    if isMovesLeft(board) == False:
        return 0
    # Hvis vi ikke er ferdige med spillet
    if isMax:
        best = -1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == '_':
                    board[i][j] = opponent

                    best = min(best, minimax(board, depth + 1, not isMax))

                    board[i][j] = '_'
        return best


##########################

def main(game_on):
    board = Board()

    print('Welcome to Tic Tac Toe.')

    board.game_over = False

    board.board = [['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_']]

    p_vs_c = input('2 player or vs computer? (2/c)')

    # for i in range(30):
    #     print('')

    if p_vs_c == '2':
        player1 = Player(input('Name player 1: '), 'X')
        player2 = Player(input('Name player 2: '), 'O')

    elif p_vs_c == 'c':
        player1 = Player(input('Name player 1: '), 'X')
        computer = Player('Computer', 'O')

    board.print_board()

    while not board.game_over and p_vs_c == '2':
        # board.print_board()

        while True and p_vs_c == '2':
            try:
                player1_turn = int(input(f"{player1.name}! Whats your move?(0-8)\n> "))
                board_move = board.move(player1_turn, player1.sign, player1.name)
                if player1_turn > 8:
                    print('Please pick a number between 1 and 8.')
                    board.print_board()
                    continue
                if board_move == 200:
                    print('Move already taken. Please try again.')
                    board.print_board()
                    continue
                else:
                    board.move(player1_turn, player1.sign, player1.name)
                    break
            except ValueError:
                print('Please enter a valid move.')
                board.print_board()
                continue

        if board.game_over:
            player1.score += 1
            game_over(player1, player2)

        board.print_board()

        while True and p_vs_c == '2':
            try:
                player2_turn = int(input(f"{player2.name}! Whats your move?\n> "))
                player2_move = board.move(player2_turn, player2.sign, player2.name)
                if player2_turn > 8:
                    print('Please pick a number between 1 and 8.')
                    board.print_board()
                    continue
                if player2_move == 200:
                    print('Move already taken. Please try again.')
                    board.print_board()
                    continue
                else:
                    board.move(player2_turn, player2.sign, player2.name)
                    break
            except ValueError:
                print('Please enter a valid move.')
                board.print_board()
                continue

        if board.game_over:
            player2.score += 1
            game_over(player1, player2)

        board.print_board()

    while not board.game_over and p_vs_c == 'c':
        while True and p_vs_c == 'c':
            try:
                player1_turn = int(input(f"{player1.name}! Whats your move?\n> "))
                board_move = board.move(player1_turn, player1.sign, player1.name)
                if player1_turn > 8:
                    print('Please pick a number between 1 and 8.')
                    board.print_board()
                    continue
                if board_move == 200:
                    print('Move already taken. Please try again.')
                    board.print_board()
                    continue
                else:
                    board.move(player1_turn, player1.sign, player1.name)
                    break
            except ValueError:
                print('Please enter a valid move.')
                board.print_board()
                continue

        if board.game_over:
            player1.score += 1
            game_over(player1, computer)

        board.print_board()

        while True and p_vs_c == 'c':
            computer_turn = 0
            bestVal = -1000  # Initialverdi som ikke er realistisk.
            bestMove = (-1, -1)  # Initialverdier - ikke realistiske. X og Y position.

            for i in range(3):
                for j in range(3):

                    if board.board[i][j] == '_':
                        board.board[i][j] = opponent
                        moveVal = minimax(board.board, 0, True)
                        board.board[i][j] = '_'  # Endrer datastrukturen tilbake til utgangspunktet.

                        if moveVal > bestVal:
                            bestMove = (i, j)
                            bestVal = moveVal

            if bestMove == (0, 0):
                computer_turn = 0
            elif bestMove == (0, 1):
                computer_turn = 1
            elif bestMove == (0, 2):
                computer_turn = 2
            elif bestMove == (1, 0):
                computer_turn = 3
            elif bestMove == (1, 1):
                computer_turn = 4
            elif bestMove == (1, 2):
                computer_turn = 5
            elif bestMove == (2, 0):
                computer_turn = 6
            elif bestMove == (2, 1):
                computer_turn = 7
            elif bestMove == (2, 2):
                computer_turn = 8

            board.move(computer_turn, 'O', 'computer')
            board.print_board()
            break

            ####

        if board.game_over:
            player1.score += 1
            game_over(player1, computer)


def game_over(player1, player2):
    print(f'{player1.name}s score: {player1.score}. {player2.name}s score: {player2.score}')
    new_game = input('Do you want to start a new game(n) or quit(q)')
    if new_game == 'q':
        print('Thank you for playing.')
        sys.exit()
    elif new_game == 'n':
        main(True)


main(True)
