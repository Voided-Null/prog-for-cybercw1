# prog-for-cybercw1
# BY BIANCA HUGHES - UWS LANARKSHIRE - B01807021 

This repository contains multiple branches, each focusing on separate programs of a similar caliber related to cyber security, such as but not limited to; login, password and IP authentication. All programs were made using python.
As per the coursework requirements. More detail on each branch and their respective program is as below and will also be located in their related branch's read-me file:


#branch 1 : security-tool
  This program has the user firstly create a temporary username and password to be authenticated;
  After which, the user will be presented with options from a security menu that they can use to test different methods of login authentication. The user can do this as many times as they wish
  until they select the exit option or enter "Q" at any point in the program when its receiving user input to force-quit it.

  Security Menu Options:
    -Security Event Counter
       The program will ask for the password 10 times and compare it to the previously user-defined answer. It will keep a record of how many times the password was entered correctly or
       incorrectly, then display an alert message if the percentage of incorrect passwords is more than 50% along with the percentage. 
    -Brute-Force Simulation
      The program will ask for the password, and will compare the result to the previously user-defined answer. It will display a message if the authentication was successful or not, and if the
      latter, continue asking for the correct password until it is received or until the maximum amount of tries have been reached.
    -Login Authentication
      The program will ask for the username and password, and will then compare the result to the 
      previously user-defined answer. Like the brute-force simulator, it will display a message if that answer was correct or will otherwise continue asking until a maximum of 3 login attempts
      have occurred. If that limit is reached, a message will be displayed to the user to tell them that the account has been frozen for 24 hours.
    -Exit
      Stops the program.


#branch 2 : security-event-logger
  This program will first get to use a temporary username and password. Then, the program will
  start a loop that asks the user to enter the previously defined username and password, repeating until the result is correct or until the user force-stops the program by entering "Q" as an
  answer. For each incorrect authentication attempt, an event log will be created and displayed, conveying related information such as; The Event ID, attempted username, IP Address, Event label
  and the Timestamp which the event occurred.


#branch 3 : ip-address-validator
  This program will ask the user for an IP address, check it amongst a set of formatting rules based on IPv4 using an appropriately named function, then tell the user if the result was valid or
  not for the formatting of an IPv4 address.


#branch 4 : security-incident-manager
  This program will use a dictionary to store information regarding a security incident. The dictionary will have 3 initialised starting fields for the following: IP Address, Event Type and Risk
  Level. There will then be following code that will do and display the results of the following:
    -Display the username and IP Address of the security incident
    -Add and display a field called status to the dictionary
    -Update and display the risk level of the security incident
    -remove a field from the dictionary
    -Display all remaining keys and values, then the number of all key-value pairs


#branch 5 : cyber-security-utilities
  This program is made up of two files; main.py & security-tools.py
  main.py will run the program and the functions from security-tools.py will be imported into it.

security-tools.py will contain the following functions:
  -IP CHECKER
    Gets an IP address from the user input and checks its formatting and values against a set of criteria to see if it matches against a standard IPv4 address, returning a boolean as the result.
  -PASSWORD VALIDATOR
    Gets a password attempt from the user. If it doesn't meet the correct criteria, it will tell the user what was incorrect about their attempt and return a boolean value.
  -PASSWORD GENERATOR
    Generates a randomized mix of characters to create a strong password based on the criteria to create a password, returning the generated password.

  main.py will use these functions to get a valid IP Address and password from the user within conditiona loops. If the user doesn't enter a correct password, a strong password will be generated
  and the user will be offered the option to change it to that option.

  
