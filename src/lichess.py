import berserk

session = berserk.TokenSession('api token')    #White
client = berserk.Client(session=session)

session_op = berserk.TokenSession('second api token')  #Black
client_op = berserk.Client(session=session_op)

email = client.account.get_email()

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
