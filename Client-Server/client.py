import time, socket, sys
print('Setup Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = input('Enter name: ')
soc.listen(1) #Try to locate using socket
print('Waiting for incoming connections...')
connection, addr = soc.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
#get a connection from client side
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
print('Press [bye] to leave the chat room')
connection.send(name.encode())
while True:
   message = input('Me > ')
   if message == '[bye]':
      message = 'Good Night...'
      connection.send(message.encode())
      print("\n")
      break
   connection.send(message.encode())
   message = connection.recv(1024)
   message = message.decode()
   print(client_name, '>', message)


# # Python program to implement client side of chat room. 
# import socket 
# import select 
# import sys 

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# if len(sys.argv) != 3: 
# 	print ("Correct usage: script, IP address, port number")
# 	exit() 
# IP_address = str(sys.argv[1]) 
# Port = int(sys.argv[2]) 
# server.connect((IP_address, Port)) 

# while True: 

# 	# maintains a list of possible input streams 
# 	sockets_list = [sys.stdin, server] 

# 	""" There are two possible input situations. Either the 
# 	user wants to give manual input to send to other people, 
# 	or the server is sending a message to be printed on the 
# 	screen. Select returns from sockets_list, the stream that 
# 	is reader for input. So for example, if the server wants 
# 	to send a message, then the if condition will hold true 
# 	below.If the user wants to send a message, the else 
# 	condition will evaluate as true"""
# 	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

# 	for socks in read_sockets: 
# 		if socks == server: 
# 			message = socks.recv(2048) 
# 			print (message) 
# 		else: 
# 			message = sys.stdin.readline() 
# 			server.send(message) 
# 			sys.stdout.write("<You>") 
# 			sys.stdout.write(message) 
# 			sys.stdout.flush() 
# server.close() 
