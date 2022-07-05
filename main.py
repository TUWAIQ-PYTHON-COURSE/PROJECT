import sys
from mode import userChoice
import portscanner

# manual = f'''
#        This program helps you with your penetration testing processes
#        ___________________________________________________________________

#        [*] Usage: python3 {sys.argv[0]} options ip_address

#        Options:
#        -h/-help     Display help message and exit
#        -Ps          Port Scanning mode
#        -Ns          Network Scanning mode
#        -De          Directory enumeration mode
#        -Se          Subdomain enumeration mode
       
# '''

# print(manual)

# First
userChoice(input())

portscanner.check_port()
