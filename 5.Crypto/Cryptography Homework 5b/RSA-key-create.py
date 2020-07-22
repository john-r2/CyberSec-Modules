from Crypto.PublicKey import RSA
#generate a key
key = RSA.generate(2048)

#export and save the private key
private_key = key.export_key()
with open('private.pem', 'wb') as file_handle:
    file_handle.write(private_key)

#export and save the public key
public_key = key.publickey().export_key()
with open('public.pem', 'wb') as file_handle:
    file_handle.write(public_key)
