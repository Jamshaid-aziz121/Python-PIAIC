def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Enter a digit value')

num1 = read_int('Enter 1st integer value  :  ')
operator = input('Enter a symbol like + - * /  :  ')
num2 = read_int('Enter 2nd integer value  :  ')


def calculator(x, operator, y):
    if operator == '+':
        result = x + y
    elif operator == '-':
        m = result - y
    elif operator == '*':
        result = x * y
    elif operator == '/':
        if y == 0:
            print('Can not divide by Zero Value')
            result = None
        else:
            result = x / y
    else:
        print('operator is invalid')
        result = None

    if result is not None:
        print(result)

    
calculator(num1, operator, num2)
    