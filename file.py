




file_name : str = "user_passwords"

def create_file():
    try:
        f = open(file_name+".txt", "x")
        f.close()
    except FileExistsError:
       # print("the file is already created no need to create again")
       return
def write_file(name : str, value : str):
    create_file()
    # Open the file in append & read mode ('a+')
    with open(file_name+".txt", "a+") as f:
        # Move read cursor to the start of file.
        f.seek(0)
        # If file is not empty then append '\n'
        data = f.read(100)
        if len(data) > 0 :
            f.write("\n")
        # Append text at the end of file
        f.write(name + " -> "+ value)

    f.close()


def read_all_file():
    try:
        f = open(file_name+".txt", "rt")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("File not found!!")

def read_by_key_file(key : str):
        x : int = int(0)
        my_list = list()
        with open(file_name+".txt", "r") as f:
            my_list = f.readlines()
            #print(my_list)
            for element in my_list:
                line = my_list[x]
                #print(line.split(" ").pop(0))
                word = line.split(" ").pop(0)
                #print(word)
                #print(key)
                x = x + 1
                if key.casefold() == word.casefold():
                    return  line.split(" ").pop(2)
                else:
                    continue
            # for i in f.readlines():
            #     f.seek(0)
                #word = f.readlines()[0].split(" ").pop(0)
                
                # word = line. split(' '). pop(0)
                #print(word)
                # if word == key:
                #     return True
                # else:
                #     return False
        
        return False

def check_key(key : str) -> bool:
    x : int = int(0)
    my_list = list()
    with open(file_name+".txt", "r") as f:
        my_list = f.readlines()
        #print(my_list)
        for element in my_list:
            line = my_list[x]
          #  print(line.split(" ").pop(0))
            word = line.split(" ").pop(0)
           # print(word)
            #print(key)
            x = x + 1
            if key.casefold() == word.casefold():
                return True
            else:
                 continue
        # for i in f.readlines():
        #     f.seek(0)
            #word = f.readlines()[0].split(" ").pop(0)
            
            # word = line. split(' '). pop(0)
            #print(word)
            # if word == key:
            #     return True
            # else:
            #     return False
    
    return False
        
        
# print(check_key("gmail"))

# f = open("user_passwords.txt", "r")
# print(f.readlines()[0])
# x = f.readlines()
# print(x)
# if f.readlines().__eq__("k"):
#     print("True")

# word2 = "hashem"
# word1 = "Hashem"
# if word2.casefold() == word1.casefold():
#     print("equal")

# print(read_by_key_file("spotify"))

# i = int(
