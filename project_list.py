
def main_list():
    num_list = []
    print("Enter your numbers and when you finish enter 00: ")
    while True:
        data = input()
        if data == "00":
            break
        num_list.append(float(data))
    
    return num_list