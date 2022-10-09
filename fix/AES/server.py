import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


sock = socket.socket()
sock.bind(('127.0.0.1', 8080))
sock.listen(2)

while True:
    con, addr = sock.accept()
    print('Connected with ', addr)
    data = con.recv(1024)
    print(data.decode())
    
    key = get_random_bytes(32) # 32 bytes * 8 = 256 bits (1 byte = 8 bits)
    print(key)

    # Save the key to a file
    file_out = open("keygen.key", "wb") # wb = write bytes
    file_out.write(key)
    file_out.close()
    
    salt = key
    password = 'password123'
    key = PBKDF2(password, salt, dkLen=32)  
    output_file = 'encryptedCBC.bin' # Encrypted file
    data = b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. N' # Must be a bytes object

    
    cipher = AES.new(key, AES.MODE_CBC) 
    ciphered_data = cipher.encrypt(pad(data, AES.block_size)) 
    file_out = open("encyrptedAESCBC.enc", "wb") 
    file_out.write(cipher.iv)
    file_out.write(ciphered_data) 
    file_out.close()
    
    file = open("encyrptedAESCBC.enc","rb")
    data = file.read()
    # Keep sending data to the client
    while(data):
        con.send(data)
        data = file.read()
    
    print('File has been transferred successfully.')

    con.close()
    break