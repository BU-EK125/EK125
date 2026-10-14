"""
Homework 6: NumPy and Dictionaries
EK125 - Spring 2026

This is a script-based assignment: write and run all of your code in this
single .py file in PyCharm.

This homework has two sections:
  Section 1 (Problems 1-6): Covers Class 11 material --
                             NumPy arrays and testing your code with assert.
  Section 2 (Problems 7-10): Covers Class 12 material -- dictionaries.

Graded for submission, not for correctness -- but this material will appear
on quizzes and exams, so treat it as real practice, not a box to check.

INSTRUCTIONS:
  - Complete ALL problems
  - Run your file often and verify your output before finishing
  - Use meaningful variable names and add comments to explain your logic

PYCHARM REMINDERS:
  - Run your file with Shift+F10 (or the green play button)
  - Output appears in the terminal at the bottom
  - Save frequently with Ctrl+S / Cmd+S
"""

# ==============================================================================
# SECTION 1: NUMPY AND CODE TESTING
# ==============================================================================

# ==============================================================================
# PROBLEM 1: Basic NumPy Operations and Assertions
# ==============================================================================
"""
Create a NumPy array arr with the following values: 3, 6, 9, 12, 15

Multiply every element in the array by 2 and store it in a new array doubled.

Add 5 to each element in the original array and store in another array
plus_five.

Write 3 assertions (using assert) to test:
  1. The length of arr is 5
  2. The second value of doubled is 12
  3. The last value of plus_five is 20
"""

# Your code here


# ==============================================================================
# PROBLEM 2: Testing Floating Point Array Equality
# ==============================================================================
"""
In this problem, you'll explore how tiny rounding errors can affect equality
comparisons between floating point arrays -- even when the math looks the
same.

Your task:
  1. Create two 2x3 NumPy arrays that should contain the same values:
       - One using: array / np.sqrt(2)
       - The other using: np.sqrt(0.5) * array
  2. Compute the sum of each array using np.sum().
  3. Compare the two sums using both:
       - == for direct equality
       - np.isclose() for tolerance-based comparison
  4. Use assert to check if the sums match.

Questions to answer (as comments):
  - What happens when you run the two assert statements?
  - Why does one of them fail?
  - How small is the difference between the two sums?
  - Why is np.isclose() the preferred method for comparing floating point
    results?
"""

# Your code here


# ==============================================================================
# PROBLEM 3: Manual and NumPy Equality Testing
# ==============================================================================
"""
We want to check whether two arrays are exactly equal.

Part A (manual test):
  - Create two arrays a = np.array([1, 2, 3]) and b = np.array([1, 2, 3]).
  - Use a for loop to compare each element.
  - Set all_equal = True if all elements match, otherwise False.
    (Change the boolean inside the for loop if an element differs.)
  - At the end, use assert all_equal for testing.

Part B (NumPy testing):
  - Do the same check again using np.testing.assert_array_equal.
    np.testing.assert_array_equal checks whether two arrays have exactly the
    same shape and elements. If they differ, it raises an AssertionError.
"""

# Your code here


# ==============================================================================
# PROBLEM 4: Shape and dtype Testing
# ==============================================================================
"""
Create a NumPy array of size (n x n) filled with numbers from 0 up to
(n^2 - 1).

  - Test that the array has the correct shape (n, n) using both assert and
    np.testing.assert_array_equal.
  - Test that the array's dtype is int64 using assert.
"""

# Your code here


# ==============================================================================
# PROBLEM 5: Edge Case Testing
# ==============================================================================
"""
Write code that computes the mean of a NumPy array.

  - Test the result on a normal case like [1, 2, 3].
  - Test the result on the edge case of an empty array, confirming that the
    result is np.nan.
  - Use assert (and np.isnan where needed).
"""

# Your code here


# ==============================================================================
# PROBLEM 6: Array Equality with np.testing
# ==============================================================================
"""
For an array of values between 0 and pi, compute (sin^2(x) + cos^2(x)).

  - Test that all results are equal to 1 within a small tolerance.
  - Use np.testing.assert_allclose for the test.

np.testing.assert_allclose checks whether two arrays are approximately
equal, allowing for small differences. The atol parameter sets the absolute
tolerance, which is the maximum absolute difference allowed between
elements.
"""

# Your code here


# ==============================================================================
# SECTION 2: DICTIONARIES
# ==============================================================================

# ==============================================================================
# PROBLEM 7: Course Profile
# ==============================================================================
"""
You are building a simple profile to track one student's information for
this course.

7.1: Create and access
  - Create a dictionary named courseProfile with the following key-value
    pairs:
      'name':   your name (as a string)
      'course': 'EK125'
      'year':   your graduation year (as an integer)
      'gpa':    3.5
  - Print the value associated with the key 'name'.
  - Print the number of key-value pairs using len().
"""

# Your code here


# ==============================================================================
# PROBLEM 7.2: Checking Keys and Updating Values
# ==============================================================================
"""
Using courseProfile:
  - Check whether the key 'major' is in the dictionary and print the result.
  - Check whether the key 'gpa' is NOT in the dictionary and print the
    result.
  - Add a new key-value pair: 'major' with your intended major as a string.
  - Update your 'gpa' to 3.8.
  - Print the updated dictionary.
"""

