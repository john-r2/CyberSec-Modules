from Crypto.PublicKey import RSA

with open(r'D:\CyberSec-Modules\5.Crypto\Cryptography Homework 5a\private.pem') as file_handle:
	privFmFile = file_handle.read()
key = RSA.import_key(privFmFile)
print('print(key) just prints the memory address of the key object***')
print(key)

print('\n***this prints the properties of the key, manually***')
print('N = {0}, p = {1}, q = {2}, e = {3}, d = {4}'.format(key.n, key.p, key.q, key.e, key.d))

print("\nI don't think print(key.publickey) should work, but it prints all the key's properties")
print(key.publickey)
