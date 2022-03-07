from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES

AES_session_key = get_random_bytes(16)

#read and import Bob's RSA public key
with open('/home/john/python/Bob_public.pem') as fh:
    Bob_pub = fh.read()
Bob_pub_key = RSA.import_key(Bob_pub)

#create an RSA cipher (encryption) object using OAEP
cipher_rsa = PKCS1_OAEP.new(Bob_pub_key)
#encrypt the AES session key
enc_session_key = cipher_rsa.encrypt(AES_session_key)

message = b'I don\'t suppose you\'ve seen anything weird around here?  13th Dr Who'

#create AES object
cipher_aes = AES.new(AES_session_key, AES.MODE_EAX)
#encrypt the message
ciphertext, tag = cipher_aes.encrypt_and_digest(message)

#save the ENCRYPTED session key, nonce, tag, and ciphertext to a file
with open("encrypted_data.bin", "wb") as file_out:
   for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext):
      file_out.write(x)

