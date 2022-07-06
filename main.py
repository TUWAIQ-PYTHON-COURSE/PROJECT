class Calculator:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    def add(self):
        return self.number_1 + self.number_2
    def sub(self):
        return self.number_1 - self.number_2
    def mul(self):
        return self.number_1 * self.number_2
    def div(self):
        return self.number_1 / self.number_2
    def descision(self, user_descision):
        if user_descision == '+' :
            return self.add()
        elif user_descision == '-':
            return self.sub()
        elif user_descision == '*':
            return self.mul()
        elif user_descision == '/':
            return self.div()

while True:
    user_input = input("inter two number and operation between them:\n")
    user_input = user_input.strip().split(" ")

    user_number_1 = int(user_input[0])
    user_number_2 = int(user_input[2])
    decision = user_input[1]

    calc = Calculator(user_number_1, user_number_2)
    result = calc.descision(decision)
    print(result)

    another_calculation = input("Do you want do another operation?:\n")
    if another_calculation.lower()[0]== 'y':
        continue
    else:
        break