"""
Class 10: Mastering Slicing in Python - Group Practice Problems
EK125 - Spring 2026

SOLUTION KEY
"""

# ==============================================================================
# WARM-UP: Quick Slicing Drills
# ==============================================================================

word = "Python"
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print("=" * 60)
print("WARM-UP: Quick Slicing Drills")
print("=" * 60)

print(word[:3])          # 1. "Pyt"
print(word[3:])          # 2. "hon"
print(word[2:4])         # 3. "th"
print(numbers[:3])       # 4. [10, 20, 30]
print(numbers[3:6])      # 5. [40, 50, 60]
print(numbers[6:])       # 6. [70, 80, 90]
print(numbers[::2])      # 7. [10, 30, 50, 70, 90]
print(numbers[1::2])     # 8. [20, 40, 60, 80]
print(numbers[-1])       # 9.  90  (single value)
print(numbers[-3:])      # 10. [70, 80, 90]

# COMMON MISTAKES:
# #3: word[2:3] only gives "t" - end index is exclusive, need [2:4]
# #9 vs #10: numbers[-1] gives 90, numbers[-1:] gives [90] - good to flag the difference


# ==============================================================================
# WARM-UP 2: Negative Index Drills
# ==============================================================================

data = [5, 10, 15, 20, 25, 30, 35, 40]
text = "HelloWorld"

print("\n" + "=" * 60)
print("WARM-UP 2: Negative Index Drills")
print("=" * 60)

print(data[-3:])         # 1. [30, 35, 40]
print(data[:-3])         # 2. [5, 10, 15, 20, 25]
print(text[-5:])         # 3. "World"
print(text[:-5])         # 4. "Hello"
print(data[-1:])         # 5. [40] as a list
print(data[-1])          # 6.  40  as a single value

# COMMON MISTAKES:
# #2: data[-3:] is wrong (gives last 3, not all-but-last-3) - reinforce :-n vs -n:
# #5 vs #6: This is the classic gotcha - use to reinforce the -1 vs -1: discussion


# ==============================================================================
# PROBLEM 1: Basic Slice Practice
# ==============================================================================

print("\n" + "=" * 60)
print("PROBLEM 1: Basic Slice Practice")
print("=" * 60)

word = input("Enter a word: ")

first3 = word[:3]
print(f"First 3 characters: {first3}")

last3 = word[-3:]
print(f"Last 3 characters: {last3}")

chars2to5 = word[2:5]
print(f"Characters 2 to 5: {chars2to5}")

everyOther = word[::2]
print(f"Every other character: {everyOther}")

# COMMON MISTAKES:
# "Characters 2 to 5": students may write word[2:6] - remind them end is exclusive
# "Every other": students may write word[0:len(word):2] - correct but verbose; [::2] is cleaner


# ==============================================================================
# PROBLEM 2: Working with Negative Indices
# ==============================================================================

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("\n" + "=" * 60)
print("PROBLEM 2: Negative Indices")
print("=" * 60)

print(f"Last element: {numbers[-1]}")
print(f"Last 4 elements: {numbers[-4:]}")
print(f"All but last 2: {numbers[:-2]}")
print(f"Second-to-last: {numbers[-2]}")

# COMMON MISTAKES:
# Last 4: numbers[-4] gives a single value, not a list - must include the colon: numbers[-4:]
# All but last 2: numbers[-2:] is the opposite of what's wanted


# ==============================================================================
# PROBLEM 3: Step Practice
# ==============================================================================

letters = "abcdefghijklmnop"

print("\n" + "=" * 60)
print("PROBLEM 3: Step Practice")
print("=" * 60)

print(f"Every 2nd character: {letters[::2]}")       # acegikmo
print(f"Every 3rd character: {letters[::3]}")       # adgjmp
print(f"Every 2nd starting from 1: {letters[1::2]}")  # bdfhjlnp
print(f"Every 4th starting from 2: {letters[2::4]}")  # cgko


# ==============================================================================
# PROBLEM 4: Reversing Practice
# ==============================================================================

print("\n" + "=" * 60)
print("PROBLEM 4: Reversing Practice")
print("=" * 60)

word = input("Enter a word: ")
midpoint = len(word) // 2

