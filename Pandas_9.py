# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:43:44 2020

@author: Kumar
Pandas has full-featured, high performance in-memory join operations
 idiomatically very similar to relational databases like SQL.
 pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)
"""

#Merge Two DataFrames on a Key
import pandas as pd
left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame({
	'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print (pd.merge(left,right,on='id'))

#Merge Two DataFrames on Multiple Keys
pd.merge(left,right,on=['id','subject_id'])

#Merge Using 'how' Argument = left,right,outer,inner
pd.merge(left, right, on='subject_id', how='right')