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
    p=subprocess.Popen(command,shell=True)
    pid = p.pid
    user = getpass.getuser()
    passCommand(user=user,pid=pid,done=False)
    p.wait()
    passCommand(user=user, pid=pid, done=True)

def runCommand2(command:str):
    status,pid=subprocess.Popen(command.split())

def passCommand(user:str,pid:str,done:bool):
    dict={"processName":pid,"userName":user,"done":done}

    'pass info to socket'
    Client.sendMessage(json.dumps(dict))


if __name__=="__main__":
    args = commandParser()

    # try:
    #     command = " "+args.command
    #     print("Monitoring Comand | " + args.command)
    #     if(os.system(command)!=0):
    #         raise Exception
    #
    #     user = getpass.getuser()
    #     pid = os.getpid()
    #     print("user is ",user)
    #     print("pid is ",pid)
    # except TypeError as err:
    #     print("TypeError: {0}, command can not be null, please use -c option".format(err))
    # except:
    #     print("Error when processing command")

    runCommand(args.command)
