#This calculates the order (number of elements) 
#that each value of alpha generates

from Crypto.Util.number import isPrime
p = 67
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
print(order)
if not isPrime(p):
    print("Whoops!! p is not prime!")
if isPrime((p-1)//2):
    print('safe prime')
else:
    print('not a safe prime')