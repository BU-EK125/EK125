# Class 25 GPP: MATLAB Scripts, Documentation, and File I/O

This is a script-based exercise: work through the problems directly in
MATLAB (not in a notebook). Download the file below, open it locally, and
run each section as you go -- the instructions are also on this page so
you can read them without switching windows.

Download: [Class25_GPP.m](Class25_GPP.m)

## Part 1: Script Basics and Documentation

**Exercise 1.1:** Create a script `temperature_converter.m` that stores a
Fahrenheit temperature, converts it to Celsius and Kelvin, and displays
all three using `fprintf` with 2 decimal places. Bonus: add a proper
header block (author, date, description, inputs, outputs).

**Exercise 1.2:** The provided code computes how many of a list of test
scores are above average, but has no documentation at all. Add a header
block, single-line comments explaining each step, and a multi-line
comment block explaining the purpose.

## Part 2: Working with Directories

**Exercise 2.1:** Display your current directory, create a folder
`MyProject` with subfolders `Data` and `Results` inside it, and create a
`Backup` folder only if it doesn't already exist.

**Exercise 2.2:** Rewrite three Windows-style hardcoded paths using
`fullfile` so they work cross-platform, then test whether each file
exists with `isfile`.

## Part 3: Reading Data Files

**Exercise 3.1:** Create a `test_scores.csv` with four students' scores
across three tests. Read it with `readtable`, calculate each student's
average, and find the highest and lowest class average per test.

**Exercise 3.2:** Read a color image (e.g. `peppers.png`), display the
original plus its three color channels in one figure with `subplot`,
build a red-only version, and save it.

## Part 4: Writing and Saving Data

**Exercise 4.1:** Generate a noisy sine signal and save it three ways:
as a `.mat` file, a `.csv` file, and a formatted `.txt` file with a
header.

**Exercise 4.2:** Create a `Results/Figures` and `Results/Data` folder
structure (checking existence first), generate a plot, and save the
figure and its underlying data into the right subfolders using
`fullfile`.

## Part 5: File I/O with Text Files

**Exercise 5.1:** Write a text file of five numbers, one per line, then
read it back line-by-line with `fopen`/`fgetl`/`fclose`, convert each
line to a number, and report the mean and standard deviation.

**Exercise 5.2:** Generate a formatted lab report file with a title
header, your name and date, and three statistics (mean, max, min) from
any dataset.

## Part 6: Integration Challenge

**Exercise 6.1:** Build a complete pipeline: set up a `Data/Raw`,
`Data/Processed`, `Results` folder structure; generate and save 24 hours
of simulated temperature data; process it (hourly stats, readings above
a threshold); plot and save a figure; and generate a full text report.
Use `fullfile` throughout and check file/folder existence before acting
on it.

## Tips for Success

1. Test incrementally -- run your script after adding each feature
2. Use `pwd` and `dir` to check your location and available files
3. Always `fclose` after `fopen`
4. Use `isfile` and `isfolder` to check existence before operating
5. Use `clear` and `clc` at the start of scripts while testing
