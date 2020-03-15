from urllib.request import quote

import webbrowser#用于打开网页

a=input('请输入你想在哔哩哔哩上观看的节目：')
b=a.encode('utf-8')#汉子编码方式
c=quote(b)#转换成url格式
url='https://search.bilibili.com/all?keyword=' + c + '&from_source=nav_search_new'#完整网页
print(url)

webbrowser.open(url)

print(webbrowser.get())