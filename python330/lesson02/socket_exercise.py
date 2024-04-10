import socket

def get_host_info(host_name):
    host_info = socket.getaddrinfo(host_name, 'http')
    ip_address = host_info[0][4][0]
    http_port = host_info[0][4][1]
    return ip_address, http_port

def setup_client(ip_address, http_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    client.connect((ip_address, http_port))
    return client

def is_page_secure(client, host_name):
    msg = "GET / HTTP/1.1\r\n"
    msg += f"Host: {host_name}\r\n\r\n"
    msg = msg.encode('utf8')
    client.sendall(msg)
    host_response = client.recv(1000)
    print(f"{host_response.decode()}")
    if b'HTTP/1.1 301 Moved Permanently' in host_response:
        return True
    return False

if __name__ == "__main__":
    host_name = input("Enter the host name: ")
    ip_address, http_port = get_host_info(host_name)
    client = setup_client(ip_address, http_port)
    if not is_page_secure(client, host_name):
        print(f"WARNING: {host_name} might not be safe!")
    else:
        print(f"{host_name} is already using HTTPS")
    client.close()