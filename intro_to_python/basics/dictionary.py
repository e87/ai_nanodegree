# Word Counter
from typing import Dict, Any, Union

book_title = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby',
              'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

word_counter = {}  # empty dictionary

# Method one: Iterate using a for loop and indexes

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)


# Method two: use the dictionary get function instead.

word_counter_2 = {}  # type: Dict[Union[str, Any], Union[int, Any]]

for word in book_title:
    word_counter_2[word] = word_counter_2.get(word, 0) + 1  # Add the word or increments the counter

print(word_counter_2)

print("_" * 15 + "End of Word Counter" + "_" * 15 + "\n")
# Iterate through both key, value pair on a dictionary

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("\nKeys in the cast dictionary")
for key in cast:
    print(key)

# key, value pair

print("\nKey : Value Pair Iteration Example")
for key, value in cast.items():  # items() return a tuple of the value pairs in the dict
    print("Actor: {}    Role: {}".format(key, value))

# Task 1
# Count the fruits in the dic if they are in list
print("\nTask #1")
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for fruit in basket_items:
    if fruit in fruits:
        result += basket_items[fruit]
# if the key is in the list of fruits, add the value (number of fruits) to result

print(result)

# You can do the same using item()
result = 0  # reset the result value
for fruit, count in basket_items.items():
    if fruit in fruits:
        result += count

print(result)

# Task 2
# Count the words in the list into the fruit_count and the words not in the list in the non_fruit_count
fruit_count, non_fruit_count = 0, 0

for fruit, count in basket_items.items():
    if fruit in fruits:
        fruit_count += count
    else:
        non_fruit_count += count
print("The number of fruits in the fruits list is {}. The number of fruits not in the fruits list is {}.".format(fruit_count, non_fruit_count))


# task
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = {}
for cast_name, height in zip(cast_names, cast_heights):
    cast[cast_name] = height

print(cast)

# More efficient method
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

