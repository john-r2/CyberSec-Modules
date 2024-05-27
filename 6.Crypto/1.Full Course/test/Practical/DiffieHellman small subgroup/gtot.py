p = 41495592889
g = 2679865019
gtot=1
for i in range(24):
    gtot = gtot * g % p
    print(gtot)
