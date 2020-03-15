import requests,gevent,time
from bs4 import BeautifulSoup
from gevent.queue import Queue
import openpyxl
wb = openpyxl.Workbook()

sheet = wb.active

sheet.title = '电视剧top100'
sheet.append(['电影名','导演','主演','简介'])

url_list = []
for i in range(1,11):
    if i == 1:
        url = 'http://www.mtime.com/top/tv/top100/'
        url_list.append(url)
    else:
        url = 'http://www.mtime.com/top/tv/top100/index-'+ str(i)+'.html'
        url_list.append(url)


headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en,zh;q=0.9,zh-CN;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_userCode_=202034224587734; _userIdentity_=202034224585387; _tt_=219EEDA5953D7084EAE6CF27FAABF18E; DefaultCity-CookieKey=294; DefaultDistrict-CookieKey=0; __utmz=196937584.1583333109.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); waf_cookie=76d06903-532c-4c33ab6e4e877729edbaa440325312908d17; _ydclearance=6634c2ab731f68b17abb78b2-4fc6-4367-a7d4-fbab9744602a-1583403933; Hm_lvt_6dd1e3b818c756974fb222f0eae5512e=1583333109,1583396733; Hm_lpvt_6dd1e3b818c756974fb222f0eae5512e=1583396733; __utma=196937584.1165652781.1583333109.1583333109.1583396733.2; __utmc=196937584; __utmt=1; __utmt_~1=1; __utmb=196937584.2.10.1583396733',
'Host': 'www.mtime.com',
'Referer': 'http://www.mtime.com/top/tv/top100/',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

work = Queue()
for i in url_list:
    work.put_nowait(i)

def crawler():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url,headers=headers)
        bs = BeautifulSoup(res.text,'html.parser')
        mov_con = bs.find_all('div',class_='mov_con')
        # print(type(mov_con))
        for mov in mov_con:
            title = mov.find('h2').text
            # print(title)
            try:
                director = mov.find_all('p')[0].text
            except:
                director = '该影片无导演'
            # print(director)
            try:
                actor = mov.find_all('p')[1].text
            except:
                actor = '该影片无演员'
            try:
                brief = mov.find('p',class_='mt3').text
                
            except:
                brief = '该影片无简介'
            sheet.append([title,director,actor,brief])

task_list = [] #创建一个队列列表
for x in range(5): #创建5条队列
    task = gevent.spawn(crawler)
    task_list.append(task)

gevent.joinall(task_list)
wb.save('Wind_crawler\\gevent\\gevent_test.xlsx')




