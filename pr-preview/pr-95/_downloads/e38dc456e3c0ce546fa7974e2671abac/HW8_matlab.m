% EK125 Homework 8 -- MATLAB half
% Plotting in MATLAB (Class 22) and creating vectors and matrices (Class 23)
%
% Name: ____________________
% Lab section: ______
%
% Due: Tuesday November 24, 11:59 PM. Submit to Gradescope.
%
% This half is worth 50 points (Problems 4-6). Problems 1-3 are in HWA_python.py.
%
% SUBMIT ALL OF THESE FILES TO GRADESCOPE (together with the Python files):
%     Homework_8_matlab.m
%     stress_strain_matlab.png
%     sensor_rows.png
%     rectifier.png
%
% RULES
% - Individual work.
% - Use good programming practice: comments, meaningful variable names,
%   consistent indentation.
% - NO global variables, NO break/continue, NO `while true` loops.
% - Your script must run from top to bottom (green Run button) without errors.
% - End lines with a semicolon UNLESS a problem tells you to display the
%   result. Where it says "display", leave the semicolon off on purpose.
% - Use %% section breaks (already provided) so you can run one problem at a
%   time with "Run Section".
%
% EVERY FIGURE NEEDS: x- and y-axis labels WITH UNITS, a title, a legend when
% there is more than one line, grid on, and saveas(gcf, 'filename.png').

clear; clc; close all;

%% ========================================================================
% PROBLEM 4 (15 points): Stress-strain curves again, in MATLAB
% ========================================================================
% Recreate your Problem 1 figure in MATLAB. Same data, same look.
% Look back at your Python code and translate it one line at a time.

% Given data (do not change):
strainPercent = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8];
steelStressMPa = [0, 200, 400, 520, 560, 580, 590, 595, 600];
aluminumStressMPa = [0, 70, 140, 210, 250, 265, 275, 280, 283];

% Part A (8 pts): Plot both materials on ONE set of axes.
% REQUIRED:
% - Steel: blue solid line with circle markers ('b-o')
% - Aluminum: red dashed line with square markers ('r--s')
% - Both lines: 'LineWidth', 2
% - x-axis label 'Strain (%)', y-axis label 'Stress (MPa)'
% - Title exactly: 'Stress-Strain Curves: Steel vs. Aluminum'
% - legend('Steel', 'Aluminum', 'Location', 'southeast') and grid on
% - Save as 'stress_strain_matlab.png'
% Hint: you need `hold on` to add the second line to the same axes.

% YOUR CODE HERE



% Part B (4 pts): Calculate the elastic modulus of each metal, exactly as in
% Problem 1 Part B: use the FIRST TWO data points, convert percent strain to
% a fraction, and convert MPa to GPa.
% CAREFUL: think about which index numbers MATLAB uses for the first two
% elements.
% REQUIRED: use fprintf to print exactly (1 decimal place):
% Steel elastic modulus: ___ GPa
% Aluminum elastic modulus: ___ GPa
% Your numbers must match your Python output.
% fprintf is MATLAB's formatted print. It works like this (%.1f means
% "a number with 1 decimal place", \n means "new line"):
% fprintf('Steel elastic modulus: %.1f GPa\n', steelModulusGPa);

% YOUR CODE HERE



% Part C (3 pts): In the comment lines below, list THREE differences between
% your Python code (Problem 1) and your MATLAB code (Problem 4).
% Each difference must be about the LANGUAGE (syntax or how it works),
% not about the data or your variable names.
%
% DIFFERENCE 1:
% DIFFERENCE 2:
% DIFFERENCE 3:


%% ========================================================================
% PROBLEM 5 (20 points): Temperature sensor grid
% ========================================================================
% A metal plate has 12 temperature sensors in a grid of 3 rows and 4
% columns. The data logger saves the readings (in °C) as one long list,
% going DOWN each column of sensors, one column at a time.

% Given data (do not change):
readings = [22 21 22 23 30 24 25 31 26 24 23 99];

% Part A (3 pts): Use reshape to turn readings into a 3 x 4 matrix called
% temps. DISPLAY temps (no semicolon).
% Then write a one-line comment explaining why the FIRST COLUMN of temps is
% 22, 21, 22 and not 22, 21, 22, 23.

