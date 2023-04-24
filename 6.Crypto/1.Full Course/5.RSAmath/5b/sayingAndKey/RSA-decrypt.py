from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#import the private key
with open('saving_private.pem') as fh:
    private_key = RSA.import_key(fh.read())

#import the encrypted message
with open('saying.bin', 'rb') as fh:
    ciphertext = fh.read()
    
# Decrypt the message with the RSA private key
cipher_rsa = PKCS1_OAEP.new(private_key)
plaintext = cipher_rsa.decrypt(ciphertext)

print(plaintext.decode())
