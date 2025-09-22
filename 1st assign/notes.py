# Python Assingnment - 01
# q-1: creat the following variables

name  = "Muhammad Jamshaid Aziz"
age = 27
is_student = True


print(f"My name is: {name}, & age is: {age}  ,  & I m a student : {is_student}")

print(type(name))
print(type(age))
print(type(is_student))

# Q-2: Arithmetic Operations

x = 20
y = 6

add = x + y
sub = x - y
mul = x * y
div = x / y 
mod = x % y
exp = x ** y
floor_div = x // y

print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", mul)  
print("Division: ", div)
print("Modulus: ", mod)
print("Exponentiation: ", exp)
print("Floor Division: ", floor_div)    

# Q-3: Assignment Operators
num = 10

num += 5
print("After += 5: ", num)

num *= 2
print("After *= 2: ", num)

num -= 4
print("After -= 4: ", num)

# Q-4: Comparison Operators

a = 15
b = 12

print(a>b)   # Greater than
print(a<b)   # Less than
print(a==b)  # Equal to
print(a!=b)  # Not equal to
print(a>=b)  # Greater than or equal to
print(a<=b)  # Less than or equal to

# Q-5: Logical Operators

p = True
q = False

print(p and q)  # Logical AND
print(p or q)   # Logical OR    
print(not p)    # Logical NOT
print(not q)    # Logical NOT

# Q-6: Real life example


value_Of_noteBook = 80

required_Total_noteBooks = 7

total_Cost = value_Of_noteBook * required_Total_noteBooks

print("Total Cost of NoteBooks: ", total_Cost)

budget = 600

can_Afford = budget >= total_Cost
print("Can I afford the notebooks? ", can_Afford)


# q-7: OPTIONAL -> Take two number from the used and print thier sum and compare them to each other

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
print("Sum of the two numbers: ", sum)

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

    