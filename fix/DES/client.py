import socket
import pyDes

sock = socket.socket()
sock.connect(('127.0.0.1', 8080))
print('Connected to server')
sock.send('Client is connected'.encode())

data = sock.recv(99999)

while(data):

    k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)    
    decrypt = k.decrypt(data)
        
    # Write Decrypted file destination
    file_out = open("decryptedDESCBC.txt", "wb") 
    file_out.write(k.decrypt(data))
    
    data = sock.recv(99999)

print('File has been received successfully.')

file_out.close()
sock.close()
print('Connection Closed.')

