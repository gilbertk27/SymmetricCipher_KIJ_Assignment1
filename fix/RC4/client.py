import socket
from Crypto.Cipher import ARC4

sock = socket.socket()
sock.connect(('127.0.0.1', 8080))
print('Connected to server')
sock.send('Client is connected'.encode())


def enc(key,data):
    		return ARC4.new(key).encrypt(data)

def dec(key,msg):
		return ARC4.new(key).decrypt(msg)

key = ''

data = sock.recv(99999)

while(data):
    
    with open('keygen.key', 'rb') as file:
        key = file.read()
    
    decrypted = dec(key, data)
    dec_file = open("decrypted.txt", "wb")
    dec_file.write(decrypted)
        
    data = sock.recv(99999)

print('File has been received successfully.')

dec_file.close()
sock.close()
print('Connection Closed.')