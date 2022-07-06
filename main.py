import enum
import requests
import time
import sys
from termcolor import colored
from pyfiglet import Figlet
from enum4dir import dirEnum
import validators as v


# TITLE
custom_fig = Figlet(font="small", width=300)
print(custom_fig.renderText("dirEnumeration"))
print(colored('\n[*] Web Directory Enumeration\n', 'cyan'))
print(colored('[*] works on HTTP protocol only\n', 'cyan'))


try:
    # input validation
    while True:
        try:
            network = input("Enter URL: ")
            
            if network[-1] != "/":
                network += ("/")
            if network[0:7] != "http://":
                network = ("http://") + network
                
            
            try:
                if v.url(network):
                    try:
                        res = requests.get(network)
                        if res.status_code == 200:
                            print("URL: ", colored(network, "green") + "\n")
                            print(colored("connected successfully!\n", "green"))
                            break
                    except:
                        print("Make sure the website uses", colored("HTTP", 'red'), "protocol")
                else:
                    print("URL: ", colored(network, "red") + "\n")
                    print("domain isn't valid. Try again.\n")
                    

            except KeyboardInterrupt:
                print(colored("\n [*] Exiting program...\n", 'red'))
            except TypeError:
                print("Please try again")
            except IndexError:
                print("Out or range error. try again.")
            # except Exception as e:
            #     print(e)
        except ValueError:
            print("Invaild URL. Please try again.")
        # except Exception as e:
        #         print(e)

    # Directory enumeration
    dirEnum(network)


except KeyboardInterrupt:
    print(colored("\n [*] Exiting program...\n", 'red'))
except FileNotFoundError:
    print("Couldn't find the payload file.")