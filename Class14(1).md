# Class 15: Scripts, File I/O, and the Local File Environment

## Learning Objectives
By the end of this reading, you should understand:
- What scripts are and how they differ from interactive code
- How to read from and write to files
- How to work with your computer's file system using Python
- When and how to use context managers (`with` statement)
- The difference between different file modes

---

## Part 1: Understanding Scripts

### What is a Script?

Until now, you've been writing code in notebooks (Colab or Jupyter), where you could run individual cells and see results immediately. A **script** is different: it's a complete Python program stored in a single `.py` file that runs from top to bottom, start to finish, when you execute it.

Think of the difference like this:
- **Interactive code (notebooks)**: Like having a conversation - you say something, get an immediate response, then continue
- **Scripts**: Like writing a letter - you write the whole thing first, then send it off to be read completely

### From Notebooks to Scripts: What Changes?

**In a Notebook:**
```python
# Cell 1
name = "Alice"

# Cell 2 (run separately)
print(f"Hello, {name}")

# Cell 3 (run separately)
age = 21
```

**In a Script (temperature_converter.py):**
```python
# Everything runs together, top to bottom
name = "Alice"
print(f"Hello, {name}")
age = 21
```

The big differences:
1. **No cells** - Everything runs in sequence
2. **Output only appears if you print it** - Unlike notebooks where the last expression in a cell displays automatically
3. **Variables persist** - Once defined, they exist for the entire script execution
4. **Must save before running** - The file must be saved to disk

### Why Use Scripts?

**Professional Development:**
- Industry standard for writing programs
- Easier to share and version control (Git/GitHub)
- Can be run from command line
- Better for larger projects

**Practical Benefits:**
- Reusable programs you can run anytime
- Can schedule scripts to run automatically
- Better organization for complex programs
- Easier debugging

### The `if __name__ == "__main__":` Pattern

You'll often see this at the bottom of Python scripts:

```python
def calculate_area(length, width):
    """Calculate area of a rectangle."""
    return length * width

def main():
    """Main program execution."""
    print("Rectangle Area Calculator")
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = calculate_area(length, width)
    print(f"Area: {area}")

if __name__ == "__main__":
    main()
```

**What does this mean?**

When you run a Python file directly (like `python calculator.py`), Python sets a special variable `__name__` to `"__main__"`. This tells Python "this is the main program being run."

**Why do we use it?**

Two reasons:
1. **Organization**: Separates the main program logic from function definitions
2. **Reusability**: Other Python files can import your functions without running your main program

**Simple analogy:**
- Imagine a cookbook (your script)
- The recipes (functions) can be used by anyone
- The `if __name__ == "__main__":` part says "only follow these dinner party instructions if you're actually hosting the party (running this file directly)"

**For now, you can think of it as:** "This is where my program starts when I run this file."

### Script Structure Best Practices

A well-organized script typically looks like this:

```python
"""
Script description at the top.
Author: Your Name
Date: 2026-03-16
"""

# Imports
import math
import numpy as np

# Constants (values that don't change)
PI = 3.14159
GRAVITY = 9.81

# Function definitions
def calculate_something(param1, param2):
    """Function docstring explaining what it does."""
    result = param1 + param2
    return result

def another_function():
    """Another helper function."""
    pass

# Main program
if __name__ == "__main__":
    # Main program code goes here
    print("Program starting...")
    result = calculate_something(5, 10)
    print(f"Result: {result}")
```

**Why this structure?**
- **Documentation at top** - Anyone opening the file knows what it does
- **Imports together** - Easy to see dependencies
- **Constants clearly defined** - Magic numbers explained
- **Functions before use** - Python needs to know about functions before calling them
- **Main at bottom** - Standard convention, easy to find

---

## Part 2: File Input and Output (I/O)

### Why Work with Files?

Until now, all your data disappeared when the program ended. Files let you:
- Save results to use later
- Process large datasets
- Share data with other programs
- Create logs and reports
- Read configuration settings

**Real-world applications:**
- Reading sensor data from a CSV file
- Saving calculation results
- Processing experimental data
- Creating automated reports
- Logging program activity

### The Basics: Opening and Closing Files

**The old way (NOT recommended):**
```python
# Old way - you have to remember to close!
file = open('data.txt', 'r')
content = file.read()
file.close()  # Easy to forget!
```

**The modern way (ALWAYS use this):**
```python
# Modern way - automatically closes the file
with open('data.txt', 'r') as file:
    content = file.read()
# File is automatically closed here
```

