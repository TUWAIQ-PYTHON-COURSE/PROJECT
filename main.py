import time
from project_list import main_list
from add import adding
from subtract import subtracting
from multiply import multiplying
from divide import dividing

class User:
    
    def __init__(self, first_name : str, last_name : str):
        self.first_name = first_name
        self.last_name = last_name
    
    def user_name(self):
        print(f"Your name is: {self.first_name} {self.last_name}")
        
user = User(str(input("Your first name: ")),str(input("Your last name:")))
user.user_name()

num_list = main_list()
print(f"The numbers you entered are: {num_list}")
time.sleep(1)

def menu():
    print("*" * 45)
    print("                 Calculator                 ")
    print("             ------------------             ")
    print(" Please Enter one of the following options: ")
    option =  input("""
 A) Add                                    
 B) Subtract                                    
 C) Multiply                                    
 D) Divide                                    
 E) Exit                                    
 ==> """)

    if option == "A" or option == "a":
        print (f"The answer is: {(adding(num_list))}")
        time.sleep(2)
        menu()
    elif option == "B" or option == "b":
        print(f"The answer is: {(subtracting(num_list))}")
        time.sleep(2)
        menu()
    elif option == "C" or option == "c":
        print(f"The answer is: {(multiplying(num_list))}")
        time.sleep(2)
        menu()
    elif option == "D" or option == "d":
        print(f"The answer is: {(dividing(num_list))}")
        time.sleep(2)
        menu()
    elif option == "E" or option == "e":
        print("Thanks, Goodbye!")
        exit()
    else:
        print("Error!!, You must choose one of the options you have")
        time.sleep(3)
        menu()

menu()