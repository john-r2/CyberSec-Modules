SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
length = len(SYMBOLS)
mult = ''
multiplier = int(input('multiplier?  '))
for index in range(26):
    mult += SYMBOLS[multiplier * index % length]
print(SYMBOLS)
print(mult)
    
