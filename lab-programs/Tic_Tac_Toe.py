board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
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

def tic_tac_toe():
    player = 'X'

    for turn in range(9):
        print_board()

        print("Player", player)
        choice = int(input("Enter position (1-9): ")) - 1

        if choice < 0 or choice > 8:
            print("Invalid position! Try again.")
            continue

        if board[choice] != ' ':
            print("Position already occupied! Try again.")
            continue

        board[choice] = player

        if check_winner(player):
            print_board()
            print("Player", player, "wins!")
            return

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    print_board()
    print("It's a draw!")


tic_tac_toe()