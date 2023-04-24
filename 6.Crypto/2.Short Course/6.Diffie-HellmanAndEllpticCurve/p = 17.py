p = 17
for alpha in range(1,16):
    powers = []
    for i in range(1,16):
        x = pow(alpha, i, p)
        if x == 1:
            break
        else powers.append(x)
    print(powers)