from Crypto.Cipher import AES
import os

#change to my python files dir
os.chdir('C:\\Users\\yorks\\python')

key = b'thisismykey!1234'
data = b'this is my message and I am not worrying about length'

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encrypted.bin", "wb")
[file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]

file_out.close()
