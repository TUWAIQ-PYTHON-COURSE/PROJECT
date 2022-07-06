from ntpath import join
import string
import random
import file

file.file_name = "user_passwords"

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_chars = list("!@#$%^&*()")
all_chars = alphabets + digits + special_chars
user_passwords = {}

def generate_password():
    try:
        length = int(input("Enter the password length: "))
        name = input("Enter the password name")
        if file.check_key(name):
            print("name is already exist choose another name pls")
            return
        print("Now you need to choose how you want to generate your password")
        alphabets_count = int(input("Enter how many letters you want"))
        digits_count = int(input("Enter how many digits you want"))
        special_char_count = int(input("Enter how many special characters you want"))
    except (ValueError, UnboundLocalError):
        print("Only numbers allowed")

    chars_count = alphabets_count + digits_count + special_char_count

    if chars_count > length:
        print("Characters total count is greater than the password length")
        return
    
    password = []

    for alpha in range(alphabets_count):
        password.append(random.choice(alphabets))

    for digit in range(digits_count):
        password.append(random.choice(digits))
    
    for i in range(special_char_count):
        password.append(random.choice(special_chars))
    random.shuffle(password)
    if chars_count < length:
        random.shuffle(all_chars)
        for char in range(length - chars_count):
            password.append(random.choice(all_chars))
    
    random.shuffle(password)
    try:
        user_passwords[name] = "".join(password)
        file.write_file(name, user_passwords[name])
    except KeyError:
        print("name is already exist choose another name pls ")
        return
    except (FileNotFoundError, FileExistsError):
        print("File not found")
    print("password generated successfully and been saved")
    print("This is your password:")
    print("".join(password))

def get_pass_by_name(name : str) -> str :
    if file.check_key(name):
        return "This is your password: ", file.read_by_key_file(name)
    return "The password you looking for Not found"

number = 0

while number != -1:
    print("choose 1 to generate password")
    print("choose 2 to see your saved passwords")
    print("choose -1 to Exit")
    try:
        number = int(input())
    except ValueError:
        print("You need to enter only numbers")
        continue

    if number == 1:
        generate_password()
    elif number == 2:
        print("If you looking for specific password press 1")
        print("Enter 2 to see all password")
        n = int(input())
        if n == 1:
            name = input("Enter password name ")
            print(get_pass_by_name(name))
        elif n == 2:
            file.read_all_file()
    elif number != -1:
        print("Wrong input pls try again")


        




