import pyDes
import time

data = b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. N' # Must be a bytes object
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

st_enc = time.time()
d = k.encrypt(data)
et_enc = time.time()
elapsed_time_enc = et_enc - st_enc
final_res_enc = elapsed_time_enc * 1000 # milisecond

enc_file = open("encryptedDESCBC.enc", "wb")
enc_file.write(d)
enc_file.close()

st_dec = time.time()
decrypt = k.decrypt(d)
et_dec = time.time()
elapsed_time_dec = et_dec - st_dec
final_res_dec = elapsed_time_dec * 1000 # milisecond

dec_file = open("decryptedDESCBC.txt", "wb")
dec_file.write(k.decrypt(d))
dec_file.close()

print ("Encrypted: %r" % d)
print ("Decrypted: %r \n" % k.decrypt(d))
print ("Elapsed time (Encrypted): %r ms"  % final_res_enc)
print ("Elapsed time (Decrypted): %r ms" % final_res_dec)