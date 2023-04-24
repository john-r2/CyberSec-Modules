from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
start_time = time.time()

#import the private key
with open('Bob_private.pem') as fh:
    private_key = RSA.import_key(fh.read())

#import the encrypted message
with open('RSAencrypted.bin', 'rb') as fh:
    ciphertext = fh.read()

chonksize = 256
plaintext = b'' 
# Decrypt the message with the RSA private key
cipher_rsa = PKCS1_OAEP.new(private_key)

for i in range(0, len(ciphertext), chonksize): 
    plaintext += cipher_rsa.decrypt(ciphertext[i:i + chonksize])

with open('RSAdecrypted.docx', 'wb') as fh:
    fh.write(plaintext)

print("--- %s seconds ---" % (time.time() - start_time))