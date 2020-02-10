import math

# String data type lesson
print('-'*20)
print('String Data Type')
print('-'*20)

a = "my first string"
s = "New "
s += "found "
s += "another"

print(a)
print(s)

# Join takes different strings and join them together
color = ';'.join(['#445444', '#674444', '#445533'])
print(color)

# Split splits strings based on a separator
print(color.split(';'))

# You can use the empty string as the separator as well

x = ' '.join(['hi', 'something', 'is', 'up'])

print(x)

# ---------------------------------------------------------------------------
print('-'*20)
print('Partition Function')
print('-'*20)
# Partition string based on a word or characters

partition = "unforgettable".partition("forget")

print(partition)
# ---------------------------------------------------------------------------

# tuple unpacking at work
departure, separator, arrival = "London:Edinburgh".partition(':')
print(departure)
print(arrival)
print(separator)

# You can do the same by using the underscore

departure, _, arrival = "London:Edinburgh".partition(':')
print(departure)
print(arrival)
print(_)

# ---------------------------------------------------------------------------
print('-'*20)
print('Format Function')
print('-'*20)
# Format Function
"My name is {0} and last name is {1}. Please call me {0}".format("Juan", "Motrel")

"You can omit the numbers if the fields are used in order."

"I don't need number {} here. Or Here {}".format("first", "second")

str_labels = "You can use field name as well {latitude} and {longitude}".format(latitude="60N", longitude="40S")

print(str_labels)

pos = (62.5, 23.1, 82.3)


# Accessing elements of a tuple inside the format function
p = "Galactic position x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos)
print(p)

# .3f tells the string function to only display three decimal float points.
m = "Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math)
print(m)


# Split names
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.lower().split()[0] for name in names]
print(first_names)

# Find method
s = 'Tomorrow I am taking an exam'
print(s.find('taking an exam'))


# -----------------------------------------------------------------
# string slicing
# Reverse a string
str = 'hello humans'
rev_str = str[::-1]
print(rev_str)