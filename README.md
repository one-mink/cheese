# Cheese

## About
Cheese stores your image on lichess.org. It takes the binary data of the image and converts them into chess moves.
Then the chess moves are played automaticcaly on lichess and last you can download the data of the games and restore your image again!

## Dependecies
berserk,
python-chess

## How to use it
Clone the repo and move into "cheese/src"

Edit lichess.py and put in your api tokens.
Make sure this is enabled:

<img width="524" height="201" alt="2026-02-17-195337_hyprshot" src="https://github.com/user-attachments/assets/c4f30166-d43d-416a-b6f1-1ee46767276d" />
<img width="511" height="133" alt="image" src="https://github.com/user-attachments/assets/fb3b2b8c-53b1-4eb3-b999-7fed2a50543c" />




Then exceute main.py

First decide if you want to Encode or decode the image.
If you encode the first thing you do is selecting the file path then you decide if it shoud be stored on lichess or just in a file. 
If you store offline then the game data will be stored in encoded.json
If you do store on lichess it may take a while...
If you see an "error" that means that there was an error with the network. You need to restart the process. :(  (I will change that soon)


To decode the image you select the path of the json file when it was stored offline.
If you stored it on lichess you put in the c_ids into games.json (last ones are saved automatically)
Your image now will be stored in dec_img.png




