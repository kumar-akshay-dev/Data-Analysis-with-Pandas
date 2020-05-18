# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:57:28 2020

@author: Kumar
handle missing values (say NA or NaN) using Pandas.
When summing data, NA will be treated as Zero
If the data are all NA, then the result will be NA
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

#Check for Missing Values-isnull() 
df['one'].isnull()

#sum
df['one'].sum()

#Replace NaN with a Scalar Value
df.fillna(0)

df.fillna(method='backfill')

#dropna:if any value within a row is NA then the whole row is excluded
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
df.dropna()

#Replace Missing (or) Generic Values
df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})
df.replace(1000,0.00)

