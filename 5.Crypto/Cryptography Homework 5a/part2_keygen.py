from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
with open("student_priv.pem", "wb") as file_out:
    file_out.write(private_key)

public_key = key.publickey().export_key()
with open("student_pub.pem", "wb") as file_out:
    file_out.write(public_key)
    
