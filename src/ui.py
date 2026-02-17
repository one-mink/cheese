import read
import encoder
import decoder
import write
import json
import lichess

def main():
    mode = input("Do ypu want to decode or encode an image? (decode/encode)")

    if mode == "encode":
        filepath = input("Which image do you want to chessify? (Filepath) ")
        try:
            raw_data = read.read(filepath)
            bin_data = read.translate(raw_data)
        except:
            print('Image not found')

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
            number = input("In how many games the image is stored? ")
            decoder.online = True
            chess_data = lichess.get_last_games(number)

        else:
            file_path = input("Where are your chess games? (.json)")
            with open(file_path, "r") as f:
                chess_data = json.load(f)

        decoder.decode(chess_data)
