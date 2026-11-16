# Homework 8: Plotting in Python and MATLAB, Vectors and Matrices

**This homework has two halves, worth 50 points each, covering**
[Class 21](https://BU-EK125.github.io/EK125/class/Class21.html),
[Class 22](https://BU-EK125.github.io/EK125/class/Class22.html), and
[Class 23](https://BU-EK125.github.io/EK125/class/Class23.html). You must
complete each half in its own downloaded file -- not on this web page.
This page's instructions mirror what's in the files so you can read them
without switching windows, but the downloaded files are what you edit,
run, and submit.

## Download the Assignment Files

Download: [HW8_python.py](HW8_python.py) and [HW8_matlab.m](HW8_matlab.m)

**Due Tuesday, November 24, 11:59 PM.** Submit to Gradescope:
- `HW8_python.py`, `stress_strain_python.png`, `turbine_dashboard.png`,
  `section_averages.png`
- `HW8_matlab.m`, `stress_strain_matlab.png`, `sensor_rows.png`,
  `rectifier.png`

## Instructions

- Individual work.
- Use good programming practice: comments, meaningful variable names,
  consistent indentation.
- **No global variables, no `break`/`continue`, no `while True`/`while
  true` loops** -- any of these is an automatic zero for that problem.
- Every figure needs an x-axis label with units, a y-axis label with
  units, a title, and a legend whenever there's more than one data
  series.
- **Python:** before you start, make sure `matplotlib` is installed in
  your PyCharm project (Python Packages tool window, or `pip install
  matplotlib` in the Terminal). Save every figure with
  `plt.savefig(..., dpi=300, bbox_inches='tight')` *before*
  `plt.show()` is called.
- **MATLAB:** end lines with a semicolon unless a problem tells you to
  display the result. Use the provided `%%` section breaks to run one
  problem at a time with "Run Section". Save every figure with
  `saveas(gcf, 'filename.png')`.

## Python Half (Problems 1-3)

### Problem 1: Stress-Strain Curves for Two Metals (15 points)

A materials lab pulled a steel bar and an aluminum bar until they began
to yield, recording stress at each amount of strain. Plot both curves on
one set of axes (steel: blue solid line with circle markers; aluminum:
red dashed line with square markers; both `linewidth 2`), then calculate
each metal's elastic modulus from the first two data points (convert
percent strain to a fraction, then MPa to GPa). You'll recreate this same
figure in MATLAB in Problem 4, so take note of every command you use.

```{literalinclude} HW8_python.py
:language: python
:lines: 40-86
```

### Problem 2: Wind Turbine Dashboard (20 points)

Write `turbine_power(wind_speed)`, returning power output in kW for a
2000 kW turbine (0 below 3.5 m/s, 2000 at or above 12.0 m/s, a cubic
ramp in between). Use it to build a day's worth of power values and
report the day's total energy. Then build a one-figure, three-subplot
dashboard: a line plot of wind speed vs. hour, a scatter plot of power
vs. wind speed, and a histogram of wind speed with the bin edges `[2, 4,
6, 8, 10, 12]`.

```{literalinclude} HW8_python.py
:language: python
:lines: 89-138
```

### Problem 3: Debug the Bar Chart (15 points)

A TA's bar-chart code has **five bugs** -- some raise errors, some
silently produce the wrong figure. Copy the buggy code in, fix it, and
write a `# FIX N:` comment above each fix explaining what was wrong and
*why* it caused a problem (not just what you changed).

```{literalinclude} HW8_python.py
:language: python
:lines: 141-179
```

## MATLAB Half (Problems 4-6)

### Problem 4: Stress-Strain Curves Again, in MATLAB (15 points)

Recreate Problem 1's figure in MATLAB -- same data, same look -- using
`hold on` to put both lines on one set of axes. Recalculate the elastic
moduli (your numbers must match your Python output), then list three
language-level differences between your Python and MATLAB code for this
problem.

```{literalinclude} HW8_matlab.m
:language: matlab
:lines: 33-84
```

### Problem 5: Temperature Sensor Grid (20 points)

A 3x4 grid of temperature sensors logs readings down each column.
`reshape` the flat data into a matrix, predict-then-verify four indexing
expressions, fix one faulty sensor reading, pull out a 2x2 "hot spot"
block, use logical indexing to cap readings above 28 degC (without
modifying the original), concatenate on a new column of sensors, and
plot each row as its own line.

```{literalinclude} HW8_matlab.m
:language: matlab
:lines: 86-172
```

### Problem 6: Half-Wave Rectifier (15 points)

Build a simulated AC input voltage (`linspace` + `sin`), then use logical
indexing (no loops) to zero out its negative half -- a half-wave
rectifier. Plot both signals stacked in subplots with time in
milliseconds, then assemble a `results` matrix with one row per time
point and report its dimensions.

```{literalinclude} HW8_matlab.m
:language: matlab
:lines: 174-220
```
