import requests
from bs4 import BeautifulSoup
from twilio.rest import Client#用于往手机上发送短信
import schedule
import time

def weather():
    url='https://you.ctrip.com/weather/huaibei657.html'
    res=requests.get(url)
    bs=BeautifulSoup(res.text,'html.parser')
    send=[]
    date = bs.find(class_='w_cur_title').text[:-9].strip()
    #获取日期
    send.append(date)
    temp = bs.find(class_='w_future_temp').text
    #获取温度
    send.append(temp)
    
    datas = bs.find_all(class_='w_zhishu_infor')
    #因字数限制只能发送一项
    for data in datas[:1]:
        h6 = data.find('h6').text
        strong = data.find('strong').text
        p = data.find('p').text
        b=(h6+':'+strong+'  '+p)
        send.append(b)
    return send

def send_message(send):#账号密码得自己注册,这个不能使用我的
    account_sid = 'AC0c532124f2f92d98e2285da84e0f9f0d'
    auth_token = 'd3ac34bde7ef6b91aefbc05959135f5e'
    client = Client(account_sid,auth_token)
    a=(','.join(send))
    message = client.messages.create(
        to = '+8618827511517',
        from_ = '+14434322044',
        body = a)
    

def job():
    print('开始一次任务')
    send = weather()
    send_message(send)
    print('任务完成')
    

schedule.every(5).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
        
 
      
        


