from pandas import DataFrame, read_csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

trip_headers = ['trip_id','trip_time',
                'start_dt','start_station','start_terminal',
                'end_dt','end_station','end_terminal',
                'bike_num','user_type','ZIP']

raw_data_1 = pd.read_csv('201402_trip_data.csv', parse_dates=True)
raw_data_1.columns = trip_headers
raw_data_2 = pd.read_csv('201408_trip_data.csv', parse_dates=True)
raw_data_2.columns = trip_headers
raw_data_3 = pd.read_csv('201508_trip_data.csv', parse_dates=True)
raw_data_3.columns = trip_headers

trip_data = pd.concat([raw_data_1, raw_data_2, raw_data_3])

trip_data.index = trip_data['trip_id'].astype(int)
trip_data.drop('trip_id', axis=1, inplace=True)

#trip_data