# opening a file in read mode

f = open('test_file.txt', 'r')
file_data = f.read()
f.close()

print(file_data)

# Calling the read method with an integer allows you to read up to that number of characters
f = open('test_file.txt', 'r')
file_data = f.read(10)
f.close()

print('I read up to a 10 characters: {}'.format(file_data))

# Opening a file with the keyword with.

with open('test_file.txt', 'r') as wf:  # closes the file Automatically.
    file_data = wf.read()

print(file_data)

# Writing to a file:

f = open("test_file2.txt", 'w')  # deletes the content of the file before writing to it
f.write("Hello there. Python is great!")
f.close()

# Append to a file:
f = open('test_file2.txt', 'a')
f.write("I am appending to the content of this file now")
f.close()

print(file_data)
