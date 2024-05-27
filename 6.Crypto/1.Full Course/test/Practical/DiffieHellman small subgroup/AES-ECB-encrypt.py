from Crypto.Cipher import AES
from base64 import b64encode

aes_obj = AES.new(b'22670xxxxxxxxxxx', AES.MODE_ECB)
plaintext = b'Send all possible cybermen to attack the Doctor and her companions.  No delay!!!'
ciphertext = aes_obj.encrypt(plaintext)
print(ciphertext.hex())
print(b64encode(ciphertext))