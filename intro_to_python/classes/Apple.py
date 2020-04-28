
class Person:
    """ Returns the instance of person initialized with a given name"""
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "Hi, my name is {}".format(self.name)

    def __str__(self):
        return "The person's name is {}".format(self.name)


sample_person = Person("Emma")
print(sample_person.greeting())
print(sample_person)
# help(sample_person)


# Inheritance
class Fruit:

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


class Apple(Fruit):
    # Constructor with inheritance
    def __init__(self, color, flavor, fruit_type):
        Fruit.__init__(self, color, flavor)
        self.fruit_type = fruit_type
        self.price = 0.0


honey_crisp = Apple("red", "sweet", "Honey Crisp")
print(honey_crisp.color)
print(honey_crisp.flavor)
print(honey_crisp.fruit_type)