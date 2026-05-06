# Step 1: Import libraries
import pandas as pd
import numpy as np

# Step 2: Read dataset
df = pd.read_csv('fb.csv', delimiter=';')

# Step 3: View data
df.head()

# Step 4: Check shape (rows, columns)
df.shape

# Step 5: Check column names
df.columns

# Step 6: Statistical summary
df.describe()

# Step 7: Create subsets
subset_1 = df[['like','share','Type']]
subset_1

subset_2 = df[['comment','Type']]
subset_2

# Step 8: Merge data
merged_data = pd.merge(subset_1, subset_2, on='Type')
merged_data.head()

# Step 9: Sort data (descending order of likes)
merged_data = merged_data.sort_values(by=['like'], ascending=False)
merged_data.head()

# Step 10: Transpose data
transposed_data = merged_data.T
transposed_data

# Step 11: Shape of data
df.shape

# Step 12: Reshape using melt
melted_data = pd.melt(df, 
                      id_vars=['Type'], 
                      value_vars=['like','comment','share'])
melted_data

# Step 13: Pivot table
pivot_data = df.pivot_table(values='like', 
                            index='Type', 
                            aggfunc='mean')
pivot_data