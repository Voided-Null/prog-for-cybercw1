import security_tools


#Validation
def validateAnswer():
    #Get User Input
    print("Use the suggested password? (Enter Y/N)")
    Check=input(">> ")
    #Makes sure the answer is either 'Y' or 'N'
    while Check.upper() not in ["Y", "N"]:
        print("You must enter either Y/N")
        Check=input(">> ")
    print()

    #Output the result
    if Check.upper() == "Y":
        Output = True
    else:
        Output = False
    return Output

#IP
ipAddr=input("Enter an IP address: \n >> ")
while security_tools.val_ip(ipAddr) == False:
    ipAddr=input("Invalid IP Address. \nEnter a valid IP address: \n >> ")

#PASSSWORD
#Input
pswrd=input("Enter a password: \n >> ")
suggestion=security_tools.genPass()
#Validation
while security_tools.pswrdVal(pswrd) == False:
    print("\nYour password doesn't meet the requirements.")
    if validateAnswer() == True:
       pswrd=suggestion
       print("Password set to:", suggestion)
    else:
        pswrd=input("Enter a password: \n >> ")
    
#BY B01807021