#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 21:42:45 2024

@author: zyanchew
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
a = pd.read_csv('/Users/zyanchew/Desktop/social-network-synthesis/data/data.csv')

# Select relevant columns
ego = a[['id', 'id_contact', 'Gender_A', 'Age_A', 'Householdsize', 'MaritalStatus', 'Education_A','Paidwork', 'Income',
         'total_friends', 'total_colleagues', 'total_neighbors', 'total_grandparents', 'total_parents', 
         'total_siblings', 'total_children', 'total_relatives', 'total_allgroups',
         'visit', 'receive', 'dining', 'bar', 'cinema', 'recreation', 'vacation', 'shopping']]

# Remove duplicate relationships
ego = ego.drop_duplicates(subset=['id', 'id_contact'])  # 17,486 unique relationships

# Frequency columns transformation
freq = ego[['visit', 'receive', 'dining', 'bar', 'cinema', 'recreation', 'vacation', 'shopping']]
freq = freq.apply(pd.to_numeric, errors='coerce').fillna(0)

# Map ordinal frequency values to continuous scale (0–1)
frequency_map = {1: 365/365, 2: 144/365, 3: 48/365, 4: 36/365, 
                 5: 12/365, 6: 3/365, 7: 1/365, 8: 1/730}
freq = freq.replace(frequency_map)

# Update the frequency columns in the dataset
for col in freq.columns:
    ego[col] = freq[col]

# Split datasets for aggregation
aa = ego[['id', 'visit', 'receive', 'dining', 'bar', 'cinema', 'recreation', 'vacation', 'shopping']]
bb = ego[['id', 'Gender_A', 'Age_A', 'Householdsize', 'MaritalStatus', 'Education_A','Paidwork', 'Income',
          'total_friends', 'total_colleagues', 'total_neighbors', 'total_grandparents', 'total_parents', 
          'total_siblings', 'total_children', 'total_relatives', 'total_allgroups']]

# Aggregation at the individual level
sum_1 = aa.groupby('id').sum()  # Sum of activity frequencies
ego_1 = bb.groupby('id').mean()  # Average socio-demographic variables

print("Zero counts per column:")
print(sum_1.apply(lambda x: (x == 0).sum()))

# Descriptive statistics for joint activities
print("Descriptive Statistics for Joint Activity Frequencies:")
ds=sum_1.describe()
ds.to_csv('/Users/zyanchew/Desktop/social-network-synthesis/results/descriptive_agg_freq.csv')
# save descriptice statistic as a table

# Visualize boxplots for all frequency columns
plt.figure(figsize=(12, 6))
sns.boxplot(data=sum_1, showfliers=False)
plt.title("Boxplot of Joint Activity Frequencies (Without Outliers)")
plt.ylabel("Normalized Frequency (0–1)")
plt.xticks(rotation=90)
plt.show()


# Merge socio-demographic data with activity frequencies
ego_2 = ego_1.merge(sum_1, on='id')

# Categorize the frequency into 4 categories based on quartiles
def categorize_quartiles(column):
    """
    Categorize a column into quartiles dynamically adjusting labels.
    """
    num_bins = 4  # Desired number of bins
    try:
        # Use qcut with dynamic label creation
        return pd.qcut(column, q=num_bins, labels=range(1, num_bins+1), duplicates='drop')
    except ValueError:
        # Return NaN for columns that cannot be binned
        return pd.Series([None] * len(column), index=column.index)

# Apply quartile categorization to all frequency columns, each columns are categorize differently based on their quartiles
categorized_freq = sum_1.apply(categorize_quartiles)

# Save categorized frequencies to the merged dataset
for col in categorized_freq.columns:
    ego_2[f"{col}_category"] = categorized_freq[col]

# Preview the updated dataset with categories
print("\nDataset with Categorized Frequencies:")
print(ego_2.head())

# Visualize the category distribution for one column (e.g., 'visit_category')
plt.figure(figsize=(8, 5))
sns.countplot(x='visit_category', data=ego_2, palette='viridis', order=[1, 2, 3, 4])
plt.title('Distribution of Visit Frequency Categories')
plt.xlabel('Frequency Category')
plt.ylabel('Count')
plt.show()

# Save the cleaned and aggregated dataset
ego_2.to_csv('/Users/zyanchew/Desktop/social-network-synthesis/results/aggregated_data.csv', index=True)
print("\nAggregated dataset saved as 'aggregated_data.csv'.")




