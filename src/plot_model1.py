#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 12:08:01 2024

@author: zyanchew
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
a = pd.read_csv('/Users/zyanchew/Desktop/social-network-synthesis/data/model1.csv')

# The size of social network by gender
plt.figure(figsize=(8, 5))
a1 = sns.boxplot(data=a, x='Gender', y='total_allgroups', showmeans=True,
                 meanprops={'marker': 'o', 'markerfacecolor': 'white', 'markeredgecolor': 'black', 'markersize': '3'},
                 showfliers=False, width=0.5, linewidth=0.8, palette="Blues")
a1.set(title='Boxplot: The size of social network by gender')
a1.set_xticklabels(['male', 'female'])
plt.ylabel('Social Network Size')
plt.xlabel('Gender')
plt.tight_layout()
plt.savefig('/Users/zyanchew/Desktop/social-network-synthesis/results/figures/social_network_by_gender.png')
plt.close()

# The size of social network by age
plt.figure(figsize=(8, 5))
a2 = sns.boxplot(data=a, x='Age', y='total_allgroups', showmeans=True,
                 meanprops={'marker': 'o', 'markerfacecolor': 'white', 'markeredgecolor': 'black', 'markersize': '3'},
                 showfliers=False, width=0.5, linewidth=0.8, palette="Blues")
a2.set(title='Boxplot: The size of social network by age')
a2.set_xticklabels(['18-35', '36-50', '51-65', '>66'])
plt.ylabel('Social Network Size')
plt.xlabel('Age')
plt.tight_layout()
plt.savefig('/Users/zyanchew/Desktop/social-network-synthesis/results/figures/social_network_by_age.png')
plt.close()

# The size of social network by household size
plt.figure(figsize=(8, 5))
a3 = sns.boxplot(data=a, x='Householdsize', y='total_allgroups', showmeans=True,
                 meanprops={'marker': 'o', 'markerfacecolor': 'white', 'markeredgecolor': 'black', 'markersize': '3'},
                 showfliers=False, width=0.5, linewidth=0.8, palette="Blues")
a3.set(title='Boxplot: The size of social network by household size')
a3.set_xticklabels(['1', '2', '>2'])
plt.ylabel('Social Network Size')
plt.xlabel('Household Size')
plt.tight_layout()
plt.savefig('/Users/zyanchew/Desktop/social-network-synthesis/results/figures/social_network_by_household.png')
plt.close()

# The size of social network by marital status
plt.figure(figsize=(10, 6))
a4 = sns.boxplot(data=a, x='MaritalStatus', y='total_allgroups', showmeans=True,
                 meanprops={'marker': 'o', 'markerfacecolor': 'white', 'markeredgecolor': 'black', 'markersize': '3'},
                 showfliers=False, width=0.5, linewidth=0.8, palette="Blues")
a4.set(title='Boxplot: The size of social network by marital status')
a4.set_xticklabels(['Single', 'Couple w/o children', 'Couple w/ children <12y/o', 'Couple w/ children >12y/o'])
plt.ylabel('Social Network Size')
plt.xlabel('Marital Status')
plt.xticks(rotation=10)
plt.tight_layout()
plt.savefig('/Users/zyanchew/Desktop/social-network-synthesis/results/figures/social_network_by_marital_status.png')
plt.close()

# The size of social network by education level
a['Education'] = a['Education'].replace(1, 2)
plt.figure(figsize=(8, 5))
a5 = sns.boxplot(data=a, x='Education', y='total_allgroups', showmeans=True,
                 meanprops={'marker': 'o', 'markerfacecolor': 'white', 'markeredgecolor': 'black', 'markersize': '3'},
                 showfliers=False, width=0.5, linewidth=0.8, palette="Blues")
a5.set(title='Boxplot: The size of social network by education level')
a5.set_xticklabels(['Low and Middle', 'High'])
plt.ylabel('Social Network Size')
plt.xlabel('Education Level')
plt.tight_layout()
plt.savefig('/Users/zyanchew/Desktop/social-network-synthesis/results/figures/social_network_by_education.png')
plt.close()

# The size of social network by working hours
plt.figure(figsize=(8, 5))
a6 = sns.boxplot(data=a, x='Paidwork', y='total_allgroups', showmeans=True,
                 meanprops={'marker': 'o', 'markerfacecolor': 'white', 'markeredgecolor': 'black', 'markersize': '3'},
                 showfliers=False, width=0.5, linewidth=0.8, palette="Blues")
a6.set(title='Boxplot: The size of social network by working hours')
plt.ylabel('Social Network Size')
plt.xlabel('Working Hours')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('/Users/zyanchew/Desktop/social-network-synthesis/results/figures/social_network_by_working_hours.png')
plt.close()

# The size of social network by income level
plt.figure(figsize=(10, 6))
a7 = sns.boxplot(data=a, x='Income', y='total_allgroups', showmeans=True,
                 meanprops={'marker': 'o', 'markerfacecolor': 'white', 'markeredgecolor': 'black', 'markersize': '3'},
                 showfliers=False, width=0.5, linewidth=0.8, palette="Blues")
a7.set(title='Boxplot: The size of social network by income level')
a7.set_xticklabels(['<625 euros', '625-1250 euros', '1251-1875 euros', '1876-2500 euros', '>2500 euros'])
plt.ylabel('Social Network Size')
plt.xlabel('Income Level')
plt.xticks(rotation=10)
plt.tight_layout()
plt.savefig('/Users/zyanchew/Desktop/social-network-synthesis/results/figures/social_network_by_income.png')
plt.close()

print("All boxplots saved successfully.")



