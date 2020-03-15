import requests,time
from bs4 import BeautifulSoup
start = time.time()
url_list = []
for i in range(1,12):
    if i <11:
        url = 'http://www.boohee.com/food/group/' + str(i)
        url_list.append(url)
    else:
        url = 'http://www.boohee.com/food/view_menu'
        url_list.append(url)
url_list2 = []
for i in url_list:
    for num in range(1,4):
        url = i + '?page=' + str(num)
        url_list2.append(url)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
for i in url_list2:
    res = requests.get(url,headers = headers)
    bs = BeautifulSoup(res.text,'html.parser')
    foods = bs.find_all('li',class_='clearfix')
    for food in foods:
        href = 'http://www.boohee.com' + food.find_all('a')[1]['href']
        name = food.find_all('a',target='_blank')[1].text
        calorie = food.find('p').text
end = time.time()
print(end-start)       

    
