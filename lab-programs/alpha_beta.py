board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if all(board[i] == player for i in position):
            return True

    return False

def is_full():
    return ' ' not in board

def alpha_beta(is_maximizing, alpha, beta):

    if check_winner('O'):
        return 1

    if check_winner('X'):
        return -1

    if is_full():
        return 0


    if is_maximizing:

        best_score = -float('inf')

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'O'

                score = alpha_beta(False, alpha, beta)

                board[i] = ' '

                best_score = max(best_score, score)

                alpha = max(alpha, best_score)

                
                if alpha >= beta:
                    break

        return best_score

    
    else:

        best_score = float('inf')

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'X'

                score = alpha_beta(True, alpha, beta)

                board[i] = ' '

                best_score = min(best_score, score)

                beta = min(beta, best_score)

                # Alpha-Beta pruning
                if alpha >= beta:
                    break

        return best_score


def best_move():

    best_score = -float('inf')
    move = 0

    for i in range(9):

        if board[i] == ' ':

            board[i] = 'O'

            score = alpha_beta(False, -float('inf'), float('inf'))

            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move


print("Tic-Tac-Toe using Alpha-Beta Pruning")
print("You are X")
print("Computer is O")

while True:

    print_board()

    
    position = int(input("Enter position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != ' ':
        print("Invalid move! Try again.")
        continue

    board[position] = 'X'

    if check_winner('X'):
        print_board()
        print("You win!")
        break

    
    if is_full():
        print_board()
        print("It's a draw!")
        break

    
    computer_position = best_move()
    board[computer_position] = 'O'

    print("Computer chose position:", computer_position + 1)

    
    if check_winner('O'):
        print_board()
        print("Computer wins!")
        break

    if is_full():
        print_board()
        print("It's a draw!")
        break