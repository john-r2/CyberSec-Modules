from Crypto.Cipher import AES

with open('aes-ecb.bin', 'rb') as myfile:
    ciphertext = myfile.read()
aes_obj = AES.new(b'This is the key!', AES.MODE_ECB)
plaintext = aes_obj.decrypt(ciphertext)
print(plaintext)