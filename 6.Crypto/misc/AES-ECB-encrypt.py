from Crypto.Cipher import AES
import codecs
aes_obj = AES.new(b'This is the key!', AES.MODE_ECB)
plaintext = b'Attack at dawn, regardless of the weather.  No excuses! 12345678'
ciphertext = aes_obj.encrypt(plaintext)
b64cipher = codecs.encode(ciphertext, "base64")
print(b64cipher)
