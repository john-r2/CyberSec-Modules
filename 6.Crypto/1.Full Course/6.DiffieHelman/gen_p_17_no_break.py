#Simple script to show the subgroup that each
#value of alpha will generate

p = 17

for alpha in range(1,p):
    powers = [pow(alpha, i, p) for i in range(1,p)]    
    print(alpha, powers)