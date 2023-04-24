# this calculates the subgroup that each
# possible value of alpha generates
# It breaks when the subgroup begins to
# repeat to make the subgroup size more
# obvious

p = 17
for alpha in range(1,p):
    powers = []
    for i in range(1,p):
        x = pow(alpha, i, p)
        if x == 1:
            powers.append(x)
            break            
        else:
            powers.append(x)
    print(alpha, powers)