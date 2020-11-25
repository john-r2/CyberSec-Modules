# Caesar Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)


# The string to be encrypted/decrypted:
message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

# The encryption/decryption key:
key = 13

# Whether the program encrypts or decrypts:
mode = 'decrypt' # Set to either 'encrypt' or 'decrypt'.

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

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
