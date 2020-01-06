
# while loops execute until a condition is met
# pop() removes the last element from a list and returns it
# sum() returns a sum of the elements in the list
card_deck = [4, 11, 8,5,13,2,8,10]
hand = []

while sum(hand) <= 20:
    hand.append(card_deck.pop())

print(hand)

# Factorial with loops

number = 6
product = 1
current = 1

while current <= number:
    product *= current
    current += 1

print(product)

# Using for loops
number = 6
product = 1

for num in range(2, number +1):
    product *= num

print(product)

# Nearest Square
limit = 40

num = 0

while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)