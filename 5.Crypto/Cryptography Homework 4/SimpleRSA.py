def gcd(a, b):
    # Return the Greatest Common Divisor of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Return the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # No mod inverse exists if a & m aren't relatively prime.

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # Note that // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

p = 41
q = 67
n = p * q
print('p= ', p, ' ,q = ', q, ', n = ', n)

#compute keys
phi = (p - 1) * (q - 1)
print('phi = ', phi)

#public key is e, choose 7
e = 7
print('e = ', e, ',  gcd(e,phi) = ', gcd(e, phi))

#compute private key, d
d = findModInverse(e, phi)
print('d = ', d)

#now encrypt a number.  I'll choose 2525
plain = 2525

cipher = pow(plain, e, n)

print('plain text integer = ', plain, ', cipher text integer = ', cipher)

#decrypt the cipher text integer with the private key, d
decrypted = pow(cipher, d, n)
print('decrypted ciphertext integer is ', decrypted)
