def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Please enter a digit instead of letter')



def calculator(x, operator, y):

    def add(x, y):
        return x + y
    def sub(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divid(x, y):
        return x / y

    if operator == '+':
        return add(x, y)
    elif operator == '-':
        return sub(x, y)
    elif operator == '*':
        return multiply(x, y)
    elif operator == '/':
        if y == 0:
            print('Can not divid any value with Zero')
            return None
        else:
            return divid(x, y)
    else:
        print('Enter a valid operator')
        return None 

x = read_int('Enter 1st integer  :  ')
operator = input('Enter a symbol like + - * /  :   ').strip()
y = read_int('Enter 2nd integer  :  ') 

result = calculator(x, operator, y)

if result is not None:
    print(result)

# result = add(x, y)
# print(result)


