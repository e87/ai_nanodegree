# Use while loops to calculate n!

# number to calculate the factorial of n
number = 6
# product equals to one
product = 1
# track the current number being multiplied
current = 1

while current <= number:
    product *= current
    current += 1

print(product)

# nearest square example

limit = 40
num = 0

while (num + 1)**2 < limit:
    num += 1

nearest_square = num ** 2

print(nearest_square)


# Break and Continue Keyword
# can be use on both for and while loops to get more control over them


