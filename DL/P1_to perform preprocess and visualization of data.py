# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/content/iris.csv'
data = pd.read_csv(file_path)
line = "--------"

# Display the shape of the dataset
print("Dataset Shape (rows, columns):", data.shape)
print(line)

# Display data types of each column
print("\nData Types of Each Column:")
print(data.dtypes)
print(line)

# Check for null values in the dataset
print("\nNull Values in Each Column:")
print(data.isnull().sum())
print(line)

# Drop duplicate rows (if any)
data_cleaned = data.drop_duplicates()

# Verify duplicates have been removed
print("\nShape after removing duplicates (rows, columns):", data_cleaned.shape)
print(line)

# Visualizations
# Bar plot for species distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=data_cleaned, x='variety', hue='variety', palette='coolwarm')
plt.title('Distribution of Variety')
plt.xlabel('Variety')
plt.ylabel('Count')
plt.show()

# Scatter plot for SepalLengthCm vs SepalWidthCm
plt.figure(figsize=(8, 5))
sns.scatterplot(data=data_cleaned, x='sepal.length', y='sepal.width', hue='variety', palette='coolwarm')
plt.title('Scatter Plot of Sepal Dimensions')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(title='Variety')
plt.show()

# Line plot for SepalLengthCm and SepalWidthCm
plt.figure(figsize=(8, 5))
sns.lineplot(data=data_cleaned[['sepal.length', 'sepal.width']], palette='coolwarm')
plt.title('Line Plot of Sepal Dimensions')
plt.xlabel('Index')
plt.ylabel('Length/Width (cm)')
plt.show()