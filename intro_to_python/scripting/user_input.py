# Taking some input from the user

name = input("Please enter your name: ").split(",")
print("Your name is {}".format(name))

# You can accept numbers as input and cast them like this:

number = int(float(int(input("Please enter a number: "))))
print("Hello " * number)

# Using Eval. It allows user to enter python expressions as input themselves.

result = eval(input("Enter an expresion for me: "))
print(result)
