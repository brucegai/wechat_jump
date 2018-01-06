import csv,os,sys
import keras,numpy
import tensorflow as tf

a=['Wednesday','Thursday','Friday']
b=[1,2,3,4,5,6,7,8,9,10]
c=[9,10,8,7,6,5,3,4,1,2]


def test1():
    for i in a[::-1]:
        print(i)

def test2():
    lower=int(input("pls enter a number:"))
    upper=int(input("pls enter a bigger number:"))
    for num in range(lower, upper+1):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num)
        else:
            print("1")

def knntest(intx,dataset,label,k):
    dataset=numpy.array(dataset)






