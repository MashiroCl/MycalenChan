import socket
import configparser


def sendMessage(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    config=configparser.ConfigParser()
    config.read('config.ini')
    port = config["DEFAULT"]["PORT"]
    s.connect((host, int(port)))
    s.send(msg.encode('utf-8'))
    s.close()