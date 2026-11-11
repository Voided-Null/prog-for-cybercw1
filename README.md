# prog-for-cybercw1 : cyber-security-utilities 
# BY BIANCA HUGHES - UWS LANARKSHIRE - B01807021
This program is made up of two files; main.py & security-tools.py main.py will run the program and the functions from security-tools.py will be imported into it.
security-tools.py will contain the following functions: 

  -IP CHECKER 
    Gets an IP address from the user input and checks its formatting and values against a set of criteria to see if it matches against a standard IPv4 address, returning a boolean as the result. 
  -PASSWORD VALIDATOR 
    Gets a password attempt from the user. If it doesn't meet the correct criteria, it will tell the user what was incorrect about their attempt and return a boolean value. 
  -PASSWORD GENERATOR 
    Generates a randomized mix of characters to create a strong password based on the criteria to create a password, returning the generated password.

main.py will use these functions to get a valid IP Address and password from the user within conditional loops. If the user doesn't enter a correct password, a strong password will be generated and the user will be offered the option to change it to that option.
