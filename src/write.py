import binascii
import read

def translate(data):
    png_data = bytearray()
    for i in range(0, len(data) -1, 2):
        a = data[i]
        b = data[i+1]

        png = ((a*20) + b) % 256
        png_data.append(png)
    with open("dec_banana.png", "wb") as f:
        f.write(png_data)
