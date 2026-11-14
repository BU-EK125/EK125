%% Part 1: Script Basics and Documentation

%%Exercise 1.1: Create Your First Script
% %Create a script called `temperature_converter.m` that:
% 1. Stores a temperature in Fahrenheit (pick any value)
% 2. Converts it to Celsius using the formula: C = (F - 32) × 5/9
% 3. Converts it to Kelvin using: K = C + 273.15
% 4. Displays all three temperatures using `fprintf` with 2 decimal places
%
% **Bonus**: Add proper header documentation including author, date, description, inputs, and outputs.
%

% TEMPERATURE_CONVERTER - Convert Fahrenheit to Celsius and Kelvin
%
% Author: Your Name
% Date: November 6, 2025
%
% Description:
%   This script converts a temperature from Fahrenheit to both
%   Celsius and Kelvin scales and displays all three values.
%
% Inputs: None (temperature hardcoded in script)
% Outputs: Formatted temperature values printed to console

% Store initial temperature in Fahrenheit
tempF = 72;

% Convert to Celsius
tempC = (tempF - 32) * 5/9;

% Convert to Kelvin
tempK = tempC + 273.15;

% Display all three temperatures
fprintf('Temperature in Fahrenheit: %.2f°F\n', tempF);
fprintf('Temperature in Celsius: %.2f°C\n', tempC);
fprintf('Temperature in Kelvin: %.2fK\n', tempK);



%% Exercise 1.2: Comment Review
% Given this poorly documented code, add:
% - A proper header block
% - Single-line comments explaining each step
% - A multi-line comment block explaining the purpose


% GRADE_ANALYZER - Count test scores above the class average
%
% Author: Your Name
% Date: November 6, 2025
%
% Description:
%   This script analyzes a set of test scores to determine how many
%   scores are above the class average. It demonstrates array operations
%   and logical indexing in MATLAB.
%
% Inputs: None (data hardcoded in script)
% Outputs: Count of above-average scores printed to console

%{
This script performs a simple statistical analysis on test scores.
It calculates the mean score, filters for scores above that mean,
and counts how many students scored above average.
This is useful for quick grade distribution analysis.
%}

% Store test scores in an array
data = [85, 92, 78, 88, 95, 72, 89];

% Calculate the average (mean) score
avg = mean(data);

% Filter for scores above average using logical indexing
above = data(data > avg);

% Count how many scores are above average
count = length(above);

% Display the result
fprintf('Count: %d\n', count);


%% Part 2: Working with Directories

%% Exercise 2.1: Directory Navigation
% Write commands to:
% 1. Display your current directory
% 2. Create a new folder called `MyProject`
% 3. Inside `MyProject`, create two subfolders: `Data` and `Results`
% 4. Check if a folder called `Backup` exists, and create it if it doesn't

% Display current directory
currentDir = pwd

% Create main project folder
mkdir('MyProject')

% Create subfolders inside MyProject
mkdir(fullfile('MyProject', 'Data'))
mkdir(fullfile('MyProject', 'Results'))

% Check if Backup folder exists, create if it doesn't
if ~isfolder('Backup')
    mkdir('Backup')
    fprintf('Backup folder created.\n');
else
    fprintf('Backup folder already exists.\n');
end



%% Exercise 2.2: Cross-Platform Paths

%Rewrite these paths using `fullfile` to make them cross-platform
%compatible:

% Original (Windows-specific)
path1 = 'Data\Raw\experiment1.csv';
path2 = 'Results\Figures\plot1.png';
path3 = '..\SharedData\reference.mat';

%Create a script that builds these paths correctly and tests if each file
%exists using `isfile`.

% BUILD_PATHS - Create cross-platform file paths
%
% This script demonstrates building portable file paths
% using fullfile instead of hardcoded path separators

% Build paths using fullfile (works on Windows, Mac, Linux)
path1 = fullfile('Data', 'Raw', 'experiment1.csv');
path2 = fullfile('Results', 'Figures', 'plot1.png');
path3 = fullfile('..', 'SharedData', 'reference.mat');

% Display the paths
fprintf('Path 1: %s\n', path1);
fprintf('Path 2: %s\n', path2);
fprintf('Path 3: %s\n', path3);

% Test if each file exists
if isfile(path1)
    fprintf('File 1 exists!\n');
else
    fprintf('File 1 does not exist.\n');
end

if isfile(path2)
    fprintf('File 2 exists!\n');
else
    fprintf('File 2 does not exist.\n');
end

