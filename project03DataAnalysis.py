# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:18:17 2022

@author: marcjacobreyes

Data Analysis for Project 03 using pandas
"""

import pandas as pd

classDataFrame = pd.read_csv('ISCS_Scheds_5YR.csv')

print(classDataFrame.columns)
print()

print(classDataFrame['Instructor'].mode())
print()

print(type(classDataFrame))
print()

print(classDataFrame['Instructor'].value_counts())
print(classDataFrame['Wait List'].value_counts())
print()

print(classDataFrame.isnull().sum())

print("\n NULL PERCENTAGES:")
for column in classDataFrame.columns:
    if classDataFrame[column].isnull().sum() > 0:
        print(column, ': {:.2%}'.format(classDataFrame[column].isnull().sum() / classDataFrame[column].shape[0]))
# end for loop

print()
print(classDataFrame['Title'].value_counts())

print()
print(classDataFrame.info())

print(classDataFrame.to_numpy())

viewOfComments = classDataFrame['Comments']
print(viewOfComments)
print(classDataFrame['Comments'].value_counts())

print(classDataFrame['Status'].value_counts())



