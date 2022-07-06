




file_name : str = "user_passwords"

def create_file():
    try:
        f = open(file_name+".txt", "x")
        f.close()
    except FileExistsError as e:
       return print(e)
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
            for element in my_list:
                line = my_list[x]
                word = line.split(" ").pop(0)
                x = x + 1
                if key.casefold() == word.casefold():
                    return  line.split(" ").pop(2)
                else:
                    continue
       
        return False

def check_key(key : str) -> bool:
    x : int = int(0)
    my_list = list()
    with open(file_name+".txt", "r") as f:
        my_list = f.readlines()
        for element in my_list:
            line = my_list[x]
            word = line.split(" ").pop(0)
            x = x + 1
            if key.casefold() == word.casefold():
                return True
            else:
                 continue
       
    return False
        