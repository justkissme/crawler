import requests
from bs4 import BeautifulSoup
url='https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
res=requests.get(url).text
#res.encoding = '' 编码
bs=BeautifulSoup(res,'html.parser')
titles=bs.find_all(class_='books')
with open('Wind_crawler\\BeautifulSoup\\BeautifulSoup.txt','wb') as f:
    for i in titles:
        type=i.find('a').text
        title=i.find(class_='title').text
        info=i.find('p').text
        href=i.find_all('a')[1]['href']
        f.write(str.encode('类型：{}\n书名：{}\n简介：{}\n链接\n：{}'.format(type,title,info,href))) #str转换成byte类型
        f.write(str.encode('------------------------------------\n'))
