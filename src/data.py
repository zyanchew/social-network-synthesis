#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 13:58:02 2024

@author: zyanchew
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
file_path = '/Users/zyanchew/Desktop/social-network-synthesis/data/data.csv'  
df = pd.read_csv(file_path, dtype="category")

df.set_index('id', inplace=True)

# Display the first few rows of the dataset
print("Dataset Preview:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# General information about the dataset
print("\nDataset Information:")
print(df.info())

# Descriptive statistics for numerical variables
print("\nDescriptive Statistics (Numerical Variables):")
print(df.describe())

# Descriptive statistics for categorical variables
print("\nDescriptive Statistics (Categorical Variables):")
print(df.describe(include=['object', 'category']))

# Additional details for each categorical variable
print("\nCategory Counts:")
for col in df.select_dtypes(include=['object', 'category']).columns:
    print(f"\nValue Counts for {col}:")
    print(df[col].value_counts(normalize=True))

# Visualize distributions for numerical variables
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numerical_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True, color='blue')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.show()

# Visualize distributions for categorical variables
categorical_cols = df.select_dtypes(include=['object', 'category']).columns
for col in categorical_cols:
    plt.figure(figsize=(8, 4))
    sns.countplot(x=col, data=df, palette='viridis')
    plt.title(f'Count of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Correlation matrix for numerical variables
if len(numerical_cols) > 1:
    plt.figure(figsize=(10, 6))
    sns.heatmap(df[numerical_cols].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix for Numerical Variables')
    plt.show()
