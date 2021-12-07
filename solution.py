# import socket module. Found this by clicking on the box in PyCharm. Still need to figure out why this happened.
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("", port))
  #Fill in start. Opens the server to listen for the 1 file.
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  #Fill in start Mofifier in Python to get ready to accept the input  #Fill in end
    try:

      try:
        message = connectionSocket.recv(1024)  #Fill in start  Receive the connection  #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()  #Fill in start  Open a read the helloworld filename   #Fill in end
        
        #Send one HTTP header line into socket.
        #Fill in start based on the same type of results from WireShark labs
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        #print('Here is the 200 OK message')
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        #print('Here is the 404 Not Found message')
        #Fill in end


        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
