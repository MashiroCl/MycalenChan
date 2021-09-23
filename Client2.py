import requests
import configparser

def sendMessage(msg):
    config=configparser.ConfigParser()
    config.read('config.ini')
    url = config["DEFAULT"]["URL"]
    r=requests.post(url,data=msg)
    print(r)
