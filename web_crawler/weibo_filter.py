import requests
from urllib.parse import quote_plus
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import html,cookies
import json,urllib


weibo_url='https://login.weibo.cn/login/'
header=''
def login():
    url_parser=urlparse(weibo_url)
    user_email=input("your_email:")
    password=input("password:")
    login_dict={"scheme":header,"netloc":user_email,"password":password}
    #store user login information into a dict and deliver dict into post



    requests.post(weibo_url,netloc=json.dump(login_dict))
    print(url_parser)


login()