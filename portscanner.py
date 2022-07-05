
import socket
from mode import vaildate, userChoice

ports_range = (1,65535)
# ports_open = []
# ports_closed = []

# port range 
# 1-1024 basic
# 1-65535

def check_port(mode., isClosed = True):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        for port in ports_range:
            if sock.connect_ex((user_choice, port)):
                print(f"{port} closed")
                
            else:
                print(f"{port} open")
                
    except:
        print("Error")

