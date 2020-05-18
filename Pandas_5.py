# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:59:43 2020

@author: Kumar
Reindexing changes the row labels and column labels of a DataFrame. To reindex means to conform the data to match a given set of labels along a particular axis.

Multiple operations can be accomplished through indexing like −

Reorder the existing data to match a new set of labels.

Insert missing value (NA) markers in label locations where no data for the label existed.
"""

import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})

#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])

print (df_reindexed)

"""Filling while ReIndexing
reindex() takes an optional parameter method which is a filling method with values as follows −

pad/ffill − Fill values forward

bfill/backfill − Fill values backward

nearest − Fill from the nearest index values"""

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print (df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill:")
print (df2.reindex_like(df1,method='ffill'))

#Limits on Filling while Reindexing
df2.reindex_like(df1,method='nearest',limit=2)

#renaming columns
df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'})

"""To iterate over the rows of the DataFrame, we can use the following functions −

iteritems() − to iterate over the (key,value) pairs

iterrows() − iterate over the rows as (index,series) pairs

itertuples() − iterate over the rows as namedtuples"""

for row_index,row in df.iterrows():
    print (row_index,row)

