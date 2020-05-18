# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:37:27 2020

@author: Kumar

Pandas provide a robust tool for working time with Time series data, especially in the financial sector. While working with time series data, we frequently come across the following −

Generating sequence of time
Convert the time series to different frequencies
"""

import pandas as pd
pd.datetime.now()
pd.Timestamp('2017-03-01')

#Create a Range of Time
pd.date_range("11:00", "13:30", freq="30min").time

#Converting to Timestamps
pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None]))

pd.to_datetime(['2005/11/23', '2010.12.31', None])

#Create a Range of Dates
pd.date_range('1/1/2011', periods=7)

#business date range
pd.bdate_range('1/1/2011', periods=8)