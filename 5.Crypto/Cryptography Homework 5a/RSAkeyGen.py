from Crypto.PublicKey import RSA
import os

#change from the Python app directory to my home
path = "C:\\Users\\John"
os.chdir(path)

key = RSA.generate(2048)
private_key = key.export_key()
with open("private.pem", "wb") as file_out:
    file_out.write(private_key)

public_key = key.publickey().export_key()
with open("receiver.pem", "wb") as file_out:
    file_out.write(public_key)
