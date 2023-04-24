# Dr Who simple AES
from Crypto.Cipher import AES
import codecs

key = b'Dual hearts rule'
plaintext = b'The Master is trapped at the embassy because of COVID lockdown.  Procure four (4) bars of Ghiardelli chocolate, INTENSE DARK, 86% CACAO.  Deliver them to The Master at the embassy.  ( ineptminion, Idiot!7 )xx'

aes_obj = AES.new(key, AES.MODE_ECB)
ciphertext = aes_obj.encrypt(plaintext)
cipherb64 = codecs.encode(ciphertext, 'base64')

print(cipherb64)

with open(r'D:\CyberSec-Modules\5.Crypto\test stuff\MastersOrder1563.b64', 'w') as fh:
    fh.write(cipherb64.decode())