### The `with` Statement (Context Manager)

The `with` statement is like having an assistant who:
1. Opens the door for you
2. Lets you do your work
3. Closes and locks the door when you're done - even if something goes wrong

**Why it's better:**
- **Automatic cleanup**: File always closes, even if there's an error
- **Less code**: No need to remember `file.close()`
- **Safer**: Prevents file corruption
- **Professional**: Standard practice in Python

**Analogy:**
Think of borrowing a book from the library:
```python
# Without 'with' - you might forget to return the book!
book = library.borrow('Python Guide')
knowledge = book.read()
library.return_book(book)  # Easy to forget!

# With 'with' - automatic return
with library.borrow('Python Guide') as book:
    knowledge = book.read()
# Book automatically returned here
```

### File Modes: Opening Files Different Ways

When you open a file, you must specify a **mode** - what you want to do with the file:

| Mode | Meaning | What it does | If file doesn't exist |
|------|---------|--------------|----------------------|
| `'r'` | Read | Opens for reading | Error |
| `'w'` | Write | Opens for writing | Creates new file |
| `'a'` | Append | Opens for appending | Creates new file |
| `'r+'` | Read/Write | Opens for both | Error |

**Important warnings:**
- `'w'` mode **DELETES the entire file** if it exists and creates a new empty one
- `'a'` mode adds to the end without deleting existing content
- `'r'` mode is read-only - you cannot write

### Reading Files: Different Methods

#### Method 1: Read Everything at Once

```python
with open('story.txt', 'r') as file:
    content = file.read()
    print(content)
```

**When to use:** Small files that fit easily in memory

**Example:**
```python
# story.txt contains:
# Once upon a time
# In a land far away
# There lived a dragon

with open('story.txt', 'r') as file:
    story = file.read()
    print(story)

# Output:
# Once upon a time
# In a land far away
# There lived a dragon
```

#### Method 2: Read One Line at a Time

```python
with open('data.txt', 'r') as file:
    line = file.readline()
    print(line)
```

**When to use:** When you only need the first few lines, or want to process one line at a time

```python
with open('grades.txt', 'r') as file:
    header = file.readline()  # First line
    first_student = file.readline()  # Second line
    print(header)
    print(first_student)
```

#### Method 3: Read All Lines into a List

```python
with open('data.txt', 'r') as file:
    lines = file.readlines()
    # lines is now a list where each element is one line
```

**When to use:** When you need to process or analyze all lines

```python
# temperatures.txt contains:
# 72
# 68
# 75
# 71

with open('temperatures.txt', 'r') as file:
    lines = file.readlines()
    # lines = ['72\n', '68\n', '75\n', '71\n']
    
    # Convert to numbers and calculate average
    temps = [float(line.strip()) for line in lines]
    average = sum(temps) / len(temps)
    print(f"Average temperature: {average}")
```

**Note:** Each line includes the newline character `\n` at the end. Use `.strip()` to remove it:

```python
line = "72\n"
clean = line.strip()  # "72"
```

#### Method 4: Iterate Directly (Best for Large Files)

```python
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

**When to use:** Large files that don't fit in memory, or when you only need to process each line once

```python
# Count how many times "error" appears in a log file
error_count = 0
with open('system.log', 'r') as file:
    for line in file:
        if 'error' in line.lower():
            error_count += 1
print(f"Found {error_count} errors")
```

### Writing Files: Creating and Saving Data

#### Basic Writing

```python
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.\n')
```

**Important:** 
- `.write()` does NOT add newlines automatically - you must add `\n` yourself
- `'w'` mode overwrites the entire file - all previous content is lost

```python
# Create a report
with open('report.txt', 'w') as file:
    file.write('Experiment Results\n')
    file.write('==================\n')
    file.write(f'Average: {avg}\n')
    file.write(f'Maximum: {max_val}\n')
```

#### Writing Multiple Lines

```python
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']

with open('output.txt', 'w') as file:
    file.writelines(lines)
```

Or use a loop:

```python
data = [10, 20, 30, 40, 50]

with open('numbers.txt', 'w') as file:
    for number in data:
        file.write(f'{number}\n')
```

#### Appending to Files

```python
# Add new data without deleting old data
with open('log.txt', 'a') as file:
    file.write('New log entry\n')
```

**Use case: Logging**
```python
import datetime

def log_action(message):
    """Add a timestamped entry to the log file."""
    timestamp = datetime.datetime.now()
    with open('activity.log', 'a') as file:
        file.write(f'{timestamp}: {message}\n')

