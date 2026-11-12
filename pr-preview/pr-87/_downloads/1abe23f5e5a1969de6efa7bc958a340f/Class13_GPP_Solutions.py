"""
Class 13 GPP Solutions: User-Defined Functions, Scope, and Copying
EK125
"""

# ==============================================================================
# PART 1: Understanding Parameter Passing
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 1.1: Predict the Output (Immutable Types)
# ------------------------------------------------------------------------------

def updateScore(score):
    score = score + 10
    print(f"Inside function: {score}")

playerScore = 50
updateScore(playerScore)
print(f"Outside function: {playerScore}")

# EXPECTED OUTPUT:
# Inside function: 60
# Outside function: 50
#
# EXPLANATION:
# Integers are IMMUTABLE. When we pass playerScore to the function, Python
# creates a NEW local variable called 'score' with the value 50. When we do
# score = score + 10, we're modifying the LOCAL variable, not the original.
# The original playerScore remains unchanged.
#
# KEY CONCEPT: Pass by value for immutable types


# ------------------------------------------------------------------------------
# Problem 1.2: Predict the Output (Mutable Types - Modifying)
# ------------------------------------------------------------------------------

def updateScores(scores):
    scores.append(100)
    print(f"Inside function: {scores}")

playerScores = [85, 90, 78]
updateScores(playerScores)
print(f"Outside function: {playerScores}")

# EXPECTED OUTPUT:
# Inside function: [85, 90, 78, 100]
# Outside function: [85, 90, 78, 100]
#
# EXPLANATION:
# Lists are MUTABLE. When we pass playerScores to the function, we're passing
# a REFERENCE to the same list object in memory. When we call .append(), we're
# modifying the actual list object, so the change is visible outside the function.
#
# KEY CONCEPT: Pass by reference for mutable types


# ------------------------------------------------------------------------------
# Problem 1.3: Predict the Output (Mutable Types - Reassigning)
# ------------------------------------------------------------------------------

def resetScores(scores):
    scores = [0, 0, 0]
    print(f"Inside function: {scores}")

playerScores = [85, 90, 78]
resetScores(playerScores)
print(f"Outside function: {playerScores}")

# EXPECTED OUTPUT:
# Inside function: [0, 0, 0]
# Outside function: [85, 90, 78]
#
# EXPLANATION:
# Even though lists are mutable, REASSIGNMENT creates a NEW local variable.
# When we do scores = [0, 0, 0], we're creating a NEW list and making the
# local variable 'scores' point to it. The original playerScores list is
# unaffected. This is different from modifying the list in place (like .append()).
#
# KEY CONCEPT: Reassignment always creates a new local variable


# ==============================================================================
# PART 2: Functions that Return Values
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 2.1: Inches to Feet Converter
# ------------------------------------------------------------------------------

def inchesToFeet(inches):
    """Convert inches to feet.

    Args:
        inches: Number of inches (int)

    Returns:
        Number of feet (float)
    """
    return inches / 12

# Test:
print(inchesToFeet(36))   # Should print 3.0
print(inchesToFeet(15))   # Should print 1.25
help(inchesToFeet)


# ------------------------------------------------------------------------------
# Problem 2.2: Sign Function
# ------------------------------------------------------------------------------

def sign(number):
    """Return the sign of a number.

    Args:
        number: A numeric value (int or float)

    Returns:
        1 if positive, 0 if zero, -1 if negative
    """
    if number > 0:
        return 1
    elif number == 0:
        return 0
    else:
        return -1

# Test all three cases:
print(sign(5))      # Should print 1
print(sign(0))      # Should print 0
print(sign(-3))     # Should print -1


# ------------------------------------------------------------------------------
# Problem 2.3: Rectangle Calculator
# ------------------------------------------------------------------------------

