from Crypto.Util.number import inverse
zstar15 = [1,2,4,7,8,11,13,14]
for x in zstar15:
    row = ''
    for y in zstar15:
        row += str(x*y%15)+'   '
    print(row)
e = 13
phi = 8
d = inverse(e, phi)
print(e,d)
pt = 13
ct = pow(pt,e,15)
print(ct)
print(pow(ct, d, 15))