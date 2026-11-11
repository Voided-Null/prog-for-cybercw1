#Init Vals - Main dictionary
userInfo={"uName":"test","ipAddr":"0:0:0:0","evTy":"Basic", "riskLvl":"Low"}

#Maps for the Event Type & Risk Level Options if you were to expand this program - unused 
evType={"B":"Basic","I":"Intermediate", "E":"Expert"}
riskLvl={"L":"Low", "M":"Medium", "H":"High"}

#Display the current dictionary details
def display():
    print(userInfo.keys())
    print(userInfo.values())
    print(userInfo.items())
    print()

#Display Init values
display()

#Add the status field
userInfo.update({"status":"unresolved"})
display()

#Delete the eventType field
del userInfo["evTy"]
display()

#Display all keys
print(len(userInfo.keys()))

#Display the total number of key-value pairs
print(len(userInfo.values()))

#BY B01807021