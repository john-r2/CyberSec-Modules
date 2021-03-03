# Dr Who simple AES
# See Cybermen Elliptic Curve Procedure.docx for session key derivation
# poor point choice only has shared key x coord of 17 or 127 possibilities
# we'll choose 17

from Crypto.Cipher import AES
import codecs

sessionkey = b'17xxxxxxxxxxxxxx'
plaintext = b'You are now eligible for ascension to Cyberman status (leethaxor, pwneverything)'
aes_obj = AES.new(sessionkey, AES.MODE_ECB)
ciphertext = aes_obj.encrypt(plaintext)
cipherb64 = codecs.encode(ciphertext, 'base64')

print(cipherb64)

with open(r'D:\CyberSec-Modules\5.Crypto\test stuff\Cyberman42.b64', 'w') as fh:
    fh.write(cipherb64.decode())

