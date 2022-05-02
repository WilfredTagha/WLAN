#import socket
# import sys
# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("socket succesfully created")
# except socket.error as err:
#     print(f"scoket creation failed with error")
#
#
# port = 80
#
# try:
#     host_ip = socket.gethostbyname('www.github.com')
# except socket.gaierror:
#     print("There is and error resolving the host")
#     sys.exit()
#
# s.connect((host_ip, port))
# print(f"socket has succesfully connecte d to github on port {host_ip} ")

# import socket
# import time
#
# s = socket.socket()
# print('Socet succesfully created')
# port = 56789
# s.bind(('', port))
# print(f'soket binded to prot {port}')
# s.listen(5)
# print("Socket is listening")
# while True:
#
#     c, addr = s.accept()
#     print('Got connection from', addr)
#     message = ('Thank you for connecting')
#     c.send(message.encode())
#     c.close()

import  threading
import socket

host ='127.0.0.1'
port = 65000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            client.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)



def recieve():
    while True:
        print('server is runnin and listening ...')
        client, address = server.accept()
        print(f'Connection is established whith {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('you are connect'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    recieve()