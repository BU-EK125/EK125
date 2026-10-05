"""
Class 11 GPP: Working with Arrays in NumPy
EK125 - Spring 2026

Work in groups of THREE.

Instructions:
- You MAY use your reading notes and previous assignments
- Do NOT use AI tools (ChatGPT, Claude, Copilot, etc.)
- Not submitted for grading - but this material WILL appear on quizzes and exams!

PyCharm reminders:
- Run your file with Shift+F10 (or the green play button)
- Output appears in the terminal at the bottom
- Save frequently with Ctrl+S / Cmd+S
"""

# ==============================================================================
# PROBLEM 1: Importing NumPy
# ==============================================================================
"""
Today we will investigate the NumPy module. NumPy is short for Numerical
Python, and it is based on arrays.

Start by:
  - importing numpy as np
  - importing the array function

Recall how we did importing from Class 5.
"""

# Your code here


# ==============================================================================
# PROBLEM 2: Arrays, Types and dtypes
# ==============================================================================
"""
  - Create a one-dimensional array variable using the array function, in
    which 5 integers are stored.
  - Also create a 1D array variable that stores 6 floats.
  - Print both arrays and their types.
  - Use the dtype method to determine the type of both array variables.
    Note that no arguments are passed to dtype, and the parentheses are
    not needed.
"""

# Your code here


# ==============================================================================
# PROBLEM 3: ndim, size, and shape
# ==============================================================================
"""
For both variables from Problem 2:
  - use the ndim method to determine the number of dimensions
  - use the shape method to determine the length of the axes
  - use the size method to determine the number of elements
"""

# Your code here


# ==============================================================================
# PROBLEM 4: 2D Arrays
# ==============================================================================
"""
  - Create a nested list variable that stores integers: two inner lists,
    each of which stores 4 integers.
  - Then, create a 2 by 4 array variable by passing the list to array().
  - Print both variables so you can see the difference.
  - Use the ndim, shape, and size methods on your 2D array variable.
  - Use the reshape method to reshape it into as many other arrays as you can.
  - Use the transpose method to transpose your array.
  - Index and slice your 2D array:
      - Index element at row 0, column 0
      - Index element at row 0, column 1
      - Slice row 0, last column
      - Slice all columns from row 1
      - Slice all rows, column 0
      - Slice all rows, first two columns
  - Replace the first row of your 2D array with other numbers.
"""

# Your code here


# ==============================================================================
# PROBLEM 5: arange and linspace
# ==============================================================================
"""
  - Create a 1D array that stores [2  5  8  11]. Do this two ways: using
    arange and linspace. Make sure that the elements are integers.
  - Create a 2 by 4 array using arange for the first row and linspace for
    the second row. Print it.
  - Use linspace to create an array with 9 elements, from 1 to 5 in steps
    of 0.5.
  - Create a 1D array (vector) with 10 linearly spaced points in the range
    from 1 to 19. Reshape this into a 2D array.
"""

# Your code here


# ==============================================================================
# PROBLEM 6: Special Arrays
# ==============================================================================
"""
  - Create and print a 3 by 5 array of all zeros (integers).
  - Create and print a 4 by 2 array of all ones (integers).
  - Create and print a 3 by 5 array of all 33's using np.full.
  - Create a 3D array of all zeros. Print it.
"""

# Your code here


# ==============================================================================
# PROBLEM 7: Random Arrays
# ==============================================================================
"""
  - Execute the following to create a random number generator, and then use
    that to create arrays of random floats and integers:

      rng = np.random.default_rng()
      randfl = rng.random(4)
      print(randfl)
      randint = rng.integers(0, 100, 5)
      print(randint)

  - Create a 6 by 1 array of random integers and transpose it. Print both.
  - Create a 2 by 4 array of random integers, in the range from 0 to 50.
    Hint: instead of a length of 5 as above, the third argument will be a
    tuple containing the number of rows and columns.
"""

# Your code here


# ==============================================================================
# PROBLEM 8: Logicals in Arrays
# ==============================================================================
"""
Using an array in a Boolean expression results in a logical array.

  - Create a 1D array variable my1d and try the expression my1d < 10. Store
    it in a variable and print it, as shown below:

      my1d = array([33, 2, 11, 5, 8, 4])
      mylog = my1d < 10
      print(mylog)

  - Now, use your logical array to index into your original 1D array:

      my1d[mylog]
"""

# Your code here


# ==============================================================================
# PROBLEM 9: Special Reshaping with vstack and ravel
# ==============================================================================
"""
  - Create two 1 by 5 arrays using arange. Use vstack to concatenate them
    into a 2D array.
  - Use the ravel method on your 2D array.
"""

# Your code here


# ==============================================================================
# PROBLEM 10: Challenges!
# ==============================================================================

# Challenge 1:
# Write an expression that will sum only the values in a vector variable v
# (1D array) that are greater than or equal to 4. Use logical indexing.

# Your code here


# Challenge 2:
# Create a 3 by 5 array (matrix) of all random integers in the range from
# 50 to 100. Write code that will count how many elements are greater than 80.

# Your code here


# Challenge 3:
# Create a 2D array. Write nested for loops to print the array in a table format.

# Your code here


# Challenge 4:
# Create the 3x3 matrix [ 1 2 3 ; 4 5 6 ; 7 8 9 ] and then:
#   - Transpose the matrix using a list comprehension
#   - Transpose the matrix using a for loop

# Your code here
