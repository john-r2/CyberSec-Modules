#This calculates the order (number of elements) 
#that each value of alpha generates

from Crypto.Util.number import isPrime
p = 337
order = []
for alpha in range(1,p):
    powers = []
    for i in range(1,p):
        x = pow(alpha, i, p)
        if x == 1:
            print(alpha, i)
            if i not in order:
                order.append(i)
            break            

order.sort()
print(('Possible order sizes are:  {0}').format(order))
if not isPrime(p):
    print("Whoops!! p is not prime!")
if isPrime((p-1)//2):
    print(('p = {0} is a safe prime').format(p))
else:
    print(('p = {0} is NOT a safe prime').format(p))