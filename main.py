# drawing a flower shape using the module "turtle"
import turtle 

pat = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor("Black")
pat.speed(0)

radius = 60
pat.pensize(2)

colour = ["Red" , "Magenta", "Blue"]

for x in range(12):
    pat.color(colour[x % 2])
    for i in range(6):
        pat.circle(radius)
        pat.right(60)
    radius = radius + 4

turtle.done() 

# the start of the app

userName = input("Enter your name: ")

welcomeMessage = f"WELOCME TO OUR STORE {userName}!" 
print('-' * len(welcomeMessage))
print(welcomeMessage)
print("Happy Eid! Now You Can Buy A Flower For Only 5 Riyals!")

print('-' * len(welcomeMessage))

def viewTotal():
    total= []
    for key, value in shoppingDict.items():
            total.append(value * 5)
    amount_to_pay = sum(total)
    print(f"The Total amount to pay: {amount_to_pay} SAR")



shoppingDict = {}

print("-" * 10, "Flowers Available In Our Store" , "-" * 10)
print("----jasmine----\n----lavender----\n----rose----\n----jory----\n----lilac----\n----sunflower----\n----daisy----\n ")
print("")

print("----your shopping options:----")
print("    |  1: add a flower  |")
print("    | 2: delet a flower |")
print("    |  3: view basket   |")
print("    | 0: exit the store |")

option = int(input("Enter an option:\n"))

while option != 0:
    if option == 1:
        flower_name = input("Enter the flower name you want to add (from the list above):\n")

        if flower_name in shoppingDict:
            print("the flower is already in basket")

            while True:
                try: # in case of entering a string instead of an integer
                    flower_quan = int(input("Enter the amount of flowers:\n"))
                    break
                except ValueError:
                    print("please enter a numeric value!")

            shoppingDict[flower_name] += flower_quan
            
        else:
            while True:
                try:
                    flower_quan = int(input("Enter the amount of flowers:\n"))
                    break
                except ValueError:
                    print("please enter a numeric value!")
            shoppingDict[flower_name] = flower_quan
    elif option == 2:

        while True:
           try: #in case the user enterd a flower name which is not in his/her basket
                flower_name = input("Enter the flower name you want to delete: \n")
                flower_quan = int(input("Enter the amount of flowers you want to delete:\n"))
                shoppingDict[flower_name] -= flower_quan
                break
           except KeyError:
                print("this flower is not in your basket!")
        # if the flower has no quantity in basket , delete the flower from basket
        if shoppingDict[flower_name] == 0:
            del(shoppingDict[flower_name])

    elif option == 3:
        print(f"--------------{userName} shopping basket --------------")
        for key,value in shoppingDict.items():
            print("flower name:", key , "| the qunatity:" , value , "| the price:" , 5*value , "SAR")
        print("--------------------------------------------------------")
        # to view the total
        viewTotal()

    elif option != 0:
        print("Enter a valid number (from the shopping options above) ")

    option = int(input("Enter an option:\n"))

    

    
print("| -----------Thank You------------ | ")
print("|GoodBye, we hope to see you again.|")






