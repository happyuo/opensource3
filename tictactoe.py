import random

def instructions():
    print("틱택토 게임")
    print("숫자 0 ~ 8을 입력하여 움직임을 나타내세요. 각 숫자는")
    print("게임 보드의 해당 위치를 나타냅니다. 다음과 같이 설명합니다:")
    print("\n 0 | 1 | 2")
    print("---------")
    print(" 3 | 4 | 5")
    print("---------")
    print(" 6 | 7 | 8")
    print("게임이 시작됩니다.\n")

def ask_yes_no(question):
    response = input(question + " (y/n): ").lower()
    while response not in ['y', 'n']:
        response = input("y 혹은 n을 입력하세요: ").lower()
    return response

def ask_number(question, low, high):
    number = None
    while number is None:
        try:
            number = int(input(question + f" ({low} - {high}): "))
            if number < low or number > high:
                raise ValueError()
        except ValueError:
            print(f"{low}부터 {high} 사이의 숫자를 입력하세요.")
            number = None
    return number

def human_piece():
    go_first = ask_yes_no("먼저 하시겠습니까?")
    return 'X' if go_first == 'y' else 'O'

def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "-" * 9)
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "-" * 9)
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def winner(board):
    # Check rows, columns, and diagonals for a win
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != ' ':
            return board[pos[0]]

    # Check for tie
    if ' ' not in board:
        return 'T'

    return None

def is_legal(board, move):
    return board[move] == ' '

def human_move(board, human):
    move = ask_number("어디에 놓으시겠습니까?", 0, 8)
    while not is_legal(board, move):
        print("이미 차있는 칸입니다. 다시 시도하세요.")
        move = ask_number("어디에 놓으시겠습니까?", 0, 8)
    return move

human = human_piece()

def computer_move(board, computer):
    # Try to win
    for move in range(9):
        if is_legal(board, move):
            board[move] = computer
            if winner(board) == computer:
                return move
            board[move] = ' '

    # Try to block human from winning
    for move in range(9):
        if is_legal(board, move):
            board[move] = human
            if winner(board) == human:
                return move
            board[move] = ' '

    # Try to take corners if available
    corners = [0, 2, 6, 8]
    available_corners = [corner for corner in corners if is_legal(board, corner)]
    if available_corners:
        return random.choice(available_corners)

    # Try to take center if available
    if is_legal(board, 4):
        return 4

    # Take any side
    sides = [1, 3, 5, 7]
    available_sides = [side for side in sides if is_legal(board, side)]
    return random.choice(available_sides)

def announce_winner(winner, computer, human):
    if winner == computer:
        print(f"컴퓨터 ({computer}) 승!")
    elif winner == human:
        print(f"인간 ({human}) 승!")
    else:
        print("It's a tie!")

def main():
    instructions()
    computer = 'O' if human == 'X' else 'X'
    board = [' '] * 9
    display_board(list(range(9)))
    turn = 'X'
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
        else:
            move = computer_move(board, computer)
        board[move] = turn
        display_board(board)
        turn = 'O' if turn == 'X' else 'X'

    announce_winner(winner(board), computer, human)

if __name__ == "__main__":
    main()
