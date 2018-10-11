def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


# Function with default value on one of its parameters
def cylinder_v(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2


def population_density(population, land_area):
    return population / land_area


def readable_timedelta(days):
    weeks = days // 7
    days = days % 7
    return "{} week(s) and {} day(s)".format(weeks, days)


# Calling the functions defined above
volume = cylinder_volume(20, 5)
print(volume)

print(readable_timedelta(10))

def word_counter(list_words, search_term):
    words = list_words.split()
    answer = 0
    for word in words:
        if word == search_term:
            answer += 1

    return answer


def nearest_square(number):
    num = 0

    while (num + 1)**2 < number:
        num += 1

    nearest_square_number = num ** 2

    return nearest_square_number

def factorial(n):
    product, current = 1,1

    while current <= n:
       product *= current
       current += 1

    return product

print(nearest_square(36))
print(factorial(4))
