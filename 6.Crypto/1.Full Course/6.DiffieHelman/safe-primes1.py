#Uses the isPrime function from PyCryptodome

from Crypto.Util.number import isPrime

# check numbers starting at 99 to see if they are prime
# only odd numbers can be prime, so use range(99, 6999, 2)
# stopping at  7000 will get about 900 primes 
safe = [x for x in range(3, 6999, 2) if isPrime(x) and isPrime((x - 1) // 2)]

print('Some safe primes are:')
print(safe)