if isfile(path3)
    fprintf('File 3 exists!\n');
else
    fprintf('File 3 does not exist.\n');
end

%% Part 3: Reading Data Files

%% Exercise 3.1: CSV Data Analysis
%Create a CSV file called `test_scores.csv` with this data:
%
% Name,Test1,Test2,Test3
% Alice,85,92,88
% Bob,78,85,90
% Carol,92,95,87
% David,88,82,91
%
% Write a script that:
% 1. Reads the CSV using `readtable`
% 2. Calculates each student's average score
% 3. Finds the highest and lowest class average for each test
% 4. Displays results using `fprintf`

% ANALYZE_TEST_SCORES - Analyze student test scores from CSV
%
% Author: Your Name
% Date: November 6, 2025
%
% Description:
%   Reads test scores from CSV file, calculates student averages,
%   and finds class statistics for each test.
%
% Inputs: test_scores.csv
% Outputs: Statistics printed to console

% Read the CSV file as a table
scores = readtable('test_scores.csv');

% Calculate each student's average
studentAvg = mean([scores.Test1, scores.Test2, scores.Test3], 2);

% Display each student's average
fprintf('Student Averages:\n');
for i = 1:height(scores)
    fprintf('%s: %.2f\n', scores.Name{i}, studentAvg(i));
end

% Calculate class statistics for each test
fprintf('\nClass Statistics by Test:\n');
fprintf('Test 1 - High: %.2f, Low: %.2f, Avg: %.2f\n', ...
    max(scores.Test1), min(scores.Test1), mean(scores.Test1));
fprintf('Test 2 - High: %.2f, Low: %.2f, Avg: %.2f\n', ...
    max(scores.Test2), min(scores.Test2), mean(scores.Test2));
fprintf('Test 3 - High: %.2f, Low: %.2f, Avg: %.2f\n', ...
    max(scores.Test3), min(scores.Test3), mean(scores.Test3));


%% Exercise 3.2: Working with Images
% Find any color image (or use a built-in MATLAB image like `peppers.png`):
%
% Write a script that:
% 1. Reads the image
% 2. Displays the original image
% 3. Extracts and displays each color channel (Red, Green, Blue) separately
% 4. Creates a new image with only the red channel (set green and blue to zero)
% 5. Saves the red-only image as `red_only.png`
%
% **Hint**: Use `subplot` to display all images in one figure.

% IMAGE_CHANNEL_ANALYSIS - Extract and display color channels
%
% Author: Your Name
% Date: November 6, 2025
%
% Description:
%   Reads a color image, displays individual RGB channels,
%   creates a red-only version, and saves it.
%
% Inputs: peppers.png (or any color image)
% Outputs: Figure with channel displays, red_only.png file

% Read a color image (using built-in MATLAB image)
img = imread('peppers.png');

% Display original image size and type
fprintf('Image size: %d x %d x %d\n', size(img, 1), size(img, 2), size(img, 3));
fprintf('Image class: %s\n', class(img));

% Extract individual color channels
redChannel = img(:, :, 1);
greenChannel = img(:, :, 2);
blueChannel = img(:, :, 3);

% Create figure with subplots
figure('Name', 'Color Channel Analysis');

% Display original image
subplot(2, 2, 1);
imshow(img);
title('Original Image');

% Display red channel
subplot(2, 2, 2);
imshow(redChannel);
title('Red Channel');

% Display green channel
subplot(2, 2, 3);
imshow(greenChannel);
title('Green Channel');

% Display blue channel
subplot(2, 2, 4);
imshow(blueChannel);
title('Blue Channel');

% Create red-only image (green and blue set to zero)
redOnly = img;
redOnly(:, :, 2) = 0;  % Remove green
redOnly(:, :, 3) = 0;  % Remove blue

% Display red-only image
figure('Name', 'Red Channel Only');
imshow(redOnly);
title('Red Channel Only');

% Save the red-only image
imwrite(redOnly, 'red_only.png');
fprintf('Red-only image saved as red_only.png\n');

%% Part 4: Writing and Saving Data

%%Exercise 4.1: Multiple File Formats

%Generate simulation data and save it in three formats:


% Save this data as:
% 1. A `.mat` file with both variables
% 2. A `.csv` file with two columns (time, signal)
% 3. A `.txt` file with a formatted header describing the data

% SAVE_SIMULATION_DATA - Save data in multiple formats
%
% Author: Your Name
% Date: November 6, 2025
%
% Description:
%   Generates simulation data and saves it in .mat, .csv,
%   and formatted .txt file formats.

