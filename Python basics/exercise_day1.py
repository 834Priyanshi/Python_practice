# Exercise 1: Program to input a number and print its cube
num = int(input("Enter a number:"))
cube = num ** 3
print("The cube of", num, "is:", cube)

# Exercise 2: Program to input two numbers and swap them
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
# Swapping
x,y = y,x
print("After swapping:")
print("First number:", x)
print("Second number:", y)
