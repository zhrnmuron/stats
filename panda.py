import pandas as pd
import matplotlib.pyplot as plt

filepath = "/home/binku/Documents/Dataset 1 (Activity 3) - Dataset1.csv"
df = pd.read_csv(filepath)

X1 = df['CurrentRatio']
X2 = df['QuickRatio']
X3 = df['CashRatio']

# Scatterplots
plt.scatter(X1, X2)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('X1 vs X2')
plt.show()

# Covariance
covariance_X1_X2 = X1.cov(X2)
print(f"Covariance(X1, X2): {covariance_X1_X2}")

# Mean and Standard Deviation
mean_X1 = X1.mean()
std_X1 = X1.std()
print(f"Mean(X1): {mean_X1}, Std Dev(X1): {std_X1}")

# Chebyshev's Inequality
k = 2
lower_bound_X1 = mean_X1 - k * std_X1
upper_bound_X1 = mean_X1 + k * std_X1
print(f"Chebyshev's bounds for X1: ({lower_bound_X1}, {upper_bound_X1})")
