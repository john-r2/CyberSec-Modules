from Crypto.Util.number import inverse
Zstar15 = [1, 2, 4, 7, 8, 11, 13, 14]
phi = (3-1)*(5-1)

for el in Zstar15:
    print(el, inverse(el,phi), el * inverse(el,phi)%15)
