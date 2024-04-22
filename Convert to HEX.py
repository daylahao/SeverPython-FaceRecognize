import binascii
filename = "API/Audio/N20DCPT021.mp3"
with open(filename, 'rb') as f:
    content = f.read()
print(binascii.hexlify(content))