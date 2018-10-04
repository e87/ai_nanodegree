# Enumerate is a build in function that returns an iterator containing the index and its value
# You will use this function when you want to get both the value and its index from a data structure like List.

# To iterate through a list a long with the indexes, you can do as follows:

items = ["banana", "mattresses", "dogs"]
item_weights = [3, 30, 5]

for i, item in zip(range(len(items)), items):
    print(i, item)

# Using the enumerate function

for i, item in enumerate(items):
    print(i, "--", item)

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)