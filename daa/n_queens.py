n = 0


def display_board(board):
    print("\nChessboard:")

    for i in range(n):
        row = ""
        for j in range(n):
            if board[i][j] == 1:
                row += " Q "
            else:
                row += " . "
        print(row)


def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row):
    if row == n:
        display_board(board)
        return True

    found = False

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens(board, row + 1):
                found = True

            board[row][col] = 0

    return found


def main():
    global n

    while True:
        print("\n===== N-QUEENS MENU =====")
        print("1. Enter Number of Queens")
        print("2. Solve N-Queens Problem")
        print("3. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            n = int(input("\nEnter number of queens: "))

            if n <= 0:
                print("Invalid number of queens!")
                n = 0
            else:
                print("\nNumber of queens entered successfully!")

        elif choice == 2:
            if n == 0:
                print("\nPlease enter the number of queens first!")
            else:
                board = [[0] * n for _ in range(n)]

                print(f"\nSolutions for {n}-Queens Problem:")

                if not solve_n_queens(board, 0):
                    print("\nNo solution exists!")

        elif choice == 3:
            print("\nExiting Program...")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()

# TC: O(n!)
# SC: O(n^2)
