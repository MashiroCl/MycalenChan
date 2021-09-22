import argparse
import getpass
import os
import json
import Client
import subprocess

def commandParser():
    parser = argparse.ArgumentParser(description="This is a script used to let calenChan monitor command status")
    parser.add_argument('-c', '--command', help="command that calenChan need to monitor")
    args = parser.parse_args()
    return args

def runCommand(command:str):
    print("command",command)
    p=subprocess.Popen(command.split())
    pid = p.pid
    user = getpass.getuser()
    passCommand(user=user,pid=pid,done=False)
    p.wait()
    passCommand(user=user, pid=pid, done=True)


def passCommand(user:str,pid:str,done:bool):
    dict={"processName":pid,"userName":user,"done":done}

    'pass info to socket'
    Client.sendMessage(json.dumps(dict))


if __name__=="__main__":
    args = commandParser()
    runCommand(args.command)
