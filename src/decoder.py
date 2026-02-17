import write
import chess
import encoder
#import lichess

number = 4

board = chess.Board()
#games_data = lichess.get_last_games(number)
#games_data = [['a2a3'],['b7b5', 'b2b3']]
games_data = encoder.full_game_data

total_data = []
def decode(moves_list):
    global board
    global total_data

    total_data = []
    for games in games_data:
        board = chess.Board()
        print(games)
        for m in games:
            legal_moves = sorted([move.uci() for move in board.legal_moves])
            print(m)
            if m in legal_moves:
                bin = legal_moves.index(m)
                total_data.append(bin)
                board.push_uci(m)
            else:
                print('not found')
        #if board.is_game_over() or bin <= len(legal_moves):
        #    board = chess.Board()

decode(games_data)
if len(total_data) > 1:
    write.translate(total_data)
print(total_data)
