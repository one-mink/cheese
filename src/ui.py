import read
import encoder
import decoder
import write
import json
import lichess

def main():
    mode = input("Do you want to decode or encode an image? (decode/encode)")

    if mode == "encode":
        bin_data = None
        filepath = input("Which image do you want to chessify? (Filepath) ")
        try:
            raw_data = read.read(filepath)
            bin_data = read.translate(raw_data)
        except Exception as e:
            print({e})
            return

        online = input("Do you want do store your image on lichess? (yes/no) ")
        if online == "yes":
            encoder.offline = False

        if bin_data:
            encoder.encode(bin_data)
            with open("encoded.json", "w") as f:
                json.dump(encoder.full_game_data, f)

            print("Encoded Image saved!")

    if mode == "decode":
        data = input("Do you want to get your Image from lichess? (yes/no) ")
        if data == "yes":
            decoder.online = True
            chess_data = []
            with open("games.json", "r") as f:
                 game_id_list = json.load(f)
                 for game_id in game_id_list:
                     current_board = lichess.get_last_games(game_id)
                     chess_data.append(current_board)
            print(chess_data)

        else:
            file_path = input("Where are your chess games? (.json)")
            with open(file_path, "r") as f:
                chess_data = json.load(f)

        decoder.decode(chess_data)
