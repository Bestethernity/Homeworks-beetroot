# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

# def oops():
#     our_error = IndexError
#     print('Index error in function')
#     raise our_error
#
#
# def oops_inside():
#     try:
#         oops()
#     except:
#         print("No element with such index")


# Task 2
# Write a function that takes in two numbers from the user via input(), call the numbers a and b,
# and then returns the value of squared a divided by b, construct a try-except block which raises an exception
# if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).

def nums_1(a, b):
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = a * a / b
    return print(c)


# try:
#     nums_1(1,1)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# It's only working if one of these exceptions is commented

# try:
#     print(nums_1(1,1))
# except ValueError:
#     print("One of given character is not numbers")







