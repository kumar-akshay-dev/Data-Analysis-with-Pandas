# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:30:13 2020

@author: Kumar
Python Pandas - Concatenation
"""

import pandas as pd

one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])

print (pd.concat([one,two]))

#to associate specific keys with each of the pieces of the chopped up DataFrame

print (pd.concat([one,two],keys=['x','y']))

#Concatenating Using append
print (one.append(two))
one.append([two,one,two])