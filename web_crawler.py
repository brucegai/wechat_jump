# author by Gai Wang
# web crawler for zhihu
import re,requests
from bs4 import BeautifulSoup
import json
import base64
import threading
import tkinter
# import pillow,rsa
agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
header = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

def main():
    get_weibo()

def get_weibo():
    session=requests.session()
    weibo_url='http://www.zhihu.com'
    weibo_reponse=session.get(url=weibo_url,headers=header)
    text=BeautifulSoup(weibo_reponse.text,'html.parser')
    xsrf_input = text.find('input', {'name': '_xsrf'})
    xsrf_token = xsrf_input['value']

    print(xsrf_input)

if __name__ == '__main__':
    main()
