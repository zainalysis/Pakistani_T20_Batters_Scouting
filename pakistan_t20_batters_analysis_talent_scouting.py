# -*- coding: utf-8 -*-
"""pakistan_t20_batters_analysis_talent_scouting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12a0V9df3IrGOWCYUbO9Zq8Es8hIcoKcW
"""

from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

import pandas as pd

file_path = '/content/drive/My Drive/t20_bbb.csv'
df = pd.read_csv(file_path)

df.head()

import pandas as pd

# Filter rows where the country is Pakistan
pakistan_df = df[df['country'] == 'Pakistan']

# Function to calculate average length of consecutive 0 or 1 patterns
def calculate_average_pattern_length(batruns):
    lengths = []  # List to store lengths of consecutive patterns
    current_pattern = []  # Track the current pattern of 0s or 1s

    for value in batruns:
        if value in [0, 1]:  # Continue the pattern
            current_pattern.append(value)
        else:  # Pattern breaks
            if current_pattern:  # Only process if there's a valid pattern
                lengths.append(len(current_pattern))
            current_pattern = []  # Reset the pattern

    if current_pattern:  # Handle remaining pattern at the end
        lengths.append(len(current_pattern))

    return sum(lengths) / len(lengths) if lengths else 0

# Group by 'bat' and calculate the average pattern length for each batter
results = {}
for bat, group in pakistan_df.groupby('bat'):
    average_length = calculate_average_pattern_length(group['batruns'].tolist())
    results[bat] = average_length

# Convert results to a DataFrame for better readability
results_df = pd.DataFrame(list(results.items()), columns=['Batter', 'Average_Consecutive_Pattern_Length'])

# Display the results
print(results_df)

# Optionally save to a CSV file
results_df.to_csv('/content/average_pattern_lengths_pakistan.csv', index=False)

# Set pandas display options to show maximum rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Convert results to a DataFrame for better readability
results_df = pd.DataFrame(list(results.items()), columns=['Batter', 'Average_Consecutive_Pattern_Length'])

# Display the results
print(results_df)

import pandas as pd



# Filter rows where the country is Pakistan
pakistan_df = df[df['country'] == 'Pakistan']

# Filter batters with at least 50 unique p_match entries
batters_with_50_matches = (
    pakistan_df.groupby('bat')['p_match']
    .nunique()
    .reset_index()
    .rename(columns={'p_match': 'unique_matches'})
)
batters_with_50_matches = batters_with_50_matches[batters_with_50_matches['unique_matches'] >= 20]
qualified_batters = batters_with_50_matches['bat'].tolist()

# Function to calculate average length of consecutive 0 or 1 patterns
def calculate_average_pattern_length(batruns):
    lengths = []  # List to store lengths of consecutive patterns
    current_pattern = []  # Track the current pattern of 0s or 1s

    for value in batruns:
        if value in [0, 1]:  # Continue the pattern
            current_pattern.append(value)
        else:  # Pattern breaks
            if current_pattern:  # Only process if there's a valid pattern
                lengths.append(len(current_pattern))
            current_pattern = []  # Reset the pattern

    if current_pattern:  # Handle remaining pattern at the end
        lengths.append(len(current_pattern))

    return sum(lengths) / len(lengths) if lengths else 0

# Group by 'bat' and calculate the average pattern length for qualified batters
results = {}
for bat, group in pakistan_df.groupby('bat'):
    if bat in qualified_batters:  # Consider only qualified batters
        average_length = calculate_average_pattern_length(group['batruns'].tolist())
        results[bat] = average_length

# Convert results to a DataFrame for better readability
results_df = pd.DataFrame(list(results.items()), columns=['Batter', 'Average_Consecutive_Pattern_Length'])

# Set pandas display options to show maximum rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# Display the results
print(results_df)

# Optionally save to a CSV file
results_df.to_csv('/content/average_pattern_lengths_pakistan_qualified.csv', index=False)

import pandas as pd


# Filter rows where the country is Pakistan
pakistan_df = df[df['country'] == 'Pakistan']

