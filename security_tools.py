import random
import secrets
import string


#IP CHECKER
def val_ip(ip):
    #Removes all empty spaces
    ip = ip.strip()
    #Format checker 
    if "." not in ip or (ip.count(".") !=3 or ip.count(".")>4):
        return False

    parts=ip.split(".")

    #Iterate each section/part
    for part in parts:
        try:
            #Handles edge cases (where the section ends with a "." eg, 192.10.)
            if not part:
                return False
        #checks that each section contains a number
            num = int(part)
        except ValueError:
            return False

        #checks that each section is a valid number
        if num <0 or num >255:
            return False
    #If all validation is sucessful, return true
    return True

#------------------------------------------------------#

#PASSWORD VALIDATION
def pswrdVal(pswrd):

    #Get the length of the password and ensure that it is atleast 10 characters long
    passlen = len(pswrd)
    while passlen < 10:
        pswrd=input("Your password must be atleast 10 characters long. \n >> ")
        passlen = len(pswrd)

    #Init Vals
    nums=0
    numsInRange = True
    uCase = False
    lCase = False
    symsNum = 0

    #Loop for each character
    for i in range(passlen):
        char = pswrd[i]

        #Get the information from the password
        if char.isdigit() == True:
            if int(char) <0 or int(char) >255:
                numsInRange = False
            nums += 1
        elif char.isupper() == True:
            uCase = True
        elif char.islower() == True:
            lCase = True
        else:
            symsNum += 1

    #Tell the user what needs to be changed
    if nums <2 or numsInRange==False:
        print("Your password must contain atleast four digits between 0 and 255")
    if uCase == False:
        print("Your password must contain a uppercase character")
    if lCase == False:
        print("Your password must contain a lowercase character")
    if symsNum<1:
        print("Your password must contain a special character.")

    #Checks if the password meets the specifications
    if nums<2 or uCase==False or lCase==False or symsNum==0:
        result = False
    else: 
        result = True
    return result

#------------------------------------------------------#


#PASSWORD GENERATOR
#'true' random
orig_randint = random.randint
def trueRand(a, b):
    #ensures that you're not trying to gen an impossible number
    low, high = min(a, b), max(a, b)
    #uses a module called 'secrets' to make the generated values more unique via the use of encryption
    return secrets.randbelow(high - low + 1) + low
random.randint=trueRand

#password generating function
def genPass():
    #initial variables
    pswrd=""
    passLength=0
    passLength=random.randint(10, 16)

    reqDigits=string.digits
    reqUC=string.ascii_uppercase
    reqLC=string.ascii_lowercase
    reqSpecial="!@#$%^&*()-_=+"

    #generate the minimum required characters
    reqChars=[*(secrets.choice(reqDigits) for i in range(4)), secrets.choice(reqUC), secrets.choice(reqLC), secrets.choice(reqSpecial)]
    allChars = reqDigits+reqUC+reqLC+reqSpecial
    #generate the rest of the password, added to the reqChars list
    reqChars.extend(secrets.choice(allChars) for i in range(passLength-len(reqChars)))
    #randomize the order of the characters in the password
    secrets.SystemRandom().shuffle(reqChars)
    #store the answer as a string
    pswrd=pswrd.join(reqChars)

    return pswrd

#BY B01807021