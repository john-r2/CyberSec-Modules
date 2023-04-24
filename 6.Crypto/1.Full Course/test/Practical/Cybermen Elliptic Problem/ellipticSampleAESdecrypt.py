#ellipticAESdecode.py

from Crypto.Cipher import AES
import codecs

sessionkey = b'192xxxxxxxxxxxxx'

with open(r'D:\CyberSec-Modules\5.Crypto\test stuff\Cyberman42.b64') as fh:
    cipherb64 = fh.read()

cipherb64 = '5ONHPLXu8wPGNibvCq+uI9zUw+oIkBSvMHVdBwY1DOUT8KLuTg6mta0rzcedKZEGbTTkdfZgLZen\n0K2uUGkbAPGgSF2aMa4uk1z4DY08jPg=\n'

ciphertext = codecs.decode(cipherb64.encode(), 'base64')
aes_obj = AES.new(sessionkey, AES.MODE_ECB)
plaintext = aes_obj.decrypt(ciphertext)

print(plaintext)
