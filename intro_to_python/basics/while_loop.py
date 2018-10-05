# Use while loops to calculate n!

# number to ding the factorial of

number = 6

# product equals to one
product = 1

# track the current number being multiplied
current = 1

while current <= number:
    product *= current
    current += 1

print(product)

