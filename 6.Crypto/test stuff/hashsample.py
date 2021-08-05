import hashlib
import os

os.chdir(r'D:\CyberSec-Modules\5.Crypto\test stuff')

with open('file97.txt') as fh:
    content = fh.read().encode()
myhash = hashlib.md5(content).hexdigest()
print(myhash)
