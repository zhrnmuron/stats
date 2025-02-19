import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
file_path = '/home/binku/Documents/Dataset 1 (Activity 3) - Dataset1.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Step 2: Extract the first three columns
col1 = data.columns[0]
col2 = data.columns[1]
col3 = data.columns[2]

# Step 3: Generate scatter plots
plt.figure(figsize=(15, 5))

# Scatter plot for Column 1 vs Column 2
plt.subplot(1, 3, 1)
plt.scatter(data[col1], data[col2], color='blue', alpha=0.7)
plt.title(f'{col1} vs {col2}')
plt.xlabel(col1)
plt.ylabel(col2)

# Scatter plot for Column 1 vs Column 3
plt.subplot(1, 3, 2)
plt.scatter(data[col1], data[col3], color='green', alpha=0.7)
plt.title(f'{col1} vs {col3}')
plt.xlabel(col1)
plt.ylabel(col3)

# Scatter plot for Column 2 vs Column 3
plt.subplot(1, 3, 3)
plt.scatter(data[col2], data[col3], color='red', alpha=0.7)
plt.title(f'{col2} vs {col3}')
plt.xlabel(col2)
plt.ylabel(col3)

# Show the plots
plt.tight_layout()
plt.savefig('example_plot.png', dpi=300)
plt.show()
