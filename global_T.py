import pandas,csv

def readfile():
    with open ('c:/kaggle/global_T.csv','r') as csvReader:
        csvfile=csv.reader(csvReader)
        i=0
        j=1
        index_kill=0
        sum_nkill=0
        for line in csvfile:
            i += 1
            if i ==1:
                firstline=line
                try:
                    for j in range(1,len(firstline)):
                        i += 1
                        if line[j]=="nkill":
                            index_kill=j
                except IndexError:
                    pass
            if i<=100:
                if line[8]=="United States":
                    print(line[index_kill])
                    sum_nkill+=line[index_kill]
                    print(sum_nkill)
            else:
                break

def readfile2():
    x=pandas.read_csv('c:/kaggle/battles.csv',encoding='utf-8')
    print(x.head(100))

# readfile2()
readfile()
