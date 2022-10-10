import socket
import pyDes

sock = socket.socket()
sock.bind(('127.0.0.1', 8080))
sock.listen(2)

while True:
    con, addr = sock.accept()
    print('Connected with ', addr)
    data = con.recv(1024)
    print(data.decode())
    
    file = open("input.txt","rb")
    data = file.read()
    # data = b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. N' # Must be a bytes object
    k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

    d = k.encrypt(data)

    enc_file = open("encryptedDESCBC.enc", "wb")
    enc_file.write(d)
    enc_file.close()
    
    file = open("encryptedDESCBC.enc","rb")
    data = file.read()
    # Keep sending data to the client
    while(data):
        con.send(data)
        data = file.read()
    
    print('File has been transferred successfully.')

    con.close()
    break