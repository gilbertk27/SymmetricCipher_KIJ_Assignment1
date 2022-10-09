import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

sock = socket.socket()
sock.connect(('127.0.0.1', 8080))
print('Connected to server')
sock.send('Client is connected'.encode())

data = sock.recv(99999)

while(data):
    input_file = 'encryptedAESCBC.enc' # Input file
    file_in = open(input_file, 'rb') 
    iv = file_in.read(16) 
    ciphered_data = file_in.read()
    
    with open('keygen.key', 'rb') as file:
        key = file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv) 
    original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) 
    
    # Write Decrypted file destination
    file_out = open("decryptedAESCBC.txt", "wb") 
    file_out.write(original_data)
    
    data = sock.recv(99999)

print('File has been received successfully.')

file_out.close()
file_in.close()
sock.close()
print('Connection Closed.')