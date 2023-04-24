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
#encrypt the hash
private_n = #copy the number from the key generation output
private_d = #copy the number from the key generation output
signature = pow(intHash, private_d, private_n)

print(signature)