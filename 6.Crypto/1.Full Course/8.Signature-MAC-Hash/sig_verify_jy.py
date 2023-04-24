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
public_n = 1418612755020740941619454943732981384388272695744343806657336134211538279197148264322602657
public_e = 65537
signature = 743291100368199649143844765607933583023877122117524882266708566313781699382937248293075228
decrypted_sig = pow(signature, public_e, public_n)
#verify
if decrypted_sig == intHash:
    print('The signature is verified!')
else:
    print('Verification FAILURE!')