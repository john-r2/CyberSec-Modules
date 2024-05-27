from Crypto.Cipher import AES
from base64 import b64decode

messageb64 = b'I7w5ncyw96zmSAFfZJ8y+lfQGMJQI/i6YxvwFLuCMAEKVfMx8q/si9nyMNUNALhoyVbNZ+xMfYTIgmFAriSMC4gDBVKCYBBEFGnhGFQw1Bm5UYC9GFsq8qHfFzAUCsgp'
ciphertext = b64decode(messageb64)

aes_obj = AES.new(b'22670xxxxxxxxxxx', AES.MODE_ECB)
plaintext = aes_obj.decrypt(ciphertext)
print(plaintext)