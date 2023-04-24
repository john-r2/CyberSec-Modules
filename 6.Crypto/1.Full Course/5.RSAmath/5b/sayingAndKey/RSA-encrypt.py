from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#  read and import saying RSA public key
with open('saving_public.pem') as fh:
    saying_pub = fh.read()

saying_pub_key = RSA.import_key(saying_pub)

#  read saying
with open('saying.txt', 'rt') as fh:
    plaintext = fh.read().encode()

#  create an RSA cipher (encryption) object using OAEP
cipher_rsa = PKCS1_OAEP.new(saying_pub_key)
#  encrypt the message
ciphertext = cipher_rsa.encrypt(plaintext)
#  save the message in a file
with open('saying.bin', 'wb') as fh:
    fh.write(ciphertext)
