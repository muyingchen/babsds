from pandas import DataFrame, read_csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

station_headers = ['station_id','station_name','lat','long',
                   'dock_count','city','install_date']

raw_data_1 = pd.read_csv('201402_station_data.csv')
raw_data_1.columns = station_headers
raw_data_1.index = raw_data_1['station_id']
raw_data_2 = pd.read_csv('201408_station_data.csv')
raw_data_2.columns = station_headers
raw_data_2.index = raw_data_2['station_id']
raw_data_3 = pd.read_csv('201508_station_data.csv')
raw_data_3.columns = station_headers
raw_data_3.index = raw_data_3['station_id']

station_data = raw_data_3.merge((raw_data_1.merge(raw_data_2, on='station_id', how='outer', suffixes=('_201402','_201408'))),
                                 on='station_id', how='outer')
station_data.index = station_data['station_id']