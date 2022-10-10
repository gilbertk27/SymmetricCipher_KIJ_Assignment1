import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import PBKDF2

#CBC
input_file = 'encryptedCBC.bin' # Input file

with open('keygen.key', 'rb') as file:
        salt = file.read()

password = 'password123' # Password provided by the user, can use input() to get this

key = PBKDF2(password, salt, dkLen=32) # Your key that you can encrypt with

# Read the data from the file
file_in = open(input_file, 'rb') 
iv = file_in.read(16) 
ciphered_data = file_in.read()
file_in.close()

cipher = AES.new(key, AES.MODE_CBC, iv=iv) 
st_dec = time.time()
original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) 
et_dec = time.time()
elapsed_time_dec = et_dec - st_dec
final_res_dec = elapsed_time_dec * 1000 # milisecond

file_out = open("decryptedCBC.txt", "wb") 
file_out.write(original_data)
file_out.close()

print ("Decrypted: %r" % original_data)
print ("Elapsed time (Decrypted): %r ms"  % final_res_dec)