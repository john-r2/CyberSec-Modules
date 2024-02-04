from Crypto.Cipher import AES

#with open('aes-ecb.bin', 'rb') as myfile:
#    ciphertext = myfile.read()
ciphertext = b'\xe6\x964\x1fG\xf77\x08*\x00\xf8\x05\x8e\x1b\xc3\xd3\xe5\xfbWa1b\x18%\x9c\xb0\xd3\xc5\xc5t/>s\xac\x15\xaf\xc1+\xa9\x94[|=\x1f\xddH\xdfS7S\xef=$\xca`\x98\x18\x95\x11\xe8-YU\xcd'
aes_obj = AES.new(b'This is the key!', AES.MODE_ECB)
plaintext = aes_obj.decrypt(ciphertext)
print(plaintext)