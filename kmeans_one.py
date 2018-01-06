import pandas,csv,os
import math
import matplotlib as mtb
import scipy

def import_data():
    with open ('c:/kaggle/global_T.csv','r') as csvReader:
        csvfile=csv.reader(csvReader)
        for line in csvfile:
            print(line)


def import_data_2():
    file_a=pandas.read_csv('c:/kaggle/games.csv')
    print(file_a.head(5))

import_data_2()