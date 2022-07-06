
from sign import sign_in

def welcome():
    print("~"*35)
    print("|         SUMMER TRUCK            |")
    print("|        Ordering System          |")
    print("~"*35)
    print("Welcome to our SUMMER TRUCK SYSTEM ")

def menu():
    print("              [1] Ice cream               ")
    print("              [2] Drinks                  ")
    print("              [3] Snacks                  ")
    print("              [4] Exit                    ")

welcome()
menu()

IceCream =[" chocolate " , " vanilla "," Strawberries"]#we use list
Drinks =[" Water "," Apple Juice "," Orange Juice "," Soda "]
Snacks =[" Sweet "," Fruits "," Salad "]

user_input=int(input("Enter your option:"))


price=0
orders = []
total_amount=[]
amount=0
#function return ice cream order 
def printIce(flavor :str , size :int,quantity : int):
    price=quantity*size*10
    total_amount.append(price)
    return f" {flavor} Ice cream  Price: {price} SR" 

#function return drinks order 
def printDrinks(drink : str , quantity : int):
    if drink=="water" or drink=="Water" :
       price=5*quantity
    else :
        price=10*quantity
    total_amount.append(price)
    return f" {drink} Price: {price} SR" 
#function return snacks order 
def printSnacks(snacks : str ,quantity : int ):
    price=quantity*5
    total_amount.append(price)
    return f" {snacks} Price: {price} SR"

def printList():
    print("-------------------------------------Your order is-------------------------------------")
    for i in orders:
        print(i)
    

     



while user_input !=4:
    
    if user_input==1:
        print(IceCream)
        price=0
        while True:  
            try:
                flavor =input("Enter your favorite flavor:")
                size =int(input("Enter size of your IceCream 1-small PRICE=10SR 2-Large PRICE=20SR:")) 
                quantity = int(input("Enter your quantity :"))
                break
            except ValueError:
                print("error input")

        orders.append(printIce(flavor,size,quantity))
    
    
    elif user_input==2:
        print(Drinks)
        drinks =input("Enter your favorite drinks:")
        quantity = int(input("Enter your quantity :"))
        orders.append(printDrinks(drinks , quantity ))

    elif user_input==3:
        print(Snacks)
        Snacks =input("Enter your favorite Snacks:")
        quantity = int(input("Enter your quantity :"))
        orders.append(printSnacks(Snacks  ,quantity  ))

    else:
        print("Invalid option Enter your option again ")   
    print()
    menu()
    user_input=int(input("Enter your option:"))
printList()
for s in total_amount:
      amount=s+amount
print("-------------------------------------Your informations is-------------------------------------")
print(sign_in("Reema Alameer",1111))
print("Total amount: ", amount ,"SR") 
print("Thanks for using this System ... Goodbye ")


    