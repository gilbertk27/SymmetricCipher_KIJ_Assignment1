# FIXED POL RC4
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256
from Crypto import Random

def enc(key,data):
		return ARC4.new(key).encrypt(data)

def dec(key,msg):
		return ARC4.new(key).decrypt(msg)

def main():
  key = ''
  data = ''
  with open('keygen.key', 'rb') as file:
    key = file.read()    
    with open('input2.txt', 'rb') as file: 
      data = file.read()

      encrypted = enc(key,data)
      enc_file = open("encrypted.enc", "wb")
      enc_file.write(encrypted)
      # print(encrypted)

      decrypted = dec(key,encrypted)
      enc_file = open("decrypted.txt", "wb")
      enc_file.write(decrypted)

if __name__=='__main__':
  main()