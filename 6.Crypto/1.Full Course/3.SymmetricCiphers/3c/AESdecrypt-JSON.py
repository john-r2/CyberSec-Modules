from Crypto.Cipher import AES
import base64
import json

key = b'thisismykey!1234'

# read the message data as JSON data
#  it is put in Python dict
with open('encrypted.json', 'rt') as file_in:
    message = json.load(file_in)

# optional, print the message dict
print(message)

# convert string to bytes with .encode() method
#  decode b64 bytes, output is bytes (cipher method wants bytes)
nonce = base64.b64decode((message["nonce"].encode()))
tag =  base64.b64decode((message["tag"].encode()))
ciphertext =  base64.b64decode((message["ciphertext"].encode()))

cipher = AES.new(key, AES.MODE_EAX,nonce)
plaintext = cipher.decrypt_and_verify(ciphertext, tag)

# print plaintext in bytes
print(plaintext)

# print plaintext as a string
#  since data is ASCII text, they look the same
print(plaintext.decode())