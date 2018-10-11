# Iterator : an object that represents a stream of data.
# List, dictionaries are iterable data structures

# Generator is a function that creates an iterator. The generator function produces an iterator.
# Sometimes, programmers refer to the output of a generator function as a generator.
# Generators use the "yield" keyword instead of the "return" keyword
# Example:


def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

# The yield keyword allows the generator to return an iterator that is incremented each time the generator function is called.
# Basically, it starts where it left off on the previous call.
# Generators can only be iterated once. They are useful when the fully realized list would not fit in memory,or when the
# cost to calculate each list element is high and you want to do it as late as possible.
# Generator expressions are surrounded by parenthesis "()"  and list comprehension expressions by brackets "[]"


for n in my_range(10):
    print(n)


# Example of a listcomps and genexps
line_list = ['  line 1\n', 'line 2  \n']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]


for line in stripped_iter:
    print(line)

print(stripped_list)


# Exercise
# Create a generator function to yield a chunk of a specified size


def chunker(iterable, size):
    # Implement function here
    i = 0
    while i < len(iterable):
        yield iterable[i: i + size]
        i += size


for chunk in chunker(range(25), 4):
    print(list(chunk))

# the code above can be implemented as follows:


def chunker2(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


for chunk2 in chunker2(range(25), 4):
    print(list(chunk2))


# another exercise. Replicate the behavior of enumerate()

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    count = start
    for item in iterable:
        yield count, item
        count += 1


# Example of list comprehension and generators. Note that one uses "[]" while the other uses "()"

sq_list = [x**2 for x in range(10)]

sq_iterator = (x**2 for x in range(10))

print(sq_iterator)
print(sq_list)