% Generate simulation data
time = 0:0.1:10;
signal = sin(time) + 0.1*randn(size(time));

% Save as .mat file
save('simulation_data.mat', 'time', 'signal');
fprintf('Data saved to simulation_data.mat\n');

% Save as .csv file (combine into matrix, then write)
data_matrix = [time; signal]';  % Transpose to get columns
writematrix(data_matrix, 'simulation_data.csv');
fprintf('Data saved to simulation_data.csv\n');

% Save as formatted .txt file with header
fileID = fopen('simulation_data.txt', 'w');
fprintf(fileID, '===================================\n');
fprintf(fileID, 'Simulation Data\n');
fprintf(fileID, '===================================\n');
fprintf(fileID, 'Generated: %s\n', datestr(now));
fprintf(fileID, 'Data points: %d\n', length(time));
fprintf(fileID, 'Time range: %.1f to %.1f seconds\n', min(time), max(time));
fprintf(fileID, '===================================\n\n');
fprintf(fileID, 'Time(s)\tSignal\n');
for i = 1:length(time)
    fprintf(fileID, '%.2f\t%.4f\n', time(i), signal(i));
end
fclose(fileID);
fprintf('Data saved to simulation_data.txt\n');


%% Exercise 4.2: Organized Results
% Create a script that:
% 1. Checks if folders `Results/Figures` and `Results/Data` exist, creates them if not
% 2. Generates a simple plot (any data)
% 3. Saves the figure to `Results/Figures/my_plot.png`
% 4. Saves the data used in the plot to `Results/Data/plot_data.mat`
% 5. Uses `fullfile` for all paths

% SAVE_ORGANIZED_RESULTS - Save results to organized folder structure
%
% Author: Your Name
% Date: November 6, 2025
%
% Description:
%   Creates organized folder structure and saves figures and data
%   to appropriate locations using fullfile for cross-platform compatibility.

% Check and create folder structure
if ~isfolder('Results')
    mkdir('Results');
end

figuresPath = fullfile('Results', 'Figures');
if ~isfolder(figuresPath)
    mkdir(figuresPath);
end

dataPath = fullfile('Results', 'Data');
if ~isfolder(dataPath)
    mkdir(dataPath);
end

fprintf('Folder structure created.\n');

% Generate sample data
x = linspace(0, 2*pi, 100);
y = sin(x);

% Create a plot
figure;
plot(x, y, 'b-', 'LineWidth', 2);
xlabel('x');
ylabel('sin(x)');
title('Sine Wave');
grid on;

% Save figure using fullfile
figurePath = fullfile(figuresPath, 'my_plot.png');
saveas(gcf, figurePath);
fprintf('Figure saved to %s\n', figurePath);

% Save data using fullfile
dataFile = fullfile(dataPath, 'plot_data.mat');
save(dataFile, 'x', 'y');
fprintf('Data saved to %s\n', dataFile);

%% Part 5: File I/O with Text Files

%% Exercise 5.1: Reading Line by Line
%Create a text file `measurements.txt` with numbers (one per line):
%
% 23.5
% 27.8
% 25.1
% 26.3
% 24.9
%
% Write a script using `fopen`, `fgetl`, and `fclose` that:
% 1. Reads each line from the file
% 2. Converts each line to a number
% 3. Stores all numbers in an array
% 4. Calculates and displays the mean and standard deviation

% READ_MEASUREMENTS - Read measurements from text file line by line
%
% Author: Your Name
% Date: November 6, 2025
%
% Description:
%   Reads numerical data from text file using fopen/fgetl,
%   converts to numbers, and calculates statistics.
%
% Inputs: measurements.txt
% Outputs: Mean and standard deviation printed to console

% Open file for reading
fileID = fopen('measurements.txt', 'r');

% Check if file opened successfully
if fileID == -1
    error('Could not open measurements.txt');
end

% Initialize array to store measurements
data = [];

% Read file line by line
while ~feof(fileID)
    line = fgetl(fileID);

    % Convert string to number and add to array
    if ischar(line)  % Check that we got a valid line
        value = str2double(line);
        if ~isnan(value)  % Make sure conversion succeeded
            data = [data; value];
        end
    end
end

% Close the file
fclose(fileID);

% Calculate statistics
meanValue = mean(data);
stdValue = std(data);

% Display results
fprintf('Number of measurements: %d\n', length(data));
fprintf('Mean: %.2f\n', meanValue);
fprintf('Standard Deviation: %.2f\n', stdValue);


