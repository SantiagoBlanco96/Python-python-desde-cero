def show_board(board):
    print(f"""
    +-------+-------+-------+
    |       |       |       |
    |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
    """)

def star_game():
    board = []
    boxes = []
    case = 1
    for i in range(3):
        row = []
        for j in range(3):
            row.append(case)
            boxes.append(case)
            case += 1
        board.append(row) 
    return board, boxes

def add_play(board, player, position):
    for i in range(3):
        for j in range(3):
            if board[i][j] == position:
                board[i][j] = player
                return board
    return board

def end_game(board):
    if board[0][0] == board[0][1] == board [0][2]:
        return True
    elif board[1][0] == board[1][1] == board [1][2]:
        return True
    elif board[2][0] == board[2][1] == board [2][2]:
        return True
    elif board[0][0] == board[1][0] == board [2][0]:
        return True
    elif board[0][1] == board[1][1] == board [2][1]:
        return True
    elif board[0][2] == board[1][2] == board [2][2]:
        return True
    elif board[0][0] == board[1][1] == board [2][2]:
        return True
    elif board[0][2] == board[0][1] == board [2][0]:
        return True
    else:
        return False

game_board, avaliable_moves = star_game()
show_board(game_board)
print(avaliable_moves)
game_board = add_play(game_board,"X",1)
avaliable_moves.remove(1)
show_board(game_board)
print(avaliable_moves)
game_board = add_play(game_board,"X",2)
avaliable_moves.remove(2)
show_board(game_board)
print(avaliable_moves)
game_board = add_play(game_board,"X",3)
avaliable_moves.remove(3)
show_board(game_board)
print(avaliable_moves)
print(end_game(game_board))


