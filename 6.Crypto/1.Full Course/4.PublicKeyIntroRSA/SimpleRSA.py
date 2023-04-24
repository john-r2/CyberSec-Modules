from Crypto.Util.number import GCD, inverse

p = 131
q = 157
n = p * q
print('p= ', p, ' ,q = ', q, ', n = ', n)

#compute keys
phi = (p - 1) * (q - 1)
print('phi = ', phi)

#public key is e, choose 7
e = 7
print('e = ', e, ',  gcd(e,phi) = ', GCD(e, phi))

#compute private key, d
d = inverse(e, phi)
print('d = ', d)

#now encrypt a number.  I'll choose 2525
plain = 2525

cipher = pow(plain, e, n)

print('plain text integer = ', plain, ', cipher text integer = ', cipher)

#decrypt the cipher text integer with the private key, d
decrypted = pow(cipher, d, n)
print('decrypted ciphertext integer is ', decrypted)
