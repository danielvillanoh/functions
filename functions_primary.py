# author: Daniel Villano-Herrera
# date: 7/7/2021


# --------------- Section 1 --------------- #

# 1 | Exploring Built-in Functions
#
# Visit this documentation:
#   - https://www.w3schools.com/python/python_ref_functions.asp
#   - https://docs.python.org/3/library/functions.html
#
# Using the documentation above of built in functions, complete the following operations:
#   1 - Print the absolute value of a negative number.
#   2 - Save the hexadecimal value of 21 to a variable. Print this variable while describing it.
#   3 - Print the id of the variable holding the hexadecimal value of 21.
#   4 - Print 2 ^ 5 using the function instead of **.
#   5 - Print the number 3.75123 after being rounded to the nearest integer.
#   6 - Get the length of your full name by adding the length of first and last name together. Print it.
#
# Hint: REMEMBER, functions are typically named after verbs or nouns. Notice that the main action for a lot of tasks is
# to print, a verb, that is also the name of the function print. Think about what is being asked of you and that should
# help you find the right function.
#
# 1 is done for you.

print('The absolute value of -15 is:', abs(-15))
print('The hexadecimal value of 21 is:', hex(21))
print('The id of the variable holding the hexadecimal value of 21', id(hex(21)))
print('2^5 =', pow(2, 5))
print("3.75123 rounded in the nearest integer is:", int(3.75123))
print('Here\'s the length of my full name:', len('Daniel Villano-Herrera'))


# --------------- Section 2 --------------- #

# 1 | Function Definitions no Parameters
#
# Relevant Documentation:
#   - https://www.w3schools.com/python/python_functions.asp
#
# Define the following functions:
#   1 - Define a function that will print out your name.
#   2 - Define a function that will print out three animals that you like.
#   3 - Define a function that will print the three odd numbers.
#
# Calling the functions:
#   1 - Call each function once.
#
# WRITE CODE BELOW
def print_name():
    print('Daniel Villano-Herrera')


def favorite_animals():
    print('Cat')
    print('Eagle')
    print('Dog')


def odd_numbers():
    print(1)
    print(3)
    print(5)


print_name()
favorite_animals()
odd_numbers()


# 2 | Function Definitions with Parameters
#
# Relevant Documentation:
#   - https://www.w3schools.com/python/python_functions.asp
#
# Define the following functions:
#   1 - Define a function that will print out the cube of a number.
#       a. Parameters:
#           Name | Type(s)         | Description
#           num  | Integer / Float | The number to be cubed.
#   2 - Define a function that will print the sum of three numbers.
#       a. Parameters:
#           Name | Type(s)         | Description
#           a    | Integer / Float | A number. Will be added with b and c to find the sum.
#           b    | Integer / Float | A number. Will be added with a and c to find the sum.
#           c    | Integer / Float | A number. Will be added with a and b to find the sum.
#   3 - Define a function that will return a string duplicated five times.
#       a. Parameters
#           Name | Type(s)| Description
#           text | String | The text to be duplicated.
#
# Calling the functions:
#   1 - Call each function once.
#   2 - For the 3rd function, save the return value to a variable and print it.
#
# WRITE CODE BELOW
def cube_of_number(num):
    print(num * num * num)


def sum_of_three_numbers(a, b, c):
    print(a + b + c)


def duplicate_five_times(text):
    return text * 5


cube_of_number(4)
sum_of_three_numbers(1, 3, 4)
print(duplicate_five_times('hi'))