def rectangleCalculator(length, width):
    """Calculate area and perimeter of a rectangle.

    Args:
        length: Length of rectangle
        width: Width of rectangle

    Returns:
        Tuple of (area, perimeter)
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Test and unpack:
rectArea, rectPerimeter = rectangleCalculator(5, 3)
print(f"Area: {rectArea}, Perimeter: {rectPerimeter}")  # Area: 15, Perimeter: 16


# ------------------------------------------------------------------------------
# Problem 2.4: Cumulative Product
# ------------------------------------------------------------------------------

def cumulativeProduct(numbers):
    """Create a list of running products.

    Args:
        numbers: List of numbers

    Returns:
        List of cumulative products
    """
    result = []
    product = 1
    for num in numbers:
        product = product * num
        result.append(product)
    return result

# Test:
print(cumulativeProduct([4, 2, 5]))     # [4, 8, 40]
print(cumulativeProduct([1, 2, 3, 4]))  # [1, 2, 6, 24]


# ==============================================================================
# PART 3: Functions that Print (No Return)
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 3.1: Star Box Printer
# ------------------------------------------------------------------------------

def printStarBox(rows, columns):
    """Print a box of stars.

    Args:
        rows: Number of rows to print
        columns: Number of stars per row
    """
    for i in range(rows):
        print('*' * columns)

# Test:
printStarBox(3, 5)
# Output:
# *****
# *****
# *****


# ------------------------------------------------------------------------------
# Problem 3.2: Understanding None
# ------------------------------------------------------------------------------

result = printStarBox(2, 4)
print(f"Return value: {result}")  # Return value: None

# EXPLANATION:
# Functions that don't have a return statement return None by default.


# ------------------------------------------------------------------------------
# Problem 3.3: Random String Selector
# ------------------------------------------------------------------------------

import random

def printRandomString(stringList):
    """Print a random string from a list.

    Args:
        stringList: List of strings to choose from
    """
    randomString = random.choice(stringList)
    print(randomString)

# Test:
fruits = ["apple", "banana", "cherry", "date"]
printRandomString(fruits)  # Prints a random fruit


# ==============================================================================
# PART 4: Working with Keyword Arguments
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 4.1: Student Record System
# ------------------------------------------------------------------------------

def createStudent(name, studentId, gpa=0.0, major="Undeclared", credits=0):
    """Create a student record dictionary."""
    return {
        'name': name,
        'id': studentId,
        'gpa': gpa,
        'major': major,
        'credits': credits
    }

# Test students:
student1 = createStudent("Alice Smith", 12345)
student2 = createStudent("Bob Jones", 23456, major="Computer Science")
student3 = createStudent("Charlie Brown", 34567, gpa=3.8, credits=45)
student4 = createStudent("Diana Prince", 45678, major="Biology", gpa=3.9, credits=60)

# Print to verify:
print(student1)
print(student2)
print(student3)
print(student4)

# WHY KEYWORD ARGUMENTS ARE USEFUL:
# - Don't have to remember parameter order
# - Can skip defaults we don't want to change
# - More readable: createStudent("Alice", 12345, gpa=3.5) is clearer than
#   createStudent("Alice", 12345, 3.5, "Undeclared", 0)


# ==============================================================================
# PART 5: Variable Scope (LEGB Rule)
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 5.1: Fix the Broken Code
# ------------------------------------------------------------------------------

# SOLUTION 1: Return the count and reassign (BEST PRACTICE)
studentsProcessed = 0

def processStudent(name, count):
    """Process a student and return updated count."""
    print(f"Processing {name}")
    count = count + 1
    return count

studentsProcessed = processStudent("Alice", studentsProcessed)
studentsProcessed = processStudent("Bob", studentsProcessed)
studentsProcessed = processStudent("Charlie", studentsProcessed)
print(f"Total processed: {studentsProcessed}")  # Prints 3


# SOLUTION 2: Use a list (works because lists are mutable)
studentCount = [0]  # List with one element

def processStudent2(name):
    """Process a student using a mutable container."""
    print(f"Processing {name}")
    studentCount[0] = studentCount[0] + 1
    return f"Processed: {name}"

processStudent2("Alice")
processStudent2("Bob")
processStudent2("Charlie")
print(f"Total processed: {studentCount[0]}")  # Prints 3

# 💡 Note: Solution 1 is better style -- avoid depending on mutable objects to
# track state. We don't teach the `global` keyword in this course since
# relying on it is bad practice.


# ------------------------------------------------------------------------------
# Problem 5.2: Understanding Variable Lookup (LEGB)
# ------------------------------------------------------------------------------

x = 10

def outer():
    x = 20

    def inner():
        print(f"Inner sees x = {x}")

    inner()
    print(f"Outer sees x = {x}")

outer()
print(f"Global sees x = {x}")

# EXPECTED OUTPUT:
# Inner sees x = 20
# Outer sees x = 20
# Global sees x = 10

# EXPLANATION OF LEGB:
# L = Local: Variables defined in the current function
# E = Enclosing: Variables in the enclosing function (for nested functions)
# G = Global: Variables defined at module level
# B = Built-in: Python's built-in names (like print, len, etc.)
#
# When Python looks up a variable, it searches in this order: L -> E -> G -> B


# ==============================================================================
# PART 6: Copying Lists
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 6.1: Protecting Your Data
# ------------------------------------------------------------------------------

grades = [85, 92, 78, 90, 88]

# WRONG WAY:
sortedGrades1 = grades  # This creates an ALIAS, not a copy!
sortedGrades1.sort()
print(f"Original: {grades}")        # [78, 85, 88, 90, 92] - MODIFIED!
print(f"Sorted: {sortedGrades1}")   # [78, 85, 88, 90, 92]

# WHAT WENT WRONG:
# sortedGrades1 and grades both point to the SAME list object in memory.
# When we sort one, we're sorting the actual list, so both names see the change.


# RIGHT WAY:
grades = [85, 92, 78, 90, 88]
sortedGrades2 = grades.copy()  # Creates a NEW list with same values
sortedGrades2.sort()
print(f"Original: {grades}")        # [85, 92, 78, 90, 88] - unchanged!
print(f"Sorted: {sortedGrades2}")   # [78, 85, 88, 90, 92]


# ------------------------------------------------------------------------------
# Problem 6.2: Shallow vs Deep Copy Challenge
# ------------------------------------------------------------------------------

import copy

# Shallow copy problem:
students = [
    ["Alice", [85, 90, 88]],
    ["Bob", [78, 82, 80]]
]

shallowCopy = students.copy()
shallowCopy[0][1].append(95)  # Add grade to Alice

print(f"Original: {students}")      # Alice has 95 added!
print(f"Shallow copy: {shallowCopy}")

# WHAT HAPPENED:
# .copy() creates a new list, but the INNER lists are still shared!
# So both students and shallowCopy have references to the same grade lists.


# Deep copy solution:
students = [
    ["Alice", [85, 90, 88]],
    ["Bob", [78, 82, 80]]
]

deepCopy = copy.deepcopy(students)
deepCopy[0][1].append(95)

print(f"Original: {students}")      # Alice still has 3 grades
print(f"Deep copy: {deepCopy}")     # Alice has 4 grades

# EXPLANATION:
# copy.deepcopy() recursively copies ALL nested objects, so the deep copy
# is completely independent from the original.


# ==============================================================================
# PART 7: Lambda Functions
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 7.1: Lambda Basics
# ------------------------------------------------------------------------------

add_eh = lambda s: s + ", eh?"

# Test:
print(add_eh("Nice weather today"))  # Nice weather today, eh?


# ------------------------------------------------------------------------------
# Problem 7.2: Lambda with Exclamation
# ------------------------------------------------------------------------------

add_excite = lambda s: s + "!!!"

# Test:
print(add_excite("Wow"))  # Wow!!!


# ==============================================================================
# PART 8: Mixed Return and Print Functions
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 8.1: Menu Function
# ------------------------------------------------------------------------------

def showMenuAndGetChoice():
    """Display menu and return user's valid choice."""
    print("\n=== MENU ===")
    print("1. Option A")
    print("2. Option B")
    print("3. Option C")
    print("============")

    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Test (commented out to avoid blocking):
