from random import  randrange
from products import *
from users import *

storeg = [product("CPU intel i5",1200,"with 3.10 of speed ",5),product("GTX650",2000,"From GIGIABYTE 6G Graphics Card",4),product("Razer Mouse",600,"6400 DPL and Optical sensor",9),product("HyperX keyboard",750,"Mechanical keyboard with RGB LED",12)]

orders_list = []
def add_new_prodect(p_name :str,p_price :int,p_des :str,quantity :int):
    item = product(p_name,p_price,p_des,quantity)
    storeg.append(item)
    return True
def get_prodect_name(id :int):
    for j in storeg:
        if id == j.p_id:
            return j.p_name
def get_prodect_price(id :int):
    for j in storeg:
        if id == j.p_id:
            return j.p_price
def get_prodect_des(id :int):
    for j in storeg:
        if id == j.p_id:
            return j.p_des

print("--Welcome to Hamad tec Shop--")
print("we have all what you need for your computer -_-")
#Home screen 
while True:
    print("_______________________Main menu_______________________")
    print("1- To browsing the shop")
    print("2- To product management(Need permission) ")
    print("3- view your shopping cart and Continue to checkout")
    print("X- To close the app")
    choice = input()
    print("_________________________________________________________")
    #Choice one will be for the customers to Brows the shop
    if choice == '1':
        print("_______________________Prodects menu_______________________")
        print("Product ID:     Product name:       Price:       description:")
        for i in storeg:
                i.info()
        print("___________________________________________________________")
        while True : 
            print("if you end your orders prees x")
            buy = input("What you want to buy(Enter the id)->")
            if buy == 'x':
                break
            orders_list.append(int(buy))
        



    #Choice two will be for managements and needs to login
    elif choice == '2':
        u = input("Enter the username: ")
        p = input("Enter your password: ")
        if(login(u,p)):
            print("Welcome mr ",u)
            while True:
                print("_______________________manager menu_______________________")
                print("1-To veiw the storeg statue")
                print("2-To add new product")
                print("x:To back to main menu")
                print("___________________________________________________________")
                ch = input()
                if ch == '1':
                    print("Product ID:     Product name:       Price:       description:        quantity:")
                    for i in storeg:
                        i.manager_info()
                    x = input("Press any key to back ->")
                        
                elif ch== '2':
                    newPName = input("Enter the product name->")
                    newP_price = input("Enter the product price->")
                    newPDes = input("Enter the product des ->")
                    try:
                        quantity = input("Enter the quantity ->")
                        add_new_prodect(newPName,int(newP_price),newPDes,int(quantity))
                    except ValueError:
                        print("you must use integer number!!!")

                    

                elif ch == 'x' or 'X':
                    break
        else:
            print("The username or password is wrong!!!")
    #Choice three will be to view the cart
    elif choice == '3':
        while True:
            if orders_list:
                sum = 0
                for i in orders_list:
                    print(f"{get_prodect_name(i)}      {get_prodect_price(i)}      {get_prodect_des(i)}")
                    sum = sum +get_prodect_price(i)
                print("___________________________________________________________")
                print(f"The Sum is {sum} RS"   )
                    
                x = input("Prise c to countinue and x to back -> ")
                if x == 'c':
                    print("_______________________customer register_______________________")
                    name = input("Enter your name ->")
                    phone = input("Enter your phone ->")
                    addr = input("Enter your addres ->")
                    order_num = randrange(1,500)
                    print("Thank you for your order >   your order number is: ",order_num)
                    orders_list.clear()
                    exit()
                elif x == 'x':
                    break
            else:
                print("The shopping cart is empty !!!!!")
                print("prise x to back to main menu")
                back = input()
                if back == 'x':
                    break
    elif choice == '9' or 'X':
        break
    else:
        print("Error you didn't choice the right option")
    