# Qualified batters from the previous step
qualified_batters = [
    "Aamer Yamin", "Abdullah Shafique", "Adil Amin", "Agha Salman",
    "Ahmed Shehzad", "Ahsan Ali", "Akbar-ur-Rehman", "Alex Hales",
    "Amad Butt", "Anwar Ali", "Asad Shafiq", "Asif Ali", "Awais Zia",
    "Azam Khan", "Babar Azam", "Ben Cutting", "Bilal Asif", "Bismillah Khan",
    "Colin Munro", "Danish Aziz", "David Wiese", "Faheem Ashraf",
    "Fakhar Zaman", "Haider Ali", "Hammad Azam", "Haris Sohail",
    "Hasan Ali", "Hussain Talat", "Iftikhar Ahmed", "Imad Wasim",
    "Imam-ul-Haq", "Irfan Khan", "Israrullah", "James Vince", "Jason Roy",
    "Kamran Akmal", "Kamran Ghulam", "Khurram Manzoor", "Khushdil Shah",
    "Kieron Pollard", "Mohammad Amir", "Mohammad Hafeez", "Mohammad Haris",
    "Mohammad Nawaz", "Mohammad Rizwan", "Mohammad Wasim", "Muhammad Akhlaq",
    "Mukhtar Ahmed", "Musadiq Ahmed", "Naseem Shah", "Nauman Anwar",
    "Phil Salt", "Qasim Akram", "Rafatullah Mohmand", "Rilee Rossouw",
    "Rohail Nazir", "Rovman Powell", "Rumman Raees", "Saad Nasim",
    "Sahibzada Farhan", "Saim Ayub", "Sarfaraz Ahmed", "Saud Shakeel",
    "Shadab Khan", "Shaheen Shah Afridi", "Shan Masood", "Sharjeel Khan",
    "Sherfane Rutherford", "Shoaib Malik", "Sikandar Raza", "Sohaib Maqsood",
    "Sohail Akhtar", "Sohail Khan", "Sohail Tanvir", "Tom Kohler-Cadmore",
    "Umaid Asif", "Umar Akmal", "Umar Amin", "Wahab Riaz", "Zain Abbas",
    "Zeeshan Ashraf"
]

# Function to calculate the average balls between boundaries (4 or 6)
def calculate_avg_balls_between_boundaries(batruns):
    boundary_indices = [i for i, value in enumerate(batruns) if value in [4, 6]]
    intervals = [boundary_indices[i] - boundary_indices[i - 1] for i in range(1, len(boundary_indices))]
    return sum(intervals) / len(intervals) if intervals else 0

# Group by 'bat' and calculate the average balls between boundaries for qualified batters
results = {}
for bat, group in pakistan_df.groupby('bat'):
    if bat in qualified_batters:  # Consider only qualified batters
        average_balls = calculate_avg_balls_between_boundaries(group['batruns'].tolist())
        results[bat] = average_balls

# Convert results to a DataFrame for better readability
results_df = pd.DataFrame(list(results.items()), columns=['Batter', 'Average_Balls_Between_Boundaries'])

# Sort by average balls in ascending order
results_df = results_df.sort_values(by='Average_Balls_Between_Boundaries')

# Display the results
print(results_df)

# Optionally save to a CSV file
results_df.to_csv('/content/average_balls_between_boundaries_pakistan.csv', index=False)

import pandas as pd
import plotly.express as px

# Load the datasets
# Average pattern lengths
pattern_lengths_file = '/content/average_pattern_lengths_pakistan_qualified.csv'
pattern_lengths_df = pd.read_csv(pattern_lengths_file)

# Average balls between boundaries
boundaries_file = '/content/average_balls_between_boundaries_pakistan.csv'
boundaries_df = pd.read_csv(boundaries_file)

# Merge the two datasets on 'Batter'
merged_df = pd.merge(
    pattern_lengths_df,
    boundaries_df,
    on='Batter',
    how='inner'
)

# Create a scatter plot
fig = px.scatter(
    merged_df,
    x='Average_Consecutive_Pattern_Length',
    y='Average_Balls_Between_Boundaries',
    text='Batter',
    title='Scatter Plot: Batting Patterns vs Balls Between Boundaries',
    labels={
        'Average_Consecutive_Pattern_Length': 'Average Consecutive 0 or 1 Pattern Length',
        'Average_Balls_Between_Boundaries': 'Average Balls Between Boundaries'
    },
    hover_name='Batter',
)

# Add batter names as text on the scatter plot
fig.update_traces(textposition='top center')

# Customize layout for better visuals
fig.update_layout(
    xaxis_title='Average Consecutive 0 or 1 Pattern Length',
    yaxis_title='Average Balls Between Boundaries',
    title_font_size=20,
    title_x=0.5,  # Center the title
    template='plotly'  # Use a dark theme for better contrast
)

# Show the plot
fig.show()

import pandas as pd
import plotly.express as px

# Load the datasets
pattern_lengths_file = '/content/average_pattern_lengths_pakistan_qualified.csv'
pattern_lengths_df = pd.read_csv(pattern_lengths_file)

boundaries_file = '/content/average_balls_between_boundaries_pakistan.csv'
boundaries_df = pd.read_csv(boundaries_file)

# Merge the datasets
merged_df = pd.merge(
    pattern_lengths_df,
    boundaries_df,
    on='Batter',
    how='inner'
)

