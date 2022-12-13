# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:43:23 2022

@author: marcjacobreyes
Lets start by slicing the columns 

"""
import pandas as pd 

# Declare a Dataframe object and "load" it from our crime data set 
dataFrame = pd.read_csv('Crime_Reports.csv') 
# \t \n 

# We can verify our load 
print(type(dataFrame))
print(dataFrame.shape)
print(dataFrame)

# We can output a SINGLE COLUMN of the frame
print(dataFrame.columns)
print() 
print(dataFrame.loc[:,'Highest Offense Code'])



