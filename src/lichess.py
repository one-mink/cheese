import berserk

session = berserk.TokenSession('LICHESS API')
client = berserk.Client(session=session)

email = client.account.get_email()

def play_game():
    client.challenges.create(username="cheese_bot2", rated=False)
    challenges = client.challenges.get_mine()
    if challenges:
        c_id = challenges['out'][0]['id']
        return c_id

def move(c_id, place):
    client.board.make_move(c_id, place)
    return "move ok"

def accept_challenge(c_id):
    session_op = berserk.TokenSession('2ND LICHESS API')
    client_op = berserk.Client(session=session_op)
    client_op.challenges.accept(c_id)
