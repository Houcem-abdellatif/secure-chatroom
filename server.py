import time, socket, sys


print('Setup Server...')
time.sleep(1)

#Get the hostname, IP Address from socket and set Port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 2222

server_socket.bind((host_name, port))
print(f'{host_name}, {ip}')

name = input('Enter name: ')
server_socket.listen(1) #Try to locate using socket
print('Waiting for incoming connections...')
connection, addr = server_socket.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))

#get a connection from client side
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
print('Press bye to leave the chat room')
connection.send(name.encode())
while True:
   message = input('Me > ')
   if message == 'bye':
       message = 'leaving chat room'
       connection.send(message.encode()) 
       print("\n")
       break
   connection.send(message.encode())
   message = connection.recv(1024)
   message = message.decode()
   print(client_name, '>', message)
