"""
================================================================================
EK125 — Class 15: Scripts, Comments, and Documentation
Group Practice Problems (Teams of 3)
Spring 2026

Team Members:
- Your Name
- Partner 1 Name  
- Partner 2 Name

Instructions:
- Work in groups of THREE
- You MAY use references (readings, slides, internet)
- Do NOT use AI to write code - you need to learn yourself!
- Focus on PROFESSIONAL CODE today - documentation matters!
- Save frequently (Ctrl+S / Cmd+S)
================================================================================
"""

# ==============================================================================
# PROBLEM 1: Good Comments vs. Bad Comments
# ==============================================================================
"""
Below are examples of comments. Identify which are GOOD and which are BAD.
Then rewrite the bad ones to be better.

Remember: Good comments explain WHY, not WHAT. They clarify non-obvious logic.
"""

# Example 1:
x = x + 1  # Add 1 to x
# Is this a good or bad comment?
# 


# Example 2:
# Apply 20% curve because this exam was particularly challenging
final_grade = raw_score * 1.20
# Is this a good or bad comment?
# 


# Example 3:
total = sum(numbers)  # Calculate the total of all numbers
# Is this a good or bad comment?
# 


# Example 4:
# Convert temperature to Celsius for consistency with weather API
temp_c = (temp_f - 32) * 5/9
# Is this a good or bad comment?
# 


# TODO: Find one line of code in your previous homework and write
# a GOOD comment for it (explain WHY, not WHAT)




print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 2: Adding Docstrings to Functions
# ==============================================================================
"""
Below is a function with NO documentation. Add a proper docstring that includes:
- Brief description of what the function does
- Parameters (with types and descriptions)
- Return value (with type and description)
- An example of usage
"""

def calculate_final_grade(homework, quizzes, exams):
    hw_avg = sum(homework) / len(homework)
    quiz_avg = sum(quizzes) / len(quizzes)
    exam_avg = sum(exams) / len(exams)
    
    final = hw_avg * 0.27 + quiz_avg * 0.20 + exam_avg * 0.30 + 18
    
    return final

# TODO: Rewrite the function above with a proper docstring




# Test your documented function:
hw = [85, 90, 88, 92]
quiz = [78, 82, 85, 80, 88]
exam = [82, 88, 85]

grade = calculate_final_grade(hw, quiz, exam)
print(f"Final grade: {grade:.1f}")

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 3: Script Organization
# ==============================================================================
"""
Below is messy code. Reorganize it properly using these principles:

1. Module docstring at the top
2. Imports next
3. Constants (if any)
4. Function definitions (with docstrings!)
5. Main program code
6. Use if __name__ == "__main__": pattern

Messy code to fix:
"""

def calculate_bmi(weight, height):
    return weight / (height ** 2)

import math

result = calculate_bmi(70, 1.75)
print(f"BMI: {result:.1f}")

PI = 3.14159

def circle_area(radius):
    return PI * radius ** 2

area = circle_area(5)
print(f"Area: {area:.2f}")

# TODO: Rewrite all the above code in proper order below:
"""
Module docstring goes here
"""







print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 4: Professional Temperature Converter
# ==============================================================================
"""
Create a COMPLETE, professionally documented temperature conversion script.

Requirements:
1. Module docstring at top explaining what the script does
2. Three functions (each with proper docstrings):
   - celsius_to_fahrenheit(celsius)
   - fahrenheit_to_celsius(fahrenheit)
   - kelvin_to_celsius(kelvin)
3. Each function should:
   - Have a clear, descriptive docstring
   - Include parameter and return descriptions
   - Have an example in the docstring
4. Use the if __name__ == "__main__": pattern
5. Include helpful (not obvious) comments where needed

Create your complete solution below:
"""

# Your complete solution:










print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 5: Code Review - Fix the Documentation
# ==============================================================================
"""
This function has TERRIBLE documentation. Your job:
1. Add a proper docstring
2. Rename variables to be more descriptive
3. Add helpful comments (not obvious ones!)
4. Make it professional!
"""

def calc(a, b):
    c = []
    for i in a:
        if i > b:
            c.append(i)
    return c

# TODO: Rewrite with proper documentation and clear variable names




# Test your improved function:
numbers = [23, 45, 12, 67, 34, 89, 15, 56]
threshold = 40
result = # call your function
print(f"Numbers above {threshold}: {result}")

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 6: Creating a Module with if __name__ == "__main__"
# ==============================================================================
"""
Create a GPA calculator module that can be both:
1. Imported and used by other programs
2. Run directly as a script

Your module should include:
- Module docstring
- calculate_gpa(grades, credits) function with proper docstring
- letter_grade(gpa) function with proper docstring
- main() function that demonstrates usage
- if __name__ == "__main__": pattern

GPA Calculation: sum(grade * credit) / sum(credits)

Letter grades:
A: 3.7-4.0, B: 2.7-3.69, C: 1.7-2.69, D: 1.0-1.69, F: <1.0
"""

# Your complete module:










print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 7: Documentation Best Practices
# ==============================================================================
"""
Write a function called analyze_sensor_data that:
- Takes a list of temperature readings (floats)
- Returns: count, average, min, max, and readings above 75°F

This function must demonstrate ALL of these documentation best practices:
1. Module-level docstring (at the very top of this section)
2. Function docstring with Parameters and Returns sections
3. Example usage in the docstring
4. Helpful comments explaining WHY, not WHAT
5. Clear variable names
6. Proper formatting and structure
"""

# Your complete solution with exemplary documentation:










print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 8: Understanding the if __name__ == "__main__" Pattern
# ==============================================================================
"""
Explain in your own words:

1. What does if __name__ == "__main__": mean?



2. When does Python set __name__ to "__main__"?



3. Why is this pattern useful?



4. What happens if you DON'T use this pattern?



Now write a simple example that demonstrates this pattern:
"""

# Your example code:










# ==============================================================================
# BONUS CHALLENGE: Professional Statistics Module
# ==============================================================================
"""
If you finish early, create a complete statistics module!

Requirements:
- Module docstring explaining the purpose
- At least 4 functions: mean, median, mode, standard_deviation
- Each function with complete docstrings
- Proper imports at the top
- Constants if needed
- Helper functions if useful
- main() function showing examples
- if __name__ == "__main__": pattern
- Professional comments throughout

This should be production-quality code!
"""

# Your complete statistics module:
