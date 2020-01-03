
# A set is a data type for mutable unordered collection of UNIQUE elements
# A set can be used to quickly remove duplicate elements in a list!
numbers = [1,1,2,3,4,3,6,5]
unique_numbers = set(numbers)
print("The set of unique numbers is: ")
print(unique_numbers)

# Sets support the in operator similar to Lists
# You can add elements to a set using the add method
# You can remove a random element of a set using the pop method
print('Examples of add, pop and in operator')
fruits = {'apple', 'banana', 'orange', 'strawberry'}
print(fruits)
print("Is grape in fruits? {}".format("grape" in fruits))

fruits.add('grapes')
print('Fruits after adding grape')
print(fruits)

print('Fruits after popping an item')
print(fruits.pop())
print(fruits)

# You can perform mathematical operations on set such as Union, intersection and difference.
# These operations are much faster than in other containers
print('Union, interception and difference set operations')
A = {0, 2, 3, 5, 1}
B = {3, 2, 0, 1, 4}

print("Set A = {} , Set B = {}".format(A,B))
# Union
print("Union: ", A | B)

# Intersection
print("Interception: ", A & B)

# Difference
print("Difference A-B: ", A - B)
print("Difference B-A: ", B - A)
# Symmetric Difference
print("Symmetric difference: ", A ^ B)