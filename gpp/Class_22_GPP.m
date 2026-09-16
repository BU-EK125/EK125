%% Class 22: GPP
%
% Instructions: Complete the following problems by writing your code
% in the indicated sections. Test each section before moving on.


%% =========================================================================
%% PROBLEM 1: Signal Processing - Finding Peaks in Noisy Data (12 minutes)
%% =========================================================================
% A sensor records temperature fluctuations over time. Your goal is to
% identify significant temperature spikes.

% Given data (copy and run this):
time = 0:0.1:10;  % Time in seconds
temperature = 20 + 5*sin(2*pi*0.5*time) + randn(size(time));  % Temperature in Celsius

% Part A (3 pts): Plot the temperature data vs. time
% Add appropriate labels and title


% YOUR CODE HERE




% Part B (4 pts): Use findpeaks() to find ALL peaks in the temperature data
% (A peak is any local maximum - a point higher than its immediate neighbors)
% Store the peak values in a variable called 'peaks'
% Store the peak locations in a variable called 'locations'
% Display how many peaks were found using fprintf


% YOUR CODE HERE




% Part C (5 pts): Now find only SIGNIFICANT peaks using these criteria:
%   - Minimum peak height: 23°C
%   - Minimum distance between peaks: 10 samples
% Plot the original data AND mark the significant peaks with red circles
% Display how many significant peaks were found
% (HINT: use hold on and plot time(locations), peaks, 'ro')


% YOUR CODE HERE




%% =========================================================================
%% PROBLEM 2: Statistics - Analyzing Heart Rate Data (15 minutes)
%% =========================================================================
% You collected heart rate data from 20 subjects under two conditions:
% resting and after exercise.

% Given data (copy and run this):
restingHR = [72, 68, 75, 70, 73, 69, 71, 74, 68, 72, 70, 73, 71, 69, 72, 74, 70, 68, 71, 73];
exerciseHR = [145, 138, 152, 141, 148, 136, 143, 150, 139, 145, 142, 147, 144, 137, 146, 151, 140, 138, 143, 148];

% Part A (3 pts): Create a histogram of the resting heart rate data
% Include appropriate axis labels and title


% YOUR CODE HERE




% Part B (4 pts): Calculate and display the following statistics for BOTH conditions:
%   - Mean
%   - Median
%   - Standard deviation
% Format: "Resting - Mean: XX.X, Median: XX.X, Std: XX.X"


% YOUR CODE HERE




% Part C (5 pts): Create a box plot to compare the two conditions
% HINT: You need to combine the data and create group labels
%   combinedData = [restingHR, exerciseHR]';
%   groups = [ones(1,20), 2*ones(1,20)]';
% Label the x-axis categories as 'Resting' and 'Exercise'
% Add appropriate y-axis label and title


% YOUR CODE HERE




% Part D (3 pts): Perform a two-sample t-test to determine if the heart rates
% are significantly different between conditions
% Display a message: "Heart rates are significantly different" or
%                   "No significant difference detected"


% YOUR CODE HERE




%% =========================================================================
%% PROBLEM 3: Signal Processing - ECG Peak Detection (12 minutes)
%% =========================================================================
% This problem simulates what you'll do in your course project.
% You have a simplified ECG signal and need to detect heartbeats.

% Given data (copy and run this):
t = 0:0.001:5;  % 5 seconds of data
ecg = sin(2*pi*1.2*t) + 0.3*sin(2*pi*2.4*t) + 0.2*randn(size(t));  % Simulated ECG

% Part A (4 pts): Plot the ECG signal
% Label axes as 'Time (s)' and 'Voltage (mV)'


% YOUR CODE HERE




% Part B (5 pts): Use findpeaks() to detect R-peaks (heartbeats) with these criteria:
%   - Minimum peak height: 0.5 mV
%   - Minimum peak distance: 400 samples (to avoid detecting the same beat twice)
% Store results in variables: peakVoltages and peakLocations


% YOUR CODE HERE




% Part C (3 pts): Calculate and display the heart rate in beats per minute (bpm)
% HINT: Count the number of peaks, divide by total time in minutes
%       Heart rate = (number of peaks / total time in minutes)


% YOUR CODE HERE




%% =========================================================================
%% PROBLEM 4: Optimization - Minimizing a Cost Function (11 minutes)
%% =========================================================================
% A company's profit function is: P(x) = -2x^2 + 20x - 30
% where x is the number of units produced (in thousands)

% Part A (3 pts): Create an anonymous function for the COST (negative profit)
% Name it: costFunction
% HINT: To minimize profit, we maximize cost, so cost = -P(x) = 2x^2 - 20x + 30


% YOUR CODE HERE




% Part B (5 pts): Use fminunc() to find the optimal production level
% - Start with an initial guess of x0 = 0
% - Store the optimal x value in: optimalProduction
% - Store the minimum cost in: minCost
% HINT: [optimalProduction, minCost] = fminunc(costFunction, x0);


% YOUR CODE HERE




% Part C (3 pts): Calculate the maximum profit and display results
% Format: "Optimal production: X.XX thousand units"
%         "Maximum profit: $X.XX"


% YOUR CODE HERE




%% =========================================================================
%% BONUS CHALLENGE: Combining Multiple Toolboxes (Optional - if time permits)
%% =========================================================================
% Create synthetic ECG data, add noise, detect peaks, and perform statistical analysis

% Part A: Generate a synthetic ECG signal (3 minutes)
% - Time vector: 0 to 10 seconds, 1000 samples per second
% - Signal: 1.5*sin(2*pi*1.5*t) with added noise (0.3*randn)


% YOUR CODE HERE




% Part B: Detect peaks and calculate inter-beat intervals (4 minutes)
% - Use findpeaks with appropriate parameters
% - Calculate time between consecutive beats (RR intervals)
% HINT: diff(peakLocations) gives you the intervals in samples
%       Convert to seconds by dividing by sampling rate


% YOUR CODE HERE




% Part C: Statistical analysis of heart rate variability (3 minutes)
% - Calculate mean and standard deviation of RR intervals
% - Create a histogram of RR intervals


% YOUR CODE HERE




