# INPUT AND OUTPUT IN PYTHON

# ---------------- OUTPUT ----------------

# print() is used to display output on the screen
print("Hello World")

# Printing numbers
print(100)

# Printing variables
name = "Abhishek"
print(name)

# Printing multiple values
age = 19
print(name, age)

# ---------------- INPUT ----------------

# input() is used to take input from the user
name = input("Enter your name: ")

# Displaying the entered input
print("Hello", name)

# By default, input() stores data as string
age = input("Enter your age: ")
print(age)

# Converting input into integer using int()
age = int(input("Enter your age: "))
print(age)

# Taking decimal number input using float()
height = float(input("Enter your height: "))
print(height)

# Taking multiple inputs in one line
a, b = input("Enter two numbers: ").split()

# Printing the inputs
print(a, b)

# Taking multiple integer inputs
x, y = map(int, input("Enter two integers: ").split())

# Printing integer inputs
print(x + y)