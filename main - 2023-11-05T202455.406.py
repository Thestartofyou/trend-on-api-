import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your housing price dataset
# Replace 'your_data.csv' with the actual dataset file path
data = pd.read_csv('your_data.csv')

# Explore the dataset
print(data.head())  # Print the first few rows to understand the data structure

# Basic data exploration and visualization
# You can modify this part to suit your analysis needs

# Summary statistics
print(data.describe())

# Line plot to visualize price trends over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Price', data=data)
plt.title('Housing Price Trends Over Time')
plt.xlabel('Year')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# Box plot to visualize price distribution
plt.figure(figsize=(10, 6))
sns.boxplot(x='Location', y='Price', data=data)
plt.title('Housing Price Distribution by Location')
plt.xlabel('Location')
plt.ylabel('Price')
plt.xticks(rotation=90)
plt.show()

# Histogram of prices
plt.figure(figsize=(10, 6))
sns.histplot(data['Price'], bins=20, kde=True)
plt.title('Housing Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Correlation matrix and heatmap (if you have more features)
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
