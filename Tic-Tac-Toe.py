def ConstBoard(board):
    print("\n\nCurrent state of the board:\n\n")
    for i in range(0, 9):
        if (i > 0) and (i % 3 == 0):
            print("\n")
        if board[i] == 0:
            print(" _ ", end=" ")
        if board[i] == -1:
            print(" X ", end=" ")
        if board[i] == 1:
            print(" O ", end=" ")
    print("\n\n")

def User1Turn(board, player_symbol):
    while True:
        pos = input(f"\n\nEnter '{player_symbol}' position from [1, 2, 3, ..., 9]: ")
        try:
            pos = int(pos)
            if pos < 1 or pos > 9 or board[pos - 1] != 0:
                print("\n\nWRONG MOVE...!!! Try again.")
            else:
                board[pos - 1] = -1
                break
        except ValueError:
            print("\n\nInvalid input. Enter a number between 1 and 9.")

def User2Turn(board):
    while True:
        pos = input("\n\nEnter 'O' position from [1, 2, 3, ..., 9]: ")
        try:
            pos = int(pos)
            if pos < 1 or pos > 9 or board[pos - 1] != 0:
                print("\n\nWRONG MOVE...!!! Try again.")
            else:
                board[pos - 1] = 1
                break
        except ValueError:
            print("\n\nInvalid input. Enter a number between 1 and 9.")

def analyzeBoard(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]] == board[cb[i][2]]:
            return board[cb[i][0]]
    return 0

def minmax(board, player):
    x = analyzeBoard(board)
    if x != 0:
        return x * player
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -minmax(board, player * -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    if pos == -1:
        return 0
    return value

def CompTurn(board):
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -minmax(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    board[pos] = 1


def main():
    while True:
        choice = input("_____WELCOME TO TIC-TAC-TOE_____\n\nHello User...!!! Enter '1' for Single-Player and '2' for Multi-Player: ")
        choice = int(choice)
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        if choice == 1:
            print("\n\nSingle-Player: You vs. Computer")
            player_symbol = input("\n\nSelect your symbol: 'X' or 'O': ").upper()
            while player_symbol not in ['X', 'O']:
                print("\n\nInvalid choice. Please select 'X' or 'O'.")
                player_symbol = input("\n\nSelect your symbol: 'X' or 'O': ").upper()
            if player_symbol == 'X':
                computer_symbol = 'O'
                player = -1
                play_first = input("\n\nEnter '1' to play first or '2' to play second: ")
                if play_first == '2':
                    CompTurn(board)
            else:
                computer_symbol = 'X'
                player = 1
                play_first = input("\n\nEnter '1' to let the computer play first or '2' to play first: ")
                if play_first == '1':
                    CompTurn(board)
        elif choice == 2:
            print("\n\nMulti-Player: Player 1 vs. Player 2")
            player_symbol = 'X'
            player = -1
            first_player = input("\n\nEnter '1' for Player 1 to play first or '2' for Player 2 to play first: ")
            if first_player == '2':
                player = 1
        else:
            print("\n\nInvalid choice. Please enter '1' for Single-Player or '2' for Multi-Player.")
            return

        for i in range(0, 9):
            if analyzeBoard(board) != 0:
                break
            if (i + 1) % 2 == 0 and choice == 1:
                CompTurn(board)
            else:
                ConstBoard(board)
                if player == -1:
                    User1Turn(board, player_symbol)
                else:
                    User2Turn(board)

        x = analyzeBoard(board)
        if x == 0:
            ConstBoard(board)
            print("\n\nDRAW..!!!")
        elif x == -1:
            ConstBoard(board)
            if player_symbol == 'X':
                print("\n\nHurrayy..!!! You ('X') win! Computer ('O') lost.")
            else:
                print("\n\nOops..!! Computer ('X') wins. You ('O') lost.")
        else:
            ConstBoard(board)
            if player_symbol == 'O':
                print("\n\nHurrayy..!!! You ('O') win! Computer ('X') lost.")
            else:
                print("\n\nOops..!!! Computer ('O') wins. You ('X') lost.")
        
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

main()