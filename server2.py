from ipaddress import ip_address
import socket
import sys
import select
 
# creating log file in the currenty directory
# ??getcwd?? get current directory,
# os function, ??path?? to specify path

server_address = ('127.0.0.1', 8080)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

try:
    while True:
        read_ready, write_ready, execption = select.select(input_socket, [], [])
        
        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)
            else:
                data = sock.recv(2048).decode
                filepath = f"test/{data}"
                msg = sock.recv(1024).decode()
                
                print(str(sock.getpeername()), str(data))
                
                #very simple way: open-read-close
                f = open(filepath, 'a+')
                msg = f.write()
                f.close
                
                if (str(msg) == '/n'):
                    sock.close()
                    input_socket.remove(sock)
        
except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)