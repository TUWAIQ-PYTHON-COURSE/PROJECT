from datetime import date
import calendar

def myCalendar():
    
    yy = int(input("* Enter year: "))
    mm= int(input("* Enter month: "))
    print()
    print("********************")
    print(calendar.month(yy,mm))
    print("********************")
    
def TodayDate():
    today = date.today()
    print("\t\t     ", today)