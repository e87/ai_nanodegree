
# Python has two kinds of loops: for and while loops
# We can use for loops to iterate over an iterable
# An iterable is an object that can return one of its elements at a time.
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city.title())

# create a new list using the append() method
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)

# Modifying a list requires the use of the range() function
# Range is a built in function used to create an immutable sequence of numbers.
# range( start, stop, step) - arguments must be integers
# start is the first number in the sequence
# stop is one above the last number in the sequence (exclusive end)
# step difference between numbers in the sequence.
# starts defaults to zero and step defaults to 1
# Examples:

print(list(range(4)))  # will print a list from 0 to 3
print(list(range(2,6)))  # will print a list from 2 to 5
print(list(range(2,10,2)))  # will print a list from 2 to 8 but only the even numbers
print(list(range(1,10,2)))  # will print a list from 1 to 9 in increment of 2 (odd numbers)

# Now we can use the range function to generate the indexes of each value in a list
# this for loop modifies the elements of the list in place.
for index in range(len(cities)):
    cities[index] = cities[index].title()

print(cities)

# Exercise: Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.
print(list(range(5, 35, 5)))
for number in range(5, 35, 5):
    print(number)

# Exercise:  Use a for loop to print the elements of the list
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for word in sentence:
    print(word)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
username = []

for name in names:
    username.append(name.lower().replace(" ", "_"))

print(username)

# Use range to modify this list in place:
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(username)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print("List modified in place result")
print(usernames)

# More exercises
tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)


items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

# Empty list
print(list(range(0, -5)))