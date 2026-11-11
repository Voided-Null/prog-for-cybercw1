#Function
def validate_ip(ip):
    #Removes all empty spaces
    ip = ip.strip()
    #Format checker
    if "." not in ip or ip.count(".") !=3:
        return False

    #Split the IP into segments/parts
    parts=ip.split(".")

    #Iterate each segment
    for part in parts:
        try:
            #Handles edge cases (where the seg ends with a . eg, 192.10.)
            if not part:
                return False
        #checks that each segment contains a number
            num = int(part)
        except ValueError:
            return False

        #checks that each segment is a valid number
        if num <0 or num >255:
            return False
    #If all validation is sucessful, return true
    return True

        
#Input
ip_address=input("Enter an ip address: \n >> ")

#Validate Input
while validate_ip(ip_address) == False:
    ip_address=input("\nInvalid IP. \nEnter an ip address: \n >> ")
print("A valid IP Address has been entered.")

#BY B01807021