"""
Class 11 GPP Solutions: Working with Arrays in NumPy
EK125 - Spring 2026
"""

# ==============================================================================
# PROBLEM 1 SOLUTION: Importing NumPy
# ==============================================================================

import numpy as np
from numpy import array

# ==============================================================================
# PROBLEM 2 SOLUTION: Arrays, Types and dtypes
# ==============================================================================

int_array = array([11, 2, 33, 9, 4])
float_array = array([1.1, 2.2, 3.3, 4.8, 5.4, 6.2])
print(int_array, type(int_array))
print(float_array, type(float_array))
print(int_array.dtype)
print(float_array.dtype)

# ==============================================================================
# PROBLEM 3 SOLUTION: ndim, size, and shape
# ==============================================================================

print(int_array.ndim)
print(float_array.ndim)
print(int_array.shape)
print(float_array.shape)
print(int_array.size)
print(float_array.size)

# ==============================================================================
# PROBLEM 4 SOLUTION: 2D Arrays
# ==============================================================================

nested_list = [[1, 22, 32, 1], [14, 5, 9, 2]]
two_d_array = array(nested_list)
print(nested_list)
print(two_d_array)
print(two_d_array.ndim)
print(two_d_array.shape)
print(two_d_array.size)
print(two_d_array.reshape(4, 2))
print(two_d_array.reshape(1, 8))
print(two_d_array.reshape(8, 1))
print(two_d_array.T)
print(two_d_array)
print(two_d_array[0, 0])
print(two_d_array[0, 1])
print(two_d_array[0, -1])
print(two_d_array[1, :])
print(two_d_array[:, 0])
print(two_d_array[:, :2])
two_d_array[0, :] = [1, 2, 3, 4]
print(two_d_array)

# ==============================================================================
# PROBLEM 5 SOLUTION: arange and linspace
# ==============================================================================

my1d = np.arange(2, 12, 3)
print(my1d)
my1d = np.linspace(2, 11, 4, dtype=np.int16)
print(my1d)

my2d = array([np.arange(2, 9, 2), np.linspace(1, 8, 4, dtype=np.int16)])
print(my2d)

ls = np.linspace(1, 5, 9)
print(ls)

arr1d = np.linspace(1, 19, 10)
arr2d = arr1d.reshape(2, 5)
print(arr2d)

# ==============================================================================
# PROBLEM 6 SOLUTION: Special Arrays
# ==============================================================================

zeros_array = np.zeros((3, 5), dtype=np.int16)
print(zeros_array)
ones_array = np.ones((4, 2), dtype=np.int16)
print(ones_array)
array33 = np.full((3, 5), 33)
print(array33)
arr3d = np.zeros((2, 4, 3))
print(arr3d)

# ==============================================================================
# PROBLEM 7 SOLUTION: Random Arrays
# ==============================================================================

rng = np.random.default_rng()
randfl = rng.random(4)
print(randfl)
randint = rng.integers(0, 100, 5)
print(randint)

my1d = rng.integers(0, 100, (6, 1))
print(my1d)
print(my1d.T)

randints = rng.integers(0, 50, (2, 4))
print(randints)

# ==============================================================================
# PROBLEM 8 SOLUTION: Logicals in Arrays
# ==============================================================================

my1d = array([33, 2, 11, 5, 8, 4])
mylog = my1d < 10
print(mylog)
print(my1d[mylog])

# ==============================================================================
# PROBLEM 9 SOLUTION: Special Reshaping with vstack and ravel
# ==============================================================================

from numpy import arange

arr1 = arange(2, 7)
arr2 = arange(3, 8)
mat = np.vstack((arr1, arr2))
print(mat)
print(mat.ravel())

# ==============================================================================
# PROBLEM 10 SOLUTION: Challenges!
# ==============================================================================

# Challenge 1: Sum values >= 4 using logical indexing
v = np.array([1, 5, -2, 11, 4])
print(v[v >= 4])
print(sum(v[v >= 4]))

# Challenge 2: Count elements > 80 in a 3x5 random integer array (range 50-100)
arr = np.random.randint(50, 100, (3, 5))
print(arr)
print(arr[arr > 80].size)

# Challenge 3: Print a 2D array in table format using nested for loops
arr2d = np.array([[33, 2, 11], [5, 4, 2]])
for row in arr2d:
    for col in row:
        print(f'{col:4d}', end=" ")
    print()

# Challenge 4: Transpose a 3x3 matrix using a list comprehension and a for loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed_matrix.append(transposed_row)
print(transposed_matrix)
