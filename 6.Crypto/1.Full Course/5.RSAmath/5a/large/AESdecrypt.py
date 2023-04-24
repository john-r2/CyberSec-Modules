from Crypto.Cipher import AES
import time
start_time = time.time()

key = b'thisismykey!1234'

with open('AESencrypted.bin', 'rb') as file_in:
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

with open('AESdecrypted.docx', 'wb') as file_out:
    file_out.write(data)

print("--- %s seconds ---" % (time.time() - start_time))