from typing import List

my_list = [1, 2, 3]  # type: List[int]

if my_list:
    print('list is not empty')

else:
    print('empty')

# Lists are mutable ordered data structure in python. Zero based indexing is used in python lists.
# List can contain mixed elements like strings, number or boolean
list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']

for item in list_of_months:
    print(str(list_of_months.index(item) + 1) + "-" + item)


list_of_months_abbreviation = []

# Slicing notation to retrieve parts of a list
# When slicing, the lower bound is inclusive while the upper bound is exclusive
#
for item in list_of_months:
    list_of_months_abbreviation.append(item[:3])

for item in list_of_months_abbreviation:
    print(str(list_of_months_abbreviation.index(item) + 1) + "-" + item)

# Lists support the in and not in operators
'Monday' in list_of_months # will return false

'September' in list_of_months # will return true


# Mutability and order
# List can be modified but strings cannot
# You can modify a list by setting the value in a given index to the desired value.

list_example = ['I', 'You', 'He']
print('Original list_example {}'.format(list_example))
# to change He with she in the list, we do the following:
list_example[2] = 'She'
print('Modified list_example {}'.format(list_example))

# Useful function for lists
# len(list) returns the number of elements in the list
# max(list) returns the greatest element of the list. The max function is not defined for list that contains mixed elements i.e. number and strings
# min(list) returns the smallest element in a list. This is basically the opposite of max()
# sorted(list) returns a COPY of a list in order from smallest to largest, leaving the original list unchanged!
# You can sort from larger to smaller by adding the reverse=tru option int the function call.

list_of_numbers= [12, 13, 1, 5, 6]
print('Sorted List of Numbers: ')
print(sorted(list_of_numbers))

print('Reversed sorted list of numbers: ')
print(sorted(list_of_numbers, reverse=True))

# Join() works with list. It takes a list of strings as its argument and returns a string joined by a separator.
# if join returns different results than expected, check for missing commas in the lsit
months = "\n".join(list_of_months)
print("list_of_months joined by \\n")
print(months)

full_name = ['Juan', 'Sanchez']
print(" ".join(full_name))


# The append() method adds a new element to the end of the list.
list_of_numbers.append(100)
print('New list_of_numbers with 100 appended: ')
print(list_of_numbers)

# Split Function
my_list = "boston".split(" ")
print(my_list)
if 'Terrier' in my_list:
    print("terrier is in the list")
else:
    print('No Terrier')