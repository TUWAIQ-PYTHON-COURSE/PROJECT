
def dividing(num_list):
    sum = num_list[0]
    for index, element in enumerate(num_list):
        if index == 0:
            continue
        try:
            sum /= element
        except ZeroDivisionError:
            print("Division by zero is not allowed.")

    
    return sum