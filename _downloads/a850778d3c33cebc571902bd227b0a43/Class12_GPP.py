"""
Class 12 GPP: Python Dictionaries
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
# PROBLEM 1: Dictionary Basics
# ==============================================================================
"""
Today we will investigate Python dictionaries. Dictionaries are key-value
stores where each key is unique. You will explore various operations on
dictionaries, including creation, modification, and iteration.

1.1: Make a dictionary
  - Create a dictionary named `hurricane` with the following key-value pairs:
      'name': 'Sandy'
      'year': 2012
      'category': 3
  - Print the value associated with the key 'year'.
"""

# Your code here


# ==============================================================================
# PROBLEM 1.2: Add New Key-Value Pairs
# ==============================================================================
"""
  - Add a new key-value pair to the hurricane dictionary: 'pressure': 940
  - Change the 'category' value to 4.
  - Print the updated dictionary.
"""

# Your code here


# ==============================================================================
# PROBLEM 1.3: Loop Over Key-Value Pairs
# ==============================================================================
"""
Use a loop to print all keys and values from the hurricane dictionary
in the format:  Key: Value
"""

# Your code here


# ==============================================================================
# PROBLEM 2: Book Information
# ==============================================================================
"""
You are tasked with storing information about a book in a dictionary.
Perform the following steps:

1. Create a dictionary named `book` with the following key-value pairs:
     'title': 'To Kill a Mockingbird'
     'author': 'Harper Lee'
     'year_published': 1960
     'genre': 'Fiction'
2. Print the value associated with the key 'author'.
3. Check if the key 'pages' exists in the dictionary and print the result.
   (Hint: use `in`!)
4. Use the len() function to determine the number of key-value pairs in
   the dictionary and print it.
"""

# Your code here


# ==============================================================================
# PROBLEM 3: get() and pop() on a Smartphone Dictionary
# ==============================================================================
"""
You are given a dictionary representing a smartphone:

    smartphone = {
        'brand': 'Apple',
        'model': 'iPhone 13',
        'year_released': 2021,
        'price': 799
    }

1. Use the get() method to retrieve the value for the key 'price'.
2. Add a new key-value pair: 'storage': '128GB'.
3. Update the 'price' to 749.
4. Remove the 'year_released' key using the pop() method.
5. Print the updated dictionary.
"""

smartphone = {
    'brand': 'Apple',
    'model': 'iPhone 13',
    'year_released': 2021,
    'price': 799
}

# Your code here


# ==============================================================================
# PROBLEM 4: clear() on a Shopping Cart Dictionary
# ==============================================================================
"""
You are managing a dictionary that tracks items in a shopping cart:

    shopping_cart = {
        'apple': 4,
        'banana': 6,
        'milk': 2,
        'bread': 1
    }

1. Print the current contents of the shopping_cart.
2. Use the clear() method to remove all items from the dictionary.
3. Print the dictionary again to confirm it is empty.
"""

shopping_cart = {
    'apple': 4,
    'banana': 6,
    'milk': 2,
    'bread': 1
}

# Your code here


# ==============================================================================
# PROBLEM 5: .keys(), .values() and .items()
# ==============================================================================
"""
You are given a dictionary representing the stock of items in a grocery store:

    store_stock = {
        'apples': 50,
        'bananas': 30,
        'milk': 20,
        'bread': 15
    }

1. Use the .keys() method to print a list of all items in the store.
2. Use the .values() method to calculate and print the total stock of all
   items.
3. Use the .items() method to print each item and its stock as tuples.
4. Use a loop to print each item and its stock in the format:
     "Item: <item>, Stock: <stock>"
"""

store_stock = {
    'apples': 50,
    'bananas': 30,
    'milk': 20,
    'bread': 15
}

# Your code here


# ==============================================================================
# PROBLEM 6: Challenge -- Nested Dictionaries
# ==============================================================================
"""
You are managing data about students and their test scores. The data is
stored in a dictionary where each key is a student's name, and the value
is another dictionary containing the student's scores for Math, Science,
and English.

    students_scores = {
        'Alice':   {'Math': 85, 'Science': 90, 'English': 88},
        'Bob':     {'Math': 78, 'Science': 82, 'English': 84},
        'Charlie': {'Math': 92, 'Science': 88, 'English': 91},
        'Dana':    {'Math': 89, 'Science': 94, 'English': 87}
    }

1. Print the scores for 'Alice'.
2. Retrieve and print the Science score for 'Charlie'.
3. Add a new student, 'Eve', with the following scores:
     Math: 88, Science: 86, English: 89
4. Calculate and print the average Math score for all students.
5. Use a loop to print each student's name and their average score in
   the format:  "Student: <name>, Average Score: <average>"
"""

students_scores = {
    'Alice':   {'Math': 85, 'Science': 90, 'English': 88},
    'Bob':     {'Math': 78, 'Science': 82, 'English': 84},
    'Charlie': {'Math': 92, 'Science': 88, 'English': 91},
    'Dana':    {'Math': 89, 'Science': 94, 'English': 87}
}

# Your code here
