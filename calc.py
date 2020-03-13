'''
Calcultor v. 0.4
'''

def input_number():
    num = input("Введите число: ")
    try:
        num = float(num)
    except ValueError:
        num = input_number()
    return num

def input_oper():
    oper = input("Операция(*, /, +, -): ")
    return oper

def calc_me(x,y, oper):
    if oper == '*':
        return x * y
    elif oper == '/':
        if y == 0:
            return "ERROR: Divide by zero!"
        else:
            return x / y
    elif oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    else:
        return "ERROR: Uknow operation"

def body():
    number1 = input_number()
    oper = input_oper()
    number2 = input_number()
    result = calc_me(number1,number2, oper)
    print(result)
if __name__ == '__main__':
    body()