# Control flow allows you to build logic into your programs
# Your program can run block of code based on a given condition
phone_balance = 3
bank_balance = 0
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

season = ''
# Example of if, elif and else statements
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')


# Complex Boolean expression
# logical operators like and, or, not

weight = 55
height = 164

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

is_raining = True
is_sunny = True

if is_raining and is_sunny:
    print("Is there a rainbow?")

unsubscribed = False
location = 'USA'

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")

# Good and bad examples of boolean expressions
# Dont use True or False as conditions
# to check whether a boolean is true use the boolean itself without the boolean_varibale == True check
# Similarly, to check if a boolean is false, use the not boolean_variable combination
# example:
is_night = True
is_day = False

if is_night:
    print("Good night!")

if not is_day:
    print("Get some more sleep!")

# Truth Value Testing
# If a control flow contains a value to the right of the equal sign that is not a boolean expression,
# python will check for its Truth value to decide whether to run the code or not.
# Constants defined to be false:
    # None, False
    # Zero of any numeric type: 0 , 0.0, 0j
    # Empty sequences and collections: (), [], {}, ' ', set(0), range(0), etc.
# Anything else not listed above will contain a truth value of True 
