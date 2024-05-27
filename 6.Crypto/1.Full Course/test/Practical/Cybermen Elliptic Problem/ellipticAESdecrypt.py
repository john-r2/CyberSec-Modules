#ellipticAESdecode.py

from Crypto.Cipher import AES
import codecs

sessionkey = b'17xxxxxxxxxxxxxx'

#with open(r'D:\CyberSec-Modules\5.Crypto\test stuff\Cyberman42.b64') as fh:
#    cipherb64 = fh.read()

cipherb64 = '+7aYffNYPs+qMlBmPs/9x1FJ+7KhmbudPronEdIWtSUPfvLBwIeEDv4QuHqjMaSWRJ+5OP6n9IchOEiM6CoRD84oF8KppHAulvMNrQTsyco='
ciphertext = codecs.decode(cipherb64.encode(), 'base64')
aes_obj = AES.new(sessionkey, AES.MODE_ECB)
plaintext = aes_obj.decrypt(ciphertext)

print(plaintext)
