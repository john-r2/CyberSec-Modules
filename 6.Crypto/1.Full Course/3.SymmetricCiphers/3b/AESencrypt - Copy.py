from Crypto.Cipher import AES

key = b'thisismykey!1234'
data = b'this is my message and I am not worrying about length'

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

with open("encrypted.bin", "wb") as file_out:
    for x in (cipher.nonce, tag, ciphertext):
        file_out.write(x)