%% Exercise 5.2: Custom Report Generation
% Write a script that generates a formatted report file `lab_report.txt` containing:
% 1. A title header with equal signs above and below
% 2. Your name and date
% 3. Three calculated statistics (mean, max, min) from any dataset
% 4. Each statistic formatted to 2 decimal places with descriptive labels
% 5. A closing line
%
% **Example output format:**
%
% ===========================
% Laboratory Analysis Report
% ===========================
% Author: Your Name
% Date: November 6, 2025
%
% Results:
% Mean Value: 45.67
% Maximum Value: 89.12
% Minimum Value: 12.34
%
% Analysis Complete.
% ===========================
%

% GENERATE_LAB_REPORT - Create formatted laboratory report
%
% Author: Your Name
% Date: November 6, 2025
%
% Description:
%   Generates a formatted text report with statistical analysis
%   of sample data.

% Generate sample dataset
data = [45.2, 67.8, 23.4, 89.1, 56.3, 34.7, 78.9, 12.5];

% Calculate statistics
meanVal = mean(data);
maxVal = max(data);
minVal = min(data);

% Open file for writing
fileID = fopen('lab_report.txt', 'w');

% Write formatted report
fprintf(fileID, '===========================\n');
fprintf(fileID, 'Laboratory Analysis Report\n');
fprintf(fileID, '===========================\n');
fprintf(fileID, 'Author: Your Name\n');
fprintf(fileID, 'Date: %s\n', datestr(now, 'mmmm dd, yyyy'));
fprintf(fileID, '\n');
fprintf(fileID, 'Results:\n');
fprintf(fileID, 'Mean Value: %.2f\n', meanVal);
fprintf(fileID, 'Maximum Value: %.2f\n', maxVal);
fprintf(fileID, 'Minimum Value: %.2f\n', minVal);
fprintf(fileID, '\n');
fprintf(fileID, 'Analysis Complete.\n');
fprintf(fileID, '===========================\n');

% Close file
fclose(fileID);

fprintf('Report generated: lab_report.txt\n');

%% Part 6: Integration Challenge

%% Exercise 6.1: Complete Data Pipeline
%
% Create a complete data analysis pipeline that:
%
% 1. **Setup**: Creates a project structure with folders: `Data/Raw`, `Data/Processed`, `Results`
%
% 2. **Data Generation**: Creates sample data (temperatures over 24 hours) and saves it as `Data/Raw/temperature_log.csv`
%
% 3. **Processing**:
%    - Reads the raw data
%    - Calculates hourly averages
%    - Identifies temperatures above a threshold (e.g., 75°F)
%    - Saves processed data to `Data/Processed/temp_summary.mat`
%
% 4. **Visualization**:
%    - Creates a plot of temperature over time
%    - Saves figure to `Results/temperature_plot.png`
%
% 5. **Reporting**:
%    - Generates a text report in `Results/analysis_report.txt` with:
%      - Number of readings
%      - Average, max, and min temperatures
%      - Number of readings above threshold
%      - Timestamp of when analysis was run
%
% **Requirements**:
% - Use `fullfile` for all paths
% - Include proper error checking (`isfile`, `isfolder`)
% - Add comprehensive documentation
% - Use appropriate file formats for each type of data

% TEMPERATURE_ANALYSIS_PIPELINE - Complete data analysis pipeline
%
% Author: Your Name
% Date: November 6, 2025
%
% Description:
%   Complete pipeline that creates project structure, generates data,
%   processes it, creates visualizations, and generates a report.
%
% Inputs: None (generates own data)
% Outputs: Processed data, figure, and text report in organized folders

% SETUP: Create project structure
fprintf('Setting up project structure...\n');

% Create main folders
folders = {
    'Data',
    fullfile('Data', 'Raw'),
    fullfile('Data', 'Processed'),
    'Results'
};

for i = 1:length(folders)
    if ~isfolder(folders{i})
        mkdir(folders{i});
    end
end

fprintf('Project structure created.\n\n');

% DATA GENERATION: Create and save sample temperature data
fprintf('Generating temperature data...\n');

% Generate 24 hours of temperature data (one reading per hour)
hours = 0:23;
% Simulate daily temperature cycle with some noise
temperatures = 65 + 15*sin((hours - 6)*pi/12) + 3*randn(size(hours));

% Save raw data to CSV
rawDataFile = fullfile('Data', 'Raw', 'temperature_log.csv');
dataTable = table(hours', temperatures', 'VariableNames', {'Hour', 'Temperature'});
writetable(dataTable, rawDataFile);