log_action('Program started')
log_action('Data loaded successfully')
log_action('Calculation complete')
```

### Working with CSV Files

CSV (Comma-Separated Values) files are a common way to store tabular data, like spreadsheets.

**Example CSV file (students.csv):**
```
Name,Grade,Age
Alice,95,20
Bob,87,21
Charlie,92,19
```

#### Reading CSV Files (Simple Method)

```python
with open('students.csv', 'r') as file:
    header = file.readline().strip().split(',')
    print(f"Columns: {header}")
    
    for line in file:
        values = line.strip().split(',')
        name, grade, age = values
        print(f"{name} scored {grade}")
```

#### Reading CSV Files (Using csv Module)

```python
import csv

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Get first line
    
    for row in reader:
        name, grade, age = row
        print(f"{name}: {grade}")
```

#### Writing CSV Files

```python
import csv

students = [
    ['Name', 'Grade', 'Age'],
    ['Alice', 95, 20],
    ['Bob', 87, 21],
    ['Charlie', 92, 19]
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students)
```

**Note:** The `newline=''` argument prevents extra blank lines on Windows.

### Practical Example: Temperature Logger

Let's put it all together with a complete example:

```python
"""
temperature_logger.py
Logs temperature readings to a file and calculates statistics.
"""

def log_temperature(temp):
    """Append a temperature reading to the log file."""
    with open('temps.txt', 'a') as file:
        file.write(f'{temp}\n')

def get_statistics():
    """Calculate statistics from all logged temperatures."""
    with open('temps.txt', 'r') as file:
        temps = [float(line.strip()) for line in file]
    
    if not temps:
        return None
    
    avg = sum(temps) / len(temps)
    min_temp = min(temps)
    max_temp = max(temps)
    
    return avg, min_temp, max_temp

def save_report():
    """Create a summary report."""
    stats = get_statistics()
    
    if stats is None:
        print("No data to report")
        return
    
    avg, min_temp, max_temp = stats
    
    with open('temp_report.txt', 'w') as file:
        file.write('Temperature Report\n')
        file.write('==================\n')
        file.write(f'Average: {avg:.1f}°F\n')
        file.write(f'Minimum: {min_temp:.1f}°F\n')
        file.write(f'Maximum: {max_temp:.1f}°F\n')
    
    print("Report saved to temp_report.txt")

if __name__ == "__main__":
    # Log some temperatures
    log_temperature(72.5)
    log_temperature(68.3)
    log_temperature(75.1)
    log_temperature(71.9)
    
    # Generate report
    save_report()
```

---

## Part 3: The Local File Environment

### Understanding Your Computer's File System

Your computer organizes files in a hierarchical structure - like a tree with branches:

```
Documents/                    (folder)
├── EK125/                    (folder)
│   ├── Class15/              (folder)
│   │   ├── script.py         (file)
│   │   └── data.txt          (file)
│   └── Homework/             (folder)
│       └── hw5.py            (file)
└── Photos/                   (folder)
```

**Key concepts:**
- **Directory** = Folder (same thing, different names)
- **Path** = The route to a file (like a file's address)
- **Current working directory** = Where Python thinks you are right now

### File Paths: Absolute vs. Relative

#### Absolute Path (Full Address)

An absolute path specifies the complete location from the root of your file system:

**Windows:**
```
C:\Users\YourName\Documents\EK125\data.txt
```

**Mac/Linux:**
```
/Users/YourName/Documents/EK125/data.txt
```

**Analogy:** Like a complete mailing address: "123 Main St, Boston, MA 02115, USA"

#### Relative Path (From Current Location)

A relative path specifies location relative to your current working directory:

```python
# If you're currently in Documents/EK125/
'data.txt'              # File in current directory
'Class15/script.py'     # File in subfolder
'../Homework/hw5.py'    # File in sibling folder
```

**Analogy:** Like giving directions from where you are: "Go to the coffee shop, it's two blocks down and on the right"

**Special directory names:**
- `.` = Current directory (where you are now)
- `..` = Parent directory (one level up)
- `~` = Home directory (your user folder)

### The `os` Module: Working with Files and Directories

Python's `os` module lets you interact with your computer's file system - creating folders, checking what files exist, moving around directories, etc.

```python
import os
```

#### Finding Out Where You Are

```python
import os

# Get current working directory
current = os.getcwd()
print(f"I am currently in: {current}")

