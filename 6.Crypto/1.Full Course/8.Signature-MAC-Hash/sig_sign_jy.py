#create a signature
from Crypto.Hash import SHA256
#read the file
with open('Cryptography Homework 8.docx', 'rb') as fh:
    plaintext = fh.read()
#create the hash
hash_obj = SHA256.new(plaintext)
myHash = hash_obj.hexdigest()
#output of hexdigest is a hex string, change that to an integer
intHash = int(myHash, 16)
print(intHash)
#encrypt the hash
private_n = 1418612755020740941619454943732981384388272695744343806657336134211538279197148264322602657
private_d = 784277237894799667313976708139423249754427212493769364180217246318161237793869757294250529
signature = pow(intHash, private_d, private_n)

print(signature)