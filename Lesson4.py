# Task 1
# myphrase = input('Write: ')
# count = 0
# if len(myphrase) >= 2:
#     for i in myphrase:
#         count += 1
#     newphrase = myphrase[0:2] + myphrase[-2::1]
#     print("How it was = " + myphrase)
#     print("How it looks now = " + newphrase)
# elif len(myphrase) < 2:
#     print('')

#Task 2 - ?
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

phone_1 = input('Please enter your number: ')
print("Your telephone number is : ", phone_1)
count = 0
while count < len(phone_1):
    count += 1
print('Number lenth: ', count)
while phone_1.isalpha():
    print('Your phone should be 10 characters long and contain only numbers.')
    phone_1 = input('Please enter your number: ')
if count >= 11 or count <= 9 :
    print('Try again')


print('Thank you!')


# Task 3
# Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong, and then responds with a message accordingly.

# expressions  = '2 + 5' #I know how to use input, but I don't know how to insert the output for this task
# print(expressions)
# answer = input('Write your answer: ')
# if answer == '7':
#     print('Correct!')
# else:
#     print('Wrong answer')

# Task 4
# Write a program that has a variable with your name stored (in lowercase) and then asks for your name
# as input. The program should check if your input is equal to the stored name even if the given
# name has another case, e.g., if your input is “Anton” and the stored name is “anton”,
# it should return True.

# my_name = "svitlana"
# my_name_input = input("Your name: ")
# my_name_input = my_name_input.lower()
# if my_name == my_name_input:
#     print('True')
# else:
#     print('Try again!')