# Define color categories based on conditions
def categorize_color(row):
    if row['Average_Consecutive_Pattern_Length'] < 4.6 and row['Average_Balls_Between_Boundaries'] < 5.51:
        return 'blue'
    elif row['Average_Consecutive_Pattern_Length'] < 5 and row['Average_Balls_Between_Boundaries'] < 6:
        return 'green'
    else:
        return 'red'

# Apply the categorization
merged_df['Color'] = merged_df.apply(categorize_color, axis=1)

# Plot the scatter plot
fig = px.scatter(
    merged_df,
    x='Average_Consecutive_Pattern_Length',
    y='Average_Balls_Between_Boundaries',
    color='Color',
    hover_data=['Batter'],
    title='Scatter Plot of Batting Patterns and Boundary Intervals',
    labels={
        'Average_Consecutive_Pattern_Length': 'Avg. Consecutive 0 or 1 Pattern Length',
        'Average_Balls_Between_Boundaries': 'Avg. Balls Between Boundaries'
    },
)

# Update layout for better appearance
fig.update_layout(
    template='plotly_white',
    legend_title_text='Color Category'
)

# Show the plot
fig.show()

import pandas as pd


# Filter rows where the country is Pakistan
pakistan_df = df[df['country'] == 'Pakistan']

# Qualified batters from the previous step
qualified_batters = [
    "Aamer Yamin", "Abdullah Shafique", "Adil Amin", "Agha Salman",
    "Ahmed Shehzad", "Ahsan Ali", "Akbar-ur-Rehman", "Alex Hales",
    "Amad Butt", "Anwar Ali", "Asad Shafiq", "Asif Ali", "Awais Zia",
    "Azam Khan", "Babar Azam", "Ben Cutting", "Bilal Asif", "Bismillah Khan",
    "Colin Munro", "Danish Aziz", "David Wiese", "Faheem Ashraf",
    "Fakhar Zaman", "Haider Ali", "Hammad Azam", "Haris Sohail",
    "Hasan Ali", "Hussain Talat", "Iftikhar Ahmed", "Imad Wasim",
    "Imam-ul-Haq", "Irfan Khan", "Israrullah", "James Vince", "Jason Roy",
    "Kamran Akmal", "Kamran Ghulam", "Khurram Manzoor", "Khushdil Shah",
    "Kieron Pollard", "Mohammad Amir", "Mohammad Hafeez", "Mohammad Haris",
    "Mohammad Nawaz", "Mohammad Rizwan", "Mohammad Wasim", "Muhammad Akhlaq",
    "Mukhtar Ahmed", "Musadiq Ahmed", "Naseem Shah", "Nauman Anwar",
    "Phil Salt", "Qasim Akram", "Rafatullah Mohmand", "Rilee Rossouw",
    "Rohail Nazir", "Rovman Powell", "Rumman Raees", "Saad Nasim",
    "Sahibzada Farhan", "Saim Ayub", "Sarfaraz Ahmed", "Saud Shakeel",
    "Shadab Khan", "Shaheen Shah Afridi", "Shan Masood", "Sharjeel Khan",
    "Sherfane Rutherford", "Shoaib Malik", "Sikandar Raza", "Sohaib Maqsood",
    "Sohail Akhtar", "Sohail Khan", "Sohail Tanvir", "Tom Kohler-Cadmore",
    "Umaid Asif", "Umar Akmal", "Umar Amin", "Wahab Riaz", "Zain Abbas",
    "Zeeshan Ashraf"
]

# Function to calculate the average balls between boundaries (4 or 6)
def calculate_avg_balls_between_boundaries(batruns):
    boundary_indices = [i for i, value in enumerate(batruns) if value in [4, 6]]
    intervals = [boundary_indices[i] - boundary_indices[i - 1] for i in range(1, len(boundary_indices))]
    return sum(intervals) / len(intervals) if intervals else 0

# Group by 'bat' and calculate the average balls between boundaries for qualified batters
results = {}
for bat, group in pakistan_df.groupby('bat'):
    if bat in qualified_batters:  # Consider only qualified batters
        average_balls = calculate_avg_balls_between_boundaries(group['batruns'].tolist())
        results[bat] = average_balls

# Convert results to a DataFrame for better readability
results_df = pd.DataFrame(list(results.items()), columns=['Batter', 'Average_Balls_Between_Boundaries'])

# Sort by average balls in ascending order
results_df = results_df.sort_values(by='Average_Balls_Between_Boundaries')

# Display the results
print(results_df)

# Optionally save to a CSV file
results_df.to_csv('/content/average_balls_between_boundaries_pakistan.csv', index=False)