# Example output:
# I am currently in: /Users/alice/Documents/EK125
```

**Why this matters:** When you open a file with a relative path, Python looks for it relative to this directory.

#### Listing Files and Folders

```python
import os

# List everything in current directory
contents = os.listdir()
print(contents)

# List contents of a specific directory
contents = os.listdir('Class15')
print(contents)

# Example output:
# ['script.py', 'data.txt', 'notes.md']
```

#### Changing Directories

```python
import os

# Move to a different directory
os.chdir('Class15')
print(f"Now in: {os.getcwd()}")

# Move up one level
os.chdir('..')
print(f"Now in: {os.getcwd()}")
```

**Analogy:** Like using `cd` (change directory) in a terminal/command prompt

#### Creating Directories

```python
import os

# Create a new directory
os.mkdir('NewFolder')

# Create multiple nested directories
os.makedirs('Projects/Python/Data')
```

**Difference:**
- `mkdir()` - Creates ONE directory (fails if path doesn't exist)
- `makedirs()` - Creates ALL necessary directories in the path

```python
# This fails if 'Projects' and 'Python' don't exist:
os.mkdir('Projects/Python/Data')  # Error!

# This works - creates all three folders:
os.makedirs('Projects/Python/Data')  # Success!
```

#### Checking if Files/Folders Exist

```python
import os

# Check if a file exists
if os.path.exists('data.txt'):
    print("File found!")
else:
    print("File not found!")

# Check if it's a file
if os.path.isfile('data.txt'):
    print("It's a file")

# Check if it's a directory
if os.path.isdir('Class15'):
    print("It's a directory")
```

**Why this is useful:** Prevents errors from trying to open files that don't exist

```python
import os

def safe_read_file(filename):
    """Read a file only if it exists."""
    if not os.path.exists(filename):
        print(f"Error: {filename} not found")
        return None
    
    with open(filename, 'r') as file:
        return file.read()
```

#### Building File Paths Correctly

Different operating systems use different path separators:
- Windows: `\` (backslash)
- Mac/Linux: `/` (forward slash)

**The problem:**
```python
# This works on Mac/Linux but fails on Windows:
path = 'Documents/EK125/data.txt'

# This is messy and hard to read:
path = 'Documents' + os.sep + 'EK125' + os.sep + 'data.txt'
```

**The solution: `os.path.join()`**
```python
import os

# Works on ALL operating systems!
path = os.path.join('Documents', 'EK125', 'data.txt')
print(path)

# Windows: Documents\EK125\data.txt
# Mac/Linux: Documents/EK125/data.txt
```

**Always use `os.path.join()` to build paths!**

#### Practical Example: Organizing Experiment Data

```python
"""
data_organizer.py
Automatically organizes experimental data into dated folders.
"""
import os
from datetime import datetime

def setup_experiment_folder():
    """Create folder structure for today's experiment."""
    # Get today's date for folder name
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Build paths
    base_path = os.path.join('Experiments', today)
    raw_data_path = os.path.join(base_path, 'raw_data')
    results_path = os.path.join(base_path, 'results')
    
    # Create all necessary folders
    os.makedirs(raw_data_path, exist_ok=True)
    os.makedirs(results_path, exist_ok=True)
    
    print(f"Created experiment folder: {base_path}")
    return base_path

def save_measurement(experiment_folder, sensor_id, value):
    """Save a sensor reading to the appropriate file."""
    filename = f'sensor_{sensor_id}.txt'
    filepath = os.path.join(experiment_folder, 'raw_data', filename)
    
    # Append reading with timestamp
    timestamp = datetime.now().strftime('%H:%M:%S')
    with open(filepath, 'a') as file:
        file.write(f'{timestamp}, {value}\n')
    
    print(f"Saved reading to {filename}")

def list_experiments():
    """List all experiment folders."""
    if not os.path.exists('Experiments'):
        print("No experiments yet")
        return
    
    experiments = os.listdir('Experiments')
    print("Available experiments:")
    for exp in experiments:
        print(f"  - {exp}")

if __name__ == "__main__":
    # Create today's experiment folder
    exp_folder = setup_experiment_folder()
    
    # Simulate taking measurements
    save_measurement(exp_folder, 'temp', 72.5)
    save_measurement(exp_folder, 'temp', 73.1)
    save_measurement(exp_folder, 'pressure', 101.3)
    
    # List all experiments
    list_experiments()
