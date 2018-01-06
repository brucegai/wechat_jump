import csv
import pandas as pd
import numpy
import pylab
import matplotlib as mtb

def import_data():
    file_a=pd.read_csv('c:/tianchi/data_format1/train_format1.csv')
    file_b=pd.read_csv('c:/tianchi/data_format1/user_info_format1.csv')
    file_c = pd.read_csv('c:/tianchi/data_format1/user_log_format1.csv')
    file_agg=pd.merge(pd.merge(file_a,file_b,on="user_id"),file_c,on="user_id")
    print(file_agg.head(10))
    return file_agg

# separate each variables into feature for behavior prediction
def feature_selection():
    feature={}
    return feature

#
def logistic_regression_predict(x,y,eta):
    x=""
    y=""
    


    file=import_data()


import_data()