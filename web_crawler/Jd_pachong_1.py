import requests as rq
from bs4 import BeautifulSoup
import urllib,json
import re,time
"""this script is based on unlogin status,try to get all comments about certain brand"""
jd_url_women="https://inman.jd.com/view_search-112147-37335-35324-0-2-0-0-1-1-80.html?keyword=2018%25E6%2598%25A5%25E8%25A3%2585&isGlobalSearch=0&other="
agent="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36"

class jd_pachong:
    def __init__(self,url):
        self.url=url

    def get_inman_page_list(url):
        content=rq.session()
        page_content=content.get(url)
        text=BeautifulSoup(page_content.text,"html.parser")

        print(type(text))





if __name__ == '__main__':
    jd_pachong.get_inman_page_list(jd_url_women)






