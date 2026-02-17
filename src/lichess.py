import berserk
import chess

token_white = 'api token'
token_black = 'second api token'


session = berserk.TokenSession(token_white)
client = berserk.Client(session=session)
username = "cheese_bot"

session_op = berserk.TokenSession(token_black)
client_op = berserk.Client(session=session_op)

def play_game():
    challenge = client.challenges.create(username="cheese_bot2", rated=False, color="white")
    c_id = challenge['id']
    client_op.challenges.accept(c_id)
    return c_id

def move(c_id, place):
    client.board.make_move(c_id, place)
    return "move ok"

def move_b(c_id, place):
    client_op.board.make_move(c_id, place)
    return "b move ok"

def get_board(c_id):
    board_state = client.board.stream_game_state(c_id)
    return board_state

def get_last_games(number):
    games = client.games.export_by_player(username, max=number)
    game_list = list(games)
    all_uci_moves = []

    for game in game_list:
        board = chess.Board()
        uci_moves = []

        moves_data = game['moves'].split()

        for move_s in moves_data:
            move_obj = board.parse_san(move_s)
            uci_moves.append(move_obj.uci())
            board.push(move_obj)

        all_uci_moves.append(uci_moves)
    return all_uci_moves
