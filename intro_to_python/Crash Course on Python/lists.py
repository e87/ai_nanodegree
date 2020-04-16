# list are one of the most useful data types in python
# list are mutable

fruits = ['Pineapple', 'Apple', 'Grapes']
print(fruits)

# Append - adds an element always at the end of the list
fruits.append('Kiwi')
print(fruits)

# Insert - at any given index - if you pass an index larger to the len of the list, the item gets added to the end
fruits.insert(0, 'Peach')
print(fruits)

# Remove method - removes from the list the first occurrence of the element we pass to it
# We get a value error if the element to remove is not in the list
fruits.remove("Kiwi")
print(fruits)

# Pop - removes an element at an specific index
fruits.pop(2)
print(fruits)

# Change an element by assigning a new element to that position
fruits[0] = "Apple"
print(fruits)


def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for element in elements:
        # Does this element belong in the resulting list?
        if elements.index(element) % 2 == 0:
            # Add this element to the resulting list
            new_list.insert(i, element)
        # Increment i
        i += 1

    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

# Iterating through lists and tuples

# use the enumerate to return the index and name on the following list
winners = ["Ashley", "Emma", "Elizabeth"]
for index, name in enumerate(winners):
    print("{} - {}".format(index + 1, name))


print()
name_list = ["Carlos", "Jane", "Maria", "Josh"]
name_list.sort()
print(name_list)
name_list.reverse()
print(name_list)

#print(name_list.pop())
#print(name_list)


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [file.lower().replace(".hpp", ".h") for file in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    new_list = list2
    # Using slicing to reverse a list
    # could have use list1.reverse() method
    new_list += list1[::-1]

    # Followed by the elements of list1 in reverse order
    return new_list


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))