"""
Class 12 GPP Solutions: Python Dictionaries
EK125 - Spring 2026
"""

# ==============================================================================
# PROBLEM 1 SOLUTION: Dictionary Basics
# ==============================================================================

# --- 1.1: Make a dictionary ---
hurricane = {'name': 'Sandy', 'year': 2012, 'category': 3}
print(hurricane['year'])       # Output: 2012

# ==============================================================================
# PROBLEM 1.2 SOLUTION: Add New Key-Value Pairs
# ==============================================================================

hurricane['pressure'] = 940    # add new key
hurricane['category'] = 4      # update existing key
print(hurricane)
# Output: {'name': 'Sandy', 'year': 2012, 'category': 4, 'pressure': 940}

# ==============================================================================
# PROBLEM 1.3 SOLUTION: Loop Over Key-Value Pairs
# ==============================================================================

for key, value in hurricane.items():
    print(f"{key}: {value}")
# Output:
#   name: Sandy
#   year: 2012
#   category: 4
#   pressure: 940

# ==============================================================================
# PROBLEM 2 SOLUTION: Book Information
# ==============================================================================

book = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'year_published': 1960,
    'genre': 'Fiction'
}

print("Author:", book['author'])             # Output: Harper Lee

has_pages = 'pages' in book
print("Does the 'pages' key exist?", has_pages)   # Output: False

num_pairs = len(book)
print("Number of key-value pairs:", num_pairs)     # Output: 4

# ==============================================================================
# PROBLEM 3 SOLUTION: get() and pop() on a Smartphone Dictionary
# ==============================================================================

smartphone = {
    'brand': 'Apple',
    'model': 'iPhone 13',
    'year_released': 2021,
    'price': 799
}

price = smartphone.get('price')
print("Price:", price)                        # Output: 799

smartphone['storage'] = '128GB'
smartphone['price'] = 749
smartphone.pop('year_released')

print("Updated Dictionary:", smartphone)
# Output: {'brand': 'Apple', 'model': 'iPhone 13', 'price': 749, 'storage': '128GB'}

# ==============================================================================
# PROBLEM 4 SOLUTION: clear() on a Shopping Cart Dictionary
# ==============================================================================

shopping_cart = {
    'apple': 4,
    'banana': 6,
    'milk': 2,
    'bread': 1
}

print("Shopping Cart Contents:", shopping_cart)
# Output: {'apple': 4, 'banana': 6, 'milk': 2, 'bread': 1}

shopping_cart.clear()
print("Shopping Cart after clear():", shopping_cart)   # Output: {}

# ==============================================================================
# PROBLEM 5 SOLUTION: .keys(), .values() and .items()
# ==============================================================================

store_stock = {
    'apples': 50,
    'bananas': 30,
    'milk': 20,
    'bread': 15
}

items = list(store_stock.keys())
print("Items in store:", items)

total_stock = sum(store_stock.values())
print("Total stock:", total_stock)           # Output: 115

print("Item-stock tuples:")
for item_tuple in store_stock.items():
    print(item_tuple)

print("Stock details:")
for item, stock in store_stock.items():
    print(f"Item: {item}, Stock: {stock}")

# ==============================================================================
# PROBLEM 6 SOLUTION: Challenge -- Nested Dictionaries
# ==============================================================================

students_scores = {
    'Alice':   {'Math': 85, 'Science': 90, 'English': 88},
    'Bob':     {'Math': 78, 'Science': 82, 'English': 84},
    'Charlie': {'Math': 92, 'Science': 88, 'English': 91},
    'Dana':    {'Math': 89, 'Science': 94, 'English': 87}
}

print("Alice's Scores:", students_scores['Alice'])

charlie_science = students_scores['Charlie']['Science']
print("Charlie's Science Score:", charlie_science)   # Output: 88

students_scores['Eve'] = {'Math': 88, 'Science': 86, 'English': 89}

math_scores = [scores['Math'] for scores in students_scores.values()]
average_math_score = sum(math_scores) / len(math_scores)
print("Average Math Score:", average_math_score)     # Output: 86.4

print("Student Average Scores:")
for student, scores in students_scores.items():
    average_score = sum(scores.values()) / len(scores)
    print(f"Student: {student}, Average Score: {average_score:.2f}")
# Output:
#   Student: Alice,   Average Score: 87.67
#   Student: Bob,     Average Score: 81.33
#   Student: Charlie, Average Score: 90.33
#   Student: Dana,    Average Score: 90.00
#   Student: Eve,     Average Score: 87.67