```

---

## Part 4: Common Patterns and Best Practices

### Pattern 1: Reading Data, Processing, Saving Results

```python
def process_temperature_data(input_file, output_file):
    """Read temperatures, convert to Celsius, save results."""
    # Read data
    with open(input_file, 'r') as file:
        temps_f = [float(line.strip()) for line in file]
    
    # Process
    temps_c = [(f - 32) * 5/9 for f in temps_f]
    
    # Save results
    with open(output_file, 'w') as file:
        file.write('Temperature (°C)\n')
        for temp in temps_c:
            file.write(f'{temp:.1f}\n')
```

### Pattern 2: Checking Before Acting

```python
import os

def safe_write(filename, content):
    """Only write if file doesn't exist, or ask permission."""
    if os.path.exists(filename):
        response = input(f'{filename} exists. Overwrite? (y/n): ')
        if response.lower() != 'y':
            print("Cancelled")
            return
    
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Saved to {filename}")
```

### Pattern 3: Error Handling

```python
def robust_file_read(filename):
    """Read file with error handling."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read {filename}")
        return None
```

---

## Part 5: Common Mistakes and How to Avoid Them

### Mistake 1: Forgetting to Close Files (Without `with`)

```python
# BAD - File might not close if there's an error
file = open('data.txt', 'r')
data = process(file.read())  # If process() errors...
file.close()  # ...this never runs!

# GOOD - File always closes
with open('data.txt', 'r') as file:
    data = process(file.read())
# File closed automatically
```

### Mistake 2: Using `'w'` Mode Carelessly

```python
# BAD - Accidentally deletes all data!
with open('important_data.txt', 'w') as file:  # OOPS! File now empty
    file.write('new data\n')

# GOOD - Use 'a' to append or check first
if os.path.exists('important_data.txt'):
    print("Warning: File exists!")

with open('important_data.txt', 'a') as file:
    file.write('new data\n')
```

### Mistake 3: Forgetting to Strip Newlines

```python
# BAD - Numbers have '\n' at the end
with open('numbers.txt', 'r') as file:
    numbers = [float(line) for line in file]  # Error! "72\n" is not a float

# GOOD - Strip whitespace first
with open('numbers.txt', 'r') as file:
    numbers = [float(line.strip()) for line in file]
```

### Mistake 4: Hardcoding Paths

```python
# BAD - Only works on your computer
path = 'C:\\Users\\Alice\\Documents\\data.txt'

# GOOD - Use relative paths or os.path.join
path = os.path.join('data', 'input.txt')
```

### Mistake 5: Not Checking if File Exists

```python
# BAD - Crashes if file doesn't exist
with open('config.txt', 'r') as file:
    config = file.read()

# GOOD - Check first
if os.path.exists('config.txt'):
    with open('config.txt', 'r') as file:
        config = file.read()
else:
    print("Config file not found!")
    config = create_default_config()
```

---

## Summary: Key Concepts

**Scripts:**
- Complete programs in `.py` files
- Run from top to bottom
- Use `if __name__ == "__main__":` for main program
- Organize: docstring → imports → constants → functions → main

**File I/O:**
- Always use `with` statement (context manager)
- Modes: `'r'` (read), `'w'` (write/overwrite), `'a'` (append)
- Read methods: `.read()`, `.readline()`, `.readlines()`, iterate directly
- Remember to `.strip()` to remove newlines
- `'w'` mode deletes existing files!

**Local File Environment:**
- Use `os.getcwd()` to see where you are
- Use `os.listdir()` to see what files exist
- Use `os.path.exists()` to check before acting
- Use `os.path.join()` to build paths (works on all systems)
- Use `os.makedirs()` to create folder structures

**Best Practices:**
- Always use `with` for files
- Check if files exist before opening
- Use relative paths when possible
- Handle errors gracefully
- Close files properly (automatic with `with`)
- Strip whitespace from input lines
- Use meaningful filenames

---

## Check Your Understanding

1. What's the difference between a script and interactive code?
2. Why should you always use the `with` statement when working with files?
3. What happens if you open a file in `'w'` mode when it already exists?
4. How do you check if a file exists before trying to open it?
5. What's the difference between `os.mkdir()` and `os.makedirs()`?
6. Why is `.strip()` important when reading lines from a file?
7. When would you use `'a'` mode instead of `'w'` mode?
8. Why should you use `os.path.join()` instead of concatenating strings with `/` or `\`?
9. What does `os.getcwd()` tell you?
10. What's the difference between `.read()` and `.readlines()`?
