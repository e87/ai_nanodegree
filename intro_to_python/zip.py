# Zip allows you to pack two list together into one

items = ["banana", "mattresses", "dogs"]
item_weights = [3, 30, 5]

# we can put together these tow lists as follow:

my_new_list = list(zip(items, item_weights))
print(my_new_list)

# Zip returns an iterator that can be used in a loop like this:
print("\nUnpacking each tuple in the list")
for item, weight in zip(items, item_weights):
    print(item, weight)

# To separate a list, you can do the following:

items2, weight_items2 = zip(*my_new_list)

print(items2)


letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))


# Transpose a 4 x 3 matrix to a 3 x 4 matrix
data = ((0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (9, 10, 11))

print("\n Original Matrix \n {}".format(data))

data_transpose = tuple(zip(*data))
print("\n Transposed Matrix \n {}".format(data_transpose))

# task
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)
print(names)
print(heights)