# Title: Web Server Implementation
# Description: This is a simple web server implementation that listens for incoming requests and serves the requested file to the
#    client. The server listens on port 6789 and serves files from the templates directory. If the requested file is not found, 
#    the server sends a 404 Not Found response to the client.
# Authors: Anders Jensen, Mohammed Alshannan
# Version: 1.0 (2-21-2024)

from socket import *
import sys
import os

def webServer(port=6789):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    serverSocket.listen(1)

    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            if not message:
                continue
            filename = message.split()[1]
            filepath = os.path.join("templates", filename[1:])
            f = open(filepath)
            outputdata = f.read()

            # Send HTTP status line and header
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

            # Send the content of the requested file to the client
            connectionSocket.send(outputdata.encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

        except IOError:
            # Send response message for file not found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())
            # Close the client socket
            connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(6789)

