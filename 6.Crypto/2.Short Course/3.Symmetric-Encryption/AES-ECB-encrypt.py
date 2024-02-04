from Crypto.Cipher import AES

aes_obj = AES.new(b'This is the key!', AES.MODE_ECB)
plaintext = b'Attack at dawn, regardless of the weather.  No excuses! 12345678'
ciphertext = aes_obj.encrypt(plaintext)
print(ciphertext)
with open('aes-ecb.bin', 'wb') as myfile:
    myfile.write(ciphertext)
