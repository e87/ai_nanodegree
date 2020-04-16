# allows you to create list in very simple steps.

# Example: capitalized the City names with no list comprehensions

cities = ["chicago", "new york", "boston"]

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
print(capitalized_cities)

# Perform the same operation using list Comprehension

cities = ["chicago", "new york", "boston"]
capitalized_cities = [city.title() for city in cities]
print(capitalized_cities)

# Structure of a list comprehension
# 1 - Expression/action/operation to apply to each value or values
# loop to iterate through the list

# List comprehension to create a list of square numbers:

square_numbers = [number ** 2 for number in range(9)]
print(square_numbers)

# You can also add conditional to list comprehensions after the iterable
# for example, the following code only calculates the square if the number is prime:
squares = [number ** 2 for number in range(9) if number % 2 == 0]
print(squares)

# to add an else statement to the prior code, you must move the conditional before the loop as follows.
# this code calculates the square only for prime number else, it adds 3 to the value of x and stores it on the list.
squares = [number ** 2 if number % 2 == 0 else number + 3 for number in range(9)]
print(squares)


# Multiple of 3
print("Multiple of 3:")
multiples_3 = [3 * number for number in range(1, 21)]
print(multiples_3)


# Working with dictionaries
print("Filter names by score:")
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [passed_name for passed_name in scores if scores[passed_name] >= 65]
print(passed)

# Using the items() to get both the name and score in the dictionary

passed = [name for name, score in scores.items() if score >= 65]
print(passed)

# Extract names
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)


def highlight_word(sentence, word):
    return " ".join([w.upper() if w == word else w for w in sentence.split()])


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
