import socket 

BYTES_TO_READ = 4096 

def get(host, port):
    # sends to the server (sent to Google (host))
    request = b"GET / HTTP/1.1\nHost: " + host.encode("utf-8") + b"\n\n"

    # client socket 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)
    result = s.recv(BYTES_TO_READ)

    while(len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)
    
    # data stream is continually sent because of BYTES_TO_READ; if there is more data to be sent (greater than 4096), more data to receive 
    
    s.close()

get("www.google.com", 80)