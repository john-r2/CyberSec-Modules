from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#  read and import Bob's RSA public key
with open('public.pem') as fh:
    pub = fh.read()

pub_key = RSA.import_key(pub)

plaintext = 'This is the message I want to send to Bob'.encode()

#  create an RSA cipher (encryption) object using OAEP
cipher_rsa = PKCS1_OAEP.new(pub_key)
#  encrypt the message
ciphertext = cipher_rsa.encrypt(plaintext)
#  save the message in a file
with open('message_to_bob.bin', 'wb') as fh:
    fh.write(ciphertext)
#  print ciphertext just so we can see it
print(ciphertext)
