import pandas as pd
import csv,os
import re
import xlrd
# convert excel into csv file
# file_a=pd.read_excel('C:/sam/test1.xlsx')
# print(file_a.head(20))
# file_a.to_csv('c:/sam/test2.csv')
# NAN read as a former value

filepath_a='C:/sam/0103'

def iter_folder(filepath):
    childpath=[]
    path=os.listdir(filepath)
    for alldirpath in path:
        childpath.append(alldirpath)
    return childpath

def conver_to_csv():
    store_no_list=[]
    filepath=iter_folder(filepath_a)
    for eachpath in filepath:
        print(eachpath)
        tmp_file= pd.read_excel('C:/sam/0103/'+ eachpath,sheet_name="HMKT Selling area")
        tmp_file.to_csv('c:/sam/0103_csv/'+eachpath)
        with open('c:/sam/0103_csv/'+eachpath, 'r') as csvreader:
            csv_reader = csv.reader(csvreader)
            next(csv_reader)
            for line in csv_reader:
                # print(line)
                for i in range(0,len(line)):
                    if "Store Number" in line[i]:
                        print(line[i],line[i+2])
                        print("found")

def csv_reader():
    sam_info_list=[]
    with open ('C:/sam/test2.csv','r') as csvReader:
        csvfile=csv.reader(csvReader)
        for i in range(1,6):
            next(csvfile)
        for line in csvfile:
            sam_info_list.append([line[4],line[5],line[8]])
        # print(sam_info_list)
        for i in range(0,len(sam_info_list)):
            # print(sam_info_list[i])
            if sam_info_list[i][0]=="":
                sam_info_list[i][0]=sam_info_list[i-1][0]
            if sam_info_list[i][1]=="":
                sam_info_list[i][1]=sam_info_list[i-1][1]
            if sam_info_list[i][2]=="":
                sam_info_list[i][2]=sam_info_list[i-1][2]

        for i in range(0, len(sam_info_list)):
            if sam_info_list[i][0]==sam_info_list[i-1][0]:
                sam_info_list[i].append(int(sam_info_list[i][2])+int(sam_info_list[i-1][2]))



        print(sam_info_list)
    return sam_info_list


conver_to_csv()


