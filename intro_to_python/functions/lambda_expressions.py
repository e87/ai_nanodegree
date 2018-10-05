# Lambda expression are expressions used to create unnamed functions.
# high order function can take other functions as arguments. This is where Lambda expressions become really useful

# Example:


def double_a_number(number):
    return number * 2


# Here is the equivalent in a Lambda format

double = lambda x: x * 2


# Another example using two arguments


def multiply(x, y):
    return x * y


two_variables = lambda x, y: x * y

# Example using map() high order function to find the averages of the list in numbers
# and create a new list of averages.

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

# using a function


def mean(num_list):
    return sum(num_list) / len(num_list)

mean = lambda num_list: sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

