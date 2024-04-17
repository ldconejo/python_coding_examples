import socket

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 8080))

# List for one client at a time
server.listen(1)

n = 1

while 1:
    (client, address) = server.accept()
    request = ""
    while 1:
        # Star pulling one character at a time
        chunk = client.recv(1)

        if chunk:
            request += chunk.decode()

        if request[-4:] == "\r\n\r\n":
            break

    # In HTTP, \r\n are a carriage return and a newline (both are required)
    # The first two lines are the header
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text\r\n"
    # This second carriage return separates the header from the body
    response += "\r\n"
    response += f"You are the {n}th visitor!"

    client.sendall(response.encode())
    # ---------------
    
    client.close()
    print(request)

    n += 1