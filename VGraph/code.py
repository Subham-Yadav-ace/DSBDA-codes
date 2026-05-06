import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load datasets
air = pd.read_csv("air.csv", encoding='latin1')
heart = pd.read_csv("heart.csv")

# Set graph style
sns.set(style="whitegrid")

# Show first 5 rows
air.head()
heart.head()

# -----------------------------
# 1. Line Plot (SO2 Trend)
# -----------------------------
plt.figure(figsize=(10,6))
plt.plot(air['so2'][::2500], marker='o')
plt.title("SO2 Trend")
plt.xlabel("Index")
plt.ylabel("SO2")
plt.show()

# -----------------------------
# 2. Count Plot (Heart Disease Count)
# -----------------------------
sns.countplot(x='output', data=heart)
plt.title("Heart Disease Count")
plt.show()

# -----------------------------
# 3. Histogram (Age Distribution)
# -----------------------------
plt.hist(heart['age'], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 4. Heatmap (Correlation Matrix)
# -----------------------------
cols = ['age', 'chol', 'thalachh', 'output']

corr = heart[cols].corr()

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")
plt.show()