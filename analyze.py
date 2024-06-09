#importing libraries
import os

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

from sklearn.utils import shuffle

#function for reading csv tables into dataframes
def read_csv_files(path):
    file_list=os.listdir(path)
    dataframes=[]
    for file_name in file_list:
        file_path=os.path.join(path, file_name)
        
        if file_name.endswith('.csv'):
            df=pd.read_csv(file_path)
            dataframes.append(df)
        #elif file_name.endswith('.json'):
            #df = pd.read_json(file_path)
    
    combined_df=shuffle(pd.concat(dataframes, ignore_index=True))
    
    return combined_df
