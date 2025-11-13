
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV
df = pd.read_csv('students_marks.csv')

# Function to calculate grade based on marks
def calculator_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    else:
        return 'D'

# Calculate total marks and percentage
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Percentage'] = df['Total'] / 3
df['Grade'] = df['Percentage'].apply(calculator_grade)

# Print updated dataframe
print(df)

# Summary statistics
highest = df['Percentage'].max()
lowest = df['Percentage'].min()
average = df['Percentage'].mean()
topper = df.loc[df['Percentage'] == highest, 'Name'].values[0]
fail_count = df[df['Percentage'] < 60].shape[0]

# Print summary
print(f'Highest Percentage: {highest} ({topper})')
print(f'Lowest Percentage: {lowest}')
print(f'Average Percentage: {average:.2f}')
print(f'Number of Students Failed (<60%): {fail_count}')

# Export updated data
df.to_csv('students_report.csv', index=False)

# --- Visualization Section ---

# 1️⃣ Vertical Bar Chart
plt.figure(figsize=(5, 5))
plt.bar(df['Name'], df['Percentage'], color='skyblue', edgecolor='black')
plt.xlabel('Student')
plt.ylabel('Percentage')
plt.title('Student Performance')
plt.tight_layout()
plt.show()

# 2️⃣ Horizontal Bar Chart with color coding based on grade
colors = []
for p in df['Percentage']:
    if p >= 90:
        colors.append('green')
    elif p >= 80:
        colors.append('blue')
    elif p >= 70:
        colors.append('red')
    else:
        colors.append('purple')

plt.figure(figsize=(5, 5))
plt.barh(df['Name'], df['Percentage'], color=colors, edgecolor='black')
plt.xlabel('Percentage')
plt.ylabel('Student')
plt.title('Student Performance (Color-coded)')
plt.tight_layout()
plt.show()

# 3️⃣ Histogram for performance distribution
plt.figure(figsize=(5, 5))
plt.hist(df['Percentage'], bins=5, color='salmon', edgecolor='black')
plt.xlabel('Percentage')
plt.ylabel('Number of Students')
plt.title('Distribution of Student Performance')
plt.tight_layout()
plt.show()

# 4️⃣ Pie chart for grade distribution
plt.figure(figsize=(5, 5))
plt.pie(df['Grade'].value_counts(), labels=df['Grade'].value_counts().index, autopct='%1.1f%%')
plt.title('Grade Distribution')
plt.show()
