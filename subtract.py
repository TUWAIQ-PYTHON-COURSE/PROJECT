
def subtracting(num_list):
    sum = num_list[0]
    for index, element in enumerate(num_list):
        if index == 0:
            continue
        sum -= element
    
    return sum