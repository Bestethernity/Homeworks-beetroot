# Task 1
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

# import random
# list_1 = []
# while len(list_1) < 10:
#     list_1.append(random.randint(1,100))
# print(list_1)
# print(max(list_1))

# Task 2
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

# import random
# list_2 = []
# list_3 = []
# while len(list_2) < 10:
#     list_2.append(random.randint(1, 100))
# print(list_2)
# while len(list_3) < 10:
#     list_3.append(random.randint(1, 100))
# print(list_3)
# list_4 = [*set([item for item in list_2 for item_2 in list_3 if item == item_2 ] + [item_2 for item_2 in list_3 for item in list_2 if item_2 == item ])]
# print(list_4)

# Task 3 - I couldn't deal with it with while loop

# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible
# by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

# list_5 = []
# for i in range(1,100):
#     if i % 7 == 0 and i % 5 != 0:
#         list_5.append(i)
# print(list_5)




