# Class 26 GPP Solutions: User Functions and Modular Programming in MATLAB

Full solutions for every problem in the [GPP](Class26_GPP.md).

## Problem 1: Temperature Converter

```matlab
function tempC = fahrenheitToCelsius(tempF)
% FAHRENHEITTOCELSIUS Converts temperature from Fahrenheit to Celsius
%   tempC = fahrenheitToCelsius(tempF) converts a temperature from
%   Fahrenheit to Celsius using the formula C = (F - 32) * 5/9
%
% Input:
%   tempF - temperature in Fahrenheit
%
% Output:
%   tempC - temperature in Celsius
tempC = (tempF - 32) * 5/9;
end
```

## Problem 2: Volume Calculator

```matlab
function volume = cylinderVolume(radius, height)
% CYLINDERVOLUME Calculates the volume of a cylinder
%   volume = cylinderVolume(radius, height) computes the volume of a
%   cylinder given its radius and height using V = pi*r^2*h
%
% Inputs:
%   radius - radius of the cylinder (must be positive)
%   height - height of the cylinder (must be positive)
%
% Output:
%   volume - volume of the cylinder

% Input validation
if radius <= 0
    error('Radius must be positive');
end
if height <= 0
    error('Height must be positive');
end

% Calculate volume
volume = pi * radius^2 * height;
end
```

## Problem 3: Circle Properties

```matlab
function [area, circumference] = circleProperties(radius)
% CIRCLEPROPERTIES Calculates area and circumference of a circle
%   [area, circumference] = circleProperties(radius) computes both the
%   area and circumference of a circle given its radius.
%
% Formulas:
%   Area = pi * r^2
%   Circumference = 2 * pi * r
%
% Input:
%   radius - radius of the circle
%
% Outputs:
%   area - area of the circle
%   circumference - circumference of the circle
area = pi * radius^2;
circumference = 2 * pi * radius;
end
```

## Problem 4: Vector Statistics

```matlab
function [minVal, maxVal, rangeVal] = vectorStats(data)
% VECTORSTATS Computes basic statistics for a vector
%   [minVal, maxVal, rangeVal] = vectorStats(data) returns the minimum,
%   maximum, and range of values in the input vector.
%
% Input:
%   data - vector of numbers
%
% Outputs:
%   minVal - minimum value in the vector
%   maxVal - maximum value in the vector
%   rangeVal - range (max - min)
minVal = min(data);
maxVal = max(data);
rangeVal = maxVal - minVal;
end
```

## Problem 5: Grade Reporter

```matlab
function printGradeReport(studentName, examScore, homeworkScore)
% PRINTGRADEREPORT Displays a formatted grade report
%   printGradeReport(studentName, examScore, homeworkScore) calculates
%   and displays a student's final grade based on exam (70%) and
%   homework (30%) scores.
%
% Inputs:
%   studentName - name of the student (string)
%   examScore - exam score (0-100)
%   homeworkScore - homework score (0-100)

% Calculate final grade
finalGrade = 0.7 * examScore + 0.3 * homeworkScore;

% Display formatted report
fprintf('Grade Report for %s\n', studentName);
fprintf('Exam Score: %.2f\n', examScore);
fprintf('Homework Score: %.2f\n', homeworkScore);
fprintf('Final Grade: %.2f\n', finalGrade);
end
```

## Problem 6: BMI Calculator with Classification

```matlab
function [bmi, category] = analyzeBMI(weight, height)
% ANALYZEBMI Calculates BMI and provides health classification
%   [bmi, category] = analyzeBMI(weight, height) computes the Body Mass
%   Index and returns a health classification category.
%
% Inputs:
%   weight - weight in kilograms (must be positive)
%   height - height in meters (must be positive)
%
% Outputs:
%   bmi - calculated BMI value
%   category - health classification string

% Input validation
if weight <= 0
    error('Weight must be positive');
end
if height <= 0
    error('Height must be positive');
end

% Calculate BMI and classify
bmi = calculateBMI(weight, height);
category = classifyBMI(bmi);
end

function bmi = calculateBMI(weight, height)
bmi = weight / height^2;
end

function category = classifyBMI(bmi)
if bmi < 18.5
    category = 'Underweight';
elseif bmi < 25
    category = 'Normal weight';
elseif bmi < 30
    category = 'Overweight';
else
    category = 'Obese';
end
end
```

## Problem 7 (Challenge): Quadratic Solver

```matlab
function [x1, x2] = solveQuadratic(a, b, c)
% SOLVEQUADRATIC Solves quadratic equation ax^2 + bx + c = 0
%   [x1, x2] = solveQuadratic(a, b, c) returns the two roots of the
%   quadratic equation using the quadratic formula. Returns NaN for
%   both roots if no real solutions exist.
%
% Inputs:
%   a - coefficient of x^2
%   b - coefficient of x
%   c - constant term
%
% Outputs:
%   x1 - first root (or NaN if no real solutions)
%   x2 - second root (or NaN if no real solutions)

% Calculate discriminant
discriminant = b^2 - 4*a*c;

% Check if real solutions exist
if discriminant < 0
    % No real solutions
    x1 = NaN;
    x2 = NaN;
else
    % Calculate both roots
    x1 = (-b + sqrt(discriminant)) / (2*a);
    x2 = (-b - sqrt(discriminant)) / (2*a);
end
end
```
