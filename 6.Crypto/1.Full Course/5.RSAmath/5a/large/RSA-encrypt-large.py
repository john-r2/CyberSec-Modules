from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
start_time = time.time()

#  read and import Bob's RSA public key
with open('Bob_public.pem') as fh:
    Bob_pub = fh.read()

Bob_pub_key = RSA.import_key(Bob_pub)

with open('Cryptography Homework 5b--new.docx', 'rb') as fh:
    message = fh.read()
    
chonksize = 214
ciphertext = b''
#  create an RSA cipher (encryption) object using OAEP
cipher_rsa = PKCS1_OAEP.new(Bob_pub_key)

for i in range(0, len(message), chonksize):
    plaintext = message[i:i + chonksize]
    #  encrypt the message1
    ciphertext += cipher_rsa.encrypt(plaintext)

#  save the message in a file
with open('RSAencrypted.bin', 'wb') as fh:
        fh.write(ciphertext)

print("--- %s seconds ---" % (time.time() - start_time))