% YOUR CODE HERE



% Part B (4 pts): PREDICT, THEN VERIFY. This is practice for paper exams.
% BEFORE running anything, look at your temps matrix and write what each
% expression will display. Then type each expression on its own line
% (no semicolon) and run the section.
% Graded on completion: write honest predictions, then say whether you were
% right. Wrong predictions that you correct still get full credit.
%
% PREDICTION 1: temps(2,3) ->
% PREDICTION 2: temps(3,:) ->
% PREDICTION 3: temps(:,2) ->
% PREDICTION 4: temps(end,end) ->

% YOUR FOUR EXPRESSIONS HERE



% VERIFY (which predictions were right? fix any that were wrong):
%


% Part C (2 pts): The sensor in row 3, column 4 is faulty (99 °C is
% impossible here). Replace that one value with 25 using row and column
% subscripts.

% YOUR CODE HERE



% Part D (3 pts): The engineers suspect a hot spot in the block made of
% rows 2-3 and columns 2-3. Store that 2 x 2 block in a variable called
% hotSpot using the colon operator. DISPLAY hotSpot.

% YOUR CODE HERE



% Part E (4 pts): Any reading above 28 °C is "hot".
% 1. Create a logical matrix called isHot that is true where temps > 28.
%    DISPLAY it.
% 2. Make a COPY of temps called cappedTemps. Then, using LOGICAL INDEXING
%    (no loops!), set every value in cappedTemps above 28 to exactly 28.
%    DISPLAY cappedTemps.
% temps itself must not change in this part.

% YOUR CODE HERE



% Part F (2 pts): Three new sensors were added as a fifth column, reading
% 20, 21, and 22 °C (top to bottom).
% Create them as a COLUMN vector called newColumn, then use concatenation
% to add it to the right side of temps (temps becomes 3 x 5).
% DISPLAY temps.

% YOUR CODE HERE



% Part G (2 pts): Plot each ROW of temps as its own line against sensor
% column number 1-5, all on one figure.
% REQUIRED: a different marker for each row, xticks(1:5),
% x-axis label 'Sensor column (position)', y-axis label 'Temperature (°C)',
% a title, legend('Row 1', 'Row 2', 'Row 3'), grid on.
% Save as 'sensor_rows.png'.

% YOUR CODE HERE



%% ========================================================================
% PROBLEM 6 (15 points): Half-wave rectifier
% ========================================================================
% A half-wave rectifier is a circuit with a diode that lets current through
% in only one direction. It turns an AC voltage into a voltage that is
% never negative: the positive half of each wave passes through unchanged,
% and the negative half becomes 0 V.

% Part A (3 pts): Create:
% - t: 1000 evenly spaced times from 0 to 0.05 s (use linspace)
% - vIn: the input voltage, vIn = 5 sin(2 pi 60 t) (5 V amplitude, 60 Hz)
% (Multiplying a vector by a scalar works element by element, just like
% the sin(x) examples in Class 22.)

% YOUR CODE HERE



% Part B (3 pts): Create vOut, the rectifier output. Start with a copy of
% vIn, then use LOGICAL INDEXING (no loops!) to set every negative value
% to 0.

% YOUR CODE HERE



% Part C (6 pts): Make ONE figure with two subplots stacked vertically
% (2 rows, 1 column):
% Top: vIn in blue. Bottom: vOut in red. Both: 'LineWidth', 1.5
% Plot time in MILLISECONDS on the x-axis (make a new vector tMs).
% REQUIRED on BOTH subplots: x-axis label 'Time (ms)', y-axis label
% 'Voltage (V)', a title, ylim([-6 6]), and grid on.
% Save as 'rectifier.png'.

% YOUR CODE HERE



% Part D (3 pts): Build a matrix called results with ONE ROW PER TIME POINT
% and three columns: time, vIn, vOut. (t, vIn, and vOut are row vectors,
% so you will need to transpose them first.)
% DISPLAY only the first 5 rows of results.
% Then, in a comment, state the dimensions of results (rows x columns).

% YOUR CODE HERE

% DIMENSIONS OF results:
