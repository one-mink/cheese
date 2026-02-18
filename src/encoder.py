import chess
import lichess
import time
import json

offline = True

full_game_data = []

board = chess.Board()  #Creates virtual chess board
moves = sorted([move.uci() for move in board.legal_moves]) #checks legal moves
game_num = 1
game_id = [] #game id of played games

c_id = None

def move_white(move):
    board.push_uci(move)


def move_black(move):
    board.push_uci(move)

def encode(data):
   global moves
   global board
   global c_id
   global game_num

   game_data = []
   board.reset()

   for e in data:
       placed = False
       while not placed:
           moves = sorted([move.uci() for move in board.legal_moves])

           if  e >= len(moves):
               full_game_data.append(game_data)
               board.reset()

               game_data = []
               game_num += 1
               continue
           m = moves[e]
           bin = moves.index(m)
           print(m, bin)

           if board.turn == chess.WHITE:
                   move_white(m)
           elif board.turn == chess.BLACK:
                   move_black(m)
           game_data.append(m)
           placed = True

           if board.is_game_over():
               full_game_data.append(game_data)
               board.reset()
               game_data = []
               game_num += 1

   if game_data:
        full_game_data.append(game_data)
        game_num += 1

   if offline == False:
       for games in full_game_data:
           board = chess.Board()
           current_id = lichess.play_game()
           game_id.append(current_id)

           for move in games:
               if board.turn == chess.WHITE:
                   lichess.move(current_id, move)
               elif board.turn == chess.BLACK:
                   lichess.move_b(current_id, move)
               board.push_uci(move)
               time.sleep(0.2)

           lichess.resign(current_id)
           
       with open("games.json", "w") as f:
            json.dump(game_id, f)

   print("Game IDs! Saved in games.json! ", game_id)
   print(game_num)
