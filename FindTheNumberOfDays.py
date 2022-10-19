import calendar

# A function that gathers the user's input toward what weekday they want to choose, if the input is not a number between 0 - 6 then there is an error prompt and takes user back to menu screen of all days of the week


def GatherWeekDayInput():

    while True:
        try:
            userInput = str(input(
                "\nWhich day of the week do you want to count?\n0: Monday\n1: Tuesday\n2: Wednesday\n3: Thursday\n4: Friday\n5: Saturday\n6: Sunday\nOr 'exit' to quit\n? "))
            if userInput == "exit":
                exit()
            else:
                userWeekDayInput = int(userInput)
                if userWeekDayInput < 0 or userWeekDayInput > 6:
                    raise ValueError
                else:
                    return userWeekDayInput
        except ValueError:
            print("Please only input a number between 0 - 6!")

# A function that ask for user's year input


def GatherYearInput():

    while True:
        try:
            userYearInput = int(input("Enter year: "))
            return userYearInput

        except ValueError:
            print("Sorry, that's not valid input.")
            GatherWeekDayInput()

# A function that ask for user's month input


def GatherMonthInput():

    while True:
        try:
            userMonthInput = int(input("Enter month: "))
            if userMonthInput > 12 or userMonthInput < 1:
                print("ERROR, There can only be 12 months in a year.")
            else:
                return userMonthInput
        except ValueError:
            print("Sorry, that's not valid input.")
            GatherWeekDayInput()

# A function that loops the program until the user's input equals 'exit'


def LoopDecision():
    if userWeekDayInput == "exit":
        return False

# This functions converts the number input of user from the selected month into the corresponding month in letters


def ChangeMonthInput(monthInput):
    if monthInput == 1:
        return "January"
    if monthInput == 2:
        return "February"
    if monthInput == 3:
        return "March"
    if monthInput == 4:
        return "April"
    if monthInput == 5:
        return "May"
    if monthInput == 6:
        return "June"
    if monthInput == 7:
        return "July"
    if monthInput == 8:
        return "August"
    if monthInput == 9:
        return "September"
    if monthInput == 10:
        return "October"
    if monthInput == 11:
        return "November"
    if monthInput == 12:
        return "December"


def ChangeWeekDayInput(weekDayInput):
    if weekDayInput == 0:
        return "Mondays"
    if weekDayInput == 1:
        return "Tuesdays"
    if weekDayInput == 2:
        return "Wednesdays"
    if weekDayInput == 3:
        return "Thursdays"
    if weekDayInput == 4:
        return "Fridays"
    if weekDayInput == 5:
        return "Saturdays"
    if weekDayInput == 6:
        return "Sundays"

# This function uses the weekday input of the user to return the calender day of the corresponding number


def FindWeekDay(weekDayInput):
    if weekDayInput == 0:
        return calendar.MONDAY
    if weekDayInput == 1:
        return calendar.TUESDAY
    if weekDayInput == 2:
        return calendar.WEDNESDAY
    if weekDayInput == 3:
        return calendar.THURSDAY
    if weekDayInput == 4:
        return calendar.FRIDAY
    if weekDayInput == 5:
        return calendar.SATURDAY
    if weekDayInput == 6:
        return calendar.SUNDAY

# This functions uses all variables gathered from previous function to find the outcome of the user's input with a for loop


def Results(weekDaysChange, weekDaysInput, monthChange, monthInput, yearInput):
    weekDays = calendar.monthcalendar(yearInput, monthInput)

    # this adds a one every time a weekday doesn't equal 0, if it equals 0 then thats not the user's choice of weekday
    outcome = sum(1 for x in weekDays if x[weekDaysInput] != 0)

    print("\nThere are", outcome, weekDaysChange, "in the month of",
          monthChange, "and in the year of", yearInput, ".")
    print("-----------")


# This must have the while loop to loop all functions of the program with their respected variables
while (LoopDecision):
    userWeekDayInput = GatherWeekDayInput()

    userYearInput = GatherYearInput()

    userMonthInput = GatherMonthInput()

    monthChange = ChangeMonthInput(userMonthInput)

    weekDayChange = ChangeWeekDayInput(userWeekDayInput)

    findCalenderWeekDay = FindWeekDay(userWeekDayInput)

    Results(weekDayChange, userWeekDayInput,
            monthChange, userMonthInput, userYearInput)
