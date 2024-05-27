from Crypto.Util.number import getPrime, isPrime

#get a random prime
#make sure it is not a safe prime, where
#(p-1)/2 is prime
while True:
    p = getPrime(36)
    if not isPrime((p-1)//2):
        break
print(p)    

#try all g < (p-1)/2
#looking for small subgroups, so only try g^n up to 32
for g in range(2,(p-1)//2):
    tot = g
    for i in range(2,32):
        tot = g * tot % p
        if tot == 1:
            print(g, i)
            break            
        