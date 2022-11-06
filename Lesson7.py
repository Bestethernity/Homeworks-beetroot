# Task 1
# Make a program that has some sentence (a string)
# on input and returns a dict containing all unique words as keys and the number of occurrences as values.
# phrase = input('Enter the sentence: ')
# phrase_1 = phrase.split()
# my_dict = dict()
# print(phrase_1)
# letter_counts = []
# for word in phrase_1:
#     word.split()
#     letter_counts = len(word)
#     my_dict[word] = letter_counts
# print(my_dict)

# Task 2
# Compute the total price of the stock where the total price is the
# sum of the price of an item multiplied by the quantity of this exact item.
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# "banana": 24, "apple": 2, "orange":48, "pear": 45
# total_price = dict()
# new_value = 0
# for key, value in stock.items():
#     for key_1, value_1 in prices.items():
#         if key == key_1:
#             new_value = value * value_1
#             total_price[key] = new_value
# print(total_price)

# Task 3
# Use a list comprehension to make a list containing
# tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

# list_1 = [(a,b) for a in range(1,11) for b in range(1,11)]
# print(list_1)

# Task 4
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

# list_2 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# my_dict = dict()
# value = 0
# for a in list_2:
#     my_dict[a] = value + 1
#     value += 1
# print(my_dict)

# reverse_dict = dict()   # I couldn't find the solution for the list as a list of values
# reverse_dict = {key: value for value in list_2 for key in range(1,8)}
# print(reverse_dict)

