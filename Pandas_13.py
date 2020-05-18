# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:11:52 2020

@author: Kumar
The Pandas I/O API is a set of top level reader functions accessed 
like pd.read_csv() that generally return a Pandas object.
pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer',
names=None, index_col=None, usecols=None
"""
import pandas as pd

df=pd.read_csv("C:\\Users\\AKSHANSH\\.spyder-py3\\Work files\\Pandas\\text.csv")
df

#custom index
file = "C:\\Users\\AKSHANSH\\.spyder-py3\\Work files\\Pandas\\text.csv"
df=pd.read_csv(file,index_col=['S.No'])

#read csv from web
df_1=pd.read_csv("https://github.com/RaghavPrabhu/pandas-dataproject-1/blob/master/railway_gauges.csv",engine=’python')


