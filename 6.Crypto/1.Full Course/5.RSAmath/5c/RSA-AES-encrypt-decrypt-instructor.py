from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
import json, base64

def RSA_AES_encrypt(rcvr_public_key_pem, plaintext):
   #create the AES session key
   AES_session_key = get_random_bytes(16)
   #import pem key into RSA
   rcvr_public_key = RSA.import_key(rcvr_public_key_pem)
   #create an RSA cipher (encryption) object using OAEP
   cipher_rsa = PKCS1_OAEP.new(rcvr_public_key)
   #encrypt the AES session key
   enc_session_key = cipher_rsa.encrypt(AES_session_key)

   #create AES object
   cipher_aes = AES.new(AES_session_key, AES.MODE_EAX)
   #encrypt the message with the UNENCRYPTED session key
   ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)

   #put ENCRYPTED session key, nonce, tag, and ciphertext in a JSON string
   enc_msg_dict = {
      "encrypted_session_key" : base64.b64encode(enc_session_key).decode(),
      "nonce" : base64.b64encode(cipher_aes.nonce).decode(),
      "tag" : base64.b64encode(tag).decode(),
      "ciphertext": base64.b64encode(ciphertext).decode()
   }
   enc_msg_json = json.dumps(enc_msg_dict)
   return enc_msg_json  

def RSA_AES_decrypt(rcvr_private_pem, enc_msg_json):
   #import key into RSA from pem
   rcvr_priv_key = RSA.import_key(rcvr_private_pem)
   # Read the data from JSON into a dict
   message = json.loads(enc_msg_json)
   encrypted_session_key = base64.b64decode(message["encrypted_session_key"].encode())
   nonce = base64.b64decode(message["nonce"].encode())
   tag = base64.b64decode(message["tag"].encode())
   ciphertext = base64.b64decode(message["ciphertext"].encode())

   # Decrypt the session key with the RSA private key
   cipher_rsa = PKCS1_OAEP.new(rcvr_priv_key)
   AES_session_key = cipher_rsa.decrypt(encrypted_session_key)

   # Decrypt the message with the AES session key, nonce, and tag.
   cipher_aes = AES.new(AES_session_key, AES.MODE_EAX, nonce)
   message = cipher_aes.decrypt_and_verify(ciphertext, tag)
   return message

'''
#ENCRYPTION
#read Bob's RSA public key
with open('instructor_pub.pem') as fh:
    Bob_pub_pem = fh.read()
with open('poem.txt', 'rt') as fh:
    message = fh.read().encode()

#encrypt the message, returns JSON with ENCRYPTED session key, nonce, tag, and ciphertext
enc_msg_json = RSA_AES_encrypt(Bob_pub_pem, message)

#this should be the encrypted message as a JSON string
print(enc_msg_json)

#save the message file
with open('poem.json', 'wt') as fh:
    fh.write(enc_msg_json)
'''
    
#DECRYPTION
#read Bob's RSA private key
with open('instructor_priv.pem', 'rt') as fh:
    Bob_priv_pem = fh.read()
#read the message JSON string
with open('poem.json', 'rb') as fh:
    enc_msg_json = fh.read()   

#decrypt the message, args are private key and message JSON string
# output is message plaintext
message = RSA_AES_decrypt(Bob_priv_pem, enc_msg_json)
print(message.decode())