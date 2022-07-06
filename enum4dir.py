import requests
import os
from time import sleep
from rich.console import Console

console = Console()

# read payload
try:
    path=os.chdir(str(r"C:\Users\azooz\Documents\python-course\final_project\PROJECT")) #This command changes directory
    # use small.txt or common.txt
    f = open("common.txt", "r")
    payloads = f.read().splitlines()
    
except FileNotFoundError:
    print("The payload file wasn't found. Please try again")

# Directory enumration function
def dirEnum(network):
    try:
        verbose = str(input("Would you like verbose mode? (y/n)"))
        open_dir = []
        open_count = 0

        with console.status("[bold green]Enumerating...") as status:
            for dir in payloads:
                try:
                    dir = payloads[0]
                except:
                    break
                url_mod = str(network) + str(dir)
                res = requests.get(url_mod)
                # sleep(0.25)

                if res.status_code == 200 or res.status_code == 302:
                    console.log(f"[bold green]/{dir} | status: {str(res.status_code)}")
                    open_dir.append(f"{dir} found")
                    open_count += 1
                else:
                    if verbose == "y":
                        console.log(f"[bold red]/{dir} | status: {res.status_code}")

                if len(payloads) > 0:
                    payloads.pop(0)
                

            # Results:
        console.log("\n[bold yellow] Results:")
        console.log(f"[bold yellow] Directories found: {open_count}")
        for i in range(len(open_dir)):
            console.log(f"[bold yellow]/{open_dir[i]}") 
        exit()   

    except KeyboardInterrupt:
        print("\nExiting program...\n")
    except Exception as e:
        print(e)
                    
                        
                
