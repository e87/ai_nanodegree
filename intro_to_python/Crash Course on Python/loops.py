# Loops and recursions

print("Hello While Loops")

x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x += 1

print("x=" + str(x))


def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            # If it's not, increment the factor by one
            factor += 1
    return "Done"


print_prime_factors(100)


# Should print 2,2,5,5


def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0 and n != 0:
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False


def sum_divisors(n):
    sum = 0
    # Return the sum of all divisors of n, not including n
    divisor = 1
    while divisor < n:
        if n % divisor == 0:
            sum += divisor
        divisor += 1

    return sum


print(sum_divisors(6))  # Should be 6 (sum of 1+2+3)
print(sum_divisors(12))  # Should be 16 (sum of 1+2+3+4+6)


# For Loops

def to_celsius(x):
    return (x - 32) * 5 / 9


print("C-F")
for x in range(0, 101, 10):
    print(x, to_celsius(x))


# Nested Loops
# Dominoes example
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()