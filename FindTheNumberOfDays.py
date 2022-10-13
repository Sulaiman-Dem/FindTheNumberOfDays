# Program that will be able to count the number of days of a specific weekday for a specific year and month

# Menu for days list, ask for year, ask for month, need to error check user

import calendar


def GatherWeekDayInput():

    while True:
        try:
            userInput = str(input(
                "Which day of the week do you want to count?\n0: Monday\n1: Tuesday\n2: Wednesday\n3: Thursday\n4: Friday\n5: Saturday\n6: Sunday\nOr 'exit' to quit\n? "))
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


def GatherYearInput():

    while True:
        try:
            userYearInput = int(input("Enter year: "))
            return userYearInput

        except ValueError:
            print("Sorry, that's not valid input.")
            GatherWeekDayInput()


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


def LoopDecision():
    if userWeekDayInput == "exit":
        return False


while (LoopDecision):
    userWeekDayInput = GatherWeekDayInput()

    userYearInput = GatherYearInput()

    userMonthInput = GatherMonthInput()