# Your code here


# ==============================================================================
# PROBLEM 7.3: Removing Entries and Using get() Safely
# ==============================================================================
"""
Using courseProfile:
  - Remove the 'gpa' key using the del command.
  - Try to retrieve the value for 'gpa' using get(). Print the result. (It
    should return None since the key no longer exists.)
  - Try again, but this time supply a default value of -1 if the key is not
    found. Print the result.
  - Print the final dictionary to confirm gpa is gone.
"""

# Your code here


# ==============================================================================
# PROBLEM 8: Lab Sensor Readings
# ==============================================================================
"""
A dictionary stores the most recent temperature reading (in Celsius) from
sensors placed around a lab:

    sensorReadings = {
        'sensor_A': 22.1,
        'sensor_B': 24.7,
        'sensor_C': 21.8,
        'sensor_D': 26.3,
        'sensor_E': 23.5
    }

8.1: Iterate using keys() and values()
  - Use .keys() to print the name of each sensor on its own line.
  - Use .values() to compute and print the average temperature across all
    sensors. Round to two decimal places.
    (Hint: you can sum a collection of values with sum() and count them
    with len().)
"""

sensorReadings = {
    'sensor_A': 22.1,
    'sensor_B': 24.7,
    'sensor_C': 21.8,
    'sensor_D': 26.3,
    'sensor_E': 23.5
}

# Your code here


# ==============================================================================
# PROBLEM 8.2: Iterate Using items() and Flag High Readings
# ==============================================================================
"""
Using sensorReadings:
  - Use .items() to loop over all key-value pairs.
  - Print each sensor name and its reading in the format:
      sensor_A: 22.1 C
  - Inside the same loop, if a sensor reading is above 25.0 C, also print a
    warning:
      WARNING: sensor_D is above threshold!
"""

# Your code here


# ==============================================================================
# PROBLEM 9: List of Dictionaries
# ==============================================================================
"""
The list below stores information about members of an engineering project
team. Each member is represented as a dictionary.

    team = [
        {'name': 'Amara',  'year': 2, 'role': 'Mechanical', 'gpa': 3.9},
        {'name': 'Ben',    'year': 1, 'role': 'Electrical',  'gpa': 3.4},
        {'name': 'Celia',  'year': 3, 'role': 'Civil',       'gpa': 3.7},
        {'name': 'Dario',  'year': 1, 'role': 'Mechanical',  'gpa': 3.2},
        {'name': 'Evelyn', 'year': 2, 'role': 'Electrical',  'gpa': 3.8},
    ]

9.1: Access and display
  - Print the name and role of the first team member using indexing.
  - Loop over the entire list and print each member's name and GPA in the
    format:
      Amara - GPA: 3.9
"""

team = [
    {'name': 'Amara',  'year': 2, 'role': 'Mechanical', 'gpa': 3.9},
    {'name': 'Ben',    'year': 1, 'role': 'Electrical',  'gpa': 3.4},
    {'name': 'Celia',  'year': 3, 'role': 'Civil',       'gpa': 3.7},
    {'name': 'Dario',  'year': 1, 'role': 'Mechanical',  'gpa': 3.2},
    {'name': 'Evelyn', 'year': 2, 'role': 'Electrical',  'gpa': 3.8},
]

# Your code here


# ==============================================================================
# PROBLEM 9.2: Filter and Compute
# ==============================================================================
"""
Using the team list:
  - Loop over the list and print the name of every team member whose GPA is
    3.7 or above.
  - Calculate and print the average GPA of all first-year students
    (year == 1). If there are no first-year students, print a message
    saying so instead. Round to two decimal places.
"""

# Your code here


# ==============================================================================
# PROBLEM 10: Dictionary with List Values
# ==============================================================================
"""
A dictionary stores the quiz scores (out of 20) for each student over four
quizzes:

    quizScores = {
        'Alice':   [18, 15, 19, 17],
        'Bob':     [12, 14, 11, 16],
        'Charlie': [20, 18, 17, 19],
        'Dana':    [15, 16, 14, 18]
    }

10.1: Access and iterate
  - Print Alice's list of scores.
  - Print Alice's score on the third quiz (index 2) only.
  - Loop over quizScores using .items() to print each student's name and
    their average quiz score, rounded to one decimal place, in the format:
      Alice: avg = 17.2
"""

quizScores = {
    'Alice':   [18, 15, 19, 17],
    'Bob':     [12, 14, 11, 16],
    'Charlie': [20, 18, 17, 19],
    'Dana':    [15, 16, 14, 18]
}

# Your code here


# ==============================================================================
# PROBLEM 10.2: Dictionary Comprehension
# ==============================================================================
"""
Using quizScores:
  - Create a new dictionary named avgScores using a dictionary comprehension.
    Each key should be a student name, and each value should be that
    student's average quiz score (rounded to one decimal place).
  - Print avgScores.

Then, using avgScores:
  - Use a dictionary comprehension to create a dictionary named honorRoll
    containing only the students whose average score is 17.0 or above.
  - Print honorRoll.
"""

# Your code here
