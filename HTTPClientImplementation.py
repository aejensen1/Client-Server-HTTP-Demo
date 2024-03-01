# Title: HTTP Client Implementation
# Description: This program is an implementation of a simple HTTP client that sends a GET request to a server and receives a response. The program has print statements to display sending and recieving times which when compared between threaded and non-threaded server implementations, will help in understanding the performance differences between the two.
# Authors: Anders Jensen, Mohammed Alshannan
# Version: 1.0 (2-21-2024)


from socket import *
import datetime

def httpClient(serverName='x.x.x.x', serverPort=6789, fileName='HelloWorld.html'):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    request = f"GET /{fileName} HTTP/1.1\r\nHost: {serverName}:{serverPort}\r\n\r\n"
    clientSocket.send(request.encode())

    response = clientSocket.recv(1024)
    print(response.decode())
    clientSocket.close()

if __name__ == "__main__":
    # Test case 1: Request an existing file

    # Printing timestamp before request is sent
    time1 = datetime.datetime.now()
    print("Timestamp before request is sent: ", time1)

    # Sending request
    print("Requesting existing file \"HelloWorld.html\"")
    httpClient(fileName='HelloWorld.html')

    # Printing timestamp after response is received
    time2 = datetime.datetime.now()
    print("Timestamp after response is received: ", time2)

    # Print the total time taken for the request
    print("Total time taken for the request: ", time2 - time1)

    #-------------------------------------

    # Test case 2: Request a non-existing file

    # Printing timestamp before request is sent
    time1 = datetime.datetime.now()
    print("Timestamp before request is sent: ", time1)

    # Sending request
    print("Requesting non-existing file \"NonExistingFile.html\"")
    httpClient(fileName='NonExistingFile.html')

    # Printing timestamp after response is received
    time2 = datetime.datetime.now()
    print("Timestamp after response is received: ", time2)

    # Print the total time taken for the request
    print("Total time taken for the request: ", time2 - time1)

# End of test cases
