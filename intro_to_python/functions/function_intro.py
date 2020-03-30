def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius**2


# Function with default value on one of its parameters
def cylinder_v(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2


def population_density(population, land_area):
    """Calculate the population density of an area
        INPUT:
        population: int. The population of the area
        land_area: int or float.
        OUTPUT:
        population_density: population/land_area. The population density of an area.
    """
    return population / land_area


def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days given to the function"""
    weeks = days // 7
    days = days % 7
    return "{} week(s) and {} day(s)".format(weeks, days)


# Calling the functions defined above
volume = cylinder_volume(20, 5)
print(volume)

print(readable_timedelta(14))

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


def factorial_1(n):
    result = 1
    for x in range(result, n+1):

        result *= x
        print(result)
    return result


print(nearest_square(36))
print(factorial(4))

print("New Factorial")
print(factorial_1(5))
