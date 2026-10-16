"""
Homework 7: Modular Functions and File I/O
EK125 - Fall 2026

This is a script-based assignment: write and run all of your code in this
single .py file in PyCharm.

This homework has two sections:
  Section 1 (Problems 1-6): Covers Class 13 material -- modular functions.
  Section 2 (Problems 7-11): Covers Class 14 material -- file I/O.

All modular programs should consist of a main program that calls the
functions. Write the function definitions and the main program. Put
docstrings in all functions. If there is user input, make sure that you
validate the input. Write function stubs when asked.

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
# SECTION 1: MODULAR FUNCTIONS
# ==============================================================================

# ==============================================================================
# PROBLEM 1: Degrees to Radians
# ==============================================================================
"""
Write a program of 3 functions:
  - getangle:    prompts the user for an angle in degrees
  - convert:     converts it to radians
  - printresult: prints the result to two decimal places

STEP 1 - Write stubs first and run the main program to verify structure:
  - getangle:    return the value 32
  - convert:     return rad as deg divided by 2
  - printresult: simply print deg and rad

STEP 2 - Replace stubs with full implementations.

Include docstrings for each function.
"""

# Your code here


# ==============================================================================
# PROBLEM 2: A Box of Characters
# ==============================================================================
"""
Write a program of two functions:
  - getnchar: generates a random integer n in the range from 5 to 10,
              prompts the user for a character, and returns both.
              If the user enters more than one character, return only
              the first.
  - printbox: prints an n x n square box of the character.

STEP 1 - Write stubs first and run the main program to verify structure:
  - getnchar: return 3 for n and 'e' for the character
  - printbox: print 'e' 3 times on one line

STEP 2 - Replace stubs with full implementations.

Include docstrings for each function.
"""

# Your code here


# ==============================================================================
# PROBLEM 3: Volume and Surface Area of a Cylinder
# ==============================================================================
"""
Write a program of three functions:
  - getradht:    prompts the user for the base radius and height
  - volsurf:     calculates the volume and surface area
  - printresults: prints the results in a sentence format to two decimals

STEP 1 - Write stubs first and run the main program to verify structure:
  - getradht:    return 3 and 10 for radius and height
  - volsurf:     return vol as rad * 2 and surf as ht * 2
  - printresults: simply print vol and surf

STEP 2 - Replace stubs with full implementations.

Include docstrings for each function.
"""

# Your code here


# ==============================================================================
# PROBLEM 4: Arithmetic Menu
# ==============================================================================
"""
Write a program of four functions:
  - randnums:   generates two random integers
  - printmenu:  displays a menu (add, subtract, multiply, divide) and
                returns the user's choice
  - compute:    computes the operation; inputs are x, y, and choice
  - printresult: prints the result nicely

STEP 1 - Write stubs first and run the main program to verify structure:
  - randnums:   return 1 and 2
  - printmenu:  return 3
  - compute:    return x + y + choice
  - printresult: print the result simply

STEP 2 - Replace stubs with full implementations.

Include docstrings for each function.
"""

# Your code here


# ==============================================================================
# PROBLEM 5: Local Scope
# ==============================================================================
"""
Part 1 - Predict and run
  Before running the code below, predict what will happen and write your
  prediction as a comment. Then run the code. Were you right? Write a
  comment explaining why.

      def computeBonus(score):
          '''Adds a 10-point bonus to a score and prints it.'''
          bonusScore = score + 10
          print(f"Inside function: {bonusScore}")

      computeBonus(85)
      print(bonusScore)   # What happens here?

Part 2 - Fix it
  Rewrite computeBonus so that the bonus score is available outside the
  function. The main program should store the returned value in a variable
  and print it. Include a docstring.
"""

# Your code here


# ==============================================================================
# PROBLEM 6: Mutable vs. Immutable Arguments
# ==============================================================================
"""
Part 1 - Numbers (immutable)
  Write a function addCurve(score, curve) that adds curve points to score
  and prints the result inside the function. In the main program, call
  addCurve with a score of 72 and a curve of 8, then print the original
  score variable afterward.
  Write a comment explaining whether the original changes and why.
  Include a docstring.

Part 2 - Lists (mutable)
  Write a function curveAll(scores, curve) that adds curve points to every
  score in the list using index assignment (scores[i] = scores[i] + curve).
  In the main program, call curveAll with the list [72, 85, 90, 68] and a
  curve of 8, then print the original list afterward.
  Write a comment explaining whether the original changes and why.
  Include a docstring.

