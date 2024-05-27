p = 41495592889
g = 2679865019

pubkey = 4520452219
tmp = 1
for privkey in range(1,100):
    tmp = g * tmp % p
    if tmp == pubkey:
        print(privkey)
