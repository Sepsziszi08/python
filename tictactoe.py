def display_board(board):
    blankBoard="""
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""

    for i in range(1,10):
        if (board[i] == 'O' or board[i] == 'X'):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)

def player_input():
    player1 = input("Válasz egyet 'X' vagy 'O' ")
    while True:
        if player1.upper() == 'X':
            player2='O'
            print("Tiéd lesz az " + player1 + ". Tehát a másik játékos az " + player2)
            return player1.upper(),player2
        elif player1.upper() == 'O':
            player2='X'
            print("Tiéd lesz az " + player1 + ". Tehát a másik játékos az " + player2)
            return player1.upper(),player2
        else:
            player1 = input("Válassz ki egyet 'X' vagy 'O' ")

def place_marker(board, marker, position):
    board[position] = marker
    return board

def space_check(board, position):
    return board[position] == '#'

def full_board_check(board):
    return len([x for x in board if x == '#']) == 1

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False

def player_choice(board):
    choice = input("Kérlek válassz egy üres helyet 1 és 9 között : ")
    while not space_check(board, int(choice)):
        choice = input("Ez nem üres. Válassz egy új helyet 1 és 9 között : ")
    return choice

def replay():
    playAgain = input("Szeretnél még egyet játszani (igen/nem) ? ")
    if playAgain.lower() == 'igen':
        return True
    if playAgain.lower() == 'nem':
        return False

def start():

    print('Üdvözöllek a Tic Tac Toe-ban!')
    i = 1
    # Choose your side
    players=player_input()
    # Empty board init
    board = ['#'] * 10
    while True:
        # Set the game up here
        game_on=full_board_check(board)
        while not game_on:
            # Player to choose where to put the mark
            position = player_choice(board)
            # Who's playin ?
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            # Play !
            place_marker(board, marker, int(position))
            # Check the board
            display_board(board)
            i += 1
            if win_check(board, marker):
                print("Aki nyert annak gratulálok!")
                break
            game_on=full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            # Choose your side
            players=player_input()
            # Empty board init
            board = ['#'] * 10
