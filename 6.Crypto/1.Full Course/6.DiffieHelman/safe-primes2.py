#Uses the isPrime function from PyCryptodome

from Crypto.Util.number import isPrime

# check numbers starting at 99 to see if they are prime
# only odd numbers can be prime, so use range(99, 6999, 2)
# stopping at  7000 will get about 900 primes 
primes = [x for x in range(99, 7000, 2) if isPrime(x)]
print('There are {0} primes between 99 and 6999'.format(len(primes)))

#check to see if (p-1)/2 is a prime so p is "safe"
safe = []
unsafe = 0
for p in primes:
    if isPrime( int((p-1)/2) ):
        safe.append(p)
    else:
        unsafe += 1
print('There are {0} "unsafe" primes'.format(unsafe))
print('Some safe primes are:')
print(safe)
