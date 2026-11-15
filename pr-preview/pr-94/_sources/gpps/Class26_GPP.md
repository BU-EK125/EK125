# Class 26 GPP: User Functions and Modular Programming in MATLAB

Each problem below asks you to write a separate MATLAB function and save
it as its own `.m` file -- there's no single script to download today.
Create a new folder for your group's work first: good modular
programming practice means keeping multiple small `.m` files organized.

## Part 1: Basic Function Writing

**Problem 1 (Temperature Converter):** Write `fahrenheitToCelsius(tempF)`
converting Fahrenheit to Celsius with `C = (F - 32) * 5/9`. Save as
`fahrenheitToCelsius.m`. Single input, single output, with a proper help
comment block.
```matlab
temp_C = fahrenheitToCelsius(98.6)  % Should return 37
temp_C = fahrenheitToCelsius(32)    % Should return 0
```

**Problem 2 (Volume Calculator):** Write `cylinderVolume(radius, height)`
using `V = pi * r^2 * h`. Save as `cylinderVolume.m`. Validate that both
inputs are positive, using `error('message')` if not.
```matlab
vol = cylinderVolume(3, 10)  % Should return approximately 282.74
```

## Part 2: Multiple Outputs

**Problem 3 (Circle Properties):** Write `circleProperties(radius)`
returning both the **area** (`pi * r^2`) and **circumference**
(`2 * pi * r`), in that order. Save as `circleProperties.m`.
```matlab
[a, c] = circleProperties(5);
fprintf('Area: %.2f, Circumference: %.2f\n', a, c);
```

**Problem 4 (Vector Statistics):** Write `vectorStats(data)` returning
three outputs -- minimum, maximum, and range (`max - min`) -- using
MATLAB's built-in `min()` and `max()`. Save as `vectorStats.m`.
```matlab
data = [12, 5, 8, 19, 3, 15];
[minVal, maxVal, rangeVal] = vectorStats(data)
```

## Part 3: Functions Without Outputs

**Problem 5 (Grade Reporter):** Write `printGradeReport(name, examScore,
homeworkScore)` that displays a formatted grade report and returns
nothing. Final grade is `0.7 * exam + 0.3 * homework`. Save as
`printGradeReport.m`.
```matlab
printGradeReport('Alice', 85, 92)
```
Expected output:
```
Grade Report for Alice
Exam Score: 85.00
Homework Score: 92.00
Final Grade: 87.10
```

## Part 4: Modular Design with Local Functions

**Problem 6 (BMI Calculator with Classification):** Write a **primary**
function `analyzeBMI(weight, height)` (BMI = `weight(kg) / height(m)^2`)
that returns the BMI and a classification string ("Underweight" below
18.5, "Normal weight" 18.5-25, "Overweight" 25-30, "Obese" 30+). Use a
**local helper function** `classifyBMI` for the classification logic, and
validate both inputs are positive. Save as `analyzeBMI.m`.
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
```matlab
[bmi, cat] = analyzeBMI(70, 1.75);
fprintf('BMI: %.1f - Category: %s\n', bmi, cat);
```

## Challenge Problem (Extra, if time permits)

**Problem 7 (Quadratic Solver):** Write `solveQuadratic(a, b, c)` solving
`ax^2 + bx + c = 0` via the quadratic formula. Return `NaN` for both
roots if the discriminant (`b^2 - 4ac`) is negative.
```matlab
[x1, x2] = solveQuadratic(1, -3, 2)   % Should give x1=2, x2=1
[x1, x2] = solveQuadratic(1, 0, -4)   % Should give x1=2, x2=-2
[x1, x2] = solveQuadratic(1, 2, 5)    % Should give NaN, NaN
```
