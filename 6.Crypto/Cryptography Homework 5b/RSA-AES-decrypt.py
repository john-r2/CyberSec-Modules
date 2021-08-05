from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES

#import the private key
with open('/home/john/python/private.pem') as fh:
    private_key = RSA.import_key(fh.read())

#import the encrypted message
with open('/home/john/python/encrypted_data.bin', 'rb') as fh:
    enc_session_key, nonce, tag, ciphertext = \
        [fh.read(x) for x in(256, 16, 16, -1)]
    
# Decrypt the session key with the RSA private key
cipher_rsa = PKCS1_OAEP.new(private_key)
AES_session_key = cipher_rsa.decrypt(enc_session_key)

# Decrypt the message with the AES session key, nonce, and tag.
cipher_aes = AES.new(AES_session_key, AES.MODE_EAX, nonce)
message = cipher_aes.decrypt_and_verify(ciphertext, tag)

print(message.decode())
