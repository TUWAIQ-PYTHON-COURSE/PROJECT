users = {"Hamad" :"123" , "Saad" :"123456"}

def login(username :str,password :str) ->bool:
    if username in users:
        if password == users[username]:
            return True
    
    return False

