from Crypto.PublicKey import RSA

with open(r'D:\CyberSec-Modules\5.Crypto\Cryptography Homework 5a\private.pem') as file_handle:
	privFmFile = file_handle.read()
key = RSA.import_key(privFmFile)

print('N = {0}, p = {1}, q = {2}, e = {3}, d = {4}'.format(key.n, key.p, key.q, key.e, key.d))

