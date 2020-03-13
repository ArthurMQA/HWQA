'''
Calcultor v. 0.1
'''

def input_number():
    num = input("Введите число: ")
    return num

def input_oper():
    oper = input("Операция('*','/', '+', '-'): ")
    return oper

def calc_me(x,y, oper):
    if oper == '*':
        return x * y
    elif oper == '/':
        return x / y
    elif oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    else:
        return "Wrong operation"
