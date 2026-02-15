import read
import chess
import lichess

board = chess.Board()  #Creates virtual chess board
c_id = 'o3mPJWONBcGe'#lichess.get_c_id() #gets game id from lichess
data = read.bin_data #binary data of the image
moves = [move.uci() for move in board.legal_moves] #checks legal moves

print(board)

def move(move):
    board.push_uci(move)

def encode(data):
   global moves
   global board
   for number in data:
       e = data[number]
       if not moves or board.is_game_over():
           board.reset()
           moves = [move.uci() for move in board.legal_moves]

       if e < len(moves):
           m = moves[e]
           print(m)

       else:
           m = moves[0]
       move(m)
       moves = [move.uci() for move in board.legal_moves]

       print(board)
       print(moves)

print(c_id)

    #lichess.move_b(c_id, move)

#board.push_uci("0000")

#move("a2a3")

encode(data)
print(board)
print(moves)
