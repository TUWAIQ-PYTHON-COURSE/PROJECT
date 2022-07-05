print ("The complexs")
list_complexes = ["\n1. The zone", "\n2. U walk" , "\n3. Riyadh front"]
string_complexs = ' '.join(list_complexes)
print (string_complexs)

def restaurant():
    try:
        c = int(input ("Where are you going ?"))
        if c == 1:
            list_thezone = ["\n1. Logma" , "\n2. Le vert" ,"\n3. Also" , "\n4. Zoe" ]
            string_thezone = ' '.join(list_thezone)
            print (string_thezone)
        r = int (input ("Choose the restaurant:"))
        if r == 3:
            list_also = ["\n1. sunday 11AM - 2PM ", "\n2. monday 9AM- 11PM", "\n3. tuesday 8AM - 10AM" , "\n4. wednesday 10AM - 1PM"]
            string_also = ' '.join(list_also)
            print (string_also)

        t = int (input ("Choose the time:"))
        if t == 2:
            list_people = ["\n1. 2 people" , "\n2. 3 people" , "\n3. 4 people" , "\n4. 5 people "]
            string_people =  ' '.join(list_people)
            print(string_people)

        p = int(input ("How many people ?"))
        if p == 4:
            print("Request accepted, Thank you")

        else:
            print("The complexs is not found")
            restaurant()
    except:
        print("try agin")
        restaurant()



restaurant()

    


