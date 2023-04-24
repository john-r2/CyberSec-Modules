#simpleAESdecode.py

from Crypto.Cipher import AES
import codecs

key = b'Dual hearts rule'

with open(r'D:\CyberSec-Modules\5.Crypto\test stuff\MastersOrder1563.b64') as fh:
    cipherb64 = fh.read()

#cipherb64 = 'TGFj6ocA5LRj7lFX23zZLTJVZwIJ9ecPDeJ3zt98m8gZGlf0gzuHFRYXrqwOD+TdLbbx5GsUhl3m\nLLQBosBVwXGTOMi5PPaj6QkjLgukWAQcKAFRlFTlj00m7dgB2r+KCLF6i6PWrRU5jvHynL5vy1ut\nWCOtu70kG0wRpXIP4DxdJf2vOkrkJzJ5gq+5dim4Lungicy9LhN03v2WNHiz+q8zaEawXBktXQp+\ndw5nYgX3vLBDbKJ4H6bkSzCBvKScYXxBwNVQJFJABnRsBWtArA==\n'

ciphertext = codecs.decode(cipherb64.encode(), 'base64')
aes_obj = AES.new(key, AES.MODE_ECB)
plaintext = aes_obj.decrypt(ciphertext)

print(plaintext)
