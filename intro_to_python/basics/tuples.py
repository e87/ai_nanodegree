
# Tuple is a data type for immutable ordered sequences of elements
# Tuples are similar to lists in that their elements can be accessed by indexes
# Example of a tuple representing age and height
# You cannot add or remove elements to tuples or sort them in place

age_to_height = (15, 5.2)
print(type(age_to_height))
print("The age of the individual is {}".format(age_to_height[0]))
print("The height of the individual is {}".format(age_to_height[1]))

# Tuples can be used to assign multiple variables in a compact way
# This is also called Tuple unpacking
# Note that the parenthesis are optional when declaring tuples. Omit them if they don't clarify the code
dimension = 43, 28, 13
length, width, height = dimension
print("The dimensions are {}x{}x{}".format(length, width, height))

