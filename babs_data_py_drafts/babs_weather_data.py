
# coding: utf-8

# In[1]:

from pandas import DataFrame, read_csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

weather_headers = ['date',
                   'max_temp','mean_temp','min_temp',
                   'max_dp','mean_dp','min_dp',
                   'max_hum','mean_hum','min_hum',
                   'max_sea','mean_sea','min_sea',
                   'max_vis','mean_vis','min_vis',
                   'max_wind','mean_wind','max_gust',
                   'rain_inches','cloud_cover','events',
                   'wind_dir_degrees','ZIP']
seasons_dict = {1: 'Winter',2: 'Spring',3: 'Spring',4: 'Spring',5: 'Summer',6: 'Summer',
                7: 'Summer',8: 'Autumn',9: 'Autumn',10: 'Autumn',11: 'Winter',12: 'Winter'}

raw_data_w1 = pd.read_csv('201402_weather_data.csv', parse_dates=['Date'])
raw_data_w1.columns = weather_headers
raw_data_w2 = pd.read_csv('201408_weather_data.csv', parse_dates=['PDT'])
raw_data_w2.columns = weather_headers
raw_data_w3 = pd.read_csv('201508_weather_data.csv', parse_dates=['PDT'])
raw_data_w3.columns = weather_headers

weather = pd.concat([raw_data_w1, raw_data_w2, raw_data_w3])
weather.index = weather['date']

weather['season'] = weather['date'].dt.month.map(seasons_dict)

