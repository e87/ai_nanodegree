
# lower and upper functions
print("Lower and Upper functions")
name = "Maria"
print(name.lower())
print(name.upper())


# Strip function removes surrounding space from a string. It also removes tabs and new line characters.

string_with_space = " yes "
right_string = "yes "
left_string = " yes"

print("\n")
print("Strip, Left and Right Strip functions")
print(string_with_space.strip())
print(right_string.rstrip())
print(left_string.lstrip())

# Count
print()
print("Count function")
sentence = "The number of times e occurs in this string is "
print(sentence + str(sentence.count("e")))

# endswith
print()
print("Endswith function")
print("Forest".endswith("rest"))

# isnumeric
print()
print("isnumeric function")
st = "Forest"
print(st.isnumeric())
print("1236".isnumeric())

st.upper()

# int()
print()
print("Int converts a string into a integer")
print(int("12345"))

# joint method is used to join or concatenate strings
print()
print("Join function")
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))

# Split function splits a string into a list of strings
print()
print("Split function")
print("This is another example".split())

# Format method
print()
print("The format method is used to format strings")
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

print("Another example with the name of the variables inside the brackets")
print("Your lucky number is {number}, {name}".format(name=name, number=len(name)*3))

# Formatting numbers
print()
print("Decimal format ")
price = 7.5
with_tax = price * 1.09

print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))


def to_celsius(x):
    return (x - 32) * 5 / 9

# the >3 makes the text be aligned to the right by 3 space.
# the >6.2f tells the format function to align the text to the right 6 spaces and print 2 decimal places
for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

# More string formatting
def difference_bases_number(number):
    print()
    print("{:*^38}".format("Base Table"))
    for num in range(1, number +1):
        #print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(num))
        print("int: {0:>3d};".format(num),  "hex: {0:>3x};".format(num), "oct: {0:>3o};".format(num), "bin: {0:>3b}".format(num))


difference_bases_number(10)

# format numbers
print('{:-f}; {:-f}'.format(3.14, -3.14)) # show only the minus -- same as '{:f}; {:f}'
print('{: f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers
print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always
print('{:,}'.format(1234567890)) # user comma as thousands separator

points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))


# Exercises
def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = len(sentence) - len(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"