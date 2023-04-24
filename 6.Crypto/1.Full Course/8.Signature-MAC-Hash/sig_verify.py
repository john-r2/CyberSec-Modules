#verify the signature
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
#decrypt the signature
public_n = #copy the n from the public key
public_e = #copy the e from the public key
signature = #copy the signature from your signing script
decrypted_sig = pow(signature, public_e, public_n)
#verify
if decrypted_sig == intHash:
    print('The signature is verified!')
else:
    print('Verification FAILURE!')