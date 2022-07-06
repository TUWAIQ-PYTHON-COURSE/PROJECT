from CalendarsDates import *
from CalendarsDates import *
from signin import login


def monthGoals():
    print("""

    -* 🎯 YOUR GOALS FOR THIS MONTH *- 
     *****************************
     ▫ Drink more water
     ▫ Meditate
     ▫ Exercise 3x a week
     ▫ Read more
     ▫ Learn a new programming langauge
     *****************************

    """)

def showMenu():
        print ("""
\t\t  ____ M E N U ____
\t\t   1.Calendar
\t\t   2.Show my goals
\t\t   3.Add tasks
\t\t   4.View tasks
\t\t   5.Delete all tasks
\t\t   6.Log out
\t\t  _________________
        """)


tasksList= []
def addTasks():
    allTasks = "     ☑ "
    print()
    print()
    print("-* 📝 TO DO:  [Enter 'Space' to end the list.] *-")
    while True:
         tasks = str(input("- "))
         allTasks +=tasks+"\n     ☑ "
         if tasks == ' ':
             break
    print("-* ✅ The tasks added successful! *-")
    tasksList.append(allTasks)

def clearTasks():
    del tasksList[:]
    print()
    print(" -* ✨YOUR LIST IS EMPTY✨ *-")

def viewTasks():
    Thetaks = tasksList
    print()
    print()
    print("     -* 🗒 YOUR TASKS FOR TODAY *- ")
    print("     ***************************")
    print('\n'.join([i for i in Thetaks[:]]))
    print("     ***************************")

def menu():
    while True:
        showMenu()
        try:
            choice = int(input(" What would you like to do? "))
            if choice == 1:
                myCalendar()
            elif choice == 2:
                monthGoals()
            elif choice == 3:
                addTasks()
            elif choice == 4:
                 viewTasks()
            elif choice == 5:
              clearTasks()
            elif choice == 6:
               print()
               print("**************************************************")
               print("  **********************************************")
               print("    -*-*-*-* Thank you, see you soon! *-*-*-*- ")
               print("  **********************************************")
               print("**************************************************")
               print()
               break
            else:
                print(f'Not a correct choice: <{choice}>, try again!')
        except ValueError:
            print("Try")