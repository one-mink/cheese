import berserk

session = berserk.TokenSession('api token')    #White
client = berserk.Client(session=session)

session_op = berserk.TokenSession('second api token')  #Black
client_op = berserk.Client(session=session_op)

email = client.account.get_email()

def play_game():
    client.challenges.create(username="cheese_bot2", rated=False, color="white")

def get_c_id():
        challenges = client.challenges.get_mine()
        if challenges:
            c_id = challenges['out'][0]['id']
            return c_id

def move(c_id, place):
    client.board.make_move(c_id, place)
    return "move ok"

def move_b(c_id, place):
    client_op.board.make_move(c_id, place)
    return "b move ok"

def accept_challenge(c_id):
    client_op.challenges.accept(c_id)

def get_board(c_id):
    board_state = client.board.stream_game_state(c_id)
    return board_state
