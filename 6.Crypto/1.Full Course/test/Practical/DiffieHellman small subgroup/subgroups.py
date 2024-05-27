# this calculates the subgroup that each
# possible value of alpha generates
# It breaks when the subgroup begins to
# repeat to make the subgroup size more
# obvious

p = 41495592889
for alpha in [2679865019]:
    powers = []
    for i in range(1,50):
        x = pow(alpha, i, p)
        if x == 1:
            powers.append(x)
            break            
        else:
            powers.append(x)
    if len(powers) < 16:
        print(alpha, len(powers))