# userChoice = showMenuAndGetChoice()
# print(f"You selected: {userChoice}")


# ------------------------------------------------------------------------------
# Problem 8.2: String Reverser
# ------------------------------------------------------------------------------

def stringReverse(text):
    """Reverse a string and return the result.

    Args:
        text: String to reverse

    Returns:
        Reversed string
    """
    return text[::-1]

# Alternative solution using a loop:
def stringReverse2(text):
    """Reverse a string using a loop."""
    result = ""
    for char in text:
        result = char + result
    return result

# Test:
print(stringReverse("Hello"))   # olleH
print(stringReverse2("World"))  # dlroW


# ==============================================================================
# PART 9: Putting It All Together
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 9.1: Class Roster with Bonus Points
# ------------------------------------------------------------------------------

def addBonus(students, bonusPoints=5, makeBackup=True):
    """
    Add bonus points to all students.

    Args:
        students: List of [name, score] pairs
        bonusPoints: Points to add (default: 5)
        makeBackup: If True, don't modify original (default: True)

    Returns:
        List with bonus points added
    """
    # Make a copy if requested
    if makeBackup:
        studentsCopy = copy.deepcopy(students)  # Use deepcopy for nested lists
    else:
        studentsCopy = students  # Use the original list directly

    # Add bonus points to each student
    for student in studentsCopy:
        student[1] = student[1] + bonusPoints

    return studentsCopy


