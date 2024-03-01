# Client-Server-HTTP-Demo
Authors: Anders Jensen, Mohammed Alshannan
Date: 2/21/2024

Description:
This was a team project for Computer Networks class demonstrates a connection between server and client over HTTP with and without multithreading.

---------------------------

Instructions:
We decided to use python in the client and server code as well as a remote server created via Droplet. The server python code was run on the server and Client code run on the local host. The port used on the server ended up being 6789, but this can be changed to any available port. As a disclaimer, the droplet is now disabled and destroyed so any attempts to connect to that IP address will fail. Make sure to chage the server IP address, which is currently set to "x.x.x.x" in the client python code. The html, which must also be on ther server, is a simple file with a HelloWorld header.

---------------------------

The main goals of this project were to demonstrate the following:

Part1: ‘HelloWorld.html’ is the name of the file you placed in the server directory. The browser should then display the contents of HelloWorld.html. Then try to get a file that is not present at the server. You should get a “404 Not Found” message.

Part 2:
Instead of using a browser, write your own HTTP client to test your server. Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output. You can assume that the HTTP request sent is a GET method.

Part 3:
Implement a multithreaded server that is capable of serving multiple requests simultaneously. Using threading, first create a main thread in which your server listens for clients at a fixed port. When it receives a TCP connection request from a client, it will set up the TCP connection through another port and services the client request in a separate thread. There will be a separate TCP connection in a separate thread for each request/response pair.
