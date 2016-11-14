# coding:utf-8
import requests
import re
from pymongo import MongoClient
from pyquery import PyQuery as pq

def initializer():
    conn = MongoClient('127.0.0.1', 27017)
    ID=1
    db = conn.user_agent
    s = requests.Session()
    url = "http://www.useragentstring.com/pages/useragentstring.php"
    html = s.get(url).text
    data = re.findall(
        "<a href='/pages/useragentstring.php\?typ=(.*?)' class='unterMenuTitel'>(.*?)</a>", html)
    for i in data:
        url="http://www.useragentstring.com/pages/useragentstring.php?typ={0}".format(i[0])
        html=s.get(url).text
        doc=pq(html)('ul')('a')
        for user_agent in doc.items():
            db[i[1]].insert({"id":ID,"user-agent":user_agent.html(),"kind":i[1]})
            ID+=1

if __name__ == '__main__':
    initializer()
