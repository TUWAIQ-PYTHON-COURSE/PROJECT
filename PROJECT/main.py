from CalendarsDates import *
from signin import login
from ToDo import *


print("\t\t---------------------")
print("\t\t\tHello!")
print("\t\t   Welcome to 'DO ☑' ")
TodayDate()
print("\t\t---------------------")


while True:
    isLoggedIn = login()
    if isLoggedIn:
        menu()
    else:
        user_choice = input("🔁 'Enter' to continue or 'x' to exit")
        print("-------------------------------")
        if user_choice == "x":
            break