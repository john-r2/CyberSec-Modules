from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
import json, base64

def RSA_AES_encrypt(rcvr_public_key_pem, plaintext):
   #stuff happens
   enc_msg_json = json.dumps(enc_msg_dict)
   return enc_msg_json  

def RSA_AES_decrypt(rcvr_private_pem, enc_msg_json):
   #stuff happens
   message = cipher_aes.decrypt_and_verify(ciphertext, tag)
   return message

#ENCRYPTION
#read Bob's RSA public key
with open('Bob_public.pem') as fh:
    Bob_pub_pem = fh.read()

message = b'I don\'t suppose you\'ve seen anything weird around here?  13th Dr Who'

#encrypt the message, returns JSON with ENCRYPTED session key, nonce, tag, and ciphertext
enc_msg_json = RSA_AES_encrypt(Bob_pub_pem, message)

#this should be the encrypted message as a JSON string
#print(enc_msg_json)

#save the message file
with open('message.json', 'wt') as fh:
    fh.write(enc_msg_json)

#DECRYPTION
#read Bob's RSA private key
with open('Bob_private.pem', 'rt') as fh:
    Bob_priv_pem = fh.read()
#read the message JSON string
with open('message.json', 'rb') as fh:
    enc_msg_json = fh.read()   

#decrypt the message, args are private key and message JSON string
# output is message plaintext
message = RSA_AES_decrypt(Bob_priv_pem, enc_msg_json)
print(message)