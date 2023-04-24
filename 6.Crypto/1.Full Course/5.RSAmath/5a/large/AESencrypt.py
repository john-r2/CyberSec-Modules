from Crypto.Cipher import AES
import time
start_time = time.time()

key = b'thisismykey!1234'

with open('Cryptography Homework 5b--new.docx', 'rb') as fh:
    data = fh.read()

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

with open("AESencrypted.bin", "wb") as file_out:
    for x in (cipher.nonce, tag, ciphertext):
        file_out.write(x)
        
print("--- %s seconds ---" % (time.time() - start_time))