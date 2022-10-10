from Crypto.Cipher import ARC4

def enc(key,data):
		return ARC4.new(key).encrypt(data)

def dec(key,msg):
		return ARC4.new(key).decrypt(msg)

key = ''
data = b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. N' # Must be a bytes object
with open('keygen.key', 'rb') as file:
  key = file.read()
# with open('input2.txt', 'rb') as file: 
  # data = file.read()

st_enc = time.time()
encrypted = enc(key,data)
et_enc = time.time()
elapsed_time_enc = et_enc - st_enc
final_res_enc = elapsed_time_enc * 1000 # milisecond
enc_file = open("encrypted.enc", "wb")
enc_file.write(encrypted)
print ("Encrypted: %r" % encrypted)
print ("Elapsed time (Encrypted): %r ms \n"  % final_res_enc)

st_dec = time.time()
decrypted = dec(key,encrypted)
et_dec = time.time()
elapsed_time_dec = et_dec - st_dec
final_res_dec = elapsed_time_dec * 1000 # milisecond
dec_file = open("decrypted.txt", "wb")
dec_file.write(decrypted)
print ("Decrypted: %r" % decrypted)
print ("Elapsed time (Decrypted): %r ms"  % final_res_dec)
