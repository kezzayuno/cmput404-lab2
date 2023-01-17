# cmput404-lab2

Assignment: https://uofa-cmput404.github.io/lab-2-tcp-proxy.html

Question 1: How do you specify a TCP socket in Python?

```python
import socket 
s = socket.socket(socket.ATF_INET, socket.SOCK_STREAM)
```

or 

```python
import socket 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    ...
```

Question 2: What is the difference between a client socket and a server socket in Python?

The difference is how we use the sockets. The client socket sends data that the user wants from the server socket, the server socket receives requests from the client socket and sends back what has been requested or notifies the client that the request was denied. Also need to specify the HOST and PORT for the server but not for the client. Client socket sends requests while Server socket receives / listens for requests and tries to satisfies the request.

Question 3: How do we instruct the OS to let us reuse the same bind port?

In order for us the reuse the same bind port: specify the socket using ```setsockopt```. 

```python
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

In particular, ```socket.SO_REUSEADD``` allows us to reuse the same bind port. 

Question 4: What information do we get about incoming connections?

When we accept client on server side, we get the connection and the address from the client. 

```python
...
conn, addr = s.accept() 
```

Question 5: What is returned by recv() from the server after it is done sending the HTTP request?

recv() sends the HTTP status of the request being made and other attributes such as Date and Expires, etc. The accompanying attributes that are sent are based on what the request asked for. For example, it could be a GET request, and if success (status code 200), the HTML will be displayed with b'' (bytes). However, with BYTES_TO_READ, it may need to send parts of what the request asked for if the data is too big to send (greater than BYTES_TO_READ).  

Question 6: Provide a link to your code on GitHub.

https://github.com/kezzayuno/cmput404-lab2
https://github.com/kezzayuno/cmput404-lab2.git

# Multithreading 

To handle multiple programs / multiple connections at a time. 

Able to connect to multiple clients at the same time. 