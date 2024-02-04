from Crypto.Util.number import isPrime
# generate a list of prime numbers
primes = []
for num in range(200, 7000):
  if isPrime(num):
    primes.append(num)
print('There are {0} primes between 200 and 7000\n'.format(len(primes)))
  
#check to see if (p-1)/2 is a prime so p is "safe"
safe = []

for p in primes:
    if isPrime( int((p-1)/2) ):
        safe.append(p)

print('There are {0} safe prime numbers between 200 and 7000\n'.format(len(safe)))
print(safe)
