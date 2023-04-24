# Caesar Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)

# The string to be encrypted/decrypted:
message = 'IWXH XH BN HTRGTI BTHHPVT'

# The encryption/decryption key:
key = 15

# Whether the program encrypts or decrypts:
mode = 'decrypt' # Set to either 'encrypt' or 'decrypt'.

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Stores the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption:
        if mode == 'encrypt':
            translatedIndex = (symbolIndex + key) % len(SYMBOLS)
        elif mode == 'decrypt':
            translatedIndex = (symbolIndex - key) % len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

# Output the translated string:
print(translated)