fprintf('Raw data saved to %s\n\n', rawDataFile);

% PROCESSING: Analyze the data
fprintf('Processing temperature data...\n');

% Set threshold temperature
threshold = 75;

% Calculate statistics
avgTemp = mean(temperatures);
maxTemp = max(temperatures);
minTemp = min(temperatures);

% Find readings above threshold
aboveThreshold = temperatures > threshold;
numAbove = sum(aboveThreshold);
hoursAbove = hours(aboveThreshold);

% Create summary structure
summary.averageTemp = avgTemp;
summary.maxTemp = maxTemp;
summary.minTemp = minTemp;
summary.threshold = threshold;
summary.numAboveThreshold = numAbove;
summary.hoursAboveThreshold = hoursAbove;
summary.totalReadings = length(temperatures);

% Save processed data
processedFile = fullfile('Data', 'Processed', 'temp_summary.mat');
save(processedFile, 'summary', 'hours', 'temperatures');

fprintf('Processed data saved to %s\n\n', processedFile);

% VISUALIZATION: Create and save plot
fprintf('Creating visualization...\n');

figure('Name', 'Temperature Analysis');
plot(hours, temperatures, 'b-o', 'LineWidth', 2, 'MarkerSize', 6);
hold on;
yline(threshold, 'r--', 'LineWidth', 2, 'Label', sprintf('Threshold (%.0f°F)', threshold));
hold off;

xlabel('Hour of Day');
ylabel('Temperature (°F)');
title('24-Hour Temperature Log');
grid on;
xlim([0 23]);

% Save figure
figurePath = fullfile('Results', 'temperature_plot.png');
saveas(gcf, figurePath);

fprintf('Figure saved to %s\n\n', figurePath);

% REPORTING: Generate text report
fprintf('Generating analysis report...\n');

reportPath = fullfile('Results', 'analysis_report.txt');
fileID = fopen(reportPath, 'w');

fprintf(fileID, '========================================\n');
fprintf(fileID, '  TEMPERATURE ANALYSIS REPORT\n');
fprintf(fileID, '========================================\n\n');

fprintf(fileID, 'Analysis Date: %s\n', datestr(now));
fprintf(fileID, 'Data Source: %s\n\n', rawDataFile);

fprintf(fileID, 'SUMMARY STATISTICS\n');
fprintf(fileID, '----------------------------------------\n');
fprintf(fileID, 'Total Readings: %d\n', summary.totalReadings);
fprintf(fileID, 'Average Temperature: %.2f°F\n', avgTemp);
fprintf(fileID, 'Maximum Temperature: %.2f°F\n', maxTemp);
fprintf(fileID, 'Minimum Temperature: %.2f°F\n', minTemp);
fprintf(fileID, 'Temperature Range: %.2f°F\n\n', maxTemp - minTemp);

fprintf(fileID, 'THRESHOLD ANALYSIS\n');
fprintf(fileID, '----------------------------------------\n');
fprintf(fileID, 'Threshold Value: %.2f°F\n', threshold);
fprintf(fileID, 'Readings Above Threshold: %d\n', numAbove);
fprintf(fileID, 'Percentage Above Threshold: %.1f%%\n', (numAbove/length(temperatures))*100);

if numAbove > 0
    fprintf(fileID, '\nHours Above Threshold:\n');
    for i = 1:length(hoursAbove)
        fprintf(fileID, '  Hour %d: %.2f°F\n', hoursAbove(i), temperatures(hours == hoursAbove(i)));
    end
end

fprintf(fileID, '\n========================================\n');
fprintf(fileID, 'Analysis Complete\n');
fprintf(fileID, '========================================\n');

fclose(fileID);

fprintf('Report saved to %s\n\n', reportPath);

% COMPLETION MESSAGE
fprintf('========================================\n');
fprintf('PIPELINE COMPLETE\n');
fprintf('========================================\n');
fprintf('All files have been generated:\n');
fprintf('  - Raw data: %s\n', rawDataFile);
fprintf('  - Processed data: %s\n', processedFile);
fprintf('  - Figure: %s\n', figurePath);
fprintf('  - Report: %s\n', reportPath);


%% Tips for Success
%
% 1. Test incrementally: Run your script after adding each feature
% 2. Use pwd and dir: Check your location and available files frequently
% 3. Close files: Always use fclose after fopen
% 4. Check existence: Use isfile and isfolder before operations
% 5. Clear workspace: Use clear and clc at the start of scripts during testing
