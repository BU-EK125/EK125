"""
================================================================================
EK125 — Class 21: Visualizing Data and Plotting in Python
Group Practice Problems (Teams of 3)
Fall 2026

Team Members:
- Your Name
- Partner 1 Name
- Partner 2 Name

Instructions:
- Work in groups of THREE
- You MAY use references (readings, slides, internet)
- Do NOT use AI to write code - you need to learn yourself!
- Focus today: choose the RIGHT plot, and make every figure COMPLETE:
  axis labels WITH UNITS, a title, a legend (if more than one series), grid
- matplotlib and numpy must be installed in your PyCharm project
- All figures appear at the end, when plt.show() runs (last line of the file)
- Save frequently (Ctrl+S / Cmd+S)
================================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

# ==============================================================================
# PROBLEM 1: Choose the Right Plot
# ==============================================================================
"""
For each scenario, choose the BEST plot type (line, scatter, bar, or
histogram) and write ONE sentence explaining why.

a) Battery voltage recorded every minute for 3 hours
b) The heights of 200 students in EK125
c) The number of engineering majors in each of 5 departments
d) Car weight vs. fuel efficiency for 40 different cars
e) A bridge's deflection as more and more load is added
f) How many times each of 6 vending machines broke down this year

YOUR ANSWERS:
a)
b)
c)
d)
e)
f)
"""

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 2: A Complete Line Plot with NumPy
# ==============================================================================
"""
A ball is thrown straight up at 20 m/s. Its height is:
    height = 20 * t - 4.9 * t**2      (height in m, t in s)

1. Use np.linspace to create 100 time values from 0 to 4 seconds.
2. Calculate the height at every time (NumPy does the whole array at once!).
3. Plot height vs. time as a solid blue line, linewidth 2.
4. Add axis labels WITH UNITS, a title, and a grid.
5. Using the grid, ESTIMATE the maximum height and when it occurs.
   Write your estimates in a comment. Then check with max(height).
"""

# TODO: Your code here




# Our estimate from the grid: max height about ___ m at about ___ s


print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 3: Several Lines with a Loop and a Legend
# ==============================================================================
"""
Compare the ball's height for three launch speeds: 10, 15, and 20 m/s.
For speed v0, the height is:  height = v0 * t - 4.9 * t**2
and the ball lands at time:   t_land = 2 * v0 / 9.8

Requirements:
- Use a FOR LOOP over the list of speeds (don't copy-paste three times!)
- For each speed, make 50 time values from 0 to THAT speed's landing time,
  so no curve goes below the ground
- Give each line a different line style: '-', '--', ':' (stored in a list)
- Each line's legend label should read like '10 m/s' (use an f-string)
- Labels with units, a title, a legend, and a grid

Hint: you need the SAME position in two lists (speeds and line styles).
What kind of loop gives you an index you can use for both?
"""

launch_speeds_mps = [10, 15, 20]
line_styles = ['-', '--', ':']

# TODO: Your code here




print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 4: Bar Chart with a Reference Line
# ==============================================================================
"""
Densities of common engineering metals (g/cm^3):
    Aluminum 2.70, Titanium 4.51, Steel 7.85, Copper 8.96, Lead 11.34

1. Make a bar chart of density by metal (any single color).
2. Draw a horizontal DASHED red line at 5.0 g/cm^3 labeled
   'Light/heavy metal cutoff' (hint: plt.axhline, used in the reading's
   complete example).
3. Labels with units, a title, a legend, and horizontal grid lines only
   (plt.grid(axis='y')).
4. Answer in a comment: which metals count as "light"?
"""

metals = ['Aluminum', 'Titanium', 'Steel', 'Copper', 'Lead']
density_g_per_cm3 = [2.70, 4.51, 7.85, 8.96, 11.34]

# TODO: Your code here




# Light metals:


print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 5: How Many Bins? Histograms Side by Side
# ==============================================================================
"""
A quality-control lab measured 30 resistors labeled 100 ohms (data below).

1. Make ONE figure with 3 subplots side by side (1 row, 3 columns).
   Hint: plt.figure(figsize=(14, 4)) makes it wide enough.
2. Plot a histogram of the SAME data in each, using bins=3, bins=6, and
   bins=15. Use black bar edges.
3. Give each subplot a title saying how many bins it uses, and axis labels
   (the y-axis counts resistors).
4. Use plt.tight_layout() so nothing overlaps.
5. Discuss as a team and answer in a comment: which bin count shows the
   shape of the data best? What goes wrong with too FEW bins? Too MANY?
"""

resistance_ohm = [99.2, 100.5, 101.1, 98.7, 100.0, 99.8, 100.9, 101.6, 99.5,
                  100.2, 98.9, 100.4, 99.9, 100.7, 101.3, 99.1, 100.1, 100.6,
                  99.4, 100.3, 102.0, 98.4, 100.8, 99.7, 100.0, 101.0, 99.6,
                  100.2, 99.3, 100.5]

# TODO: Your code here




# Best bin count and why:
# Too few bins:
# Too many bins:


print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 6: Measured vs. Theoretical, with Residuals
# ==============================================================================
"""
Students tested a 10-ohm resistor. Ohm's law predicts voltage = 10 * current.

Make ONE figure with 2 subplots side by side:

LEFT subplot:
- Measured data as a SCATTER plot (label 'Measured')
- The theoretical line as a LINE plot, using np.linspace for 50 current
  values from 0 to 0.5 A (label "Ohm's law, R = 10 ohm")
- Labels with units, title, legend, grid

RIGHT subplot: residuals (measured - theoretical) at each measured current
- Convert both lists to NumPy arrays so you can subtract element by element
- Scatter plot of residual vs. current, plus a dashed black line at 0
- Labels with units, title, grid

Then save the figure as 'ohms_law.png' (dpi=300, bbox_inches='tight').
Print the residuals, and answer in a comment: is the error random, or does
it show a pattern?
"""

current_a = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
measured_voltage_v = [0.03, 0.97, 2.06, 2.95, 4.04, 5.02]
resistance = 10   # ohm

# TODO: Your code here




# Random or a pattern? Why?


print("\n" + "="*60 + "\n")


# ==============================================================================
# BONUS CHALLENGE: Radar Chart Comparing Two Robot Designs
# ==============================================================================
"""
If you finish early: two robot designs were scored 0-10 on five criteria.

Using the radar chart example in the Class 21 reading, plot both designs on
one radar chart with a legend and the radial axis from 0 to 10. Which design
would you pick for a delivery robot, and why?
"""

criteria = ['Speed', 'Battery life', 'Payload', 'Cost', 'Reliability']
design_a = [8, 5, 6, 7, 9]
design_b = [6, 9, 8, 5, 7]

# TODO: Your code here




# Our pick for a delivery robot, and why:


# ==============================================================================
# Leave this line at the very end so all figures appear
plt.show()
