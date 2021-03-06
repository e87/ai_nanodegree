# Handling errors
# Try statement

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number')
    finally:
        print('\nAttempted Input\n')

# You can catch specific exception as follows:

try:
    x = int(input('Enter a number: '))
except (ValueError, KeyboardInterrupt):  # specific exceptions
    print('entered the except block')

try:
    x = int(input('Enter a number: '))
except ValueError:  # specific exceptions
    print('entered the except block')
except KeyboardInterrupt :
    print("\nKeyboard Interrupt exception")


# You can access the error message for a given exception as follows

try:
    x = int(input("enter a number: "))
    y = 10 / x
except ZeroDivisionError as e:
    print("ZeroDivisionError occurred: {}".format(e))

# to handle non - specific exceptions use Exception as E in the except statements.\


# party planner function
def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return(num_each, leftovers)