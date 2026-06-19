# Start of the program

def print_board(board):
    for i, row in enumerate(board):
        #  gives row elements by being seperated by a vertical bar
        print(" " + " | ".join(row))
        #  gives a horizontal divider line between the rows
        if i < 2:
            print("---+" * 2 + "---")


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
            all(board[j][i] == player for j in range(3)):
                return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def is_board_full(board):
    # Returns True if there are no empty spaces left
    return all(cell !=" " for row in board for cell in row)


def play_game():
    # Start the game
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Enter moves as row and column numbers (0, 1, or 2) seperated by a space.")

    while True:
        print_board(board)
        print(f"\nPlayer {current_player}'s turn.")

        # Get valid input from a player
        try:
            row, col = map(int, input("Enter row and column (e.g, 0 2): ").split())
            if row not in range(3) or col not in range(3):
                print("Invalid grid position! Use numbers 0, 1, or 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

        except (ValueError, IndexError):
            print("Invalid input format! Enter two numbers seperated by a space.")
            continue

        # marker
        board[row][col] = current_player

        # check game
        if check_winner(board,current_player):
            print_board(board)
            print(f"\nGame Over! Player {current_player} wins! 🎉")
            break

        if is_board_full(board):
            print_board(board)
            print("\nGame Over! It's a tie! 🤝")
            break

        current_player = "0" if current_player == "X" else "X"


# Start the game
if __name__ == "__main__":
    play_game()