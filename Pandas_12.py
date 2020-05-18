# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:49:59 2020

@author: Kumar
Python Pandas - Visualization
This functionality on Series and DataFrame is just a simple wrapper 
around the matplotlib libraries plot() method
"""
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
   periods=10), columns=list('ABCD'))

df.plot()

#bar plot
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar()
#stacked bar plot
df.plot.bar(stacked=True)

#To get horizontal bar plots
df.plot.barh(stacked=True)

#histogram
df.plot.hist()

#Area Plot
df.plot.area()
#scatter plot
df.plot.scatter(x='a', y='b')

#Pie Chart
df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)
