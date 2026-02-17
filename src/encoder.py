import read
import chess
#import lichess

offline = True
full_game_data = []

board = chess.Board()  #Creates virtual chess board
#c_id = lichess.play_game() #gets game id from lichess
data = read.bin_data #binary data of the image
moves = sorted([move.uci() for move in board.legal_moves]) #checks legal moves
game_num = 1

games = [] #game id of played games

test_data = [6, 17, 4, 0, 3, 18, 3, 11, 0, 13, 0, 10, 1, 6, 0, 10, 0, 0, 0, 0, 0, 0, 0, 13, 3, 13, 3, 12, 3, 4, 17, 18, 23, 0, 1, 17, 0, 17, 0, 8, 15, 14, 6, 5, 7, 4, 2, 3, 4, 3, 5, 1, 15, 1]

def move(move):
    board.push_uci(move)
    if offline == False:
        lichess.move(c_id, move)

def move_b(move):
    board.push_uci(move)
    if offline == False:
        lichess.move_b(c_id, move)

def encode(data):
   global moves
   global board
   global c_id
   global game_num

   game_data = []

   for e in data:
       placed = False
       while not placed:
           moves = sorted([move.uci() for move in board.legal_moves])

           if  board.is_game_over() or e >= len(moves):
               full_game_data.append(game_data)
               board.reset()

               game_data = []
               game_num += 1

               if offline == False:
                   c_id = lichess.play_game()
                   games.append(c_id)
               continue
           m = moves[e]
           bin = moves.index(m)
           print(m, bin)
           print(moves)

           try:
               if board.turn == chess.WHITE:
                   move(m)
               elif board.turn == chess.BLACK:
                   move_b(m)
               game_data.append(m)
               placed = True
           except:
               print('error')
               break

   if game_data:
        full_game_data.append(game_data)




encode(data)
print(game_num)
print(full_game_data)
