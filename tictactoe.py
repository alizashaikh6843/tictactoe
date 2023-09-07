# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board():
    print(" | ".join(board[0:3]))
    print("-" * 9)
    print(" | ".join(board[3:6]))
    print("-" * 9)
    print(" | ".join(board[6:9]))

# Function to check if there's a winner
def check_winner(player):
    # Check rows, columns, and diagonals for a win
    for i in range(0, 3):
        if (
            board[i] == board[i + 3] == board[i + 6] == player
            or board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player
        ):
            return True
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the board is full (a tie)
def is_board_full():
    return " " not in board

# Main game loop
current_player = "X"

while True:
    print_board()
    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move. Try again.")
        continue

    board[move] = current_player

    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins! Congratulations!")
        break
    elif is_board_full():
        print_board()
        print("It's a tie!")
        break

    current_player = "X" if current_player == "O" else "O"
