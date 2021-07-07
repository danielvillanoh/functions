# --------------- Section 3 --------------- #
# 1 | Fahrenheit to Celsius Conversion
#
# Fahrenheit is way we measure temperature and is commonly used in the United States, the Cayman Islands, and Liberia.
# The other unit of measurement is celsius. Celsius is commonly used throughout the rest of the world. Since they are
# different units of measurement, then the exact same temperature will have different values.
#
# For example, 68° fahrenheit is 20° celsius.
# https://www.google.com/search?client=firefox-b-1-d&q=68+degrees+fahrenheit+to+celsius
#
#
# To calculate celsius from fahrenheit, you use the following equation:
#   c = (f - 32) * (5/9)
#       where; f represents degrees fahrenheit
#              c represents degrees celsius
#
# Function
#   1 - Define a function that will convert a temperature in fahrenheit to celsius.
#   2 - Define a function that will convert a temperature in celsius to fahrenheit.
#   3 - Return the new temperature.

def fahrenheit_to_celsius(f):
    c = (f - 32) * (5 / 9)
    return c


def celsius_to_fahrenheit(c):
    f = (c * (9 / 5)) + 32
    return f


#
# Function Call
#   1 - Call both of these functions, and save the return value. Use any temperature.
#   2 - Print the old and converted temperature.
#
# EXAMPLE OUTPUT:
#   72° fahrenheit is 22.2222° celsius
#   10° celsius is 50° fahrenheit
#
# WRITE CODE BELOW

print('32 fahrenheit is', fahrenheit_to_celsius(32), 'celsius')
print('2 celsius is', celsius_to_fahrenheit(2), 'fahrenheit')


# 2 | Celsius to Kelvin
#
# There is another unit of measurement, called kelvin. It is closely related to celsius. In fact to convert an equation
# from Celsius to Kelvin is as thus:
#   k = c + 273.15
#   where; c represents degrees celsius
#
# Function
#   1 - Define a function that will convert a temperature in celsius to kelvin.
#   2 - Define a function that will convert a temperature in kelvin to celsius.
#   3 - Return the new temperature.
#
# Function Call
#   1 - Call both of these functions, and save the return value. Use any temperature.
#   2 - Print the old and converted temperature.
#
# EXAMPLE OUTPUT:
#   45° celsius is 318.15° kelvin
#   232° kelvin is -41.15° celsius
#
# WRITE CODE BELOW
def celsius_to_kelvin(c):
    k = c + 273.15
    return k


def kelvin_to_celsius(k):
    c = k - 273.15
    return c


print('45 celsius is', celsius_to_kelvin(45), 'kelvin')
print('232 kelvin is', kelvin_to_celsius(232), 'celsius')


# Question: How could you use these functions to convert a temperature in fahrenheit to kelvin?

# In order to get from fahrenheit to kelvin, we combine formula fahrenheit to celsius and celsius to kelvin.

def fahrenheit_to_kelvin(f):
    c = (f - 32) * (5 / 9)
    k = c + 273.15
    return k


print('22 fahrenheit is', fahrenheit_to_kelvin(22), 'kelvin')


