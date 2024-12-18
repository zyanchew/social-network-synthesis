#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:03:25 2024

@author: zyanchew
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
aaa = pd.read_csv('/Users/zyanchew/Desktop/social-network-synthesis/data/model2.csv')


# Set plot style
sns.set(style="whitegrid")

# Function to save plots
def save_plot(title, filename):
    plt.title(title)
    plt.tight_layout()
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig(f'/Users/zyanchew/Desktop/social-network-synthesis/results/figures/{filename}.png', bbox_inches='tight')
    plt.close()

# 1. Distribution of gender difference according to social categories
des_diff = pd.DataFrame(aaa.groupby('Socialcategory')['Gender_diff'].value_counts(normalize=True))
des_diff = des_diff.rename(columns={'proportion': 'proportion'}).reset_index()
a1 = sns.barplot(x='Gender_diff', y='proportion',
                 data=des_diff.assign(socialcategory=des_diff['Socialcategory'].map({1: 'friends', 2: 'colleagues', 3: 'neighbors',
                                                                                     4: 'grandparents', 5: 'parents', 6: 'siblings',
                                                                                     7: 'children', 8: 'relatives'})),
                 hue='Socialcategory', palette="Paired")
plt.xlabel('Gender Difference')
plt.xticks([0, 1], ['Same', 'Different'])
save_plot('Distribution of gender difference according to social categories', 'gender_difference_social_categories')

# 2. Distribution of age difference according to social categories
des_diff = pd.DataFrame(aaa.groupby('Socialcategory')['Age_diff'].value_counts(normalize=True))
des_diff = des_diff.rename(columns={'proportion': 'proportion'}).reset_index()
a1 = sns.barplot(x='Age_diff', y='proportion',
                 data=des_diff.assign(socialcategory=des_diff['Socialcategory'].map({1: 'friends', 2: 'colleagues', 3: 'neighbors',
                                                                                     4: 'grandparents', 5: 'parents', 6: 'siblings',
                                                                                     7: 'children', 8: 'relatives'})),
                 hue='Socialcategory', palette="Paired")
plt.xlabel('Age Difference')
save_plot('Distribution of age difference according to social categories', 'age_difference_social_categories')

# 3. Distribution of education difference according to social categories
des_diff = pd.DataFrame(aaa.groupby('Socialcategory')['Edu_diff'].value_counts(normalize=True))
des_diff = des_diff.rename(columns={'proportion': 'proportion'}).reset_index()
a1 = sns.barplot(x='Edu_diff', y='proportion',
                 data=des_diff.assign(socialcategory=des_diff['Socialcategory'].map({1: 'friends', 2: 'colleagues', 3: 'neighbors',
                                                                                     4: 'grandparents', 5: 'parents', 6: 'siblings',
                                                                                     7: 'children', 8: 'relatives'})),
                 hue='Socialcategory', palette="Paired")
plt.xlabel('Education Difference')
plt.xticks([0, 1, 2], ['Lower', 'Same', 'Higher'])
save_plot('Distribution of education difference according to social categories', 'education_difference_social_categories')

# 4. Distribution of relationship duration according to social categories
des_diff = pd.DataFrame(aaa.groupby('Socialcategory')['Duration'].value_counts(normalize=True))
des_diff = des_diff.rename(columns={'proportion': 'proportion'}).reset_index()
a1 = sns.barplot(x='Duration', y='proportion',
                 data=des_diff.assign(socialcategory=des_diff['Socialcategory'].map({1: 'friends', 2: 'colleagues', 3: 'neighbors',
                                                                                     4: 'grandparents', 5: 'parents', 6: 'siblings',
                                                                                     7: 'children', 8: 'relatives'})),
                 hue='Socialcategory', palette="Paired")
plt.xlabel('Relationship Duration')
plt.xticks([0, 1, 2], ['<5 years', '5-15 years', '>15 years'])
save_plot('Distribution of relationship duration according to social categories', 'relationship_duration_social_categories')

# 5. Distribution of distance according to social categories
des_diff = pd.DataFrame(aaa.groupby('Socialcategory')['Distance'].value_counts(normalize=True))
des_diff = des_diff.rename(columns={'proportion': 'proportion'}).reset_index()
a1 = sns.barplot(x='Distance', y='proportion',
                 data=des_diff.assign(socialcategory=des_diff['Socialcategory'].map({1: 'friends', 2: 'colleagues', 3: 'neighbors',
                                                                                     4: 'grandparents', 5: 'parents', 6: 'siblings',
                                                                                     7: 'children', 8: 'relatives'})),
                 hue='Socialcategory', palette="Paired")
plt.xlabel('Distance')
plt.xticks([0, 1, 2, 3, 4], ['<1km', '1-10km', '10-50km', '>50km', 'Abroad'])
save_plot('Distribution of distance according to social categories', 'distance_social_categories')

print("All plots have been saved successfully.")




















