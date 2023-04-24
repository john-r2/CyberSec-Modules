from Crypto.Util.number import inverse
n = 591
e = 157
c = '290 279 275 141 247 290 557 374 141 582 255 227 291'.split(' ')

#factors of 591 are 3 and 197
p = 3
q = 197
phi = (p-1)*(q-1)
d = inverse(e, phi)

print('n = ', n)
print('e = ', e)
print('c, the ciphertext, is:')
print(c)
print('p = ',p, 'q = ', q)
print('phi = ', phi)
print('d = ', d)
print('Solving the first letter using chr(pow(290, d, n)) ', chr(pow(290, d, n)) )
print('Solving the entire thing with a loop:')
flag = ''
for ciphertext in c:
    flag += chr(pow(int(ciphertext), d, n))
print(flag)
