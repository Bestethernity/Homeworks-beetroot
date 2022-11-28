# Task 1
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.

# def favorite_movie(name):
#     print('My favorite movie is ' + (name))
# favorite_movie('Harry Potter')

# Task 2
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.

# def make_country(country, capital):
#     dict_1 = {country[i]: capital[i] for i in range(len(country))}
#     return dict_1
# country = ['France', 'Germany', 'Italy', 'Ukraine']
# capital = ['Paris', 'Berlin', 'Rome', 'Kiev']
# print(make_country(country,capital))


# Task 3
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
# as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.
# For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42

# def make_operation(operator, *args):
#     result = int()
#     if operator == "+":
#         result = sum(args)
#     elif operator == "-":
#         result = args[0]
#         for i in range(len(args)-1):
#             i += 1
#             result -= args[i]
#     elif operator == "*":
#         result = args[0]
#         for i in range(len(args)-1):
#             i += 1
#             result *= args[i]
#     return result
#
#
# print(make_operation("*",5, 5, 3, 2))