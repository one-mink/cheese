import binascii

def read(file):
   with open(file, "rb") as image:
      f = image.read()
      data = bytearray(f)
   return data

raw_data = read('banana.png')

def translate(data):
    bin = []
    for byte in data:
        bin.append(byte // 20)
        bin.append(byte % 20)
    return bin

bin_data = translate(raw_data)