Part 3 - Protect the original
  Write a new function curveAllSafe(scores, curve) that returns a new list
  with the curved scores WITHOUT modifying the original. Verify in the main
  program that the original list is unchanged after calling curveAllSafe.
  Include a docstring.
"""

# Your code here


# ==============================================================================
# SECTION 2: FILE I/O
# ==============================================================================

# ==============================================================================
# PROBLEM 7: Writing and Reading Back Sensor Data
# ==============================================================================
"""
A thermometer recorded the following body temperatures (in F):

    readings = [98.6, 99.1, 97.8, 100.4, 98.2]

7.1: Write
  - Using a with statement and 'w' mode, write each reading to a file named
    body_temps.txt, one reading per line.
    (Remember: .write() does NOT add newlines for you.)

7.2: Read three ways
  - Open the file and use .read() to store its contents in a variable.
    Print the variable and print its type.
  - Open the file again and use .readlines(). Print the resulting list.
  - Open the file a third time and iterate over it directly to build a list
    of floats named temps_read. Use .strip() on each line.
  - Print the average of temps_read, rounded to two decimal places.

7.3: Test
  - Use assert to confirm that temps_read is equal to the original readings
    list.

Questions to answer (as comments):
  - What type does .read() return? What type does .readlines() return?
  - What extra character appears at the end of each element in the
    .readlines() list, and where did it come from?
  - Why did you need to open the file again for each read method, instead
    of calling all three methods inside one with block?

See the reading's [Reading Files: Different Methods](https://BU-EK125.github.io/EK125/class/Class14.html#reading-files-different-methods) section for a refresher.
"""

readings = [98.6, 99.1, 97.8, 100.4, 98.2]

# Your code here


# ==============================================================================
# PROBLEM 8: Write vs. Append, a Lab Activity Log
# ==============================================================================
"""
8.1: Start the log
  - Open a file named lab_log.txt in 'w' mode and write the header line:
      Lab Activity Log
  - Write a function log_event(filename, message) that opens filename in
    'a' mode and writes message on its own line.

8.2: Log some events
  - Call log_event three times with the messages:
      'Calibrated sensor'
      'Started trial 1'
      'Trial 1 complete'
  - Open lab_log.txt in 'r' mode and print its contents.

8.3: Experiment
  - Run your whole HW7.py file a second time and look at the contents of
    lab_log.txt that you print.
  - Temporarily change the header in 8.1 to use 'a' mode instead of 'w'.
    Run the file twice more and look at the output again. Then change it
    back to 'w'.

Questions to answer (as comments):
  - After running the file twice with the header in 'w' mode, how many
    lines are in lab_log.txt? Why isn't the log twice as long?
  - What happened when the header used 'a' mode instead? Why?
  - Give one real situation where 'a' is the right choice and one where
    'w' is the right choice.

See the reading's [Appending to Files](https://BU-EK125.github.io/EK125/class/Class14.html#appending-to-files) and [Mistake 2: Using `'w'` Mode Carelessly](https://BU-EK125.github.io/EK125/class/Class14.html#mistake-2-using-w-mode-carelessly) sections for a refresher.
"""

# Your code here


# ==============================================================================
# PROBLEM 9: Reading and Writing CSV Files
# ==============================================================================
"""
Store resting heart-rate trials in a CSV file. Then read the file back,
compute a mean for each subject, and save a summary CSV. This problem also
reviews dictionaries from HW6.

Resting heart rate (bpm) was measured three times for each subject:

    hr_data = [
        ['Subject', 'Trial1', 'Trial2', 'Trial3'],
        ['S01', 72, 75, 71],
        ['S02', 64, 66, 63],
        ['S03', 81, 78, 80],
        ['S04', 69, 70, 74]
    ]

9.1: Write the CSV
  - Use the csv module to write hr_data to heart_rates.csv.
    (Remember newline='' when opening the file.)

9.2: Read and process
  - Open heart_rates.csv and create a csv.reader.
  - Use next() to skip the header row and store it in a variable.
  - For each remaining row, convert the three trial values to integers and
    compute their mean.
  - Store the results in a dictionary named mean_hr, mapping each subject
    ID to that subject's mean heart rate. Print mean_hr.

9.3: Write a summary CSV
  - Write a new file heart_rate_summary.csv with the header row
      Subject,Mean_HR
    followed by one row per subject, with the mean rounded to one decimal
    place.
  - Open heart_rate_summary.csv and print its contents to verify it.

