from Crypto.Util.number import GCD, inverse

n = 1909
p = 23
q = 83
e = 31

phi = (p-1)*(q-1)
d = inverse(e, phi)
print('Inverse using phi = {0} is {1}'.format(phi, d))

lam = (p-1)*(q-1)//GCD(p-1, q-1)
d = inverse(e, lam)
print('Inverse using lambda = {0} is {1}'.format(lam, d))

m = '1079 1189 1155 137 500 572 1659 128 137 404 42 462 42'.split(' ')
pt = ''
for ct in m:
    ct_int = int(ct)
    pt_int = pow(ct_int, d, n)
    pt_ascii = chr(pt_int)
    pt += pt_ascii
print('The plaintext is {0}'.format(pt))