# Test cases:
roster = [["Alice", 85], ["Bob", 90]]

# Test 1: With backup (default)
result1 = addBonus(roster)
print(f"Original: {roster}")  # [["Alice", 85], ["Bob", 90]] - unchanged!
print(f"Result: {result1}")    # [["Alice", 90], ["Bob", 95]]

# Test 2: Without backup
roster2 = [["Charlie", 78], ["Diana", 92]]
result2 = addBonus(roster2, bonusPoints=10, makeBackup=False)
print(f"Original: {roster2}")  # [["Charlie", 88], ["Diana", 102]] - modified!
print(f"Result: {result2}")    # [["Charlie", 88], ["Diana", 102]] - same object


# ==============================================================================
# PART 10: Challenge Problems
# ==============================================================================

# ------------------------------------------------------------------------------
# Challenge 10.1: Interpolate Function
# ------------------------------------------------------------------------------

def interpolate(point1, point2, x_i):
    """
    Linear interpolation between two points.

    Args:
        point1: Tuple (x0, y0)
        point2: Tuple (x1, y1)
        x_i: X value to interpolate

    Returns:
        Interpolated y value
    """
    x0, y0 = point1
    x1, y1 = point2

    # Check if x_i is in valid range
    if x_i < x0 or x_i > x1:
        return "Error: x_i must be between x0 and x1"

    # Calculate slope
    slope = (y1 - y0) / (x1 - x0)

    # Calculate interpolated value
    y_i = y0 + slope * (x_i - x0)

    return y_i

# Test:
print(interpolate((0, 0), (1, 0.5), 0.5))   # 0.25
print(interpolate((0, 0), (1, 0.5), 0.9))   # 0.45
print(interpolate((0, 0), (1, 0.5), 1.5))   # Error message


# ------------------------------------------------------------------------------
# Challenge 10.2: Prompt for Positive Number
# ------------------------------------------------------------------------------

def promptForPositive(prompt_text):
    """
    Prompt user for a positive number with error checking.

    Args:
        prompt_text: Description of what to enter (e.g., "length")

    Returns:
        Valid positive number
    """
    while True:
        try:
            value = float(input(f"Enter {prompt_text}: "))
            if value > 0:
                return value
            else:
                print("Error: Value must be positive.")
        except ValueError:
            print("Error: Please enter a valid number.")

# Test (commented to avoid blocking):
# length = promptForPositive("length")
# print(f"You entered: {length}")


# ------------------------------------------------------------------------------
# Challenge 10.3: Type-Dependent Return
# ------------------------------------------------------------------------------

def typeDependentFunction(value):
    """
    Return different results based on input type.

    Args:
        value: Can be int, float, list, or string

    Returns:
        Different output depending on type
    """
    if isinstance(value, int):
        return value ** 2
    elif isinstance(value, float):
        return round(value, 2)
    elif isinstance(value, list):
        return len(value)
    elif isinstance(value, str):
        return value.upper()
    else:
        return "Unsupported type"

# Test with different types:
print(typeDependentFunction(5))              # 25
print(typeDependentFunction(3.14159))        # 3.14
print(typeDependentFunction([1, 2, 3, 4]))   # 4
print(typeDependentFunction("hello"))        # HELLO


# ------------------------------------------------------------------------------
# Challenge 10.4: Identity Matrix
# ------------------------------------------------------------------------------

def createIdentityMatrix(size):
    """
    Create an identity matrix.

    Args:
        size: Number of rows and columns

    Returns:
        Nested list representing identity matrix
    """
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

# Test:
identity3 = createIdentityMatrix(3)
for row in identity3:
    print(row)
# Output:
# [1, 0, 0]
# [0, 1, 0]
# [0, 0, 1]
