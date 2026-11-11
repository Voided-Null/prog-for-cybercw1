import shutil
import socket
import sys
from datetime import datetime
from random import randint


class EventLogs:
    def __init__(self, EvID="", UsrName="", IPAddr="", FailedLogin="", timestamp=""):
        self.EvID=EvID
        self.UsrName=UsrName
        self.IPAddr=IPAddr
        self.FailedLogin=FailedLogin
        self.timestamp=timestamp


    def view(self):
        if self.FailedLogin==True:
            Msg="Failed login"
        else:
            Msg="Successful login"

        print(f"\nEvent ID: {self.EvID} \n Username: {self.UsrName} \n IP Address: {self.IPAddr} \n Event: {Msg} \n Timestamp: {self.timestamp}")
        print("="*20)

#data dictionary init
data=[]
logs={log.EvID: log for log in data}

#VALIDATION
#User UN Val
def UNval():
    UsrName = get_input("Enter the username: \n >> ")
    #Validation
    while UsrName != testUN:
        UsrName = get_input("That username doesn't exist in the database. \n Enter the username: \n >> ")
    return UsrName

#User Pass Val
def passVal():
    FailedEvent=False
    passwrd = get_input("Enter the password: \n >> ")
    #Validation
    while passwrd != testPass:
        passwrd=get_input("Incorrect. Re-enter the password: \n >> ")
        FailedEvent = True
    return FailedEvent

#Force-Stop
def get_input(prompt):
    stop = input(prompt).strip()
    if stop == "Q":
        print("Force-Stopping the program...")
        br()
        sys.exit()
    return stop

#Neatness
def br():
    w, h = shutil.get_terminal_size()
    for i in range(int(h/3)):
        print("-" * w)


#MAIN FUNCTIONS
#Get IP
def findIP():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        localIP =s.getsockname()[0]
    return localIP

#Event creator
def tryLogin():
    #User Inputs/Funtion Calls
    UsrName = UNval()
    EvRes = passVal()
    EvID=randint(1000, 9999)
    ipAddr=findIP()
    tStamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #Take all of the above information and convert it into a log
    newLog=EventLogs(EvID, UsrName, ipAddr, EvRes, tStamp)
    logs[newLog.EvID]=newLog
    data.append(newLog)


#Init User Inputs
print("-"*25)
testUN = get_input("\nEnter the test username: \n >> ")
testPass = get_input("Enter the test password: \n >> ")
print("-"*25, "\n [Enter 'Q' at any point to quit]\n")

#init Vals
Run = True

#Program
while Run:
    Ans=get_input("Would you like to login? (Y/N) \n >> ")

    #Validation
    if Ans.upper() == "Y":
        tryLogin()
    elif Ans.upper() == "N":
        Run = False
    else:
        print("Enter either Y/N")

#OUTPUT
print("\nSECURITY EVENT LOG:")
print("="*20)
#DISPLAY ALL LOGS
for log in logs.values():
    log.view()

#BY B01807021