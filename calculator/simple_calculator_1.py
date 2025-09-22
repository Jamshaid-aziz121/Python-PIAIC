
def read_int(prompt):
    while True:
        try:
         return int(input(prompt))
        except ValueError:
           print('Please enter a valid operator')

x = read_int('enter 1st number  :  ')
operator = input('Enter any sign like + - * /  :  ').strip()
y = read_int('enter 2nd number  :  ')

if operator == '+':
   sum =  x + y
   print(sum)
elif operator == '-':
   minus = x - y
   print(minus)
elif operator == '*':
    multiply = x * y
    print(multiply)
elif operator == '/':
   if y==0:
      print('can not divide by Zero value')
   else:
      divid = x/y
      print(divid)
else:
   print('Operator is invalid')
      