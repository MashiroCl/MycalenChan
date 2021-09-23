import argparse
import getpass
import json
import subprocess
import requests
import configparser

def sendMessage(msg):
    config=configparser.ConfigParser()
    config.read('config.ini')
    url = config["DEFAULT"]["URL"]
    r=requests.post(url,data=msg)
    print(r)


def commandParser():
    parser = argparse.ArgumentParser(description="This is a script used to let calenChan monitor command status")
    'Required argument command: command need to be required'
    parser.add_argument('command',help="command that calenChan need to monitor")
    args = parser.parse_args()
    return args

def runCommand(command:str):
    print("command",command)
    p=subprocess.Popen(command.split())
    pid = p.pid
    user = getpass.getuser()
    'command start'
    passCommand(user=user,pid=pid,done=False)
    p.wait()
    'command finish'
    passCommand(user=user, pid=pid, done=True)


def passCommand(user:str,pid:str,done:bool):
    dict={"processName":pid,"userName":user,"isTerminated":done}
    'pass info to socket'
    sendMessage(json.dumps(dict))


if __name__=="__main__":
    args = commandParser()
    runCommand(args.command)
