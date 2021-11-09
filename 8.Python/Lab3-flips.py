import random

flipcount = 0
for j in range(10000):
    flip = []
    for i in range(100):
        if random.randint(0,1) == 1:
            flip.append('T')
        else:
            flip.append('F')
    flipstr = ''.join(flip)
    if 'TTTTTT' in flipstr:
        flipcount += 1
    elif 'FFFFFF' in flipstr:
        flipcount += 1
        
print(flipcount)
