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

