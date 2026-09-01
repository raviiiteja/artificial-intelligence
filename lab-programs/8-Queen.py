def print_board(board):
    print("\nSolution:\n")
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()


def is_safe(board, row, col, n):
    
    for i in range(col):
        if board[row][i] == 1:
            return False

    
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(board, col, n):
    
    if col == n:
        return True

    
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            print(f"Placed Queen at Row {row}, Column {col}")

            if solve(board, col + 1, n):
                return True

            
            board[row][col] = 0
            print(f"Backtracking from Row {row}, Column {col}")

    return False



n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

print("Solving 8-Queen Problem...\n")

if solve(board, 0, n):
    print("\n8-Queen Problem Solved Successfully!")
    print_board(board)

    print("Queen Positions:")
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print(f"Queen -> Row {i}, Column {j}")
else:
    print("No solution exists.")