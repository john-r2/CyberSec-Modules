from Crypto.Cipher import AES
import os

os.chdir('C:\\Users\\yorks\\python')

key = b'thisismykey!1234'

with open('encrypted.bin', 'rb') as file_in:
    nonce = file_in.read(16)
    tag = file_in.read(16)
    ciphertext = file_in.read(-1)

cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

print(data)
