import write
import chess
import json
import lichess

board = chess.Board()
total_data = []

def decode(games_data):
    global board
    global total_data

    total_data = []

    for games in games_data:
        board = chess.Board()
        for m in games:
            legal_moves = sorted([move.uci() for move in board.legal_moves])
            if m in legal_moves:
                bin = legal_moves.index(m)
                total_data.append(bin)
                board.push_uci(m)
            else:
                print('not found')

    if len(total_data) > 1:
        write.translate(total_data)
