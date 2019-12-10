import time, socket, sys


print('Client Server...')
time.sleep(1)

#Get the hostname, IP Address from socket and set Port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
print(shost, '({})'.format(ip))
server_host = input('Enter server\'s IP address:')
name = input('Enter Client\'s name: ')
port = 2222
print(f'Trying to connect to the server: {server_host}, ({port})')
time.sleep(1)

client_socket.connect((server_host, port))
print("Connected...\n")
client_socket.send(name.encode())
server_name = client_socket.recv(1024)
server_name = server_name.decode()
print(f'{server_name} has joined...')
print('Enter bye to exit.')
while True:
   message = client_socket.recv(1024)
   message = message.decode()
   print(server_name, ">", message)
   message = input(str("Me > "))
   if message == "bye":
       message = 'leaving the chat room'
       client_socket.send(message.encode())
       print("\n")
       break
   client_socket.send(message.encode())