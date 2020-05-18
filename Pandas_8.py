# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:21:03 2020

@author: Kumar

GROUP BY
Aggregation − computing a summary statistic
Transformation − perform some group-specific operation
Filtration − discarding the data with some condition
"""
import numpy as np
import pandas as pd
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

#Split Data into Groups

df.groupby(['Team','Year']).groups

#iterating through elements
for a,b in df.groupby(['Team','Year']).groups:
    print(a,b)
    
#Select a Group
grouped = df.groupby('Year') 
grouped.get_group(2014) 

#Aggregations
grouped.agg(np.mean)
grouped['Points'].agg(np.mean)
grouped['Points'].agg([np.sum, np.mean, np.std])

#Transformations
grouped_1 = df.groupby('Team')
score = lambda x:x*10

grouped_1.transform(score)

#filter
df.groupby('Team').filter(lambda x: len(x) >= 3)