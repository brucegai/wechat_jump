import requests as rq
import re,time,random,sys
from urllib import parse
weibo_login_url='https://weibo.com/'

def login(username,password):
    username={}