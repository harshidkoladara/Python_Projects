import time, socket, sys
print('Client Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
print(shost, '({})'.format(ip))
server_host = input('Enter server\'s IP address:')
name = input('Enter Client\'s name: ')
port = 1234
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("Connected...\n")
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print('Enter [bye] to exit.')
while True:
   message = soc.recv(1024)
   message = message.decode()
   print(server_name, ">", message)
   message = input(str("Me > "))
   if message == "[bye]":
      message = "Leaving the Chat room"
      soc.send(message.encode())
      print("\n")
      break
   soc.send(message.encode())

# # Tcp Chat server

# import socket, select

# #Function to broadcast chat messages to all connected clients
# def broadcast_data (sock, message):
# 	#Do not send the message to master socket and the client who has send us the message
# 	for socket in CONNECTION_LIST:
# 		if socket != server_socket and socket != sock :
# 			try :
# 				socket.send(message)
# 			except :
# 				# broken socket connection may be, chat client pressed ctrl+c for example
# 				socket.close()
# 				CONNECTION_LIST.remove(socket)

# if __name__ == "__main__":
	
# 	# List to keep track of socket descriptors
# 	CONNECTION_LIST = []
# 	RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
# 	PORT = 5000
	
# 	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	# this has no effect, why ?
# 	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 	server_socket.bind(("0.0.0.0", PORT))
# 	server_socket.listen(10)

# 	# Add server socket to the list of readable connections
# 	CONNECTION_LIST.append(server_socket)

# 	print ("Chat server started on port " + str(PORT))

# 	while 1:
# 		# Get the list sockets which are ready to be read through select
# 		read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

# 		for sock in read_sockets:
# 			#New connection
# 			if sock == server_socket:
# 				# Handle the case in which there is a new connection recieved through server_socket
# 				sockfd, addr = server_socket.accept()
# 				CONNECTION_LIST.append(sockfd)
# 				print ("Client (%s, %s) connected" % addr)
				
# 				broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)
			
# 			#Some incoming message from a client
# 			else:
# 				# Data recieved from client, process it
# 				try:
# 					#In Windows, sometimes when a TCP program closes abruptly,
# 					# a "Connection reset by peer" exception will be thrown
# 					data = sock.recv(RECV_BUFFER)
# 					if data:
# 						broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)                
				
# 				except:
# 					broadcast_data(sock, "Client (%s, %s) is offline" % addr)
# 					print ("Client (%s, %s) is offline" % addr)
# 					sock.close()
# 					CONNECTION_LIST.remove(sock)
# 					continue
	
# 	server_socket.close()