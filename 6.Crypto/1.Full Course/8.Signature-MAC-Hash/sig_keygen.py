#Generate primes for p and q that are ~150 bits long
#Since n = p*q, n will be ~300 bits long
#We need n to be larger than the size of the 
#  hash we are signing, which is 256 bits.

from Crypto.Util.number import getPrime, GCD, inverse

p = getPrime(150)
q = getPrime(150)
n = p * q

phi = (p - 1) * (q - 1)
#select e, must be < n
e = 65537
d = inverse(e, phi)

print('The public key is\nn = {0}\ne = {1}'.format(n, e))
print('The private key is\nn = {0}\nd = {1}'.format(n, d))