print(f"Reversed: {word[::-1]}")
print(f"First half reversed: {word[:midpoint][::-1]}")
print(f"Second half reversed: {word[midpoint:][::-1]}")
print(f"Every other character reversed: {word[::-2]}")

# NOTE: word[::-2] steps backwards through the string with step -2, giving
# every other character starting from the last. For "Python" this gives "nhy".
# This is equivalent to taking every other character from the reversed string.
#
# A common alternative students may try: word[::2][::-1]
# For "Python" this gives "otP" (every other from the front, then reversed).
# Both approaches are defensible - if a group gets "otP" with clear reasoning,
# accept it and show them the [::-2] version as a discussion point.


# ==============================================================================
# PROBLEM 5: Palindrome Checker
# ==============================================================================

print("\n" + "=" * 60)
print("PROBLEM 5: Palindrome Checker")
print("=" * 60)

word = input("Enter a word: ")

if word == word[::-1]:
    print(f'"{word}" is a palindrome!')
else:
    print(f'"{word}" is not a palindrome.')

# COMMON MISTAKES:
# Students may use word.reverse() - this doesn't work on strings (strings are immutable)
# Students may forget the quotes around the word in the output - minor, don't deduct


# ==============================================================================
# PROBLEM 6: Extracting Parts of a Sentence
# ==============================================================================

print("\n" + "=" * 60)
print("PROBLEM 6: Extracting Parts of a Sentence")
print("=" * 60)

sentence = input("Enter a sentence: ")

firstSpace = sentence.index(' ')     # position of the first space
lastSpace = sentence.rfind(' ')      # position of the last space

firstWord = sentence[:firstSpace]
lastWord = sentence[lastSpace + 1:]  # +1 to skip past the space itself
middle = sentence[firstSpace + 1:lastSpace]

print(f"First word: {firstWord}")
print(f"Last word: {lastWord}")
print(f"Middle: {middle}")

# COMMON MISTAKES:
# lastWord = sentence[lastSpace:] gives " fox" with a leading space - need +1
# middle = sentence[firstSpace:lastSpace] gives " quick brown" with a leading space - need +1
# Students may use .split() - this works but isn't practicing slicing; redirect them


# ==============================================================================
# PROBLEM 7: Combining Slices
# ==============================================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\n" + "=" * 60)
print("PROBLEM 7: Combining Slices")
print("=" * 60)

# First 3 elements + every 2nd from middle (indices 3-8) + last 2 elements
result = numbers[:3] + numbers[3:9:2] + numbers[-2:]
print(f"Result: {result}")

# COMMON MISTAKES:
# Middle section: numbers[3:8:2] misses index 8 - end is exclusive so need [3:9:2]
# Last 2: numbers[8:] also works for this specific list - accept it


# ==============================================================================
# PROBLEM 8: Slice Assignment
# ==============================================================================

print("\n" + "=" * 60)
print("PROBLEM 8: Slice Assignment")
print("=" * 60)

# Task 1: Replace indices 2, 3, 4 with the single value 99
list1 = [10, 20, 30, 40, 50, 60]
print(f"Task 1 original: {list1}")
list1[2:5] = [99]         # replacing 3 elements with 1 - list shrinks
print(f"Task 1 after:    {list1}")

# Task 2: Replace every third element with "SKIP"
list2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print(f"\nTask 2 original: {list2}")
list2[::3] = ["SKIP", "SKIP", "SKIP"]   # step assignment requires matching length
print(f"Task 2 after:    {list2}")

# Task 3: Insert [100, 200, 300] between indices 3 and 4
list3 = [1, 2, 3, 4, 5]
print(f"\nTask 3 original: {list3}")
list3[3:3] = [100, 200, 300]    # empty slice at index 3 inserts without removing
print(f"Task 3 after:    {list3}")

# COMMON MISTAKES:
# Task 1: list1[2:5] = 99 raises TypeError - must assign a list, not a bare value
# Task 2: list2[::3] = ["SKIP"] raises ValueError (length mismatch) - must match slice length
#          This is a great teaching moment about step-slice assignment rules
# Task 3: list3[3:4] = [100, 200, 300] replaces index 3 instead of inserting -
#          must use [3:3] (empty slice) to insert without removing
