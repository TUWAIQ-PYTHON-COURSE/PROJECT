def login():    
    user =input("👤 Username: ")
    passw =input("🔑 Password: ")

    f = open("users.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
    if (user in us) and (passw in pw):
            print ("✅ Login successful! \n\n")
            return True
    print ("❌ Wrong username/password")
    return False