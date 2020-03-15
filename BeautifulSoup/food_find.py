import requests
from bs4 import BeautifulSoup
url='http://www.xiachufang.com/explore/'
res=requests.get(url)
bs=BeautifulSoup(res.text,'html.parser')
infos=bs.find_all(class_='info pure-u')
food=open('Wind_crawler\\BeautifulSoup\\food_find.txt','wb')
for info in infos[:10]:
    name=info.find(class_='name').text.strip()#去除前后空白
    href='http://www.xiachufang.com'+info.find(class_='name').find('a')['href']
    ingredients=info.find(class_='ing ellipsis').text
    food.write(str.encode('菜名：{}\n链接：{}\n所需食材：{}'.format(name,href,ingredients)))
    food.write(str.encode('-------------------------\n'))
food.close()
    

