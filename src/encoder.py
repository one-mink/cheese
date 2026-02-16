import read
import chess
import lichess

board = chess.Board()  #Creates virtual chess board
c_id = lichess.play_game() #gets game id from lichess
data = read.bin_data #binary data of the image
moves = [move.uci() for move in board.legal_moves] #checks legal moves
game_num = 1

games = [] #game id of played games
print(board)

#test_data = [0, 8, 14, 3, 6, 4, 16, 6, 10]

def move(move):
    board.push_uci(move)
    lichess.move(c_id, move)

def move_b(move):
    board.push_uci(move)
    lichess.move_b(c_id, move)


def encode(data):
   global moves
   global board
   global c_id
   global game_num

   for e in data:
       if not moves or board.is_game_over():
           board.reset()
           c_id = lichess.play_game()
           game_num += 1
           games.append(c_id)
           moves = [move.uci() for move in board.legal_moves]

       if e < len(moves):
           m = moves[e]
           print(m)

       else:
           m = moves[0]

       try:
          if board.turn == chess.WHITE:
             move(m)
          elif board.turn == chess.BLACK:
              move_b(m)
       except:
           moves = []
           continue
       moves = [move.uci() for move in board.legal_moves]

       print(board)
       print(moves)

print(c_id)
encode(data)
print(game_num)
