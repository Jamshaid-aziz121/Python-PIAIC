def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Please enter an integer value / digit')

    
num1 = read_int('Enter 1st number  :  ')
operator = input('Enter a sign like + - * /  :  ').strip()
num2 = read_int('Enter 2nd number  :  ')


def calculator(x, operator, y):
    if operator == '+':
     return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x*y
    elif operator == '/':
        if y == 0:
            print('You can not divid by Zero Value')
        else:
            return x/y
    else:
        print('You entered invalid sign')    

result = calculator(num1,operator,num2)
print(result)
