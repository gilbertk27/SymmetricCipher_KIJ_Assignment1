import socket
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad

sock = socket.socket()
sock.connect(('127.0.0.1', 8080))
print('Connected to server')
sock.send('Client is connected'.encode())

data = sock.recv(99999)

while(data):
    
    with open('keygen.key', 'rb') as file:
        salt = file.read()
    password = 'password123'
    key = PBKDF2(password, salt, dkLen=32) # Your key that you can encrypt with
    input_file = 'encryptedCBC.bin' # Input file
    file_in = open(input_file, 'rb') 
    iv = file_in.read(16) 
    ciphered_data = file_in.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv) 
    original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) 
    
    # Write Decrypted file destination
    file_out = open("decryptedCBC.txt", "wb") 
    file_out.write(original_data)
    
    data = sock.recv(99999)

print('File has been received successfully.')

file_out.close()
file_in.close()
sock.close()
print('Connection Closed.')