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

Then exceute main.py

First decide if you want to Encode or decode the image.
If you encode the first thing you do is selecting the file path then you decide if it shoud be stored on lichess or just in a file. 
If you store offline then the game data will be stored in encoded.json
If you do store on lichess it may take a while...
If you see an "error" that means that there was an error with the network. You need to restart the process. :(  (I will change that soon)

(lichess decoding doesn't work yet!!)
To decode the image you select the path of the json file when it was stored offline.
If you stored it on lichess you put in the number of the last games in or the challange ids (c_id).
Your image now will be stored in dec_img.png




