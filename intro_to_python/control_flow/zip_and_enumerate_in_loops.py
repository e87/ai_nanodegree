
# it will be pretty helpful to iterate over a list containing tuple values
# Zip and Enumerate are useful built-in functions specially when dealing with loops

# Zip returns an iterator that combines multiple iterables into one sequence of tuples.
# Each tuple contains the elements in that position from all the iterables.

letters_list = ['a', 'b', 'c', 'd']
number_list = [1,2,3,4]

mixed_list = list(zip(letters_list, number_list))
print(mixed_list)

# To unzip a list into tuples use an asterisk
print("Unzip list into tuples")
letters, numbers = zip(*mixed_list)
print(letters, numbers)

# Enumerate is a built-in function that returns an iterator of tuples containing indices and values of a list
# You will often use it when you want the index along with the value of each element of an iterable in a loop
print("\nEnumerate examples")
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
print("\n")


# Zip coordinates example
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)

# Zip a two list into a dictionary
print("Zip two lists into a dictionary")
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

# Unzip tuples
print("Unzip tuples")
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))  # tuple of tuples

names, heights = zip(*cast)
print(names)
print(heights)

# Transpose with Zip
print("Transpose with Zip")
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

# Enumerate
print("Enumerate over a two lists")
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
print(cast)
print(heights)
for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])  # note the enumerate let us access the index of the lists

print(cast)