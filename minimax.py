# Dette programmet finner det optimale trekk for X gitt et board.

player, opponent = 'x', 'o'


def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False


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


def getBestMove(board):
    bestVal = -1000  # Initialverdi som ikke er realistisk.
    bestMove = (-1, -1)  # Initialverdier - ikke realistiske. X og Y position.

    for i in range(3):
        for j in range(3):

            if board[i][j] == '_':
                board[i][j] = player  # Tester først med x på den posisionen.
                moveVal = minimax(board, 0, False)  # MoveVALUE...av o sin tur?
                board[i][j] = '_'  # Endrer datastrukturen tilbake til utgangspunktet.

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    print("The value of the best Move is :", bestVal)
    print()
    return bestMove


board = [
    ['o', 'x', 'o'],
    ['o', 'x', '_'],
    ['x', '_', '_']
]


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


bestMove = getBestMove(board)

print("The Optimal Move is :")
print("ROW:", bestMove[0], " COL:", bestMove[1])
