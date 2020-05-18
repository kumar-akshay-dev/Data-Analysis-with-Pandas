# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:23:50 2020

@author: Kumar
Statistics
"""

import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)
print (df)

#sum():Returns the sum of the values for the requested axis. By default, axis is index (axis=0).
print (df.sum(1))

#mean():returns average value
print (df.mean())

#Summarizing Data:describe
print (df.describe())

