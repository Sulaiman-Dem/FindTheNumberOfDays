# (FindTheNumberOfDays)

## Pseudocode

### User Interface =

1. Choose what day of the week they want to use between 0 - 6
2. Input a year they want to do it with
3. Input a month they want
4.

### Code Interface =

##### Functions :

1. A function that gathers the user's input toward what weekday they want to choose, if the input is not a number between 0 - 6 then there is an error prompt and takes user back to menu screen of all days of the week
2. A function that ask for user's year input
3. A function that ask for user's month input
4. A function that loops the program until the user's input equals 'exit'
5. This functions converts the number input of user from the selected month into the corresponding month in letters
6. This functions converts the number input of user from the selected weekday into the corresponding weekday in letters
7. This function uses the weekday input of the user to return the calender day of the corresponding number
8. This functions uses all variables gathered from previous function to find the outcome of the user's input with a for loop

##### Int main () :

1. This must have the while loop to loop all functions of the program with their respected variables

### Issues =

1. I have having problems understanding why the program wouldn't loop properly because it would stop looping and exit the program automatically for two uses.
   Solution: I created a loop function which uses the user's weekInput to determine if the loop should break and exit or continue
2. I was having problem with finding a way for the program to actually find the number of days in a month in "Results" function
   Solution: I found how to use for loops in python because during this time I just starting using python from C++. So for loops were formatted differently. However I found out from online how to set up a for loop then made a loop that adds a 1 every time the specific day comes out in the user's choice of month.
