# Class 21 GPP: User Functions and Modular Programming in MATLAB

## Setup Instructions

Create a new folder for today's work. Good modular programming practice requires the creation of multiple .m files, so keeping them organized is important!

## Part 1: Basic Function Writing

## Problem 1: Temperature Converter

Write a function called fahrenheitToCelsius that converts a temperature from Fahrenheit to Celsius using the formula: C = (F - 32) × 5/9

Requirements:

- Save as fahrenheitToCelsius.m
- Single input: temperature in Fahrenheit
- Single output: temperature in Celsius
- Include a proper help comment block

**Test your function:**

```matlab
temp_C = fahrenheitToCelsius(98.6)  % Should return 37
temp_C = fahrenheitToCelsius(32)    % Should return 0
```

### Problem 2: Volume Calculator

Write a function called cylinderVolume that calculates the volume of a cylinder using

V = π r²h

Requirements:

- Save as cylinderVolume.m
- Two inputs: radius and height
- Single output: volume
- Include input validation to ensure both inputs are positive
- Use error('message') if validation fails

**Test your function:**

```matlab
vol = cylinderVolume(3, 10)  % Should return approximately 282.74
```

## Part 2: Multiple Outputs

### Problem 3: Circle Properties

Write a function called circleProperties that calculates both the area and circumference of a circle given its radius.

- Area = π r²
- Circumference = 2 π r

Requirements:

- Save as circleProperties.m
- Single input: radius
- Two outputs: area and circumference (in that order)
- Include proper help comments

**Test your function:**

```matlab
[a, c] = circleProperties(5);
fprintf('Area: %.2f, Circumference: %.2f\n', a, c);
```

### Problem 4: Vector Statistics

Write a function called vectorStats that takes a vector of numbers and returns three statistics: the minimum value, maximum value, and range (max - min).

Requirements:

- Save as vectorStats.m
- Single input: a vector of numbers
- Three outputs: minimum, maximum, range
- Use MATLAB's built-in min() and max() functions

**Test your function:**

```matlab
data = [12, 5, 8, 19, 3, 15];
[minVal, maxVal, rangeVal] = vectorStats(data)
```

## Part 3: Functions Without Outputs

### Problem 5: Grade Reporter

Write a function called printGradeReport that displays a formatted grade report to the console. It should NOT return any values.

Requirements:

- Save as printGradeReport.m
- Three inputs: student name, exam score, homework score
- No outputs
- Calculate and display the final grade as: (0.7 × exam + 0.3 × homework)
- Use fprintf to display results nicely formatted

**Example output:**

```
Grade Report for Alice
Exam Score: 85.00
Homework Score: 92.00
Final Grade: 87.10
```

**Test your function:**

```matlab
printGradeReport('Alice', 85, 92)
```

## Part 4: Modular Design with Local Functions

### Problem 6: BMI Calculator with Classification

Write a primary function called analyzeBMI that calculates Body Mass Index and classifies it. Use local helper functions for organization.

BMI = weight(kg) / height(m)²

Classifications:

- BMI < 18.5: "Underweight"
- 18.5 ≤ BMI < 25: "Normal weight"
- 25 ≤ BMI < 30: "Overweight"
- BMI ≥ 30: "Obese"

Requirements:

- Save as analyzeBMI.m
- Primary function inputs: weight (kg) and height (m)
- Primary function outputs: BMI value and classification string
- Create a local helper function classifyBMI that takes the BMI number and returns the classification string
- Include input validation in the primary function

**Structure:**

```matlab
function [bmi, category] = analyzeBMI(weight, height)
    % Your code for validation and calling helper
    % ...
    bmi = calculateBMI(weight, height);
    category = classifyBMI(bmi);
end

function bmi = calculateBMI(weight, height)
    % Local helper function
end

function category = classifyBMI(bmi)
    % Local helper function
end
```

**Test your function:**

```matlab
[bmi, cat] = analyzeBMI(70, 1.75);
fprintf('BMI: %.1f - Category: %s\n', bmi, cat);
```

## Challenge Problem (Extra - if time permits)

### Problem 7: Quadratic Solver

Write a function called solveQuadratic that solves the quadratic equation ax² + bx + c = 0 using the quadratic formula.

Requirements:

- Three inputs: coefficients a, b, c
- Two outputs: the two roots (x1 and x2)
- Handle the case where there are no real solutions by returning NaN for both roots
- Remember: discriminant = b² - 4ac
- If discriminant < 0: no real solutions
- Roots: x = (-b ± √discriminant) / (2a)

**Test cases:**

```matlab
[x1, x2] = solveQuadratic(1, -3, 2)     % Should give x1=2, x2=1
[x1, x2] = solveQuadratic(1, 0, -4)     % Should give x1=2, x2=-2
[x1, x2] = solveQuadratic(1, 2, 5)      % Should give NaN, NaN (no real solutions)
```
