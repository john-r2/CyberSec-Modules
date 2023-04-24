from Crypto.PublicKey import RSA

with open(r'D:\CyberSec-Modules\6.Crypto\Cryptography Homework 5a\private.pem') as file_handle:
	privFmFile = file_handle.read()
key = RSA.import_key(privFmFile)

print('N = {0},\n p = {1},\n q = {2},\n e = {3},\n d = {4}'.format(key.n, key.p, key.q, key.e, key.d))
