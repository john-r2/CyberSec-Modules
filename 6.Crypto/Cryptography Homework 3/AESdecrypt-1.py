from Crypto.Cipher import AES
import os

os.chdir('C:\\Users\\john\\python')

key = b'thisismykey!1234'

with open('encrypted.bin', 'rb') as file_in:
    nonce = file_in.read(16)
    tag = file_in.read(16)
    ciphertext = file_in.read(-1)

cipher = AES.new(key, AES.MODE_EAX, nonce)
plaintext = cipher.decrypt_and_verify(ciphertext, tag)

print('nonce: {0}\ntag:  {1}\nciphertext:  {2}'.format(nonce,tag, ciphertext))
print(plaintext)
