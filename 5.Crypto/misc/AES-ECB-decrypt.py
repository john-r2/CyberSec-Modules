from Crypto.Cipher import AES
import codecs

ciphertext = codecs.decode(b'5pY0H0f3NwgqAPgFjhvD0+X7V2ExYhglnLDTxcV0Lz5zrBWvwSuplFt8PR/dSN9TN1PvPSTKYJgYlRHoLVlVzQ==', 'base64')
aes_obj = AES.new(b'This is the key!', AES.MODE_ECB)
plaintext = aes_obj.decrypt(ciphertext)
print(plaintext)
