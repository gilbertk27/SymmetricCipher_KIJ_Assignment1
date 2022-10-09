from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2

salt = key
password = 'password123' # Password provided by the user, can use input() to get this

key = PBKDF2(password, salt, dkLen=32) # Your key that you can encrypt with

#CBC
output_file = 'encryptedCBC.bin' # Output file
data = b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. N' # Must be a bytes object

cipher = AES.new(key, AES.MODE_CBC) 
st_enc = time.time()
ciphered_data = cipher.encrypt(pad(data, AES.block_size)) 
et_enc = time.time()
elapsed_time_enc = et_enc - st_enc
final_res_enc = elapsed_time_enc * 1000 # milisecond

file_out = open(output_file, "wb") 
file_out.write(cipher.iv)
file_out.write(ciphered_data) 
file_out.close()

print ("Encrypted: %r" % ciphered_data)
print ("Elapsed time (Encrypted): %r ms"  % final_res_enc)