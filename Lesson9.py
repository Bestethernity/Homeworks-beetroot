# Task 1
# Make a directory with 2 modules; make a function in one of them;
# then import this function in the other module and use that in your script of choice.

# from Lesson8 import make_country
# country = ['Ireland', 'Norway']
# capital = ['Dublin', 'Oslo']
# print(make_country(country, capital))

# Task 2
# The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change it from within Python?
# If so, does it affect where Python looks for module files? Run some interactive tests to find it out.

# import sys
# print(sys.path)
# my_path = sys.path.copy()
# # My print is look like ['D:\\Beetroot cources\\Homework-beetroot\\Homeworks-beetroot', 'D:\\Beetroot cources', 'C:\\Program Files\\JetBrains\\PyCharm 2022.2.3\\plugins\\python\\helpers\\pycharm_display', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310', 'D:\\Beetroot cources\\venv', 'D:\\Beetroot cources\\venv\\lib\\site-packages', 'C:\\Program Files\\JetBrains\\PyCharm 2022.2.3\\plugins\\python\\helpers\\pycharm_matplotlib_backend']
# for i in my_path:
#     print(my_path)
#     my_path.remove('D:\\Beetroot cources')
# print(my_path)
# for i in my_path:
#     my_path.append('D:\\Beetroot cources')
# print(my_path)
#
# my_path.append('D:\\exercise1')
# print(my_path)


# Task 3 - in a separate folder

