
import socket
import validators as v
from ipaddress import ip_address


# choices and modes
switcher_choice = {0:"ip address", 1:"URL"}
switcher_mode = {0:"Port Scanner", 1: "Subdomain enumeration mode"}

def userMode(user_mode:int):
    user_mode = int(input('''
        [*] Enter 0 for Port scanning mode
        [*] Enter 1 for Subdomain Enumeration mode
        ''')) 
    while True:
        try:
            if user_mode not in switcher_mode:
                print("Your input isn't vaild. Please try again.")
            else:
                user_mode = switcher_mode[user_mode]
                print(f"    [*] Current mode: {user_mode}")
                print("\n")
                return user_mode
        except Exception as e:
            print(e)

def userChoice(user_choice:int):
    while True:
        try:
            user_choice = int(input('''
        [*] Enter 0 for ip
        [*] Enter 1 for URL
    
        [*]: '''))
            if user_choice in switcher_choice:
                user_choice = switcher_choice[user_choice]
                print(f"        [*] Current mode: {user_choice}")
                print("\n")
                return user_choice
                break
            else:
                print("Your input isn't vaild. Please try again.")
        
        except Exception as e:
            print(e)



def vaildate(user_input):

    # Vaildate the ip address
    while True:
        try:
            ip = ip_address(input("Enter an ip address: "))
            pass
        except:
            print("The ip address isn't vaild. Please try again.")
        else:
            print(f"Scanning {ip} for open ports...")
            break

    # Vaildate the URL
    while True:
        try:
            url = v.url(input("Enter a URL: "))
            if not url:
                print("The URL isn't vaild. Please try again.")
            else:
                print(f"Scanning {url} for open ports...")
                break
        except Exception as e:
            print(e)