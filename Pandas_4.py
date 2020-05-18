# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:38:07 2020

@author: Kumar

The appropriate method to use depends on whether your function expects to operate on an entire DataFrame, row- or column-wise, or element wise.

Table wise Function Application: pipe()
Row or Column Wise Function Application: apply()
Element wise Function Application: applymap()
"""

#Table-wise Function Application
import pandas as pd
import numpy as np

def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)

#Row or Column Wise

df.apply(np.mean)

#element wise:the methods applymap() on DataFrame and analogously map() on Series accept any Python function taking a single value and returning a single value.

df['col1'].map(lambda x:x*100)
print (df.apply(np.mean))



