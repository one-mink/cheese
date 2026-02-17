import chess
import lichess

offline = True

full_game_data = []

board = chess.Board()  #Creates virtual chess board
moves = sorted([move.uci() for move in board.legal_moves]) #checks legal moves
game_num = 1
games = [] #game id of played games

if offline == False:
    c_id = None #gets game id from lichess

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
   board.reset()

   if offline == False:
       c_id = lichess.play_game()
       games.append(c_id)

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
        game_num += 1

   print(game_num)
