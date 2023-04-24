SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
length = len(SYMBOLS)
shift = 3
plaintext = 'CAESARZ'
ciphertext = ''
for letter in plaintext:
    print(letter)
    index = SYMBOLS.find(letter)
    print(index,SYMBOLS[(index + shift)% length])
    ciphertext += SYMBOLS[(index + shift) % length]
print(ciphertext)
