import socket


if __name__ == '__main__':
    hostname = socket.gethostname()
    print(socket.gethostbyname(hostname))
    input()
