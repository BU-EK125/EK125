"""
EK125 Homework 8 -- Python half
Plotting with matplotlib (Class 21) and getting ready for MATLAB (Class 22)

Name: ____________________
Lab section: ______

Due: Tuesday November 24, 11:59 PM. Submit to Gradescope.

This homework has two halves, worth 50 points each:
    HWA_python.py (this file) -- Problems 1-3
    HWA_matlab.m -- Problems 4-6

SUBMIT ALL OF THESE FILES TO GRADESCOPE:
    Homework_8_python.py
    stress_strain_python.png
    turbine_dashboard.png
    section_averages.png
    (plus the MATLAB files listed at the top of Homework_8_matlab.m)

RULES
- Individual work.
- Use good programming practice: comments, meaningful variable names,
  consistent indentation.
- NO global variables, NO break/continue, NO `while True` loops.
  Using any of these is an automatic zero for that problem.
- Your file must run from top to bottom in PyCharm without errors.
  Before you start, make sure matplotlib is installed in your project
  (Python Packages tool window, or `pip install matplotlib` in the Terminal).

EVERY FIGURE IN THIS HOMEWORK NEEDS:
- an x-axis label WITH UNITS, a y-axis label WITH UNITS, and a title
- a legend whenever there is more than one data series
- to be saved with plt.savefig(..., dpi=300, bbox_inches='tight')
  BEFORE plt.show() is called
"""

import matplotlib.pyplot as plt

# ============================================================================
# PROBLEM 1 (15 points): Stress-strain curves for two metals
# ============================================================================
# A materials lab pulled a steel bar and an aluminum bar until they began to
# yield, recording stress (force per area) at each amount of strain
# (stretch). You will plot both curves and calculate each metal's stiffness.
#
# You will make this SAME figure again in MATLAB in Problem 4, so take note
# of every command you use.

# Given data (do not change):
strain_percent = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
steel_stress_mpa = [0, 200, 400, 520, 560, 580, 590, 595, 600]
aluminum_stress_mpa = [0, 70, 140, 210, 250, 265, 275, 280, 283]

# Part A (10 pts): Plot both materials on ONE set of axes.
# REQUIRED:
# - Steel: blue, solid line, circle markers, label 'Steel'
# - Aluminum: red, dashed line, square markers, label 'Aluminum'
# - Both lines: linewidth 2
# - x-axis label: 'Strain (%)' y-axis label: 'Stress (MPa)'
# - Title exactly: 'Stress-Strain Curves: Steel vs. Aluminum'
# - A legend and grid lines
# - Save as 'stress_strain_python.png' (dpi=300, bbox_inches='tight')

# YOUR CODE HERE



# Part B (5 pts): Calculate the elastic modulus (stiffness) of each metal.
# The elastic modulus E is the slope of the FIRST, straight part of the curve:
#
# E = (change in stress) / (change in strain)
#
# Use the FIRST TWO data points of each list (access them by index).
# Strain is given in percent, so divide by 100 to turn it into a fraction.
# The result will be in MPa; divide by 1000 to convert to GPa.
#
# REQUIRED: print exactly these two lines (with your calculated numbers,
# 1 decimal place):
# Steel elastic modulus: ___ GPa
# Aluminum elastic modulus: ___ GPa
#
# Self-check: steel should be about 3 times stiffer than aluminum.

# YOUR CODE HERE



# ============================================================================
# PROBLEM 2 (20 points): Wind turbine dashboard
# ============================================================================
# A wind farm engineer wants a one-figure "dashboard" summarizing one day of
# wind data for a single 2000 kW turbine.

# Given data (do not change):
hours = list(range(24))
wind_speed_mps = [3.2, 3.5, 3.1, 2.8, 2.9, 3.6, 4.8, 6.1, 7.4, 8.2, 9.0, 9.6,
10.3, 11.1, 11.8, 12.0, 11.2, 10.1, 8.7, 7.2, 5.9, 4.8, 4.1, 3.6]

# Part A (5 pts): Write a function named turbine_power(wind_speed) that takes
# ONE wind speed in m/s and RETURNS the power output in kW. Do not print
# inside the function. The turbine follows these rules:
#
# - Wind speed below 3.5 m/s: power = 0
# - Wind speed of 12.0 m/s or more: power = 2000
# - Otherwise: power = 2000 * ((wind_speed - 3.5) / (12.0 - 3.5)) ** 3
#
# Self-check: turbine_power(2.0) -> 0, turbine_power(12.5) -> 2000,
# turbine_power(7.75) -> 250.0

# YOUR CODE HERE



# Part B (5 pts): Use a for loop and your function to build a list called
# power_kw with the power for every hour.
# Each value lasts one hour, so the day's total energy in kWh is the sum of
# all 24 power values (kW x 1 h = kWh).
# REQUIRED: print exactly (1 decimal place):
# Total energy for the day: ___ kWh

# YOUR CODE HERE



# Part C (10 pts): Make ONE figure with three side-by-side subplots
# (1 row, 3 columns). Use plt.figure(figsize=(15, 4)).
# Subplot 1: LINE plot of wind speed vs. hour, with markers
# Subplot 2: SCATTER plot of power (y) vs. wind speed (x)
# Subplot 3: HISTOGRAM of wind speed, with bin edges [2, 4, 6, 8, 10, 12]
# and black bar edges (edgecolor='black')
# Every subplot needs its own title and axis labels with units.
# (For the histogram, the y-axis is 'Number of hours'.)
# Call plt.tight_layout() so labels don't overlap, then save as
# 'turbine_dashboard.png'.

# YOUR CODE HERE



# ============================================================================
# PROBLEM 3 (15 points): Debug the bar chart
# ============================================================================
# A TA wrote the code below to make a bar chart of homework averages by lab
# section. It has FIVE bugs. Some cause error messages; some silently produce
# the wrong figure.
#
# Copy the buggy code into the space below the line and fix it.
# For EACH bug, write a comment directly above the fixed line:
#
# # FIX 1: <what was wrong> and <WHY it caused a problem>
#
# Grading: 1 point for each fix, 2 points for each explanation.
# An explanation must say WHY, not just what you changed.
# ("Changed colour to color" earns 1 of 3 points.)
#
# Hint: the averages for sections A1-A5 are 82.5, 78.0, 88.3, 85.1, 80.4.
#
# ---------------------- BUGGY CODE (do not run as-is) ----------------------
# import matplotlib as plt
#
# lab_sections = ['A1', 'A2', 'A3', 'A4', 'A5']
# section_averages = [82.5, 78.0, 88.3, 85.1]
#
# plt.figure()
# plt.bar(lab_sections, section_averages, colour='green')
# plt.xlabel = ('Lab section')
# plt.ylabel('Average score (points)')
# plt.title('Homework Averages by Lab Section')
# plt.grid(axis='y')
# plt.show()
# plt.savefig('section_averages.png', dpi=300, bbox_inches='tight')
# ---------------------------------------------------------------------------
#
# NOTE: this file already imports matplotlib.pyplot correctly at the top.
# Still write your FIX comment for the import bug here.

# YOUR FIXED CODE HERE



# ============================================================================
# Leave this line at the very end of the file so all figures appear
plt.show()
