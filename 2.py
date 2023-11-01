import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
df = pd.read_csv('D:\\test.csv', names = ['products'], sep = ',')

print(df.head())
print(df.shape)
data = list(df["products"].apply(lambda x:x.split(",") ))
print(data)
from mlxtend.preprocessing import TransactionEncoder
a = TransactionEncoder()
a_data = a.fit(data).transform(data)
df = pd.DataFrame(a_data,columns=a.columns_)
df = df.replace(False,0)
print(df)
df = apriori(df, min_support = 0.2, use_colnames = True, verbose = 1)
print(df)

df_ar = association_rules(df, metric = "confidence", min_threshold = 0.6)
print(df_ar[['antecedents','consequents','support', 'confidence']])

#   The code you provided is a Python script that applies the Apriori algorithm for association rule mining to a dataset of items or products. Here's a breakdown of the code and the algorithm used:

# Import necessary libraries:

# pandas for data manipulation.
# numpy for numerical operations.
# mlxtend.frequent_patterns for Apriori algorithm and association rule mining.
# mlxtend.preprocessing for TransactionEncoder.
# Read a CSV file named 'test.csv' into a Pandas DataFrame. The CSV file should have a single column named 'products'.

# Print the first few rows of the DataFrame and its shape to inspect the data.

# Split the 'products' column into lists of items using a comma as the separator and store the result in the data variable.

# Use mlxtend.preprocessing.TransactionEncoder to one-hot encode the list of itemsets, which will be used as input for the Apriori algorithm.

# Replace the boolean values (True/False) in the one-hot encoded DataFrame with 1s and 0s.

# Apply the Apriori algorithm using the mlxtend.frequent_patterns.apriori function. It calculates itemset support and returns frequent itemsets based on a minimum support threshold (min_support = 0.2 in this code). use_colnames is set to True to preserve item names in the result, and verbose is set to 1 for additional information during the process.

# Extract association rules from the frequent itemsets using the mlxtend.frequent_patterns.association_rules function. The code specifies that you want association rules with a minimum confidence of 0.6.

# Finally, it prints the 'antecedents', 'consequents', 'support', and 'confidence' columns of the resulting association rules DataFrame.

# In summary, this code applies the Apriori algorithm for finding frequent itemsets and association rules from transaction data, which is often used in market basket analysis and recommendation systems to discover patterns in customer purchase behavior.
