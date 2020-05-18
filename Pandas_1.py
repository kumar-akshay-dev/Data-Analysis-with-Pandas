# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:38:08 2020

@author: KUMAR
pandas.DataFrame( data, index, columns, dtype, copy)
"""

#Create an Empty DataFrame
import pandas as pd
df = pd.DataFrame()
print (df)

#Create a DataFrame from Lists
df = pd.DataFrame([1,2,3,4,5])


data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)

df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print (df)

#Create a DataFrame from Dict of ndarrays / Lists
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)

#create an indexed DataFrame 
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print (df)

#NaN (Not a Number) is appended in missing areas.
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print (df)
