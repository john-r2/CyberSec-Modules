from Crypto.Cipher import AES
import os

#change to my python files dir
os.chdir('C:\\Users\\yorks\\python')

key = b'thisismykey!1234'
data = b'this is my message and I am not worrying about length'

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

with open("encrypted.bin", "wb") as file_out:
    file_out.write(cipher.nonce)
    file_out.write(tag)
    file_out.write(ciphertext)
