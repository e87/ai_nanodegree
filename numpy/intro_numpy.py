import time
import numpy as np

x = np.random.random(1000000)

print("time it takes regular python code to calculate the mean of X")
start = time.time()
avg = sum(x) / len(x)
print(time.time() - start)

print("time it takes numpy to calculate the mean of X")
start = time.time()
np.mean(x)
print(time.time() - start)

# Creating Numpy ndarrays (n dimensional arrays)
x = np.array([1,2,3,4,5,6])  # 1 dimensional array
print(x)
print(type(x))
print(x.dtype)  # returns the data type in the x numpy array

print(x.shape)  # return the shape of the np array
print(x.ndim)  # return the n dimension of hte np array
print(x.size) # total number of elements in the array

# Two dimensional array
# We create a rank 2 ndarray that only contains integers
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y has a total of', Y.size, 'elements')
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)

# specify the data type in an array
s = np.array([1,2,3.4,5.5], dtype=int)
print(s)

# Save np array to the directory as int_array.npy
np.save('int_array', s)

# load the np array saved as int_array.npy from the directory
t = np.load('int_array.npy')
print("Array loaded into T from the directory \n", t)

s = np.array([[1,2,3], [6,5,4]])
print(s.shape)
print(s.size)

print("3-d Array")
three_d = np.array([[[1,2,3], [4,5,6]],
                   [[9,8,7], [10,11,12]]])
print(three_d)
print(three_d.shape)
print(three_d.size)

