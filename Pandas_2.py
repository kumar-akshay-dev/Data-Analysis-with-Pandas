# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:07:57 2020

@author: Kumar

DataFrame Basic Functionality
"""
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data series is:\n" , df )

#T (Transpose):Returns the transpose of the DataFrame
print (df.T)

#axes-Returns the list of row axis labels and column axis labels.
print (df.axes)

#dtypes-Returns the data type of each column.
print (df.dtypes)

#empty-Returns the Boolean value saying whether the Object is empty or not
print (df.empty)

#ndim:Returns the number of dimensions of the object.
print (df.ndim)

#shape-Returns a tuple representing the dimensionality of the DataFrame.
print (df.shape)

#size:Returns the number of elements in the DataFrame.
print (df.size)

#values:Returns the actual data in the DataFrame as an NDarray.
print (df.values)

#Head & Tail:To view a small sample of a DataFrame object
df.head(2)
df.tail(2)