Questions to answer (as comments):
  - What type are the trial values when they come out of csv.reader, even
    though you wrote them as integers?
  - What error do you get if you call sum(row[1:]) without converting the
    values first? Explain why.

See the reading's [Working with CSV Files](https://BU-EK125.github.io/EK125/class/Class14.html#working-with-csv-files) section for a refresher.
"""

hr_data = [
    ['Subject', 'Trial1', 'Trial2', 'Trial3'],
    ['S01', 72, 75, 71],
    ['S02', 64, 66, 63],
    ['S03', 81, 78, 80],
    ['S04', 69, 70, 74]
]

# Your code here


# ==============================================================================
# PROBLEM 10: Organizing Experiment Folders with os
# ==============================================================================
"""
Use the os module to find out where Python is working, build a folder
structure, and save files inside it.

10.1: Where am I?
  - Import os and print the current working directory.
  - In PyCharm's Project panel, find body_temps.txt from Problem 7. Is it in
    the folder that getcwd() printed?

10.2: Build a folder structure
  - Use os.path.join to build two paths:
      HW7_data/raw
      HW7_data/results
  - Use os.makedirs with exist_ok=True to create both folders.

10.3: Save files into a subfolder
  - For each subject in ['S01', 'S02', 'S03'], use os.path.join to build a
    path to a file named <subject>.txt inside HW7_data/raw, for example
    HW7_data/raw/S01.txt.
  - Write the line 'Subject <subject> raw data' into each file.

10.4: Check what exists
  - Use os.listdir to print the contents of HW7_data/raw.
  - Use os.path.isdir to check whether HW7_data/results is a directory, and
    print the result.
  - Use os.path.isfile to check whether HW7_data/raw/S01.txt is a file, and
    print the result.
  - Use os.path.exists to check for HW7_data/raw/S04.txt, and print the
    result.

Questions to answer (as comments):
  - What would happen the second time you run the file if you left out
    exist_ok=True? Why?
  - Suppose HW7_data did not exist yet and you called
    os.mkdir(os.path.join('HW7_data', 'raw')). Would it work? Why or why not?
  - Why is os.path.join('HW7_data', 'raw') better than typing
    'HW7_data/raw' or 'HW7_data\\raw'?

See the reading's [The `os` Module: Working with Files and Directories](https://BU-EK125.github.io/EK125/class/Class14.html#the-os-module-working-with-files-and-directories) section for a refresher.
"""

# Your code here


# ==============================================================================
# PROBLEM 11: A Read-Process-Save Function with a Main Guard
# ==============================================================================
"""
Combine everything into the reading's read -> process -> save pattern.
Include error handling and an if __name__ == "__main__": block.

11.1: Write the function
  - Write a function convert_temps(input_path, output_path) that:
      * Returns None and prints an error message if input_path does not
        exist. You can check with os.path.exists, or catch
        FileNotFoundError with try/except.
      * Otherwise reads the Fahrenheit temperatures from input_path, one
        per line.
      * Converts each temperature to Celsius: C = (F - 32) * 5/9.
      * Writes the header line 'Temperature (C)' to output_path, then one
        value per line formatted to two decimal places.
      * Returns the list of Celsius values.

11.2: Write main()
  - Write a function main() that:
      * Calls convert_temps with input_path set to body_temps.txt (from
        Problem 7) and output_path set to a file named body_temps_C.txt
        inside HW7_data/results. Build that path with os.path.join.
      * Prints the returned list.
      * Uses assert to confirm that the first value is within 0.01 of 37.0.
      * Calls convert_temps again with input_path set to 'missing_file.txt'
        and uses assert to confirm that it returns None.

11.3: Add the main guard
  - At the bottom of your file, add:
      if __name__ == "__main__":
          main()

Questions to answer (as comments):
  - When you run HW7.py directly in PyCharm, what is the value of __name__?
  - Suppose another file contained the line: import HW7
    Would main() run? Would your code from Problems 1-10 run? Explain the
    difference.
  - Why does convert_temps take file paths as arguments instead of
    hard-coding the file names inside the function?

See the reading's [Common Patterns and Best Practices](https://BU-EK125.github.io/EK125/class/Class14.html#common-patterns-and-best-practices) and [The `if __name__ == "__main__":` Pattern](https://BU-EK125.github.io/EK125/class/Class14.html#the-if-name-main-pattern) sections for a refresher.
"""

# Your code here
