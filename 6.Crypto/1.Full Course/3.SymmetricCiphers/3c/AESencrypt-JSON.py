from Crypto.Cipher import AES
import base64
import json

key = b'thisismykey!1234'
data = b'this is my message and I am not worrying about length'

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

# JSON only uses strings, so use BASE64 encoding
#  b64.encode outputs bytes, so use .decode() to convert to string
nonce_b64 = base64.b64encode(cipher.nonce).decode()
ciphertext_b64 = base64.b64encode(ciphertext).decode()
tag_b64 = base64.b64encode(tag).decode()

# Put our data in a Python dictionary and print (print optional)
message = {"nonce" : nonce_b64, "tag" : tag_b64, "ciphertext" : ciphertext_b64}
print(message)

# Print what our data looks like as a JSON string (optional)
#  notice we use the dumps ('s' at the end) method because we want string output
#  notice that the dict and JSON are the same for simple data
print(json.dumps(message))

# save message to a file
#  notice we use the dump method (no 's') because output to file
with open("encrypted.json", "wt") as file_out:
    json.dump(message, file_out)