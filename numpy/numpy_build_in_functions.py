import numpy as np


# helper method to print np array details
def np_array_details(np_array):
    d = "Numpy array details \n" \
        "Dimension:  {} \n" \
        "    Shape:  {} \n" \
        "     Size:  {} \n" \
        "Data Type:  {} ".format(np_array.ndim, np_array.shape, np_array.size, np_array.dtype)
    print(d)

# Useful built-in functions to create np arrays

# Zeros
x = np.zeros((3,4,)) # creates an array of zeros of the given shape/dtype. etc.
np_array_details(x)

# Ones
y = np.ones((4,5))
np_array_details(y)

# full creates an array with fills it with a constant value
w = np.full((3,4), 5)
np_array_details(w)

# Identity creates an identity matrix (square matrix with 1 in the main diagonal and zeros everywhere else).

identity_matrix = np.eye(4)
np_array_details(identity_matrix)
print(identity_matrix)



