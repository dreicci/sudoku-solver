# This is a code for solving a 9x9 traditional sudoku puzzle.

# Sudoku puzzle is formatted as a 2D Array where board[i][j] is the number located at the i-th row and j-th column.
# Unfilled spaces in the puzzle are assigned as '0'.
sudoku_board = [[3, 0, 6, 5, 0, 8, 4, 0, 2],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]]


# Function for printing the board in the console.
# Expected input for this function is the 2D array board
def print_puzzle(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - - - -")  # Separates the first 3, second 3, and last 3 rows
        for column in range(len(board[row])):
            if column % 3 == 0 and column != 0:
                print("| ", board[row][column], " ", end="")
            else:
                print(board[row][column], " ", end="")
        print()
    return

# Basic Logic behind the Sudoku Solver:
# 1. Find an empty space (System of determining a space is by row)
# 2. Return a valid value in the empty space
# 3. Move to next space
# 4. If there are no solutions, return to the previously filled space.
# 5. While returning to the previous space, check other possible solutions.
# 6. Repeat until all filled.


def find_empty(board):  # Find an empty space .
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                return row, column
    return None


def valid_row(board, row, number):  # Checks whether a number has not yet been repeated on the row. Returns tru if it is a valid solution.
    if number not in board[row]:
        return True
    else:
        return False


def valid_column(board, column, number):  # Checks whether the number has not yet been used in the column. Returns true if it is a valid solution
    column_numbers = [board[i][column] for i in range(len(board))]  # Obtains the numbers found in the column
    if number not in column_numbers:
        return True
    else:
        return False


def valid_grid(board, row, column, number):  # Checks whether the number is already found in its 3x3 grid. Returns true if the number is a valid solution.
    for i in range((row // 3) * 3, (row // 3) * 3 + 3):
        for j in range((column // 3) * 3, (column // 3) * 3 + 3):
            if board[i][j] == number:
                return False
    return True


def check_solved(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return False
    return True


def solve(board):

    # Checks whether the board is already solved.
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find

    for number in range(1, 10):  # tries each number from 1-9
        if valid_row(board, row, number) and valid_column(board, column, number) and valid_grid(board, row, column, number):  # checks if valid solution
            board[row][column] = number

            if solve(board):  # Repeats trial-and-error step using the next space found by find_empty() fxn.
                return True

            board[row][column] = 0  # Code gets here if solve(board) recursion does not lead to a full board. This resets the latest iteration to 0.

    return False

print_puzzle(sudoku_board)
print("- - - - SOLVING PUZZLE - - - -")
solve(sudoku_board)
print_puzzle(sudoku_board)

