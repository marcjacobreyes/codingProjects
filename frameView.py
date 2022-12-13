# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:51:21 2022

@author: marcjacobreyes
Demonstrating a VIEW **IS NOT** separate from its underlying DataFrame

"""
import pandas as pd

smallFrame = pd.DataFrame( [ ["Tuesday", 3.54, 12],
               ["Wednesday", 4.55, 13],
               ["Thursday", 5.56, 14] ] )

# Lets create a view of one row...
frameView = smallFrame[1]
print(frameView)

# Let's make a CHANGE using the VIEW....
frameView[1] = 555.55

# What Happened? 
print(smallFrame)

 







