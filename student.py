# My name: Clinton Campbell, My Partner: Naisarg Bhatt

from socket import *
import random
import time

# In this client-server program, the server is the robot and 
# the student is the client 

# connect to the ROBOT TCP Port 3310 and send your 
# BlazerID via the connection established.
#serverName = '25.3.242.102' # Hamachi
serverName = input('Pleaser enter the server IP: ') # clint93 local
blazerid = 'clint93'
HOST = '' # Symbolic name meaning all available interfaces
serverPort = 3310 

def part2():
	# creates the client's socket called s1. 
	# The first parameter again indicates that the underlying network is using IPv4. 
	# The second parameter indicates that the socket is of type SOCK_STREAM, meaning it is a TCP Socket
	# Note: Here I am not specifying the port number of the client socket when creating it; I'm instead letting the
	# operating system do this for me. 
	print("")
	print("Creating the client socket")
	s1 = socket(AF_INET, SOCK_STREAM)

	# before the client can send data to the server or vice versa, using a TCP socket,
	# a TCP connection must first be established between the client and server
	# line 32 initiates the TCP connection between the client and server
	# the first parameter of the connect() method is the address of the server side of the connection 
	# after this line is executed, the three0way handshake is perfomed and the TCP connection is
	# established between the client and server and the second parameter is the server port you 
	# intend to connect to
	print("Connecting to ROBOT on port 3310...")
	s1.connect((serverName, serverPort))
	 # CHECK TO SEE IF THERE'S A WAY TO DO ERROR HANDLING TO ENSURE THAT A CONNECTION WAS MADE
	 # AND PRINT THE STATUS TO THE TERMINAL 

	# sends blazerid string to server/robot after the connection is made in line 34
	blazerid1 = blazerid.encode()
	print("Sending blazerid to ROBOT")
	s1.send(blazerid1)
	print("")
	# Yes, this closes the TCP connection between the client and the server. 
	# When the connection is terminated, it causes TCP in the client to send a TCP 
	# message to the TCP in the server. 
	#clientSocket.close()
	return s1

def part3(s1):
	# when characters arrive from the server, they get placed into the string serverPort2.
	# characters continue to accumulate in serverPort2 until the ilne ends with a carriage return character.
	serverPort2 = int(s1.recv(1024))

	# creates new TCP socket called s_2 using IPv4 and and a TCP connection 
	print("Creating second TCP socket for student 2...")
	s_2 = socket(AF_INET, SOCK_STREAM)
	# here I'm associating/binding the server port number serverPort with this socket
	s_2.bind((HOST, serverPort2))

	# with TCP, s_2 will be our welcoming socket. After establishing this 
	# welcome door, it will wait and listen for some client to "knock on the door"
	# This line has the server listen for TCP connection requests from the client. 
	# The parameter specifies the maximum number of queued connections (at least 5)
	s_2.listen(5)

	print("Done")
	print("\nTCP socket created, ready for listening and accepting connection...")
	s2, address = s_2.accept() # accepts the new TCP connection
	studentIP = address[0]
	print("\nClient from %s at port %d connected" %(studentIP,address[1]))
	print("")
	return s2

def part4(s2):
	# capture the data sent from robot on the new connection 
	UDPConnection1 = s2.recv(2048).decode().split(',') # ffffff,eeeeee

	# code to split UDPC comma delimted string into two different variables of type int
	UDPC1 = list(map(int, UDPConnection1))
	ServerPortfffff = UDPC1[0]
	ServerPorteeeee = UDPC1[1]

	# create a UDP connection using fffff
	# the first parameter in socket() indicates the address family, 
	# where AF_INET indicates that the uderlying network is using IPv4
	# the second parameter indicates that the socket is of type SOCK_DGRAM, 
	# which means it is a UDP socket
	print("creating UDP socket...")
	s3 = socket(AF_INET,SOCK_DGRAM) 

	# variable number 5 < num < 10
	num = str((random.randint(5,9))).encode()

	# sends num to '192.168.1.80' on port fffff
	print("Sending num to port fffff")
	s3.sendto(num,(serverName, ServerPortfffff)) 
	print('sent!')
	print("")

	# when the packet arrives from the internet at the client's socket, 
	# the packet's data is put into the variable 
	# modifiedMessage and the packet's source address is put into the variable serverAddress
	# serverAddress carries both the server's IP address and port number
	# the method recvfrom also takes the buffer size 2048 as input 
	# (this buffer size works for most purposes)
	print('Recieving packets from ROBOT on s3')

	s_3 = socket(AF_INET, SOCK_DGRAM)
	s_3.bind((HOST, ServerPorteeeee))  # binds the port number eeeee to the server's socket
	modifiedMessage, serverAddress = s_3.recvfrom(2048)
	print('Recieved packets from s_3 port eeeee:' + modifiedMessage.decode()) # prints the string recieved from robot on UDP connection s_3
	print("")
	return s3,modifiedMessage,ServerPortfffff
	
def part5(s3,modifiedMessage,ServerPortfffff):
	# code to send the packet 5 times to the server at port fffff
	for i in range(0,5):
	    s3.sendto(modifiedMessage,(serverName, ServerPortfffff)) 
	    time.sleep(1)
	    print("UDP packet %d sent" %(i+1))
	print("Finished")


if __name__ == "__main__": 
	skt1 = part2()
	skt2 = part3(skt1)
	skt3,message,ServerPortfffff = part4(skt2)
	part5(skt3,message,ServerPortfffff)
 
	# CLOSE SOCKETS HERE .close() OR USE WITH STATEMENTS IN FUNCTIONS 
 
	# Yes, this closes the TCP connection between the client and the server. 
	# When the connection is terminated, it causes TCP in the client to send a TCP 
	# message to the TCP in the server. 
	#s1.close()
