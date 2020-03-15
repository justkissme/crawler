from gevent import monkey
monkey.patch_all()
import gevent,time,requests
from gevent.queue import Queue

start = time.time()

url_list=['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']

work = Queue()#创建队列对象,并赋值给work
for url in url_list:
    work.put_nowait(url)

def crawler():
    while not work.empty():
    #当队列不是空的时候,执行下面程序
        url = work.get_nowait()
        # 把队列中的网址取出
        r=requests.get(url)
        print(url,work.qsize(),r.status_code)

tasks_list = []
#创建空的列表任务
for x in range(2):
    task = gevent.spawn(crawler)
    #用gevent.spawn函数执行crawler函数的任务
    tasks_list.append(task)

gevent.joinall(tasks_list)
#执行列表里的所有任务
end = time.time()
print(end - start)
