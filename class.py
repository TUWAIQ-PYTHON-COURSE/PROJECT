#creating a basic class (blueprint)

from turtle import color
from unicodedata import name


class Car:
    
    #initializer Attribute
    def __init__(self, name : str, color : str, Model: str, price : int):
        self.name = name #property / Attribute
        self.color = color
        self.Model = Model
        self.price = price
       

    
    def __repr__(self) -> str:
        return f"{self.name}  {self.Model}  {self.color}" 




#creating instances/objects from Car
car1 = Car("Toyota", "black", "Corola", 72000 )      # create variable and orginzing them in order : name , color , model and price 
car2 = Car("Toyota", "white", "Hilux", 90000)        # create variable and orginzing them in order : name , color , model and price 
car3 = Car("Toyota", "red", "Camry", 1200000)        # create variable and orginzing them in order : name , color , model and price 
car_Toyota_list = [car1 ,car2 ,car3]                 # create a list for car company 
print(car_Toyota_list)                               # print out the list as programmer wants to show for user 

car4 = Car("Honda", "black", "Civic", 80000)
car5 = Car("Honda", "blue", "Accord", 110000)
car6 = Car("Honda", "red", "Pilot", 1270000)
car_Honda_list = [car4 ,car5 ,car6]
print(car_Honda_list)

while True:                                            # cheick if the condition True 
    choice = input("Enter your car brand name: ")      # Ask user to pick brand name 
    if choice == "Toyota" :                            # if user chose Toyota 
        print("Cars in Toyota: ")                      # print out Toyota brand
        for car in car_Toyota_list:                    # use for loop and varivel to espisifc 
            print(car.Model)                           # use for loop to set value from list for example model
            
            
        choice = input ("Enter your car modele: ")     # let user enter the car model
        if choice == "Corola" or "Hilux" or "Camry" :   # if the choise was one of the cars model it will go for next step
           print("what is your favorite color: ")       # ask user to pick car color
           for car in car_Toyota_list:                  # use for loop to set value from list for example color 
            print(car.color)                            # print out the car colors for user 

        choice = input(" the price will show after picking color: " )
        if choice == "black":
           print("The price is: ")
           print("Toyota","Corola","black color", "Price is:",car1.price,"SR")
        elif choice == "white":
           print("The price is: ")
           print("Toyota","Hilux","white color", "Price is:",car2.price,"SR")
        elif choice == "red":
            print("The price is: ")
            print("Toyota","Camry","red color","Prise is:",car3.price,"SR")
            
            
            

    elif choice == "Honda":
        print("Cars in Honda: ")
        for car in car_Honda_list:
          print(car.Model)

        choice = input ("Enter your car modele: ")
        if choice == "Civic" or "Accord" or "Pilot" :
           print("what is your favorite color: ")
           for car in car_Honda_list:
            print(car.color)

        choice = input(" the price will show after picking color: " )
        if choice == "black":
           print("The price is: ")
           print("Honda","Civic", "black color","Price is:",car4.price,"SR")
        elif choice == "blue":
           print("The price is: ")
           print("Honda","Accord","blue color","Price is:",car5.price,"SR")
        elif choice == "red":
            print("The price is: ")
            print("Honda","Pilot","blue color","Prise is:",car6.price,"SR")


    elif choice == "exit":             # to get of of the loop 
        break







