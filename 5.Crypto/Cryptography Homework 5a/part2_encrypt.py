from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

with open("poem.txt","r") as file_in:
    data = (file_in.read()).encode("utf-8")
# print(data)

with open("student_pub.pem") as file_in:
    recipient_key = RSA.import_key(file_in.read())

recipient_key = RSA.import_key(open("student_pub.pem").read())
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Encrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

with open("poem.bin", "wb") as file_out:
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, \
                                  tag, ciphertext) ]

    
