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





%% Exercise 1.2: Comment Review 
% Given this poorly documented code, add:
% - A proper header block
% - Single-line comments explaining each step
% - A multi-line comment block explaining the purpose


data = [85, 92, 78, 88, 95, 72, 89];
avg = mean(data);
above = data(data > avg);
count = length(above);
fprintf('Count: %d\n', count);


%% Part 2: Working with Directories 

%% Exercise 2.1: Directory Navigation 
% Write commands to:
% 1. Display your current directory
% 2. Create a new folder called `MyProject`
% 3. Inside `MyProject`, create two subfolders: `Data` and `Results`
% 4. Check if a folder called `Backup` exists, and create it if it doesn't





%% Exercise 2.2: Cross-Platform Paths 

%Rewrite these paths using `fullfile` to make them cross-platform
%compatible:

% Original (Windows-specific)
path1 = 'Data\Raw\experiment1.csv';
path2 = 'Results\Figures\plot1.png';
path3 = '..\SharedData\reference.mat';

%Create a script that builds these paths correctly and tests if each file
%exists using `isfile`.



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



%%Part 4: Writing and Saving Data 
 
%%Exercise 4.1: Multiple File Formats 

%Generate simulation data and save it in three formats:

time = 0:0.1:10;
signal = sin(time) + 0.1*randn(size(time));

% Save this data as:
% 1. A `.mat` file with both variables
% 2. A `.csv` file with two columns (time, signal)
% 3. A `.txt` file with a formatted header describing the data




%% Exercise 4.2: Organized Results 
% Create a script that:
% 1. Checks if folders `Results/Figures` and `Results/Data` exist, creates them if not
% 2. Generates a simple plot (any data)
% 3. Saves the figure to `Results/Figures/my_plot.png`
% 4. Saves the data used in the plot to `Results/Data/plot_data.mat`
% 5. Uses `fullfile` for all paths



%% Part 5: File I/O with Text Files (10 minutes)

%% Exercise 5.1: Reading Line by Line (5 min)
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




%% Exercise 5.2: Custom Report Generation (5 min)
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




## Tips for Success

1. **Test incrementally**: Run your script after adding each feature
2. **Use `pwd` and `dir`**: Check your location and available files frequently
3. **Close files**: Always use `fclose` after `fopen`
4. **Check existence**: Use `isfile` and `isfolder` before operations
5. **Clear workspace**: Use `clear` and `clc` at the start of scripts during testing

