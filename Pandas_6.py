# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:18:31 2020

@author: Kumar

There are two kinds of sorting available in Pandas. They are −

By label
By Actual Value
"""

import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],\
                         columns=['col2','col1'])

df.sort_index(axis=0)
df.sort_index(axis=1)

#By Value
df.sort_values(by='col1')

"""Indexing and Selecting Data
	
.loc()-Label based
.iloc()-Integer based
ix()-Both Label and Integer based"""
df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
df.loc[:,'A']
df.loc[:,['A','C']]
df.loc[['a','g'],['A','C']]
df.iloc[:4]

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])