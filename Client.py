import socket

def sendMessage(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.connect((host, port))
    s.send(msg.encode('utf-8'))
    s.close()


