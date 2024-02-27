from Crypto.Util.number import inverse
zstar21 = [1,2,4,5,8,10,11,13,16,17,19,20]
for x in zstar21:
    row = ''
    for y in zstar21:
        row += str(x*y%21)+'\t'
    print(row)
e = 5
phi = 12
d = inverse(e, phi)
print(e,d)
pt = 13
ct = pow(pt,e,21)
print(ct)
print(pow(ct, d, 21))