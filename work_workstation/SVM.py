# svm algorithm
import math,csv,numpy
from sklearn.datasets import make_moons

# city_list=["成都","上海","广州","黑龙江"]

class LR:
    def __init__(self,type,theta):
        self.type=2
        self.theta=1

    def sigmode_function(self,x):
        return 1.0/1+numpy.exp(-x)

    def logistic_regression(self):
        





