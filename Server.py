import socket


def setupSocket():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    'Get Host Name'
    host = socket.gethostname()
    port = 9999
    'Bind Port Number'
    s.bind((host,port))
    "set Max TCP conections"
    s.listen(5)

    while True:
        clientsocket,addr = s.accept()
        msg = clientsocket.recv(2048)
        print(msg.decode('utf-8'))
        clientsocket.close()

if __name__ =="__main__":
    setupSocket()