from random import randrange

# Funciones

def show_board(board): # Esta funcion muestra el tablero del juego en el estado actual
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

def star_game(): # Setea una lista que representa el tablero y una lista que guarda los movimientos disponibles
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

def add_play(board:list, player:str, position:int): # Modifica el tablero agregando la jugada del jugador
    for i in range(3):
        for j in range(3):
            if board[i][j] == position:
                board[i][j] = player
                return board
    return board

def end_game(board:list): #Verifica que haya un ganador
    if board[0][0] == board[0][1] == board [0][2]:
        return True, board[0][0]
    elif board[1][0] == board[1][1] == board [1][2]:
        return True, board[1][0]
    elif board[2][0] == board[2][1] == board [2][2]:
        return True, board[2][0]
    elif board[0][0] == board[1][0] == board [2][0]:
        return True, board[0][0]
    elif board[0][1] == board[1][1] == board [2][1]:
        return True, board[0][1]
    elif board[0][2] == board[1][2] == board [2][2]:
        return True, board[0][2]
    elif board[0][0] == board[1][1] == board [2][2]:
        return True, board[0][0]
    elif board[0][2] == board[0][1] == board [2][0]:
        return True, board[0][2]
    else:
        return False, " "

def move_machine(avaliable_moves:list, game_board:list): # Realiza un movimiento aleatorio, es el juego de la maquina
    move = 0
    if len(avaliable_moves)!= 0:
        if 5 in avaliable_moves:
            move = 5
        else:
            while move not in avaliable_moves:
                move = randrange(1,9)            
        avaliable_moves.remove(move)
        game_board = add_play(game_board,player_machine,move)    
    return avaliable_moves, game_board

def move_user(avaliable_moves:list, game_board:list): #Le pide al usuario que ingrese un movimiento y lo aplica
    move = 0
    while move == 0:
        
        try:
            move = int(input("Ingresa tu movimiento: "))
            if not (move > 0 and move < 10):
                print("Parece que ingresaste un número que no se encuentra en el tablero, vuelve a intentarlo")
                move = 0
            elif move not in avaliable_moves:
                print("El movimiento que ingresaste no se encuentra disponible, vuelve a intentarlo")
                move = 0
        except ValueError:
            print("Solo puedes ingresar números, vuelve a intentarlo")
            move = 0
        except:
            print("Parece que algo salió mal, vuelve a intentarlo")
            move = 0
    
    avaliable_moves.remove(move)
    game_board = add_play(game_board,player_user,move)
        
    return avaliable_moves, game_board

# Juego

game_board, avaliable_moves = star_game()
player_user = "O"
player_machine = "X"

print("Vamos a jugar un TIC TAC TOE!")
show_board(game_board)

print("Comienzo yo!")
avaliable_moves, game_board = move_machine(avaliable_moves,game_board)
end, ganador = end_game(game_board)

while not end and len(avaliable_moves) != 0 :
    show_board(game_board)
    avaliable_moves, game_board = move_user(avaliable_moves,game_board)
    end, ganador = end_game(game_board)
    if end:
        break
    print("Es mi turno")
    avaliable_moves, game_board = move_machine(avaliable_moves,game_board)
    end, ganador = end_game(game_board)

show_board(game_board)
end, ganador = end_game(game_board)
if not end and len(avaliable_moves) == 0:
    print("Empatamos!")
elif ganador == "X": 
    print("Perdiste!")
else:
    print("Has Ganado!")