from random import randrange

main = 'This is just a plain, old, ordinary file and it wont help!'
once = 'This is the file you are looking for!  (cbhash, GrindItUp)'

print(len(main))
print(len(once))

thefile = randrange(100)
print(thefile)

for i in range(100):
    with open(r'D:\CyberSec-Modules\5.Crypto\test stuff\file' + str(i) + '.txt', 'w') as fh:
        if i == thefile:
            fh.write(once)
        else:
            fh.write(main)
        
