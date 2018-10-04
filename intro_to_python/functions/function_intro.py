def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


# Function with default value on one of its parameters
def cylinder_v(height, radius=5):
    pi = 3.14159
    return height * pi * radius **2


volume = cylinder_volume(20, 5)
print(volume)


