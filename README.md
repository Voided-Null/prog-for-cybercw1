# prog-for-cybercw1 : security-tool
# BY BIANCA HUGHES - UWS LANARKSHIRE - B01807021 

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
