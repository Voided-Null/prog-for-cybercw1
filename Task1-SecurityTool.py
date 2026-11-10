import shutil
import sys


#FUNCTIONS - VAL/MISC
#Confirm input
def valAns():
    #input
    print("Was the prior answer correct? (Enter Y/N)")
    Check=get_input(">> ")

    #validation
    while Check.upper() not in["Y", "N"]:
        print("You must enter either Y/N")
        Check=get_input(">> ")

    #output result
    if Check.upper() == "Y":
        Output = True
    else:
        Output = False
    return Output

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


#FUNCTIONS - MAIN
#Security Event Counter
def EvCounter(origPass):
    #init
    totalFails=0

    #Get the password 10 times from the user
    for i in range(10):
        #Get input and validate
        pswrd=get_input("\nEnter the password: \n >>")
        while valAns() == False:
            pswrd=get_input("Enter the password: \n >>")

        #Calc the incorrect percentage
        if pswrd!=origPass:
            print("Incorrect Password received")
            totalFails+=1
            percentage=(totalFails/10)*100
        
        #Alert Suspiscous activity
        if percentage >= 50:
            print(f"{percentage}%")
            print("ALERT: Suspiscous Activity Detected")
            


#Brute-Force Simulation
def BruteForce(origPass):
    #init Vals
    maxTries=10
    idx=1

    #Get initial input and validation
    pswrd=get_input("\nEnter the password: \n >>")
    while valAns() == False:
                pswrd=get_input("Enter the password: \n >>")

    #loop until
    while pswrd!=origPass and idx<=maxTries:
        #Attempts Left
        print(f"Incorrect. \nTries Left: {maxTries-idx}")
        idx+=1

        #input and val
        pswrd=get_input("\nEnter the password: \n >>")
        while valAns() == False:
            pswrd=get_input("Enter the password: \n >>")

    #Output
    if pswrd==origPass:
        print("\n Access Granted.")
    else:
        print("\n Access Denied.")
        
            

#Login Authentication
def LoginAuth(origUN, origPass):
    #init Vals
    check=False
    idx=0

    #Get initial input and validation
    #Username
    un=get_input("\nEnter the username: \n >>")
    while valAns() == False:
        un=get_input("\nEnter the username: \n >>")

    #Password
    pswrd=get_input("\nEnter the password: \n >>")
    while valAns() == False:
        pswrd=get_input("Enter the password: \n >>")

    #Initial Check
    if un==origUN and pswrd==origPass:
        check=True
    else:
        #For a max attempt of 3 times
        while check == False and idx<2:
            print(f"Incorrect. \nTries Left: {3-idx}")
            idx+=1

            #Username
            un=get_input("\nEnter the username: \n >>")
            while valAns() == False:
                un=get_input("\nEnter the username: \n >>")
        
            #Password
            pswrd=get_input("\nEnter the password: \n >>")
            while valAns() == False:
                pswrd=get_input("Enter the password: \n >>")

            if un==origUN and pswrd==origPass:
                check=True

    if check==False:
        print("\n Access Denied. The account has been frozen for 24 hours.")
    else:
        print("\n Access Granted.")


#SECURITY MENU
def options():
    print("\nChoose one of the following options: \n 1. Security Event Counter \n 2. Brute-Force Simulation \n 3. Login Authentication \n 4. to Exit \n[Input 'Q' at any point to force-stop the program]")


#PROGRAM
#Initial Variables
Run=True

#Test UN & Val
initUN=get_input("Enter the test username \n >>")
while valAns() == False:
    initUN=get_input("Enter the test username \n >>")

#Test Pass & Val
initPass=get_input("Enter the test password \n >>")
while valAns() == False:
    initPass=get_input("Enter the test password \n >>")

#Run Loop
while Run:
    #Display the Security Menu Options
    options()

    #Get an option from the user
    Ans=get_input(" >>")
    #Validation
    while valAns()==False or Ans not in {"1","2","3","4"}:
        print("Your answer must be an integer.")
        options()
        Ans=get_input(" >>")

    #Use the corresponding function to use the users choice of security tool
    if Ans == "4":
        print("Thank you for using the security tool.")
        Run=False
    elif Ans == "1":
        EvCounter(initPass)
    elif Ans == "2":
        BruteForce(initPass)
    else:
        LoginAuth(initUN, initPass)

    #BY B01807021