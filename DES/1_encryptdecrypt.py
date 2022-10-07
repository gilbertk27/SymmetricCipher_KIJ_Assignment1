# DES prerequisite
# ! pip install pyDES

import pyDes

data = "DES Algorithm Implementation"
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)

enc_file = open("encryptedDESCBC.enc", "wb")
enc_file.write(d)
enc_file.close()

dec_file = open("decryptedDESCBC.enc", "wb")
dec_file.write(k.decrypt(d))
dec_file.close()

print ("Encrypted: %r" % d)
print ("Decrypted: %r" % k.decrypt(d))