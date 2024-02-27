# Affine Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# this version modified by John York to use GCD and inverse from Pycryptodome to
#   be consistent with the rest of this class.  Key changed to separate variables
#   for multiplication and addition for simplicty.  Checks on
#   GCD(myKeyMult, len(SYMBOLS)) removed to give students a problem to find.

import sys, random
from Crypto.Util.number import GCD, inverse
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
print(len(SYMBOLS))

def main():
    myMessage = 'What a fine mess you have gotten us into!'
    myKeyMult = 19
    myKeyAdd = 33
    myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

    if myMode == 'encrypt':
        translated = encryptMessage(myKeyMult, myKeyAdd, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKeyMult, myKeyAdd, myMessage)
    print('Key Multiplier: %s   Key Addition:  %s' % (myKeyMult, myKeyAdd))
    print('%sed text:' % (myMode.title()))
    print(translated)

  
def encryptMessage(keyMult, keyAdd, message):
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # Encrypt the symbol:
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyMult + keyAdd) % len(SYMBOLS)]
        else:
            ciphertext += symbol # Append the symbol without encrypting.
    return ciphertext


def decryptMessage(keyMult, keyAdd, message):
    plaintext = ''
    modInverseOfkeyMult = inverse(keyMult, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # Decrypt the symbol:
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbolIndex - keyAdd) * modInverseOfkeyMult % len(SYMBOLS)]
        else:
            plaintext += symbol # Append the symbol without decrypting.
    return plaintext


def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if GCD(keyA, len(SYMBOLS)) == 1:
            return keyA, keyB


# If affineCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
