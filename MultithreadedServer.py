# Title: Multithreaded Web Server
# Description: This program is a multithreaded web server that serves files from the templates directory.
#              It listens for incoming connections and creates a new thread to handle each request.
#              It can serve multiple requests simultaneously.
# Authors: Anders Jensen, Mohammed Alshannan
# Version: 1.0 (2-21-2024)



from socket import *
import threading
import sys
import os

def handleClient(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        filepath = os.path.join("templates", filename[1:])
        
        if os.path.isfile(filepath):  # Check if file exists
            with open(filepath, 'r') as f:
                outputdata = f.read()

            # Send HTTP status line and header
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            connectionSocket.send(outputdata.encode())
            connectionSocket.send("\r\n".encode())
        else:
            raise IOError

    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())

    finally:
        connectionSocket.close()

def webServer(port=6789):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", port))
    serverSocket.listen(5)

    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        threading.Thread(target=handleClient, args=(connectionSocket,)).start()

    serverSocket.close()
    sys.exit()  # Terminate the program

webServer(6789)

