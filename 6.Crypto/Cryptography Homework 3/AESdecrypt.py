from Crypto.Cipher import AES
import os

os.chdir('C:\\Users\\yorks\\python')

key = b'thisismykey!1234'

file_in = open('encrypted.bin', 'rb')
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

print(data)
